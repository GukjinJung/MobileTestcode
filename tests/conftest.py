import json
import os
import pytest
from utils.browser_manager import BrowserManager
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.element_locator import ElementLocator
from utils.screenshot_handler import ScreenshotHandler
from utils.wait_helper import WaitHelper
from config.settings import SCREENSHOT_DIR, TIMEOUT, BASE_URL


@pytest.fixture(scope="session")
async def browser_manager():
    """브라우저 생명주기 관리"""
    manager = BrowserManager()
    await manager.launch_browser()
    yield manager
    await manager.close_browser()


@pytest.fixture
async def page(browser_manager):
    """각 테스트마다 새 페이지 생성"""
    page = await browser_manager.create_page()
    yield page
    await browser_manager.close_page()


@pytest.fixture
async def login_page(page):
    """로그인 페이지 객체"""
    lp = LoginPage(page)
    await lp.page.goto(BASE_URL)
    return lp


@pytest.fixture
async def dashboard_page(page):
    """대시보드 페이지 객체"""
    return DashboardPage(page)


@pytest.fixture
async def element_locator(page):
    """요소 찾기 유틸"""
    return ElementLocator(page)


@pytest.fixture
def screenshot_handler():
    """스크린샷 처리 유틸"""
    return ScreenshotHandler(SCREENSHOT_DIR)


@pytest.fixture
async def wait_helper(page):
    """대기 전략 유틸"""
    return WaitHelper(page, TIMEOUT)
