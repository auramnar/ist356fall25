from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd
from io import StringIO


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://en.wikipedia.org/wiki/National_Football_League")

    # wait for tables to load
    page.wait_for_selector("table")
    
    # Let's scrape the page!
    # use pandas read_html to parse the HTML
    html = StringIO(page.content()) #converts string into file-like object
    dfs = pd.read_html(html)

    # print the table
    df_teams = dfs[2]
    print(df_teams)
    #df_teams.to_csv('nfl_teams.csv', index = False)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
