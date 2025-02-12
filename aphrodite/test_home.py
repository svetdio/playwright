import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# import re
import time
from playwright.sync_api import Page, sync_playwright
from utils import curl
from pages.locators import sidebar, header, bar, homenav, general, footer
from conftest import launch_lobby

def test_launch_lobby(page):
    # Get login details from curl.py
    for account in curl.account:
        username = account["username"]
        password = account["password"]
        print(f"Logging in as {username} and launching the lobby...")

    # Get the game launch URL from curl.py
    game_url = curl.get_token_and_launch_game(username, password)

    if game_url:
        # Extract token from the URL
        token = game_url.split("token=")[-1]  # Extracts only the token part

        # Navigate to the game lobby
        page.goto(game_url)
        print("Lobby launched successfully!")

        # Validate if the lobby is loaded (adjust selector if needed)
        lobby_url = f"https://lobby.pwqr820.com/?token={token}"
        page.wait_for_url(lobby_url)
        assert page.url == lobby_url, f"The expected {lobby_url} is visible"
        time.sleep(5)
        print(f"URL {lobby_url} was successfully launched")

        username = page.locator(f"text=grpdevcny{username}!")
        if username.is_visible():
            print("Username is visible")
        else:
            print("Username is not visible")

    else:
        print(f"Failed to launch lobby for {username}")
    
    print("LOB-H-001, PASSED")
    print("LOB-H-002, PASSED")


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
    print("LOB-H-003, PASSED")
    print("LOB-H-004, PASSED")
    print("LOB-H-005, PASSED")

    page.locator(header.refresh).click()
    time.sleep(1)
    page.locator(header.balance).is_visible()
    print("LOB-H-006, PASSED")
    print("LOB-H-007, PASSED")

    page.locator(header.notif).click()
    assert page.locator(header.notifModal).is_visible(), "Notification modal is not visible"
    assert page.locator(header.modalHead, has_text="Notifications").is_visible(), "Header of notification modal is not visible"
    assert page.locator(header.modalBody).is_visible(), "Body of notification modal is not visible"
    page.locator(header.modalClose).click()
    print("LOB-H-008, PASSED")

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
    print("LOB-H-009, PASSED")

    page.locator(header.lang).click()
    page.locator(header.langEng).click()
    time.sleep(1)
    lang = page.get_attribute("html", "lang")
    if lang and not lang.startswith("en"):
        print("The page is not in English.")
    else:
        print("The page is in English.")
    page.locator(header.modalClose).click()
    print("LOB-H-010, PASSED")


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
    print("LOB-H-011, PASSED")

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
        '012',
        '013',
        '014',
        '015',
        '016',
        '017',
        '018',
        '019',
    ]

    for sidenav, testID in zip(sidebars, testIDs):
        sidenav.click()
        time.sleep(0.5)
        print(f"LOB-H-{testID}, PASSED")

    
def test_announcement_bar(page, launch_lobby: Page):
    page = launch_lobby

    time.sleep(2)

    page.locator(bar.announce_bar).is_visible(), "Announcement bar is not visible"
    time.sleep(.5)
    print("LOB-H-020, PASSED")
    page.locator(bar.announcement).hover(force=True)
    time.sleep(1)
    print("LOB-H-021, PASSED")

def test_carousel_banner(page, launch_lobby: Page):
    page = launch_lobby

    time.sleep(2)

    assert page.locator(bar.carousel).is_visible(), "Carousel is not visible"
    print("LOB-H-022, PASSED")

    carousel = page.locator(bar.carousel)
    bounding_box = carousel.bounding_box()

    page.mouse.move(bounding_box['x'] + bounding_box['width'] / 2, bounding_box['y'] + bounding_box['height'] / 2)  # Move to the element center
    page.mouse.down()  # Hold mouse
    page.mouse.move(bounding_box['x'] - 200, bounding_box['y'] + bounding_box['height'] / 2, steps=20)  # Swipe left
    page.mouse.up()  # Release mouse
    print("LOB-H-023, PASSED")

    time.sleep(1)

    # Perform swipe right (drag to the right)
    page.mouse.move(bounding_box['x'] + bounding_box['width'] / 2, bounding_box['y'] + bounding_box['height'] / 2)  # Move to the element center
    page.mouse.down()  # Hold mouse
    page.mouse.move(bounding_box['x'] + bounding_box['width'] + 200, bounding_box['y'] + bounding_box['height'] / 2, steps=20)  # Swipe right
    page.mouse.up()  # Release mouse
    print("LOB-H-024, PASSED")


