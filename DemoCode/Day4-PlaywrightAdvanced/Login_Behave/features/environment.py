import os # Import the os module
import logging
from playwright.sync_api import sync_playwright, expect

def before_all(context):
    filename = "test_log.log"
    logging.basicConfig(
        filename=filename,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='w',
        force=True
    )
    logging.info("Before All hook executed. Log file created.")
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False, slow_mo=1000)
    context.page = context.browser.new_page()
    logging.info("Context and page created.")


def before_scenario(context, scenario):
    logging.info(f"Before Scenario hook executed for {scenario.name}")
    # context.browser.tracing.start(title="Login_Behave Trace")

def after_scenario(context, scenario):
    # context.browser.tracing.stop(path="trace.zip")
    if 'browser' in context:
        logging.info(scenario.name + " completed")
    if scenario.status == "failed":
        filename = f"screenshots/{scenario.name.replace(' ', '_')}.png"
        try:
            context.page.screenshot(path=filename, full_page=True)
            logging.error(f"Scenario failed. Screenshot saved to {filename}")
        except Exception as e:
            logging.error(f"Failed to take screenshot in after_scenario: {e}")

def after_all(context):

    context.browser.close()
    logging.info("Test session finished.")