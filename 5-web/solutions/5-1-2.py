'''
Create an outline!

Scrape the Sections H2 and H3 from this page:  https://ist256.com/fall2023/syllabus/

Print the titles, and detect the tag name so that you indent the H3 tags under the H2 tags.


'''




from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    # .launch(headless=False) makes the browser. 
    # If you wanted to run it in the background without viewing set headless=True
    context = browser.new_context()
    # creates a new browser context. 
    # Browser contexts are isolated environments within a browser, so separate sessions without sharing cookies or other  data
    page = context.new_page()
    # open a new tab in your browser
    page.goto("https://ist256.com/fall2023/syllabus/")
    # Let's scrape the heading off the page!
    # find all HTML elements with the tag names h2 or h3 on the loaded page. 
    # It returns a list of these element handles.
    headings = page.query_selector_all("h2, h3")
    #loop over the list of headings and print the tag name and text content of each heading.
    for heading in headings:
        #executes JS code within the browser context to get the tag name of the current heading element (e.g., "H2", "H3").
        tag = heading.evaluate('el => el.tagName').lower()
        # get text content of the heading element using the inner_text() method.
        text = heading.inner_text()
        if tag == "h2":
            print(text)
        else:
            print(f"\t {text}")    

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)