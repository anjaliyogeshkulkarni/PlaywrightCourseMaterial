import asyncio
from datetime import datetime
from playwright.async_api import async_playwright, expect

################ Input Data ################
page_url = "https://www.saucedemo.com/"
userName = "standard_user"
password = "secret_sauce"
###########################################

################ Locators #################
xPath_loginButton = '//input[@data-test="login-button"]'
css_loginButton = 'input[type="submit"][value="Login"]'
id_userName = '#user-name'
name_userName = '[name="user-name"]'
placeholder_userName = 'input[placeholder="Username"]'
id_password = '#password'
###########################################

async def test_LoginSuccess():
    async with async_playwright() as p:
        # browser = await p.chromium.launch(headless=False)
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()
        #
        # # Listen for console messages
        # page.on("console", lambda msg: print(f"[Console]: {msg.type} - {msg.text}"))
        #
        # # Listen for dialog boxes (alerts, confirms)
        # page.on("dialog", lambda dialog: print(f"[Dialog]: {dialog.message}"))

        # Listen for network requests and responses
        page.on("request", lambda request: print(f"[Request]: {request.method} - {request.url}"))
        page.on("response", lambda response: print(f"[Response]: {response.status} - {response.url}"))

        await page.goto(page_url)

        try:
            # Wait for the login button to appear
            await page.wait_for_selector(css_loginButton, timeout=3000)
            # print("Login button is present.")

            # Enter username and password
            await page.locator(id_userName).fill(userName)
            await page.locator(id_password).fill(password)

            # Click login
            await page.locator(css_loginButton).click()

            # Check for expected title
            await expect(page).to_have_title("Swag Labs")
            print("Testcase : 'test_LoginSuccess' Passed")

        except AssertionError as e:
            print("Testcase : 'test_LoginSuccess' Failed")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            await page.screenshot(path=f"screenshot_{timestamp}.png")

        except Exception as e:
            print("Testcase : 'test_LoginSuccess' Failed")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            await page.screenshot(path=f"screenshot_{timestamp}.png")

        await browser.close()


async def test_IncorrectPassword():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(page_url)

        try:
            # Wait for the login button to appear
            await page.wait_for_selector(css_loginButton, timeout=3000)
            # print("Login button is present.")

            # Enter username and password
            await page.locator(id_userName).fill(userName)
            await page.locator(id_password).fill("nnnn")

            # Click login
            await page.locator(css_loginButton).click()

            # Check for expected title
            await expect(page).to_have_url(url="https://www.saucedemo.com/inventory.html")
            print("Testcase : 'test_IncorrectPassword' Passed")

        except AssertionError as e:
            print("Testcase : 'test_IncorrectPassword' Failed")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            await page.screenshot(path=f"screenshot_{timestamp}.png")

        except Exception as e:
            print("Testcase : 'test_IncorrectPassword' Failed")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            await page.screenshot(path=f"screenshot_{timestamp}.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_LoginSuccess())
    asyncio.run(test_IncorrectPassword())
