import asyncio
from playwright.async_api import async_playwright

async def fetch_timezone():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(

            timezone_id="Europe/Paris"  # Simulate a specific timezone

        )
        page = await context.new_page()
        await page.goto("https://example.com")

        # Evaluate JavaScript to fetch timezone from browser
        timezone = await page.evaluate("Intl.DateTimeFormat().resolvedOptions().timeZone")
        print(f"Browser Timezone: {timezone}")

        await browser.close()

asyncio.run(fetch_timezone())
