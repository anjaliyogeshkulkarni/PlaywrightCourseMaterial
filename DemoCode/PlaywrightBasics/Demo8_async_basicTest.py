import asyncio
from playwright.async_api import async_playwright, expect

async def test_pageOpen():
    async with async_playwright() as p:
        browser = await  p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://example.com")
        title = await page.title()
        await expect(page).to_have_title("Example Domain")
        # assert title == "Example Domain"
        print("Title matched.")
        await browser.close()

if __name__ == "__main__":
    # test_pageOpen()
    asyncio.run(test_pageOpen())
