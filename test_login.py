import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Add/Remove Elements").click()
    page.get_by_role("button", name="Add Element").click()
    page.get_by_role("button", name="Add Element").click()
    page.get_by_role("button", name="Add Element").click()
    page.get_by_role("button", name="Delete").nth(2).click()
    page.get_by_role("button", name="Delete").nth(1).click()
    expect(page.get_by_role("button", name="Delete")).to_be_visible()
