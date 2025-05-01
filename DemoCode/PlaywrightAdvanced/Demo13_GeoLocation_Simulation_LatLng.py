import asyncio
import time
from pathlib import Path
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

        context = await browser.new_context(
            geolocation = {"latitude": 16.9716, "longitude": 87.5946},
            permissions = ["geolocation"]
        )

        page = await context.new_page()

        # Render the html to extract its location coordinates
        path = Path("geo_test.html").resolve().as_uri()
        await page.goto(path)
        time.sleep(2)

        await page.click("text=Get Location")
        time.sleep(2)

        await page.wait_for_function(
            "document.getElementById('output').innerText !== 'Waiting...'"
        )

        result = await page.text_content("#output")
        print("Browser context Location coordinates: ", result.split(","))

        await browser.close()

asyncio.run(main())
