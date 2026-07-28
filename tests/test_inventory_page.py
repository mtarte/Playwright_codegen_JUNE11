
    # Logins using login PO
    # Complete the Invetory PO (add sort and add Sause Labs Backpack)
    # Perform a Select from the Dropdown
    # assert the option was selected

import pytest
from playwright.sync_api import Page

from pages.LoginPage import LoginPage

@pytest.mark.parametrize(
    "options",
    [
        ("az"),
        ("za"),
        ("lohi"),
        ("hilo"),
    ],
)
def test_sort_options(page: Page, options):
    login_page = LoginPage(page)
    login_page.open()
    inventory_page = login_page.login_standard_user()

    inventory_page.sort_products_by(options)

    assert inventory_page.get_selected_sort() == options
    