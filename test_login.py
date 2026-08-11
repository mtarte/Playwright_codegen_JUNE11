import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"title\"]").click()
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("Qa")
    page.locator("[data-test=\"lastName\"]").click()
    page.locator("[data-test=\"lastName\"]").fill("Test")
    page.locator("[data-test=\"postalCode\"]").click()
    page.locator("[data-test=\"postalCode\"]").fill("94087")
    page.locator("[data-test=\"continue\"]").click()
    page.locator("[data-test=\"finish\"]").click()
    expect(page.locator("[data-test=\"complete-header\"]")).to_be_visible()
    page.goto("https://www.saucedemo.com/checkout-step-one.html")
    page.locator("[data-test=\"continue\"]").click()
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("qa")
    page.locator("[data-test=\"lastName\"]").click()
    page.locator("[data-test=\"lastName\"]").fill("test")
    page.locator("[data-test=\"postalCode\"]").click()
    page.locator("[data-test=\"postalCode\"]").fill("94087")
    page.locator("[data-test=\"continue\"]").click()
    expect(page.get_by_text("Swag Labs")).to_be_visible()
    page.locator("[data-test=\"title\"]").click()
    page.goto("https://www.saucedemo.com/")
