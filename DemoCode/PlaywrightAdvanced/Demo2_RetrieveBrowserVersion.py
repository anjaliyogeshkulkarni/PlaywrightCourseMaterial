from playwright.sync_api import sync_playwright

def test_getBrowserVersion():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        print("Browser version is : ",browser.version)

        browser = p.chromium.launch(executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe", headless=False)
        print("Browser version is : ",browser.version)


if __name__ == '__main__':
    test_getBrowserVersion()
