import pytest
from playwright.sync_api import Page


def test_valid_login(page):
    page.goto("https://www.saucedemo.com/")
    page.fill('input[data-test="username"]', 'standard_user')
    page.fill('input[data-test="password"]', 'secret_sauce')
    page.click('input[data-test="login-button"]')

    assert page.url == "https://www.saucedemo.com/inventory.html"