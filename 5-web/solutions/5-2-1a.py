from playwright.sync_api import Playwright, sync_playwright, expect



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ist256.com/fall2023/syllabus")
    
    
    start_element = page.query_selector("h4#criteria-for-project-grade")
    next_element = start_element.query_selector("~ *")
    bullet_element = next_element.query_selector_all("li")
    
    criteria = []
    for item in bullet_element:
        criteria.append(item.inner_text())
    
       
    # ---------------------
    context.close()
    browser.close()
    
    return criteria

    

with sync_playwright() as playwright:
    criteria = run(playwright)
    print(criteria)
    