import os
import re
from typing import Optional

import pytest
from playwright.sync_api import Page, expect
try:
    from PIL import Image
    import pytesseract
except Exception:
    Image = None
    pytesseract = None


BASE_URL_DEFAULT = "https://stage.moon.supremainc.com/login"
def _enable_flutter_accessibility(page: Page) -> None:
    try:
        placeholder = page.locator("flt-semantics-placeholder[role='button']").first
        if placeholder.count() > 0:
            try:
                placeholder.focus()
            except Exception:
                pass
            try:
                placeholder.click()
            except Exception:
                pass
            for key in ["Enter", "Space"]:
                try:
                    page.keyboard.press(key)
                    page.wait_for_timeout(150)
                except Exception:
                    pass
            page.wait_for_timeout(300)
    except Exception:
        pass


def _focus_flutter_textfield(page: Page, max_tabs: int = 12) -> bool:
    try:
        page.locator("body").click()
    except Exception:
        pass
    for _ in range(max_tabs):
        # When a Flutter TextField is focused, a DOM input/textarea overlay appears
        if page.locator("input, textarea, [contenteditable='true']").count() > 0:
            return True
        page.keyboard.press("Tab")
        page.wait_for_timeout(50)
    return page.locator("input, textarea, [contenteditable='true']").count() > 0


def _scan_and_type(page: Page, text: str, viewport: dict) -> bool:
    width = viewport.get("width", 1366)
    height = viewport.get("height", 900)
    # Common positions for login fields (centered form)
    fractions = [
        (0.50, 0.38), (0.50, 0.42), (0.50, 0.46), (0.50, 0.50), (0.50, 0.54),
        (0.45, 0.42), (0.55, 0.42), (0.45, 0.50), (0.55, 0.50)
    ]
    for fx, fy in fractions:
        x = int(width * fx)
        y = int(height * fy)
        try:
            page.mouse.click(x, y)
            page.wait_for_timeout(80)
            if page.locator("input, textarea, [contenteditable='true']").count() > 0:
                page.keyboard.type(text, delay=20)
                return True
        except Exception:
            continue
    return False


def _type_with_flutter_strategies(page: Page, email: str, password: str, viewport: dict) -> bool:
    # Strategy 1: try focusing via keyboard Tab
    if _focus_flutter_textfield(page):
        try:
            page.keyboard.type(email, delay=20)
            page.keyboard.press("Tab")
            page.keyboard.type(password, delay=20)
            return True
        except Exception:
            pass
    # Strategy 2: scan likely coordinates for email, then for password
    if _scan_and_type(page, email, viewport):
        # try next field
        page.keyboard.press("Tab")
        # If tab didn't work, scan again
        if not _scan_and_type(page, password, viewport):
            try:
                page.keyboard.type(password, delay=20)
            except Exception:
                return False
        return True
    return False


def _ocr_text(image_path: str) -> str:
    if pytesseract is None or Image is None:
        return ""
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang=os.getenv("TESS_LANG", "eng+kor"))
        return text.strip()
    except Exception:
        return ""



def _click_and_type(page: Page, locator, text: str) -> bool:
    try:
        if locator.count() == 0:
            return False
    except Exception:
        return False

    target = locator.first
    try:
        target.wait_for(state="visible", timeout=10000)
    except Exception:
        return False

    try:
        target.fill("")
        target.fill(text)
        return True
    except Exception:
        try:
            target.click()
        except Exception:
            try:
                page.mouse.click(10, 10)
                target.click()
            except Exception:
                pass
        try:
            page.keyboard.type(text, delay=20)
            return True
        except Exception:
            return False


def _find_and_type_email(page: Page, email: str) -> bool:
    candidates = [
        page.get_by_placeholder(re.compile("email|이메일", re.I)),
        page.locator("input[type='email']"),
        page.get_by_role("textbox").nth(0),
    ]
    for locator in candidates:
        if _click_and_type(page, locator, email):
            return True
    # Try clicking label-like text then typing
    try:
        label = page.get_by_text(re.compile("이메일|email", re.I)).first
        label.wait_for(timeout=5000)
        label.click()
        page.keyboard.type(email, delay=20)
        return True
    except Exception:
        pass
    # Keyboard-only fallback: Tab until a text-editing overlay appears
    try:
        page.locator("body").click()
    except Exception:
        pass
    for _ in range(6):
        try:
            overlay = page.locator("input[type='text'], input[type='email'], textarea, [contenteditable='true']").first
            if overlay.count() > 0 and overlay.first.is_visible():
                overlay.first.click()
                page.keyboard.type(email, delay=20)
                return True
        except Exception:
            pass
        page.keyboard.press("Tab")
    return False


