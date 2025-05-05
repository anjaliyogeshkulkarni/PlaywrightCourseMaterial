from playwright.sync_api import sync_playwright

def demo_debugging_selectors():
    with sync_playwright() as p:
        # Launch the browser in visible mode
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Go to a demo page (replace with your own if needed)
        page.goto("https://www.saucedemo.com/")

        # Pause to manually inspect elements in the browser
        print("Pausing to inspect the page... Playwright Inspector will open.")
        page.pause()

        # Highlight the login button (correct selector)
        login_button = page.locator("input[type='submit']")
        login_button.highlight()

        # Attempt to click a wrong/failing selector to simulate failure
        try:
            page.locator("input[type='submit-button']").click()
        except Exception as e:
            print("Failed to click element with wrong selector:")
            print(e)

        # Try a working selector and perform an action
        try:
            page.locator("input[name='user-name']").fill("standard_user")
            page.locator("input[name='password']").fill("secret_sauce")
            page.locator("input[type='submit']").click()
            print("Login submitted successfully!")
        except Exception as e:
            print("Login attempt failed:")
            print(e)

        # Wait to observe result before closing
        page.wait_for_timeout(3000)
        browser.close()

if __name__ == "__main__":
    demo_debugging_selectors()
