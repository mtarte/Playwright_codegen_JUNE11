from playwright.sync_api import Page, expect 
import pytest


def test_click_action(page: Page):
    # 1. Go to Page
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    add_element_button = page.get_by_role("button", name="Add Element")
    delete_button = page.get_by_role("button", name="Delete")

    # 2. Click on the Add Element button
    add_element_button.click()
    add_element_button.click()
    add_element_button.click()
    # 3. Click on the Delete button
    delete_button.first.click()
    delete_button.nth(1).click()
    assert delete_button.is_visible() 
    # delete_count=page.get_by_role("button",name="Delete").count()
    # for d in range (delete_count):
    #     page.get_by_role("button",name="Delete").first.click()

    #     assert page.get_by_role("button",name="Delete").count() == "$0"


    
    
    # expect(delete_button).to_have_count(2)

def test_fill_and_press(page: Page):
    # 1. Go to Page
    page.goto("https://the-internet.herokuapp.com/login")
    username_field = page.get_by_label("Username")
    password_field = page.get_by_label("Password")

    username_field.fill("tomsmith")
    username_field.press("Tab")
    password_field.fill("SuperSecretPassword!")
    password_field.press("Enter")
  # Store the text from the page as actual restult THEN compare against Expected Result in assert statement
    actual_text = page.get_by_role("heading", name="Welcome to the Secure Area.").text_content()
    expected_text = "Welcome to the Secure Area. When you are done click logout below."
    assert expected_text in actual_text

    
    
def test_checkboxes(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    boxes = page.get_by_role("checkbox")

    boxes.first.check()
    boxes.last.uncheck()
    
    assert boxes.first.is_checked()
    assert not boxes.last.is_checked()
    
    
def test_dropdown(page: Page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    dropdown = page.locator("#dropdown")

    dropdown.select_option("2")
    dropdown.select_option(label="Option 1")
    dropdown.select_option(index=2)


def test_hovers(page: Page):
    page.goto("https://the-internet.herokuapp.com/hovers")
    image= page.locator(".figure").first
    image.hover()

def test_upload(page: Page):
    page.goto("https://the-internet.herokuapp.com/upload")
    #  locator of the input          path to the file
    page.locator("#file-upload").set_input_files("/Users/tartemr/Ozzy_codegen_JUNE11/test_data/resume.txt")
    page.locator("#file-submit").click()


def test_drag_and_drop(page: Page):
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")
    a = page.locator("#column-a")
    b = page.locator("#column-b")

    a.drag_to(b)
    b.drag_to(a)

@pytest.mark.parametrize(
    "link", 
    [
        "random_data.txt", "sample.txt", "sample.pdf"    
    ],             
)
def test_download(page: Page, link: str) -> None:
    page.goto("https://the-internet.herokuapp.com/download")
    with page.expect_download() as download_info:
        page.get_by_role("link", name=link).click()
    download = download_info.value
    assert link in str(download)
    
def test_hidden_ad(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/entry_ad")
    modal = page.locator("#modal")
    # Wait for the modal to load
    assert modal.is_visible()

    page.get_by_text("Close", exact=True).click()
    modal.wait_for(state="hidden")

    assert not modal.is_visible()
