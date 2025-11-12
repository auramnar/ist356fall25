from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd 
from time import sleep # add pause to allow page to load
import sys # handy for command line

# function does browsing, scraping, and data extraction
def run(playwright: Playwright, year) -> str:
    browser = playwright.chromium.launch(headless=False) # launch browser
    context = browser.new_context() # open a new broser profile
    page = context.new_page() # open a tab
    page.goto(f"https://cuse.com/sports/football/schedule/{year}") # go to this url
    page.wait_for_load_state("load") # wait for page to load
    sleep(1) # pause to ensure you get the schedule table
    page.get_by_role("tab", name="Table View not selected").click() # on the page there is list and table view. Get table view 
    sleep(1)
    dfs = pd.read_html(page.content())
    # page.content give all the html
    #pd.read_html scans for table elements 
    
    # ---------------------
    context.close()
    browser.close()
    return dfs[0].to_html(index=False) # get the first table


with sync_playwright() as playwright:
    year = input("  Enter year")
    html_table = run(playwright, year = str(year))
    print (html_table)

