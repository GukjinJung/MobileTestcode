from __future__ import annotations
from typing import Optional
from playwright.async_api import async_playwright, Browser, BrowserContext, Page
from config.settings import BROWSER_TYPE, HEADLESS, VIEWPORT, BASE_URL


class BrowserManager:
    """
    브라우저 생명주기 관리 - 시작, 페이지 생성, 종료
    """

    def __init__(self, headless: bool = HEADLESS, browser_type: str = BROWSER_TYPE) -> None:
        self.browser: Optional[Browser] = None
        self.context: Optional[BrowserContext] = None
        self.page: Optional[Page] = None
        self.headless = headless
        self.browser_type = browser_type
        self._pw = None

    async def launch_browser(self) -> None:
        self._pw = await async_playwright().start()
        if self.browser_type == "chromium":
            self.browser = await self._pw.chromium.launch(headless=self.headless)
        elif self.browser_type == "firefox":
            self.browser = await self._pw.firefox.launch(headless=self.headless)
        elif self.browser_type == "webkit":
            self.browser = await self._pw.webkit.launch(headless=self.headless)
        else:
            raise ValueError(f"Unsupported browser type: {self.browser_type}")
        self.context = await self.browser.new_context(
            viewport=VIEWPORT,
            base_url=BASE_URL,
        )

    async def create_page(self) -> Page:
        if not self.context:
            raise RuntimeError("Browser not launched")
        self.page = await self.context.new_page()
        return self.page

    async def navigate_to(self, url: str) -> None:
        if not self.page:
            raise RuntimeError("Page not created")
        await self.page.goto(url)

    async def close_page(self) -> None:
        if self.page:
            await self.page.close()
            self.page = None

    async def close_browser(self) -> None:
        if self.context:
            await self.context.close()
            self.context = None
        if self.browser:
            await self.browser.close()
            self.browser = None
        if self._pw:
            await self._pw.stop()
            self._pw = None

    def get_page(self) -> Page:
        if not self.page:
            raise RuntimeError("Page not created")
        return self.page
