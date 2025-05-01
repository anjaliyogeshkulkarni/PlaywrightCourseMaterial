import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, args = ["--start-maximized"])

        context = await browser.new_context(no_viewport = True,
            locale="fr-FR"  # Simulate French (France) language setting
        )

        page = await context.new_page()
        await page.goto("https://www.wikipedia.org")
        await asyncio.sleep(5)
        await browser.close()

asyncio.run(run())
