import asyncio
from playwright.async_api import async_playwright

async def simulate_geolocation():
    async with async_playwright() as p:
        # Launch the browser
        browser = await p.chromium.launch(headless=False)

        # Grant geolocation permissions & set geolocation
        context = await browser.new_context(
            geolocation={"latitude": 37.7749, "longitude": -122.4194},  # San Francisco, CA
            permissions=["geolocation"]  # Grant permission
        )

        page = await context.new_page()

        # Open a website that shows your geolocation
        await page.goto("https://mycurrentlocation.net/")  # You can also try: https://browserleaks.com/geo

        await asyncio.sleep(10)  # Let user see the result before closing
        await browser.close()

if __name__ == "__main__":
    asyncio.run(simulate_geolocation())
