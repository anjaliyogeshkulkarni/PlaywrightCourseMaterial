from playwright.sync_api import sync_playwright

def run_debug_demo():
    with sync_playwright() as p:
        # Launch with visible browser and slow motion
        browser = p.chromium.launch(headless=False, slow_mo=1000)

        # Record video of the session (optional)
        context = browser.new_context(record_video_dir="videos/")

        # Open new page
        page = context.new_page()

        try:
            print("Navigating to Example.com")
            page.goto("https://example.com")

            # Take initial screenshot
            page.screenshot(path="screenshot1_home.png")
            print("Screenshot taken of homepage.")

            # Pause for interactive debugging
            print("Pausing for manual inspection...")
            page.pause()

            # Click on link (just as a sample action)
            page.click("text=More information")

            # Take screenshot after click
            page.screenshot(path="screenshot2_after_click.png")
            print("Clicked and took another screenshot.")

        except Exception as e:
            print(f"An error occurred: {e}")
            page.screenshot(path="error_screenshot.png")

        finally:
            print("Closing browser...")
            context.close()
            browser.close()

run_debug_demo()
