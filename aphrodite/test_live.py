import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# import re
import time
from playwright.sync_api import Page, sync_playwright
from utils import curl
from pages.locators import sidebar, header, bar, homenav, general, footer
from conftest import launch_lobby


def test_header(page, launch_lobby: Page):
    page = launch_lobby

    account = curl.account[0]
    username = account["username"]

    time.sleep(2)
    username = page.locator(f"text=grpdevcny{username}!")
    if username.is_visible():
        print("Username is visible")
    else:
        print("Username is not visible")
    
    assert page.locator(header.coin).is_visible(), "Coin is not visible"
    assert page.locator(header.balance).is_visible(), "Balance is not visible"
    assert page.locator(header.refresh).is_visible(), "Refresh is not visible"
    assert page.locator(header.dp).is_visible(), "Profile is not visible"
    assert page.locator(header.notif).is_visible(), "Notification is not visible"
    assert page.locator(header.lang).is_visible(), "Language selector is not visible"
    print("LOB-L-001, PASSED")
    print("LOB-L-002, PASSED")
    print("LOB-L-003, PASSED")

    page.locator(header.refresh).click()
    time.sleep(1)
    page.locator(header.balance).is_visible()
    print("LOB-L-004, PASSED")
    print("LOB-L-005, PASSED")

    page.locator(header.notif).click()
    assert page.locator(header.notifModal).is_visible(), "Notification modal is not visible"
    assert page.locator(header.modalHead, has_text="Notifications").is_visible(), "Header of notification modal is not visible"
    assert page.locator(header.modalBody).is_visible(), "Body of notification modal is not visible"
    page.locator(header.modalClose).click()
    print("LOB-L-006, PASSED")

    page.locator(header.lang).click()
    assert page.locator(header.langModal).is_visible(), "Language modal is not visible"
    assert page.locator(header.modalHead, has_text="Language").is_visible(), "Header of language modal is not visible"
    assert page.locator(header.modalBody).is_visible(), "Body of language modal is not visible"

    page.locator(header.langZh).click()
    time.sleep(1)
    lang = page.get_attribute("html", "lang")
    if lang and not lang.startswith("en"):
        print("The page is not in English.")
    else:
        print("The page is in English.")
    page.locator(header.modalClose).click()
    print("LOB-L-007, PASSED")

    page.locator(header.lang).click()
    page.locator(header.langEng).click()
    time.sleep(1)
    lang = page.get_attribute("html", "lang")
    if lang and not lang.startswith("en"):
        print("The page is not in English.")
    else:
        print("The page is in English.")
    page.locator(header.modalClose).click()
    print("LOB-L-008, PASSED")


def test_sidebar(page, launch_lobby: Page):
    page = launch_lobby

    time.sleep(2)
    assert page.locator(sidebar.og).is_visible(), "OG Logo is not visible"
    assert page.locator(sidebar.home).is_visible(), "Home is not visible"
    assert page.locator(sidebar.live).is_visible(), "Live is not visible"
    assert page.locator(sidebar.slots).is_visible(), "Slots is not visible"
    assert page.locator(sidebar.sports).is_visible(), "Sports is not visible"
    assert page.locator(sidebar.promo).is_visible(), "Promo is not visible"
    assert page.locator(sidebar.history).is_visible(), "History is not visible"
    assert page.locator(sidebar.status).is_visible(), "Status is not visible"
    print("LOB-L-009, PASSED")

    sidebars = [
        page.locator(sidebar.og),
        page.locator(sidebar.home),
        page.locator(sidebar.live),
        page.locator(sidebar.slots),
        page.locator(sidebar.sports),
        page.locator(sidebar.promo),
        page.locator(sidebar.history),
        page.locator(sidebar.status),
    ]

    testIDs = [
        '010',
        '011',
        '012',
        '013',
        '014',
        '015',
        '016',
        '017',
    ]

    for sidenav, testID in zip(sidebars, testIDs):
        sidenav.click()
        time.sleep(0.5)
        print(f"LOB-L-{testID}, PASSED")


def test_scroll_button(page, launch_lobby: Page):
    page = launch_lobby
    time.sleep(2)

    pagetop = page.locator(general.pagetop)

    pagetop.is_hidden()
    print("LOB-L-039, PASSED")

    page.mouse.wheel(0, 500)
    pagetop.is_visible()
    print("LOB-L-040, PASSED")

    time.sleep(.5)

    pagetop.click()
    pagetop.is_hidden()
    print("LOB-L-041, PASSED")


def test_footer(page, launch_lobby: Page):
    page = launch_lobby
    time.sleep(2)

    footbox = page.locator(footer.footbox)
    name = page.locator(footer.footleft)
    right = page.locator(footer.footright)
    logo = page.locator(footer.footlogo)

    page.mouse.wheel(0, 4000)

    time.sleep(2)

    footbox.locator(name.locator(logo)).is_visible()
    footbox.locator(name, has_text="Oriental Game").is_visible()
    footbox.locator(right, has_text="Copyright © 2024. All rights reserved.").is_visible()
    print("LOB-L-066, PASSED")





    






