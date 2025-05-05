import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless = False,args = ["--start-maximized"])
    page = browser.new_page(no_viewport = True)

    # page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())

    page.goto("https://www.leapwork.com/services/learning-center/testing-internet-introduction")
    page.pause()

    # time.sleep(10)
    browser.close()
