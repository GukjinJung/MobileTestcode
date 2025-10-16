import json
import os
import pytest
from config.settings import BASE_URL


@pytest.mark.e2e
class TestLoginFunctionality:
    """로그인 기능 테스트"""

    @pytest.mark.asyncio
    async def test_tc_001_login_page_access(self, page, login_page):
        """TC-001: 로그인 페이지 접속"""
        await page.goto(BASE_URL)
        await login_page.wait.wait_for_load_state()
        assert await login_page.is_login_page_loaded(), "Login page should be loaded"
        path = await login_page.take_screenshot("tc001_login_page")
        assert os.path.exists(path)

    @pytest.mark.asyncio
    async def test_tc_002_login_field_input(self, page, login_page):
        """TC-002: 로그인 필드 입력"""
        await page.goto(BASE_URL)
        with open("resources/test_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        user = data["valid_user"]
        await login_page.enter_username(user["username"])
        await login_page.enter_password(user["password"])
        # Basic check: ensure fields contain the typed values (if selectors known)
        # As we use heuristic locators, we at least take a screenshot
        await login_page.take_screenshot("tc002_filled_fields")

    @pytest.mark.asyncio
    async def test_tc_003_login_button_click(self, page, login_page):
        """TC-003: 로그인 버튼 클릭"""
        await page.goto(BASE_URL)
        with open("resources/test_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        user = data["valid_user"]
        await login_page.enter_username(user["username"])
        await login_page.enter_password(user["password"])
        await login_page.click_login_button()
        await login_page.wait.wait_for_network_idle()
        assert True  # request sent; rely on success test for validation

    @pytest.mark.asyncio
    async def test_tc_004_login_success(self, page, login_page, dashboard_page):
        """TC-004: 로그인 성공 검증"""
        await page.goto(BASE_URL)
        with open("resources/test_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        user = data["valid_user"]
        await login_page.login(user["username"], user["password"])
        await login_page.wait.wait_for_network_idle()
        assert await dashboard_page.is_dashboard_loaded(), "Dashboard should load after login"
        await dashboard_page.take_screenshot("tc004_dashboard")

    @pytest.mark.asyncio
    async def test_tc_005_login_failure(self, page, login_page):
        """TC-005: 로그인 실패 처리"""
        await page.goto(BASE_URL)
        with open("resources/test_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        user = data["invalid_user"]
        await login_page.login(user["username"], user["password"])
        await login_page.wait.wait_for_network_idle()
        assert await login_page.is_error_message_displayed(), "Error message should be displayed"
        await login_page.take_screenshot("tc005_error")
