from playwright.sync_api import sync_playwright, expect
import re
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
        # Check existence of Login button with xpath
        # page.wait_for_selector(xPath_loginButton, timeout=3000)
        # Check existence of Login button with css
        page.wait_for_selector(css_loginButton, timeout=3000)
        print("Login button is present.")
        ### Using get_by methods ###
        page.get_by_placeholder('Username').fill(userName)
        page.get_by_placeholder('Password').fill(password)
        page.get_by_role("button", name="Login").click()
        page.wait_for_selector('.app_logo')
        # assertion to check if next page has opened
        page_title = page.title()  # Retrieve the page title
        expect(page).to_have_title("Swag Labs")
        print(f"Page opened successfully")

        # Assertion to check if title is "Employee Management"
        # assert page_title == "Employee Management", f"Title is '{page_title}', but expected 'Swag Labs'."

        print("Test passed: Title is 'Swag Labs'.")

    except AssertionError as e:
        # Print the assertion error message
        print(f"AssertionError: {e}")

    except Exception as e:
        print(f"Exception: {e}")

