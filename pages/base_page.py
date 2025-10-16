from __future__ import annotations
from typing import Optional
from utils.logger import LoggerSetup
from utils.element_locator import ElementLocator
from utils.image_recognition import ImageRecognition
from utils.screenshot_handler import ScreenshotHandler
from utils.wait_helper import WaitHelper
from config.settings import SCREENSHOT_DIR, TIMEOUT


class BasePage:
    """
    모든 페이지의 기본 클래스 - 공통 메서드 및 속성
    """

    def __init__(self, page) -> None:
        self.page = page
        self.logger = LoggerSetup.setup_logger(self.__class__.__name__)
        self.locator = ElementLocator(page)
        self.wait = WaitHelper(page, TIMEOUT)
        self.screenshots = ScreenshotHandler(SCREENSHOT_DIR)
        self.vision = ImageRecognition(page, SCREENSHOT_DIR)

    # 공통 메서드
    async def get_page_title(self) -> str:
        return await self.page.title()

    async def wait_for_url(self, url_pattern: str, timeout: int = TIMEOUT) -> None:
        await self.page.wait_for_url(url_pattern, timeout=timeout)

    async def take_screenshot(self, name: str) -> str:
        path = await self.screenshots.take_screenshot(self.page, name)
        LoggerSetup.log_screenshot(self.logger, path)
        return path

    async def find_element_by_coordinate(self, x: int, y: int) -> None:
        await self.locator.find_by_coordinate(x, y)

    async def find_element_by_text(self, text: str):
        return await self.locator.find_by_text(text)

    async def find_element_by_image(self, image_path: str) -> Optional[tuple[int, int]]:
        return await self.vision.find_image_on_screen(image_path)

    async def click_at_coordinate(self, x: int, y: int) -> None:
        await self.page.mouse.click(x, y)

    async def type_text(self, selector: str, text: str) -> None:
        await self.page.fill(selector, text)

    async def wait_for_element(self, selector: str, timeout: int = TIMEOUT) -> None:
        await self.wait.wait_for_element_visible(selector)

    async def is_element_visible(self, selector: str) -> bool:
        return await self.page.is_visible(selector)

    async def get_page_screenshot(self) -> bytes:
        return await self.page.screenshot(full_page=True)
