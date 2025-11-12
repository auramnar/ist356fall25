from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd
from time import sleep
import sys

# Function takes playwright object and year as input
def run(playwright: Playwright, year) -> str:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(f"https://cuse.com/sports/football/schedule/{year}")
    
    # Wait for the page to load completely
    page.wait_for_load_state("load")
    sleep(1)  # pause to allow table to render

    # Click "Table View" to show the schedule table
    page.get_by_role("tab", name="Table View not selected").click()
    sleep(1)

    # Extract all HTML tables on the page
    dfs = pd.read_html(page.content())

    # Close browser
    context.close()
    browser.close()

    # Return the first table as a DataFrame
    return dfs[0]

with sync_playwright() as playwright:
    year = input("Enter year: ")
    df = run(playwright, year=str(year)) # get table data as a dataframe
    
    # Save to CSV file
    output_filename = f"syracuse_football_schedule_{year}.csv" # name the file
    df.to_csv(output_filename, index=False, encoding="utf-8-sig") # do not include row numbers. use utf to capture any special characters

    print(f"✅ Schedule saved to '{output_filename}'") # notification
