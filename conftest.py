import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from playwright.sync_api import Page, expect, sync_playwright
from utils import curl
from utils.config import VIEWPORT, HEADLESS, SLOW_MO

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        print("VISIBLE!!!")
        browser = p.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)  
        context = browser.new_context(viewport=VIEWPORT)
        page = context.new_page()

        yield page


@pytest.fixture(scope="function")
def launch_lobby(page: Page):
    print("LOGIN!!!")
    account = curl.account[0]
    username = account["username"]
    password = account["password"]

    game_url = curl.get_token_and_launch_game(username, password)

    page.goto(game_url)

    yield page
    

    
    