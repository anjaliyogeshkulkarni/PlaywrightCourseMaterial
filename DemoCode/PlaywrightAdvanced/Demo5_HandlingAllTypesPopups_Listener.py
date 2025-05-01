import time
from playwright.async_api import async_playwright
import asyncio

# Separated out globally
NAME_TO_ENTER = "Atlas Copco"
# Separate function: outside the test
async def handle_dialog(dialog):
    print(f"Dialog message: {dialog.message}")
    if dialog.type == "alert":
        time.sleep(2)
        await dialog.accept()
    elif dialog.type == "confirm":
        time.sleep(2)
        await dialog.accept()
    elif dialog.type == "prompt":
        time.sleep(2)
        print(f"Filling prompt with name: {NAME_TO_ENTER}")
        await dialog.accept(NAME_TO_ENTER)
    else:
        await dialog.dismiss()

# Main test function
async def test_Listeners():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://example.com")

        # Inject buttons and JS to create dialogs
        await page.evaluate("""
            const alertBtn = document.createElement('button');
            alertBtn.id = 'trigger-alert';
            alertBtn.innerText = 'Trigger Alert';
            alertBtn.onclick = () => alert('This is an alert!');
            document.body.appendChild(alertBtn);

            const confirmBtn = document.createElement('button');
            confirmBtn.id = 'trigger-confirm';
            confirmBtn.innerText = 'Trigger Confirm';
            confirmBtn.onclick = () => confirm('Is this OK?');
            document.body.appendChild(confirmBtn);

            const promptBtn = document.createElement('button');
            promptBtn.id = 'trigger-prompt';
            promptBtn.innerText = 'Trigger Prompt';
            promptBtn.onclick = () => prompt('Enter your organisation name:');
            document.body.appendChild(promptBtn);
        """)

        # Attach the (external) dialog handler
        page.on("dialog", handle_dialog)

        # Actions to trigger dialogs
        time.sleep(2)
        print("Clicking Alert Button...")
        await page.click("button#trigger-alert")

        time.sleep(2)
        print("Clicking Confirm Button...")
        await page.click("button#trigger-confirm")

        time.sleep(2)
        print("Clicking Prompt Button...")
        await page.click("button#trigger-prompt")

        time.sleep(2)
        await browser.close()

# Run it
asyncio.run(test_Listeners())
