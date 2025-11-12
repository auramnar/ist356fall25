    page1 = page1_info.value
    page1.goto(page1.url)

    course_selector = page1.query_selector("table")
    course_text = course_selector.inner_text()