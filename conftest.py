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
        browser = p.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)  
        context = browser.new_context(viewport=VIEWPORT)
        page = context.new_page()

        page.add_style_tag(content="* { cursor: default !important; }")

        yield page

        browser.close()


@pytest.fixture(scope="function")
def launch_lobby(page: Page):
    account = curl.account[0]
    username = account["username"]
    password = account["password"]

    game_url = curl.get_token_and_launch_game(username, password)

    page.goto(game_url)

    yield page
    

    
    