import time

from playwright.sync_api import sync_playwright

# Modify headers using request interception
def modify_request(route, request):
    new_headers = request.headers.copy()
    # new_headers["Authorization"] = "Bearer my-fake-token"
    new_headers["Accept-Language"] = "fr-FR"
    route.continue_(headers=new_headers)

def test_ModifyRequest():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://httpbin.org/headers")
        time.sleep(5)

        # Intercept all requests to httpbin.org
        page.route("**/headers", modify_request)

        # Go to a page that displays the headers it received
        page.goto("https://httpbin.org/headers")

        # Wait so you can see the output before the browser closes
        page.wait_for_timeout(5000)
        browser.close()

if __name__ == "__main__":
    test_ModifyRequest()
