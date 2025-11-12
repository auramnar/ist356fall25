from playwright.sync_api import Playwright, sync_playwright
import json
from time import sleep

# Function to scrape course info for a given course code
def course_scraper(playwright: Playwright, course: str):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Go to the Syracuse course search page
    page.goto("https://coursecatalog.syracuse.edu/course-search/")
    page.get_by_placeholder("Keyword").fill(course)  # find search box by placeholder
    page.get_by_role("button", name="SEARCH").click()  # click search button

    # Wait for search results and click the first matching course
    course_code = course.split()[0].upper()
    page.wait_for_selector(f"a:has-text('{course_code}')", timeout=15000)
    page.locator(f"a:has-text('{course_code}')").first.click()

    # Wait for the course detail page to load
    page.wait_for_load_state("networkidle")
    sleep(2)

    # Extract course info
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

    # Create dictionary
    course_data = {
        "course_code": course.strip(),
        "title": title.strip(),
        "credits": credits.strip(),
        "description": description.strip(),
    }

    context.close()
    browser.close()
    return course_data  # ✅ return the dictionary so it can be saved later


# -----------------------------
# Run main logic
# -----------------------------
if __name__ == "__main__":
    courses = ["IST 256", "IST 387", "IST 101", "IST 356"]
    all_courses = []

    with sync_playwright() as playwright:
        for course in courses:
            print(f"Scraping {course}...")
            course_info = course_scraper(playwright, course)
            all_courses.append(course_info)

    # Save all data to JSON
    with open("course_data.json", "w", encoding="utf-8") as f:
        json.dump(all_courses, f, indent=2, ensure_ascii=False)

    print("✅ All course data saved to 'course_data.json'")
