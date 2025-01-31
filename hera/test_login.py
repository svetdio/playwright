import re
import time
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright

# def test_has_title(page: Page):
#     page.goto("https://hera.pwqr820.com/")
    # expect(page).to_have_title(re.compile("Playwright"))

def test_login(page: Page):
    # with sync_playwright() as p:
        # Launch browser in headed mode for debugging
        # browser = p.chromium.launch(headless=False)
        # page = browser.new_page()

        # Navigate to the login page
        page.goto("https://hera.pwqr820.com/")
        time.sleep(2)

        # Fill in the username and password fields
        page.fill('#username', 'superqa')  # Replace 'your_username' with actual username
        time.sleep(2)
        page.fill('#password', '4dmin')  # Replace 'your_password' with actual password
        time.sleep(2)

        # # Click the login button
        page.click('.btn.btn-primary.btn-block')
        time.sleep(5)

        # Validate that "Welcome, superqa!" is visible
        welcome_message = page.get_by_text("Welcome,")  # Text locator
        assert welcome_message.is_visible(), "Welcome message is not visible!"