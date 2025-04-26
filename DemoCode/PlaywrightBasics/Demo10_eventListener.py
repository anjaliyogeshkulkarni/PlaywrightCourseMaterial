import asyncio
from playwright.async_api import async_playwright

async def test_eventListener():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Listen for console messages
        page.on("console", lambda msg: print(f"[Console]: {msg.type} - {msg.text}"))

        # Listen for dialog boxes (alerts, confirms)
        page.on("dialog", lambda dialog: print(f"[Dialog]: {dialog.message}"))

        # Listen for network requests and responses
        page.on("request", lambda request: print(f"[Request]: {request.method} - {request.url}"))
        page.on("response", lambda response: print(f"[Response]: {response.status} - {response.url}"))

        # Navigate to example.com
        await page.goto("http://example.com")

        # Inject a button with a click event and dialog
        await page.evaluate("""
            () => {
                const btn = document.createElement("button");
                btn.innerText = "Click Me";
                btn.id = "demoBtn";
                btn.onclick = () => {
                    console.log("Button clicked from injected script");
                    alert("Hello from Playwright on example.com!");
                };
                document.body.appendChild(btn);
            }
        """)
        # Click the button
        await page.click("#demoBtn")
        await asyncio.sleep(3)
        await browser.close()

asyncio.run(test_eventListener())