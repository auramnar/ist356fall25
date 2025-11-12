from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://en.wikipedia.org/wiki/National_Football_League")

    # Let's scrape the page!
    # use pandas read_html to parse the HTML
    dfs = pd.read_html(page.content())

    # print the table
    df_teams = dfs[2]
    df_teams.to_csv('nfl_teams.csv', index = False)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)