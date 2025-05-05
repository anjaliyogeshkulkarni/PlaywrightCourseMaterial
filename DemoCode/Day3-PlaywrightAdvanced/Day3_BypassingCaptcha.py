from playwright.sync_api import sync_playwright, Route, Request

def handle_captcha_request(route: Route, request: Request):
    print("Intercepted CAPTCHA request:", request.url)
    route.fulfill(
        status=200,
        content_type="application/json",
        body='{"success": true}'
    )

def fill_and_submit_captcha(page):
    page.goto("http://localhost:3000/")
    page.fill('input[name="captchaInput"]', '12345')
    page.wait_for_timeout(1000)

    page.click("button[id=loginBtn]")
    page.wait_for_timeout(3000)

def test_bypass_captcha():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Log all outgoing requests
        page.on("request", lambda req: print(">>", req.method, req.url))
        page.on("dialog", lambda dialog: print("ALERT:", dialog.message) or dialog.dismiss())

        # Intercept and mock CAPTCHA verification
        page.route("**/verify-captcha", handle_captcha_request)

        fill_and_submit_captcha(page)

        browser.close()

if __name__ == "__main__":
    test_bypass_captcha()
