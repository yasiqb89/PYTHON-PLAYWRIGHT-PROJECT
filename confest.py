import pytest
from playwright.sync_api import sync_playwright

# Reusable setup, teardown code, define hooks for logging, enviornment setting, pytest automatically finds it so no need to import manually
@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page 
        context.close()
        browser.close()
