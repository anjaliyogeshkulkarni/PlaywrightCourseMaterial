import asyncio
import time

import requests
from playwright.async_api import async_playwright
import pytest

@pytest.mark.asyncio
async def test_POSTData():
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False,slow_mo=1000)
            context = await browser.new_context()
            page = await context.new_page()

            await page.goto("http://127.0.0.1:5000")

            # Hard wait
            await asyncio.sleep(5)

            print("New Page Title:", await page.title())

            await page.fill("#name", "Deepika")
            await page.fill("#age", "12")

            # Click the POST button (use exact button text or index if needed)
            await page.click("text=POST")
            time.sleep(5)

            assert await page.title() == "Simple Form", "\nTestcase Failed"

            await page.close()
            time.sleep(2)
            await browser.close()
    except Exception as e:
        print(f"Test case failed: {e}")
        assert False, f"Test case failed due to error: {e}"

@pytest.mark.asyncio
async def test_clear_button():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=1000)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("http://127.0.0.1:5000")

        # Hard wait
        await asyncio.sleep(5)

        print("New Page Title:", await page.title())

        await page.fill("#name", "Sarita")
        await page.fill("#age", "22")

        # Click Clear button
        clear_button = page.locator("text=CLEAR")
        await clear_button.scroll_into_view_if_needed()
        await clear_button.wait_for(state="visible")

        # Click the Clear button
        await clear_button.click()

        # Assert that the fields are now cleared
        assert await page.locator("#name").input_value() == ""
        assert await page.locator("#age").input_value() == ""

        await browser.close()

@pytest.mark.asyncio
async def test_get_api_and_set_fields():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("http://127.0.0.1:5000")

        time.sleep(5)

        response = requests.get("http://127.0.0.1:5000/demo_get_endpoint")

        if response.status_code == 200:
            data = response.json()
            name = data.get('name', '')
            age = data.get('age', '')
        else:
            print("Error fetching data from the API!")
            name = age = ""


        await page.fill("#name", name)
        await page.fill("#age", age)
        time.sleep(5)

        assert await page.locator("#name").input_value() == name
        assert await page.locator("#age").input_value() == age


        await browser.close()
