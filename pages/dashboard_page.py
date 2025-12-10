from __future__ import annotations
from .base_page import BasePage


class DashboardPage(BasePage):
    """
    대시보드 페이지 객체 - 로그인 후 메인 화면
    """

    DASHBOARD_HEADER = {
        "text": "Dashboard",
        "image": "resources/images/dashboard_header.png",
    }

    USER_PROFILE = {
        "coordinate": (1800, 50),
        "text_pattern": "사용자명",
    }

    LOGOUT_BUTTON = {
        "text": "로그아웃",
    }

    async def is_dashboard_loaded(self) -> bool:
        header = await self.locator.find_by_text(self.DASHBOARD_HEADER["text"], exact=True)
        try:
            return await header.is_visible()
        except Exception:
            return False

    async def get_logged_in_username(self) -> str:
        profile = await self.locator.find_by_text_pattern(self.USER_PROFILE["text_pattern"])
        try:
            return await profile.inner_text()
        except Exception:
            return ""

    async def is_user_logged_in(self) -> bool:
        return await self.is_dashboard_loaded()

    async def verify_page_elements(self) -> bool:
        ok_header = await self.is_dashboard_loaded()
        return ok_header
