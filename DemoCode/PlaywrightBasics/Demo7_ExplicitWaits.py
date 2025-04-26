
from playwright.sync_api import sync_playwright, expect

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
        page.wait_for_selector(css_loginButton)
        print("Login button is present.")

        #Hard Wait
        page.wait_for_timeout(5000)

        # Enter username and password credentials and click Login
        page.locator(id_userName).fill(userName)
        page.locator(id_password).fill(password)
        page.locator(css_loginButton).click()

        # /dashboard
        page.wait_for_url(url="https://www.saucedemo.com/inventory.html")

        # assertion to check if next page has opened
        page_title = page.title()  # Retrieve the page title

        expect(page).to_have_title("Swag Labs")
        print("Test passed: Title is 'Swag Labs'.")

    except AssertionError as e:
        # Print the assertion error message
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Exception: {e}")
