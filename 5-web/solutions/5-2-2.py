from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd
from time import sleep
import sys

def run(playwright: Playwright, year: str) -> str:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Navigate to the page
    page.goto(f"https://cuse.com/sports/football/schedule/{year}")

    # --- FIX: handle cookie consent dialog safely ---
    try:
        # Wait for consent manager to appear, then click
        page.locator("#transcend-consent-manager").wait_for(state="visible", timeout=5000)
        page.locator("#transcend-consent-manager").click()
    except:
        print("No consent manager dialog found or already closed.")

    # Wait for the page and table to fully load
    page.wait_for_load_state("load")
    sleep(1)

    # Switch to table view if available
    try:
        page.get_by_role("tab", name="Table View not selected").click()
        sleep(1)
    except:
        print("Table view button not found — continuing...")

    # Extract all tables on the page
    dfs = pd.read_html(page.content())

    # Cleanup
    context.close()
    browser.close()

    # Return the first table as HTML
    return dfs[0].to_html(index=False)


# --- Main ---
if __name__ == "__main__":
    with sync_playwright() as playwright:
        year = input("Enter season year (e.g., 2024): ")
        html_table = run(playwright, year=str(year))
        print(html_table)


