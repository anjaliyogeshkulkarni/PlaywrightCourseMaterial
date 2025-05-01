import asyncio
import time

from playwright.async_api import async_playwright

async def test_handlePopup():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://example.com")

        # JavaScript to create a fake popup button
        await page.evaluate("""
            let btn = document.createElement('button');
            btn.id = 'open-new-tab';
            btn.innerText = 'Open Popup';
            btn.onclick = function() {
                window.open('https://www.wikipedia.org', '_blank');
            };
            document.body.appendChild(btn);
        """)

        # Hard wait
        await asyncio.sleep(5)

        # Inspection
        # await page.pause()

        # click on button
        async with page.expect_popup() as new_page_info:
            await page.click("button#open-new-tab")  # Click to open new tab
        new_page = await new_page_info.value
        time.sleep(2)
        print("New Page Title:", await new_page.title())
        await new_page.close()
        time.sleep(2)
        await browser.close()

# Run the test
asyncio.run(test_handlePopup())