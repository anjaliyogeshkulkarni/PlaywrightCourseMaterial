import requests
import asyncio
import time
from pathlib import Path
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

        context = await browser.new_context(
            geolocation={"latitude": 12.9716, "longitude": 77.5946},
            timezone_id="Europe/Paris",  # Simulate a specific timezone
            permissions=["geolocation"]
        )

        page = await context.new_page()

        # Render the html to extract its location cocordinates
        path = Path("geo_test.html").resolve().as_uri()
        await page.goto(path)
        time.sleep(2)

        await page.click("text=Get Location")
        time.sleep(2)

        await page.wait_for_function(
            "document.getElementById('output').innerText !== 'Waiting...'"
        )

        result = await page.text_content("#output")
        print("Location shown on page:", result.split(","))


        latitude = result.split(",")[0].split(": ")[1]
        longitude = result.split(",")[1].split(": ")[1]

        url = f"https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json"
        headers = {'User-Agent': 'Mozilla/5.0'}

        response = requests.get(url, headers=headers)
        data = response.json()

        print("Address:", data.get("display_name"))

        # Evaluate JavaScript to fetch timezone from browser
        timezone = await page.evaluate("Intl.DateTimeFormat().resolvedOptions().timeZone")
        print(f"Browser Timezone: {timezone}")

        await browser.close()

asyncio.run(main())