
    # Logins using login PO
    # Complete the Invetory PO (add sort and add Sause Labs Backpack)
    # Perform a Select from the Dropdown
    # assert the option was selected

import re
from playwright.sync_api import Page,expect

from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage


def test_product_sort(page: Page) -> None:
  
    # login_page.open()
    login_page = LoginPage(page)
    login_page.open()
    login_page.login_standard_user()

    #Perform a Select from the Dropdown

    page.get_by_text("Name (A to Z)Name (A to Z)").click()
    page.get_by_text("Name (A to Z)Name (A to Z)").click()
    page.locator("[data-test=\"product-sort-container\"]").select_option("za")
    page.get_by_text("Name (Z to A)Name (A to Z)").click()
    page.locator("[data-test=\"product-sort-container\"]").select_option("lohi")
    page.get_by_text("Price (low to high)Name (A to").click()
    page.locator("[data-test=\"product-sort-container\"]").select_option("hilo")
    page.locator("[data-test=\"item-4-title-link\"]").click()
    page.locator("[data-test=\"inventory-item-name\"]").click()
    page.locator("[data-test=\"add-to-cart\"]").click()
    page.get_by_text("Sauce Labs Backpackcarry.").click()
    page.locator("[data-test=\"inventory-container\"] div").filter(has_text="Sauce Labs Backpackcarry.").first.click()
   
   #Assert the option was selected
    assert page.get_by_text("Sauce Labs Backpack").text_content() == "Sauce Labs Backpack"
    