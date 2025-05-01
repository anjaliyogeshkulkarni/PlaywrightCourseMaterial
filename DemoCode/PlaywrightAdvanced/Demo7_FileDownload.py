import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

async def handle_route(route):
    print("handle_route called")
    print(f"Route URL: {route.request.url}")
    file_path = Path("example_download.txt")
    file_path.write_text("This is the content of the example file. Now new content")

    await route.fulfill(
        status=200,
        headers={
            "Content-Type": "text/plain",
            "Content-Disposition": "attachment; filename=example_download.txt",
        },
        body=file_path.read_bytes(),
    )
    print("handle_route finished")


async def test_file_download():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(accept_downloads=True)
        page = await context.new_page()

        # Navigate to example.com
        await page.goto("https://example.com")
        print(f"Navigated to: {page.url}")

        # Inject custom content with a download link
        await page.set_content('''
            <html>
              <body>
                <h1>Download Test</h1>
                <a href="/download/example_download.txt" id="download-link">Click to Download</a>
              </body>
            </html>
        ''')

        # Route the download link to custom handler
        await page.route("**/download/example_download.txt", handle_route)

        try:
            # Trigger download
            async with page.expect_download() as download_info:
                await page.click("#download-link")
            obj_download = await download_info.value

            # Save to disk
            await obj_download.save_as("example_download.txt")
            print(f"File downloaded and saved as: example_download.txt")

        except Exception as e:
            print("Download failed.")
            print(e)

        await browser.close()


if __name__ == "__main__":
    asyncio.run(test_file_download())
