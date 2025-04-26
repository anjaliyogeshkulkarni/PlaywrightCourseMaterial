from playwright.sync_api import sync_playwright, expect

def swagLabs_Page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        # page.wait_for_timeout(5000)
        page_title = page.title()
        try:
            #Check for title of page using expect
            expect(page).to_have_title("Swag Labs")
            print(f"Page opened successfully")
        except Exception as e:
            # Close the browser
            browser.close()
            print(f"Title is '{page_title}', but expected 'Swag Labs'.")

if __name__ == "__main__":
    swagLabs_Page()