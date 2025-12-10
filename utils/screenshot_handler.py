import os
from datetime import datetime
from typing import Optional
from PIL import Image, ImageDraw
from config.settings import SCREENSHOT_DIR
from config.constants import DATE_FORMAT


class ScreenshotHandler:
    """
    스크린샷 관리 - 저장, 비교, 주석 처리
    """

    def __init__(self, screenshot_dir: Optional[str] = None) -> None:
        self.screenshot_dir = screenshot_dir or SCREENSHOT_DIR
        os.makedirs(self.screenshot_dir, exist_ok=True)

    def _timestamped_path(self, name: str) -> str:
        ts = datetime.now().strftime(DATE_FORMAT)
        safe = name.replace(" ", "_")
        return os.path.join(self.screenshot_dir, f"{safe}_{ts}.png")

    async def take_screenshot(self, page, name: str) -> str:
        path = self._timestamped_path(name)
        await page.screenshot(path=path, full_page=True)
        return path

    async def take_screenshot_on_failure(self, page, test_name: str) -> str:
        return await self.take_screenshot(page, f"FAIL_{test_name}")

    def compare_with_baseline(self, current_path: str, baseline_path: str) -> bool:
        # Simple pixel equality; can be replaced by perceptual diff
        try:
            with Image.open(current_path) as cur, Image.open(baseline_path) as base:
                return list(cur.getdata()) == list(base.getdata()) and cur.size == base.size
        except Exception:
            return False

    def annotate_screenshot(self, image_path: str, x: int, y: int) -> None:
        try:
            with Image.open(image_path) as img:
                draw = ImageDraw.Draw(img)
                r = 10
                draw.ellipse((x - r, y - r, x + r, y + r), outline="red", width=3)
                img.save(image_path)
        except Exception:
            pass

    async def save_failure_screenshot(self, page, test_name: str) -> str:
        return await self.take_screenshot(page, f"ERROR_{test_name}")
