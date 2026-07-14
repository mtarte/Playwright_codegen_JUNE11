import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demoqa.com/automation-practice-form")
    page.get_by_role("textbox", name="First Name").click()
    page.get_by_role("textbox", name="First Name").fill("QA")
    page.get_by_role("textbox", name="Last Name").click()
    page.get_by_role("textbox", name="Last Name").fill("AUTO")
    page.get_by_role("textbox", name="name@example.com").click()
    page.get_by_role("textbox", name="name@example.com").fill("qa_auto@example.com")
    expect(page.get_by_text("Female")).to_be_visible()
    page.get_by_role("radio", name="Female").check()
    page.get_by_role("textbox", name="Mobile Number").click()
    page.get_by_role("textbox", name="Mobile Number").fill("4081234567")
    expect(page.get_by_role("checkbox", name="Reading")).to_be_visible()
    page.get_by_role("checkbox", name="Reading").check()
    page.locator("#uploadPicture").click()
    page.locator("#uploadPicture").set_input_files("resume.txt")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Thanks for submitting the form")).to_be_visible()
