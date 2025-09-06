from playwright.sync_api import Page, Browser, Playwright
from behave.runner import Context

class CustomContext(Context):
    page: Page
    browser: Browser
    playwright: Playwright
