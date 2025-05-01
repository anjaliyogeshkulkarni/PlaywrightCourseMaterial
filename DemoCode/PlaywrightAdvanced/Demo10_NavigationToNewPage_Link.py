import asyncio
from playwright.async_api import async_playwright
import time

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://example.com")

        # Inject a clickable link that opens Wikipedia in a new tab
        await page.evaluate("""
            const link = document.createElement('a');
            link.href = 'https://www.wikipedia.org/';
            link.innerText = 'Go to Wikipedia';
            link.target = '_blank';  // Opens in new tab
            link.id = 'wiki-link';
            document.body.appendChild(link);
        """)

        time.sleep(2)

        # Navigation to new page
        async with context.expect_page() as handle_new_page:
            await page.click('#wiki-link')

        #Retrieve page object from handle
        obj_newPage = await handle_new_page.value
        await obj_newPage.wait_for_load_state()

        # Get and print the title of the new page
        title = await obj_newPage.title()
        print(f"Title of the new page: {title}")

        await browser.close()

asyncio.run(run())
