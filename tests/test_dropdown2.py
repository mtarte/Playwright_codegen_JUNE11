import re
from playwright.sync_api import Page, expect


def test_dropdown2(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Dropdown").click()
    page.locator("#dropdown").select_option("1")