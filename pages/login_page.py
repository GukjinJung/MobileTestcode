from __future__ import annotations
from typing import Optional
from config.settings import BASE_URL
from .base_page import BasePage


class LoginPage(BasePage):
    """
    로그인 페이지 객체 - 요소 및 동작 정의
    """

    USERNAME_FIELD = {
        "coordinate": (800, 300),
        "text_hint": "사용자명 또는 이메일",
        "image": "resources/images/username_field.png",
    }

    PASSWORD_FIELD = {
        "coordinate": (800, 400),
        "text_hint": "비밀번호",
        "image": "resources/images/password_field.png",
    }

    LOGIN_BUTTON = {
        "coordinate": (800, 500),
        "text": "로그인",
        "image": "resources/images/login_button.png",
    }

    ERROR_MESSAGE = {
        "text_pattern": "로그인 실패",
        "image": "resources/images/error_message.png",
    }

    async def goto(self) -> None:
        await self.page.goto(BASE_URL)

    async def is_login_page_loaded(self) -> bool:
        title = await self.get_page_title()
        return "Login" in title or "로그인" in title

    async def enter_username(self, username: str) -> None:
        await self.locator.find_and_type(self.USERNAME_FIELD, username)

    async def enter_password(self, password: str) -> None:
        await self.locator.find_and_type(self.PASSWORD_FIELD, password)

    async def click_login_button(self) -> None:
        await self.locator.find_and_click(self.LOGIN_BUTTON)

    async def get_error_message(self) -> str:
        locator = await self.locator.find_by_text_pattern(self.ERROR_MESSAGE["text_pattern"])
        try:
            return await locator.inner_text()
        except Exception:
            return ""

    async def is_error_message_displayed(self) -> bool:
        locator = await self.locator.find_by_text_pattern(self.ERROR_MESSAGE["text_pattern"])
        try:
            return await locator.is_visible()
        except Exception:
            return False

    async def login(self, username: str, password: str) -> None:
        await self.enter_username(username)
        await self.enter_password(password)
        await self.click_login_button()
