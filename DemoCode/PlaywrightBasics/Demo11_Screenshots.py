from playwright.sync_api import sync_playwright, expect
from datetime import datetime
################input data################
page_url = "https://www.saucedemo.com/"
userName = "standard_user"
password = "secret_sauce"
##########################################

##################################### Locators #####################################
xPath_loginButton = '//input[@data-test="login-button"]'
css_loginButton = 'input[type="submit"][value="Login"]'
id_userName = '#user-name'
name_userName = '[name="user-name"]'
placeholder_userName = 'input[placeholder="Username"]'
id_password = '#password'
####################################################################################

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(page_url)

    try:
        # Check existence of Login button with css
        page.wait_for_selector(css_loginButton, timeout=3000)
        print("Login button is present.")

        ### Using locator method ###
        # Enter username using id attribute
        locator = page.locator(id_userName).fill(userName)

        # Enter password using id attribute
        page.locator(id_password).fill(password)

        page.locator(css_loginButton).click()

        # assertion to check if next page has opened
        page_title = page.title()  # Retrieve the page title
        expect(page).to_have_title("Swag Labsgggg")
        print(f"Page opened successfully")

        # Assertion to check if title is "Swag Labs"
        # assert page_title == "Swag Labs"
        # print("Test passed: Title is 'Swag Labs'.")

    except AssertionError as e:
        # Print the assertion error message
        print(f"AssertionError: {e}")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(path=f"screenshot_{timestamp}.png")

    except Exception as e:
        print(f"Exception: {e}")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(path=f"screenshot_{timestamp}.png")


