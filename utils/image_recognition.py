from __future__ import annotations
import os
from typing import Optional, Tuple
import numpy as np
import cv2
from PIL import Image
import pytesseract


class ImageRecognition:
    """
    이미지 기반 요소 인식
    - OCR 및 템플릿 매칭
    """

    def __init__(self, page, screenshot_dir: str) -> None:
        self.page = page
        self.screenshot_dir = screenshot_dir
        os.makedirs(self.screenshot_dir, exist_ok=True)

    async def _grab_screen(self) -> str:
        path = os.path.join(self.screenshot_dir, "_screen_tmp.png")
        await self.page.screenshot(path=path, full_page=True)
        return path

    async def extract_text_from_screen(self) -> str:
        path = await self._grab_screen()
        img = Image.open(path)
        text = pytesseract.image_to_string(img, lang="eng+kor")
        return text

    async def find_image_on_screen(self, image_path: str) -> Optional[Tuple[int, int]]:
        screen_path = await self._grab_screen()
        screen = cv2.imread(screen_path, cv2.IMREAD_GRAYSCALE)
        template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if screen is None or template is None:
            return None
        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val < 0.85:
            return None
        h, w = template.shape
        center = (max_loc[0] + w // 2, max_loc[1] + h // 2)
        return center

    async def compare_screenshots(self, expected_path: str, actual_path: str) -> bool:
        img1 = cv2.imread(expected_path)
        img2 = cv2.imread(actual_path)
        if img1 is None or img2 is None or img1.shape != img2.shape:
            return False
        diff = cv2.absdiff(img1, img2)
        non_zero = np.count_nonzero(diff)
        return non_zero == 0

    async def find_button_by_image(self, button_image_path: str) -> Optional[Tuple[int, int]]:
        return await self.find_image_on_screen(button_image_path)

    async def ocr_text_at_region(self, x: int, y: int, width: int, height: int) -> str:
        path = await self._grab_screen()
        img = Image.open(path)
        crop = img.crop((x, y, x + width, y + height))
        return pytesseract.image_to_string(crop, lang="eng+kor")