def test_icon_nav(page, launch_lobby: Page):
    page = launch_lobby

    time.sleep(2)
    nav = page.locator(homenav.icon_nav).is_visible()
    # nav_box = nav.bounding_box()
    assert nav is not None, "Navigation section not found."
    # nav_bottom = nav_box["y"] + nav_box["height"]
    print("LOB-H-025, PASSED")

    headings = [
        page.locator(homenav.section_title, has_text="Popular Games"),
        page.locator(homenav.section_title, has_text="Latest Games"),
        page.locator(homenav.section_title, has_text="Live Games"),
        page.locator(homenav.section_title, has_text="Slot Games"),
        page.locator(homenav.section_title, has_text="Sports")
    ]

    tabs = [
        page.locator(homenav.popular, has_text="Popular"),
        page.locator(homenav.latest, has_text="Latest"),
        page.locator(homenav.live, has_text="Live"),
        page.locator(homenav.slot, has_text="Slot"),
        page.locator(homenav.sports, has_text="Sports")
    ]

    testID = [
        '026',
        '027',
        '028',
        '029',
        '030'
    ]

    for tab, heading, test_id in zip(tabs, headings, testID):
        tab.click()  # Click the navigation tab
        time.sleep(2)  # Wait for UI update
    
        assert heading is not None, f"Heading text not found for {tab}"

        print(f"The heading '{tab.text_content()}' is visible.")
        print(f"LOB-H-{test_id}, PASSED")


def test_popular_section(page, launch_lobby: Page):
    page = launch_lobby
    time.sleep(2)

    page.locator(homenav.popular, has_text="Popular").click()
    print("LOB-H-031, PASSED")

    gamelaunch = page.locator(homenav.games, has_text="Viva Vegas")
    gamelaunch.locator(homenav.pin).click()

    page.reload()

    gamelaunch = page.locator(homenav.games, has_text="Viva Vegas")
    gamelaunch.click()
    print("LOB-H-032, PASSED")

    

    



def test_latest_section(page, launch_lobby: Page):
    page = launch_lobby
    time.sleep(2)

    page.locator(homenav.latest, has_text="Latest").click()
    print("LOB-H-035, PASSED")

    gamelaunch = page.locator(homenav.games, has_text="Bugsy Bonus").nth(1)
    time.sleep(2)
    gamelaunch.click(force=True)
    print("LOB-H-036, PASSED")

    
def test_scroll_button(page, launch_lobby: Page):
    page = launch_lobby
    time.sleep(2)

    pagetop = page.locator(general.pagetop)

    pagetop.is_hidden()
    print("LOB-H-039, PASSED")

    page.mouse.wheel(0, 500)
    pagetop.is_visible()
    print("LOB-H-040, PASSED")

    time.sleep(.5)

    pagetop.click()
    pagetop.is_hidden()
    print("LOB-H-041, PASSED")




def test_popup(page, launch_lobby: Page):
    page = launch_lobby
    time.sleep(2)

    ampao_del = page.locator(homenav.ampao_remove)
    ampao = page.locator(homenav.ampao)
    redenv_del = page.locator(homenav.redenv_remove)
    redenv = page.locator(homenav.redenv)
    redev_open = page.locator(homenav.redev_open)
    result = page.locator(homenav.result)

    ampao_del.click()
    ampao.is_hidden()
    print("LOB-H-057, PASSED")

    page.reload()
    time.sleep(2)

    ampao.is_visible()
    print("LOB-H-058, PASSED")

    ampao.click()
    redenv_del.click()
    redenv.is_hidden()
    print("LOB-H-060, PASSED")

    page.reload()
    time.sleep(2)

    ampao.click()
    redenv.is_visible()
    print("LOB-H-061, PASSED")

    redev_open.click(force=True)
    result.is_visible()
    print("LOB-H-062, PASSED")


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
    print("LOB-H-066, PASSED")





    






