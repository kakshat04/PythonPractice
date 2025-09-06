from playwright.sync_api import Page, expect, Playwright
import time

def test_browser_launch(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")
    print("Testing browser launch")
    print(page.title())
    # browser.close()

def test_launch_browser_shortcut(page: Page):
    page.goto("https://rahulshettyacademy.com")

def test_core_locators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    print(page.title())
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("learning")
    page.get_by_role("combobox").select_option("Teacher")
    time.sleep(2)
    # page.get_by_role("checkbox", name="terms").click()
    page.locator("#terms").click()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)

def test_FirefoxBrowser(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page(no_viewport=True)
    test_core_locators(page)
