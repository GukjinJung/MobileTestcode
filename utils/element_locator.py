from __future__ import annotations
from typing import Any, Dict, Optional


class ElementLocator:
    """
    다양한 방식으로 요소 찾기 - 좌표, 텍스트, 이미지 기반
    """

    def __init__(self, page):
        self.page = page

    async def find_by_coordinate(self, x: int, y: int) -> None:
        await self.page.mouse.move(x, y)

    async def find_by_text(self, text: str, exact: bool = False):
        selector = f"text={text}" if exact else f"text=/.*{text}.*/i"
        return self.page.locator(selector)

    async def find_by_text_pattern(self, pattern: str):
        return self.page.locator(f"text=/{pattern}/i")

    async def find_by_image(self, image_path: str) -> Optional[tuple[int, int]]:
        # Expect image recognition handled outside; placeholder returns None
        return None

    async def find_and_click(self, locator_dict: Dict[str, Any]) -> None:
        if "text" in locator_dict:
            loc = await self.find_by_text(locator_dict["text"], exact=True)
            await loc.click()
            return
        if "text_hint" in locator_dict:
            loc = await self.find_by_text(locator_dict["text_hint"], exact=False)
            await loc.first().click()
            return
        if "coordinate" in locator_dict:
            x, y = locator_dict["coordinate"]
            await self.page.mouse.click(x, y)
            return
        if "image" in locator_dict:
            # Integration point for ImageRecognition
            # Left as a hook to be wired in BasePage
            raise NotImplementedError("Image-based click is handled in BasePage via ImageRecognition")
        raise ValueError("Unsupported locator schema")

    async def find_and_type(self, locator_dict: Dict[str, Any], text: str) -> None:
        if "text" in locator_dict:
            loc = await self.find_by_text(locator_dict["text"], exact=True)
            await loc.fill(text)
            return
        if "text_hint" in locator_dict:
            loc = await self.find_by_text(locator_dict["text_hint"], exact=False)
            await loc.first().fill(text)
            return
        if "coordinate" in locator_dict:
            x, y = locator_dict["coordinate"]
            await self.page.mouse.click(x, y)
            await self.page.keyboard.type(text)
            return
        if "image" in locator_dict:
            raise NotImplementedError("Image-based type is handled in BasePage via ImageRecognition")
        raise ValueError("Unsupported locator schema")

    async def verify_element_exists(self, locator_dict: Dict[str, Any]) -> bool:
        try:
            if "text" in locator_dict:
                loc = await self.find_by_text(locator_dict["text"], exact=True)
                return await loc.is_visible()
            if "text_hint" in locator_dict:
                loc = await self.find_by_text(locator_dict["text_hint"], exact=False)
                return await loc.first().is_visible()
            if "coordinate" in locator_dict:
                # We cannot verify visibility by coordinate; assume present
                return True
            if "image" in locator_dict:
                # BasePage integrates OCR/template matching
                return False
            return False
        except Exception:
            return False
