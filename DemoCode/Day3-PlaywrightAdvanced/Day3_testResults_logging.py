from playwright.sync_api import sync_playwright
import logging

# Configure logging
logging.basicConfig(
    filename='test_log.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w',
    force=True
)

def test_open_webpage():
    try:

        logging.info("Starting Playwright sync test...")
        print("Starting Playwright sync test...")
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            url = "https://example.com"
            expected_title = "Example Domain"

            logging.info(f"Navigating to {url}")
            print(f"Navigating to {url}")
            page.goto(url)

            actual_title = page.title()
            logging.info(f"Page title is: '{actual_title}'")

            assert actual_title == expected_title, f"Expected title '{expected_title}', got '{actual_title}'"
            logging.info("Title assertion passed.")

            browser.close()
            logging.info("Browser closed successfully.")

    except AssertionError as ae:
        logging.error(f"Assertion failed: {ae}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Run the test
if __name__ == "__main__":
    test_open_webpage()

