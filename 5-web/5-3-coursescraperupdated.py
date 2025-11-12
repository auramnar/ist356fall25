'''
This program uses Playwright to automatically open Syracuse University’s course catalog website, 
search for a given course (like IST 256), 
and extract details such as the course title, credits, and description.


'''


from playwright.sync_api import Playwright, sync_playwright
import json
from time import sleep

# function takes browser automation and searches for IST256
def course_scraper(playwright: Playwright, course: str):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Go to the Syracuse course search page
    page.goto("https://coursecatalog.syracuse.edu/course-search/")
    page.get_by_placeholder("Keyword").fill(course) # finds search by placeholder text fills in the argument
    page.get_by_role("button", name="SEARCH").click() # find the search button and click it

    # Wait for search results and click the first matching course
    course_code = course.split()[0].upper() # extract the course code convert to upper case
    page.wait_for_selector(f"a:has-text('{course_code}')", timeout=15000) # wait up to 15 secs 
    page.locator(f"a:has-text('{course_code}')").first.click() # click the first result

    # Wait for the course detail page to load
    page.wait_for_load_state("networkidle") # wait until no more request are happening
    sleep(2)

    # Extract course info from the actual course page
    # check if an element in the css selector used for tile exists
    # if found get its inner text 
    title = (
        page.locator("div.text.detail-title.margin--tiny.text--semibold.text--big").inner_text()
        if page.locator("div.text.detail-title.margin--tiny.text--semibold.text--big").count() > 0
        else "N/A"
    )
    credits = (
        page.locator("div.text.detail-hours_html.margin--tiny.text--semibold.text--big").inner_text()
        if page.locator("div.text.detail-hours_html.margin--tiny.text--semibold.text--big").count() > 0
        else "N/A"
    )

    # Extract description
    # find the specific div
    # if fail then find the first paragraph
    # if nothing then default to NA
    try:
        if page.locator("div.section.section--description > div.section__content").count() > 0:
            description = page.locator("div.section.section--description > div.section__content").inner_text()
        elif page.locator("p").count() > 0:
            description = page.locator("p").nth(0).inner_text()
        else:
            description = "N/A"
    except Exception as e:
        print(f"Error while getting description: {e}")
        description = "N/A"

    # Clean and combine
    # create a dictionary for the data
    course_data = {
        "course_code": course,
        "title": title.strip(),
        "credits": credits.strip(),
        "description": description.strip()
    }

    print(json.dumps(course_data, indent=2)) # print as json

    #close browser
    context.close()
    browser.close()


# Run scraper
with sync_playwright() as playwright:
    course_scraper(playwright, "IST 256")

# run the function with the input
# close browser automatically









