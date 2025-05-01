import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:

# Device configurations list
    print("Devices that can be simulated for UI testing: ",list(p.devices.keys()))

# device configuration parameters
    device_name = "Galaxy S5"
    device_descriptor = p.devices[device_name]

    print(f"\n📱 {device_name} configuration:")
    for key, value in device_descriptor.items():
        print(f"{key}: {value}")

# Launch a browser window
    device_under_test = p.devices["Blackberry PlayBook"]
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(**device_under_test)
    page = context.new_page()
    page.goto("https://example.com")
    time.sleep(2)
