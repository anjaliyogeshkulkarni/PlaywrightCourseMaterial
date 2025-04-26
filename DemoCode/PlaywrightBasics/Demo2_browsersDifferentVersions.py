from playwright.sync_api import sync_playwright

def run_test():
    with sync_playwright() as p:

        browser = p.chromium.launch(executable_path='/path/to/older/chromium', headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the test URL
        page.goto('https://www.saucedemo.com/')

        # Example test: Check if the title is correct
        title = page.title()
        print('Page Title:', title)
        if title != 'Swag Labs':
            print('Test failed: Title mismatch')
        else:
            print('Test passed: Title matches')

        # Close the browser
        browser.close()

if __name__ == '__main__':
    run_test()
