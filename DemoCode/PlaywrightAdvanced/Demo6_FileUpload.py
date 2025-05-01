import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
import time

async def test_fileUpload():
    async with async_playwright() as p:
        print("in test_fileUpload ")
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={"width": 1280, "height": 800})
        page = await context.new_page()

        await page.set_content(
            """
            <input type="file" id="file-input" />
            <button id="upload-button">Upload</button>
            <div id="feedback"></div>
            <script>
            const input = document.getElementById('file-input');
            const button = document.getElementById('upload-button');
            const feedback = document.getElementById('feedback');
    
            button.addEventListener('click', async () => {
                const files = input.files;
                if (files.length > 0) {
                    feedback.textContent = `Uploaded ${files[0].name} of type ${files[0].type} and size ${files[0].size} bytes`;
                } else {
                    feedback.textContent = 'No file selected';
                }
            });
            </script>
            """
        )
        time.sleep(5)
        try:
            # file for upload
            file_path = "examples.txt"

            # Upload the file
            await page.set_input_files("#file-input", file_path)
            await page.click("#upload-button")

            # Verify the upload (optional)
            feedback_text = await page.inner_text("#feedback")
            print(f"Feedback: {feedback_text}")  # Output the feedback message

        except Exception as e:
            print(e)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_fileUpload())