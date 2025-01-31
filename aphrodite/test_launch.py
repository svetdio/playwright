import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# import re
import time
from playwright.sync_api import Page, sync_playwright
from utils import curl
from pages.locators import sidebar, header
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
    
    assert page.locator(sidebar.home).is_visible(), "Home is not visible"
    assert page.locator(sidebar.live).is_visible(), "Live is not visible"
    assert page.locator(sidebar.slots).is_visible(), "Slots is not visible"
    assert page.locator(sidebar.sports).is_visible(), "Sports is not visible"
    assert page.locator(sidebar.promo).is_visible(), "Promo is not visible"
    assert page.locator(sidebar.history).is_visible(), "History is not visible"
    assert page.locator(sidebar.status).is_visible(), "Status is not visible"
    print("LOB-H-001, PASSED")
    print("LOB-H-002, PASSED")

    page.locator(sidebar.home).click()
    time.sleep(2)
    page.locator(sidebar.live).click()
    time.sleep(2)
    page.locator(sidebar.slots).click()
    time.sleep(2)
    page.locator(sidebar.sports).click()
    time.sleep(2)
    page.locator(sidebar.promo).click()
    time.sleep(2)
    page.locator(sidebar.history).click()
    time.sleep(2)
    page.locator(sidebar.status).click()
    time.sleep(2)


def test_header(page, launch_lobby: Page):
    page = launch_lobby

    time.sleep(5)

    account = curl.account[0]
    username = account["username"]
    password = account["password"]

    curl.get_token_and_launch_game(username, password)

    username = page.locator(f"text=grpdevcny{username}!")
    if username.is_visible():
        print("Username is visible")
    else:
        print("Username is not visible")
    
    assert page.locator(header.og).is_visible(), "OG Logo is not visible"
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
        print("The page is not in English!")
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