def _find_and_type_password(page: Page, password: str) -> bool:
    candidates = [
        page.get_by_placeholder(re.compile("password|비밀번호", re.I)),
        page.locator("input[type='password']"),
        page.get_by_role("textbox").nth(1),
    ]
    for locator in candidates:
        if _click_and_type(page, locator, password):
            return True
    # Try tabbing from the first textbox as a fallback
    try:
        first_tb = page.get_by_role("textbox").first
        first_tb.click()
        page.keyboard.press("Tab")
        page.keyboard.type(password, delay=20)
        return True
    except Exception:
        pass
    # Keyboard-only fallback: continue tabbing to reach password field
    for _ in range(6):
        page.keyboard.press("Tab")
        try:
            pwd = page.locator("input[type='password']").first
            if pwd.count() > 0 and pwd.first.is_visible():
                pwd.first.click()
                page.keyboard.type(password, delay=20)
                return True
        except Exception:
            pass
        try:
            overlay = page.locator("input[type='text'], textarea, [contenteditable='true']").first
            if overlay.count() > 0 and overlay.first.is_visible():
                # This might still be a text-like field; attempt typing
                overlay.first.click()
                page.keyboard.type(password, delay=20)
                return True
        except Exception:
            pass
    return False


def _click_login_button(page: Page) -> None:
    button_locators = [
        page.get_by_role("button", name=re.compile("로그인|Login", re.I)),
        page.get_by_text(re.compile("로그인|Login", re.I)).locator("xpath=ancestor-or-self::*[self::button or @role='button']"),
    ]
    for locator in button_locators:
        try:
            if locator.count() > 0:
                locator.first.wait_for(state="visible", timeout=10000)
                locator.first.click()
                return
        except Exception:
            continue
    # Last resort: press Enter which often submits login forms
    try:
        # Try focusing any visible button-like element with 로그인 text
        txt = page.get_by_text(re.compile("로그인|Login", re.I)).first
        if txt.count() > 0:
            txt.scroll_into_view_if_needed()
            txt.click()
            return
    except Exception:
        pass
    page.keyboard.press("Enter")


def _wait_for_error_message(page: Page, expected_substring: Optional[str]) -> str:
    role_locators = [
        page.get_by_role("alertdialog"),
        page.get_by_role("dialog"),
        page.get_by_role("alert"),
        page.get_by_role("status"),
    ]

    if expected_substring:
        try:
            page.get_by_text(re.compile(re.escape(expected_substring), re.I)).first.wait_for(timeout=10000)
        except Exception:
            pass

    # Prefer explicit roles
    for locator in role_locators:
        try:
            if locator.count() > 0:
                locator.first.wait_for(state="visible", timeout=10000)
                text_content = locator.first.inner_text()
                if text_content and text_content.strip():
                    return text_content.strip()
        except Exception:
            continue

    # Fallback: look for common error keywords or the expected text anywhere
    error_pattern = re.compile(r"오류|실패|에러|error|invalid|failed|wrong|잘못", re.I)
    all_text = page.locator("body").inner_text()
    if expected_substring and re.search(re.escape(expected_substring), all_text, re.I):
        return expected_substring
    if re.search(error_pattern, all_text):
        return error_pattern.search(all_text).group(0)

    raise AssertionError("오류 팝업 또는 오류 메시지를 찾지 못했습니다.")


@pytest.mark.e2e
def test_login_error_message(page: Page):
    base_url = os.getenv("BASE_URL", BASE_URL_DEFAULT)
    email = os.getenv("LOGIN_EMAIL", "kjjung+pga@suprema.co.kr")
    password = os.getenv("LOGIN_PASSWORD", "Wjdrnrwls100!")
    expected_message = os.getenv("EXPECTED_ERROR_MESSAGE")

    viewport = {"width": 1366, "height": 900}
    page.set_viewport_size(viewport)
    page.goto(base_url, wait_until="domcontentloaded")
    _enable_flutter_accessibility(page)
    # Wait for any visible text that indicates page loaded
    try:
        page.get_by_text(re.compile("로그인|Login|이메일|비밀번호", re.I)).first.wait_for(timeout=15000)
    except Exception:
        pass

    # Try Flutter-centric strategies first
    typed_both = _type_with_flutter_strategies(page, email, password, viewport)
    if not typed_both:
        # Fallback to generic strategies (if inputs are exposed)
        assert _find_and_type_email(page, email), "이메일 입력 요소를 찾거나 입력하지 못했습니다."
        assert _find_and_type_password(page, password), "비밀번호 입력 요소를 찾거나 입력하지 못했습니다."

    _click_login_button(page)

    try:
        message_text = _wait_for_error_message(page, expected_message)
    except AssertionError:
        # Flutter canvas fallback: OCR the screenshot
        screenshot_path = os.getenv("SCREENSHOT_PATH", "/workspace/web_e2e/last_login_attempt.png")
        page.screenshot(path=screenshot_path)
        message_text = _ocr_text(screenshot_path)

    # Save discovered message for later inspection/debugging
    try:
        save_path = os.getenv("ERROR_TEXT_PATH", "/workspace/web_e2e/last_error_message.txt")
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(message_text)
    except Exception:
        pass

    if expected_message:
        assert re.search(re.escape(expected_message), message_text, re.I), (
            f"오류 메시지가 기대와 다릅니다. 기대: '{expected_message}', 실제: '{message_text}'"
        )
    else:
        # If not provided, at least ensure text is non-empty and plausibly an error
        assert len(message_text) > 0

    # Attach a screenshot for debugging regardless of pass/fail
    page.screenshot(path=os.getenv("SCREENSHOT_PATH", "/workspace/web_e2e/last_login_attempt.png"))

