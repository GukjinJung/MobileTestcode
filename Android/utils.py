import re
import html
import time
import datetime
import requests
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import os

#from setuptools.command.build_ext import if_dl

from configuration.webDriver import AppiumConfig
from configuration.utill import capture_screenshot
from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append('../Android')
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


" XPath "
# 2.2.0 구조: View('휴대폰 번호') → ImageView('+82') → EditText / View('비밀번호') → EditText
phoneNumberInputBox = "//android.view.View[@content-desc='휴대폰 번호']/following-sibling::android.widget.EditText[1]"
passwordInputBox = "//android.view.View[@content-desc='비밀번호']/following-sibling::android.widget.EditText[1]"
emailInputBox = "//android.view.View[@content-desc='이메일 주소']/following-sibling::*[1][self::android.widget.EditText]"
emailPasswordInputBox = "//android.view.View[@content-desc='비밀번호']/following-sibling::*[1][self::android.widget.EditText]"
lead = "//android.widget.FrameLayout[@resource-id=\"android:id/content\"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView"

" AccessBilityID "
login = "로그인"
logout = "로그아웃"
confirm = "확인"
cancel = "취소"
allAgree = "약관 전체 동의"
next = "다음"
authRequest = "인증요청"
authComplete = "인증완료"
mobileLogin = "모바일로 로그인"
emailLogin = "이메일로 로그인"

" ClassName "
signUpInput = "android.widget.EditText"
widgetImage = "android.widget.ImageView"

OUTLOOK_PKG = "com.microsoft.office.outlook"
OUTLOOK_ID = OUTLOOK_PKG + ":id/"
_last_outlook_code = None  # 직전에 읽은 인증번호 (같은 번호를 다시 읽으면 이전 메일로 판단)


def _find_auth_code_in_source(self):
    """화면 XML(page_source)을 한 번만 받아 메일 본문의 6자리 인증번호를 찾는다.
    (요소마다 get_attribute를 호출하던 방식보다 훨씬 빠름)"""
    found = re.findall(r'<android\.view\.View\b[^>]*\btext="(\d{6})"', self.driver.page_source)
    return found[0] if found else None


def _parse_outlook_time(text, today):
    """메일 헤더의 수신 시각('오후 1:20', '오전 11:25')을 오늘 날짜의 datetime으로 변환.
    날짜가 붙은 표시('11월 17일', '어제' 등)는 오늘 메일이 아니므로 None."""
    m = re.search(r"(오전|오후)\s*(\d{1,2}):(\d{2})", text or "")
    if not m:
        return None
    hour = int(m.group(2)) % 12 + (12 if m.group(1) == "오후" else 0)
    return today.replace(hour=hour, minute=int(m.group(3)), second=0, microsecond=0)


def _tap_latest_mail(self):
    """메일 목록 첫 번째 메일 열기. 목록이 Compose라 행이 요소로 잡히지 않아
    목록 영역(conversation_list)의 위치를 기준으로 첫 행을 탭한다. (기존 고정 좌표 497,358과 동일 위치)"""
    lst = self.driver.find_elements(AppiumBy.ID, OUTLOOK_ID + "conversation_list")
    if lst:
        r = lst[0].rect
        self.driver.tap([(r["x"] + r["width"] // 2, r["y"] + 98)])
    else:
        self.driver.tap([(497, 358)])


def get_outlook_auth_code(self, expected_to=None, max_attempts=5):
    """Outlook Clue 폴더의 최신 메일에서 6자리 인증번호를 읽어 반환한다.

    새 메일 판단 (메일 헤더는 재실행 없이 바로 읽힘 → 오래된 메일이면 재실행 없이 바로 새로고침):
      1) 수신 시각이 이 함수 호출 시각(기기 시계, 분 단위) - 1분 이후일 것
      2) expected_to가 주어지면 받는 사람 주소가 일치할 것
      3) 읽은 인증번호가 직전에 읽은 번호와 다를 것
    메일 본문(인증번호)은 Outlook을 홈으로 보냈다가 다시 실행해야 읽을 수 있어 재실행 단계를 유지한다.
    끝까지 못 찾으면 예외를 발생시킨다.
    반환 시 화면: Outlook (메일 닫기 완료)"""
    global _last_outlook_code
    started = time.time()
    device_now = datetime.datetime.strptime(self.driver.get_device_time("YYYY-MM-DD HH:mm"), "%Y-%m-%d %H:%M")
    not_before = device_now - datetime.timedelta(minutes=1)

    self.driver.press_keycode(3)  # 홈화면
    time.sleep(1)
    if "outlook" not in self.driver.current_package:
        self.driver.activate_app(OUTLOOK_PKG)

    WebDriverWait(self.driver, 10).until(lambda d: d.find_elements(AppiumBy.ID, OUTLOOK_ID + "account_button"))
    self.driver.find_element(AppiumBy.ID, OUTLOOK_ID + "account_button").click()
    clueBtn = self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='com.microsoft.office.outlook:id/drawer_folder_composable']//android.widget.TextView[@text='Clue'])[1]")
    clueBtn.click()
    time.sleep(2)

    reason = ""
    for attempt in range(1, max_attempts + 1):
        self.driver.swipe(573, 291, 573, 1320)  # 새로고침
        time.sleep(2)
        _tap_latest_mail(self)

        # 메일이 열릴 때까지 대기 (제목 요소)
        try:
            WebDriverWait(self.driver, 8).until(lambda d: d.find_elements(AppiumBy.ID, OUTLOOK_ID + "conversation_subject"))
        except Exception:
            reason = "메일이 열리지 않음"
            print(f"{reason} - 다시 시도 ({attempt}/{max_attempts})")
            continue

        # 1), 2) 헤더로 새 메일 여부 확인 (재실행 전에 판단)
        mail_time_text = self.driver.find_element(AppiumBy.ID, OUTLOOK_ID + "short_date").text
        to_text = self.driver.find_element(AppiumBy.ID, OUTLOOK_ID + "from").text
        mail_time = _parse_outlook_time(mail_time_text, device_now)
        if mail_time is None or mail_time < not_before:
            reason = f"이전 메일(수신 {mail_time_text})"
        elif expected_to and expected_to.lower() not in to_text.lower():
            reason = f"다른 수신자 메일({to_text.splitlines()[-1]})"
        else:
            reason = ""

        if reason:
            print(f"{reason} - 새 메일 대기 후 다시 시도 ({attempt}/{max_attempts})")
            self.driver.press_keycode(4)  # 메일 닫고 목록으로
            time.sleep(1)
            continue

        # 홈 -> Outlook 재실행 (재실행해야 메일 본문의 인증번호가 화면 구조에 나타남)
        self.driver.press_keycode(3)
        time.sleep(1)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Outlook").click()

        code = None
        end = time.time() + 6
        while time.time() < end:
            code = _find_auth_code_in_source(self)
            if code:
                break
            time.sleep(1)

        # 3) 직전 번호와 비교
        if code and code != _last_outlook_code:
            _last_outlook_code = code
            print(f"최종 인증번호: {code} (수신 {mail_time_text}, 시도 {attempt}회, {time.time() - started:.1f}초)")
            officeBack = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "닫기")
            officeBack.click()
            time.sleep(1)
            return code

        reason = f"직전과 같은 인증번호({code})" if code else "본문에서 인증번호를 찾지 못함"
        print(f"{reason} - 다시 시도 ({attempt}/{max_attempts})")
        self.driver.press_keycode(4)  # 메일 닫고 목록으로
        time.sleep(1)

    raise Exception(f"Outlook에서 새 인증번호를 찾지 못했습니다. 마지막 사유: {reason} ({max_attempts}회 시도)")


def authCode(self, expected_to=None):
    auth_code = get_outlook_auth_code(self, expected_to)

    self.driver.press_keycode(3)
    # 홈화면
    time.sleep(1)

    clue_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Suprema CLUe")
    clue_button.click()
    time.sleep(0.5)

    auth_input_box = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
    auth_input_box.click()
    auth_input_box.send_keys(auth_code)


_last_teams_code = None  # 직전에 읽은 휴대폰 인증번호


def _parse_teams_cards(page_source):
    """Teams 채널 화면 XML에서 인증 카드 목록을 위→아래(오래된→최신) 순서로 추출.
    Workflows 카드는 WebView 안의 TextView 'text'에만 내용이 있고 content-desc는 비어 있으므로
    content-desc가 아닌 text 속성을 순서대로 읽는다. (예전 webhook 카드도 text에 내용이 있음)
    반환: [{"time": '오후 8:47', "target": '01039512139', "code": '086007'}, ...]"""
    cards, cur_time, cur_target = [], None, None
    for m in re.finditer(r'<[^>]*?\btext="([^"]*)"[^>]*>', page_source):
        node, text = m.group(0), html.unescape(m.group(1))
        if "message_status" in node or re.fullmatch(r"(\d{4}년 \d{1,2}월 \d{1,2}일 |\d{1,2}월 \d{1,2}일 )?(오전|오후) \d{1,2}:\d{2}", text):  # 카드 헤더의 수신 시각
            cur_time, cur_target = text, None
            continue
        t = re.search(r"대상\((\d+)\)", text)  # '가입 인증코드 대상(010...)' / '패스워드 찾기 대상(010...)'
        if t:
            cur_target = t.group(1)
        c = re.search(r"\[(\d{6})\]", text)    # '... 인증번호는 [123456] 입니다.'
        if c:
            cards.append({"time": cur_time, "target": cur_target, "code": c.group(1)})
    return cards


def get_teams_auth_code(self, phone_number=None, timeout=25):
    """Teams 'CLUe 인증 코드 수신채널'에서 최신 휴대폰 인증번호를 읽어 반환한다.
    새 카드 판단:
      1) 카드 수신 시각이 이 함수 호출 시각(기기 시계, 분 단위) - 1분 ~ 현재 사이일 것
      2) phone_number가 주어지면 카드의 '대상(번호)'가 일치할 것
      3) 직전에 읽은 번호와 다를 것
    Workflows 카드는 WebView라 채널 진입 후 몇 초 뒤에 내용이 나타나므로 timeout까지 반복 확인한다.
    반환 시 화면: Teams 채널 화면"""
    global _last_teams_code
    started = time.time()
    device_now = datetime.datetime.strptime(self.driver.get_device_time("YYYY-MM-DD HH:mm"), "%Y-%m-%d %H:%M")
    not_before = device_now - datetime.timedelta(minutes=1)
    target = re.sub(r"\D", "", phone_number) if phone_number else None

    self.driver.press_keycode(3)  # 홈화면
    time.sleep(1)
    self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Teams").click()

    # Teams UI 변경: 하단 '채널' 탭 제거 → '채팅' 탭의 '팀 및 채널' 섹션에서 채널 선택
    self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.microsoft.teams:id/bb_bottom_bar_title' and @text='채팅']").click()
    self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.microsoft.teams:id/teams_channel_text' and @text='CLUe 인증 코드 수신채널']").click()

    reason, polls = "채널 카드 없음", 0
    while time.time() - started < timeout:
        time.sleep(1)
        polls += 1
        if polls % 6 == 0:  # 6초마다 맨 아래(최신)로 스크롤
            self.driver.swipe(540, 1700, 540, 700, 300)

        cards = _parse_teams_cards(self.driver.page_source)
        if target:
            cards = [c for c in cards if c["target"] == target]
        if not cards:
            reason = f"대상({target}) 카드 없음" if target else "채널 카드 없음"
            continue

        latest = cards[-1]
        # 오늘 카드는 '오후 8:47'처럼 시각만 표시됨. '6월 16일 오후 6:24'처럼 날짜가 붙으면 이전 카드
        is_today = bool(re.fullmatch(r"(오전|오후) \d{1,2}:\d{2}", latest["time"] or ""))
        card_time = _parse_outlook_time(latest["time"], device_now) if is_today else None
        if card_time is None or not (not_before <= card_time <= device_now + datetime.timedelta(minutes=1)):
            reason = f"이전 카드(수신 {latest['time']}, 대상 {latest['target']}, {latest['code']})"
            continue
        if latest["code"] == _last_teams_code:
            reason = f"직전과 같은 인증번호({latest['code']})"
            continue

        _last_teams_code = latest["code"]
        print(f"Teams 인증번호: {latest['code']} (대상 {latest['target']}, 수신 {latest['time']}, {time.time() - started:.1f}초)")
        return latest["code"]

    raise Exception(f"Teams 인증 코드 수신채널에서 새 인증번호를 찾지 못했습니다. 마지막 사유: {reason} ({timeout}초)")


def authCode_mobile(self, phone_number=None):
    num_value = get_teams_auth_code(self, phone_number)

    teamsBack = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "뒤로")
    teamsBack.click()
    time.sleep(0.3)

    self.driver.press_keycode(3)
    #홈화면
    time.sleep(1)

    clue_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Suprema CLUe")
    clue_button.click()
    time.sleep(0.5)

    auth_input_box = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
    auth_input_box.click()
    auth_input_box.send_keys(num_value)


def placeInviteEmail(self, placeId, emailAddress, role):
    url1 = "https://api.moon.supremainc.com/stage/v1/accounts/login/email"
    headers1 = {
        "Content-Type": "application/json"
    }
    body1 = {
        "email": "kjjung+pga@suprema.co.kr",
        "password": "Kjstar36!!",
        "authDeviceType": "WEB_BROWSER"
    }
    response1 = requests.post(url1, headers=headers1, json=body1)
    print("Status Code:", response1.status_code)
    try:
        print("Response JSON:", response1.json())
    except Exception:
        print("Response Text:", response1.text)

    auth_code2 = get_outlook_auth_code(self, "kjjung+pga@suprema.co.kr")

    url2 = "https://api.moon.supremainc.com/stage/v1/accounts/login/two-factor"
    headers2 = {
        "Content-Type": "application/json"
    }
    body2 = {
        "email": "kjjung+pga@suprema.co.kr",
        "twoFactor": auth_code2,
        "authDeviceType": "WEB_BROWSER"
    }
    time.sleep(1)
    response2 = requests.post(url2, headers=headers2, json=body2)
    if response2.status_code == 200:
        data = response2.json().get("data", {})
        access_token = data.get("accessToken")
        refresh_token = data.get("refreshToken")
        print("Access Token:", access_token)
        print("Refresh Token:", refresh_token)
    else:
        print("토큰 발급 실패:", response2.text)
        return  # 또는 raise Exception("토큰 발급 실패")

    url = f"https://api.moon.supremainc.com/stage/v1/places/{placeId}/invite-email"
    # 현재 공간 그룹에서 발급된 API Key로 동작이 안되어 SO계정 로그인 후 해당 토큰으로 임시로 넣어둠, 테스트 할때 마다 토근 입력해야 됨
    #token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0dGMiOiJhYyIsImR0YyI6IndiIiwiZXhwIjoxNzUzNDE3Mjk3LCJyaWMiOjE3OCwiaWF0IjoxNzUzNDEzNjk3fQ.ALhZ53j8gSvmKPFLeL5oS4d3WuIAM7bBIZgo_4DaZfA"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    body = {
        "invitees": [
            {
                "email": emailAddress,
                "role": role
            }
        ]
    }
    response = requests.post(url, headers=headers, json=body)
    print("Status Code:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except Exception:
        print("Response Text:", response.text)

    self.driver.press_keycode(3)
    # 홈화면
    time.sleep(0.5)

    clue_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Suprema CLUe")
    clue_button.click()
    time.sleep(0.5)

def placeInvitePhone(self, placeId,countryCode, phoneNumber, role):
    url1 = "https://api.moon.supremainc.com/stage/v1/accounts/login/email"
    headers1 = {
        "Content-Type": "application/json"
    }
    body1 = {
        "email": "kjjung+pga@suprema.co.kr",
        "password": "Kjstar36!!",
        "authDeviceType": "WEB_BROWSER"
    }
    response1 = requests.post(url1, headers=headers1, json=body1)
    print("Status Code:", response1.status_code)
    try:
        print("Response JSON:", response1.json())
    except Exception:
        print("Response Text:", response1.text)

    if response1.status_code == 200:
        print("로그인 성공")
    else:
        print("로그인 실패")

    auth_code = get_outlook_auth_code(self, "kjjung+pga@suprema.co.kr")

    while True:
        url2 = "https://api.moon.supremainc.com/stage/v1/accounts/login/two-factor"
        headers2 = {
            "Content-Type": "application/json"
        }
        body2 = {
            "email": "kjjung+pga@suprema.co.kr",
            "twoFactor": auth_code,
            "authDeviceType": "WEB_BROWSER"
        }
        time.sleep(1)
        response2 = requests.post(url2, headers=headers2, json=body2)
        time.sleep(2)
        if response2.status_code == 200:
            data = response2.json().get("data", {})
            access_token = data.get("accessToken")
            refresh_token = data.get("refreshToken")
            print("Access Token:", access_token)
            print("Refresh Token:", refresh_token)
            break
        else:
            print("토큰 발급 실패:", response2.text)
            time.sleep(2)
            return  # 또는 raise Exception("토큰 발급 실패")

    url = f"https://api.moon.supremainc.com/stage/v1/places/{placeId}/invite-phone"
    # 현재 공간 그룹에서 발급된 API Key로 동작이 안되어 SO계정 로그인 후 해당 토큰으로 임시로 넣어둠, 테스트 할때 마다 토근 입력해야 됨
    #token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0dGMiOiJhYyIsImR0YyI6IndiIiwiZXhwIjoxNzUzNDE3Mjk3LCJyaWMiOjE3OCwiaWF0IjoxNzUzNDEzNjk3fQ.ALhZ53j8gSvmKPFLeL5oS4d3WuIAM7bBIZgo_4DaZfA"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    body = {
        "invitees": [
             {
                "countryCode": countryCode,
                "phone": phoneNumber,
                "role": role
            }
        ]
    }
    response = requests.post(url, headers=headers, json=body)
    print("Status Code:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except Exception:
        print("Response Text:", response.text)

    self.driver.press_keycode(3)
    # 홈화면
    time.sleep(0.5)

    clue_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Suprema CLUe")
    clue_button.click()
    time.sleep(0.5)

    self.driver.press_keycode(3)
    # 홈화면
    time.sleep(0.5)

    clue_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Suprema CLUe")
    clue_button.click()
    time.sleep(0.5)

def signUpEmail(self, emailAddress): #랜덤 이메일 회원가입
    signUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
    signUp.click()

    agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
    agree.click()

    nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
    nextBtn.click()
    time.sleep(0.5)

    emailInput = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
    emailInput.click()
    emailInput.send_keys(emailAddress)

    #self.driver.hide_keyboard()

    authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
    authBtn.click()
    time.sleep(2)

    authCode(self, emailAddress)

    authComBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
    authComBtn.click()

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소").is_displayed()
    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailAddress).is_displayed()

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이름").is_displayed()
    nameInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[1]")
    nameInput.click()
    nameInput.send_keys("Test singUP")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호").is_displayed()
    passwordInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[2]")
    passwordInput.click()
    passwordInput.send_keys("Kjstar36!!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재입력").is_displayed()
    rePasswordInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[3]")
    rePasswordInput.click()
    rePasswordInput.send_keys("Kjstar36!!")

    self.driver.hide_keyboard()

    startBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "시작하기")
    startBtn.click()

def signUpMobile(self, mobileNumber): #랜덤 폰번호 회원가입
    signUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
    signUp.click()

    agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "약관 전체 동의")
    agree.click()

    nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
    nextBtn.click()

    mobileSel = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "모바일")
    mobileSel.click()
    time.sleep(1)

    mobileInput = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
    mobileInput.click()
    mobileInput.send_keys(mobileNumber)

    authRequest = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청")
    authRequest.click()
    time.sleep(0.5)

    authCode_mobile(self, mobileNumber)

    #self.driver.hide_keyboard()

    authApply = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
    authApply.click()

    time.sleep(0.1)

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호").is_displayed()

    phoneNumber1 = re.sub(r"(\d{3})(\d{4})(\d{4})", r"\1 \2 \3", mobileNumber)
    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, phoneNumber1)

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이름").is_displayed()
    nameInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[1]")
    nameInput.click()
    nameInput.send_keys("Test SingUP")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호").is_displayed()
    passwordInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[2]")
    passwordInput.click()
    passwordInput.send_keys("Kjstar36!!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재입력").is_displayed()
    rePasswordInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[3]")
    rePasswordInput.click()
    rePasswordInput.send_keys("Kjstar36!!")

    self.driver.hide_keyboard()

    startBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "시작하기")
    startBtn.click()

def mobilePlaceSetting(self, mobileNumber):
    login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
    login_button.click()

    phone_input_box = self.driver.find_element(AppiumBy.XPATH, phoneNumberInputBox)
    phone_input_box.click()
    phone_input_box.send_keys("01020905304")

    password_input_box = self.driver.find_element(AppiumBy.XPATH, passwordInputBox)
    password_input_box.click()
    password_input_box.send_keys("Kjstar36!!")

    login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
    login_button.click()

    placeMove = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "지문 카드 테스트")
    placeMove.click()
    time.sleep(0.5)

    placeInput = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
    placeInput.click()
    placeInput.send_keys("비디오 공간")

    placeSeachBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='비디오 공간']/following-sibling::*[1][self::android.widget.ImageView]")
    placeSeachBtn.click()

    placeSel = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ImageView")
    placeSel.click()
    time.sleep(0.3)

    placeSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
    placeSetting.click()

    adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
    adminInvite.click()

    mobileInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력")
    mobileInvite.click()

    mobileInputBox = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
    mobileInputBox.click()
    mobileInputBox.clear()
    mobileInputBox.send_keys(mobileNumber)

    inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
    inviteBtn.click()
    time.sleep(1)

    for _ in range(3):
        self.driver.press_keycode(4)
        time.sleep(1)

    logoutBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, logout)
    logoutBtn.click()

    confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
    confirmBtn.click()

def emailPlaceSetting(self, emailAdress):
    login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
    login_button.click()

    email_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='이메일 주소']/following-sibling::*[1][self::android.widget.EditText]")
    email_input_box.click()
    email_input_box.send_keys("kjjung+p1@suprema.co.kr")

    password_input_box = self.driver.find_element(AppiumBy.XPATH, emailPasswordInputBox)
    password_input_box.click()
    password_input_box.send_keys("Kjstar36!!")

    login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
    login_button.click()

    authCode(self, emailAdress)

    self.driver.hide_keyboard()

    authApply = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
    authApply.click()

    placeMove = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "지문 카드 테스트")
    placeMove.click()
    time.sleep(0.5)

    placeInput = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
    placeInput.click()
    placeInput.send_keys("비디오 공간")

    placeSeachBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='비디오 공간']/following-sibling::*[1][self::android.widget.ImageView]")
    placeSeachBtn.click()

    placeSel = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ImageView")
    placeSel.click()
    time.sleep(0.3)

    placeSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
    placeSetting.click()

    adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
    adminInvite.click()

    emailInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일")
    emailInvite.click()

    emailInputBox = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
    emailInputBox.click()
    emailInputBox.send_keys(emailAdress)

    inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
    inviteBtn.click()
    time.sleep(1)

    for _ in range(3):
        self.driver.press_keycode(4)

    logoutBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, logout)
    logoutBtn.click()

    confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
    confirmBtn.click()

def passwordValidtion(self):
    input = "//android.widget.ScrollView/android.widget.EditText[2]"
    passInput1 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput1.click()
    passInput1.send_keys("Suprem!")

    lookBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='•••••••']/following-sibling::*[1][self::android.widget.ImageView]")
    lookBtn.click()
    pass1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprem!']")
    text1 = pass1.get_attribute('text')
    print(f"추출한 text 값 : {text1}")
    self.assertEqual(text1, "Suprem!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.").is_displayed()
    errorText1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.']")
    contentDesc1 = errorText1.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc1}")
    self.assertEqual(contentDesc1, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.")

    passInput1.clear()
    print("--------------- 비밀번호 Suprem! 완료")

    passInput2 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput2.click()
    passInput2.send_keys("Suprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!")

    pass2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!']")
    text2 = pass2.get_attribute('text')
    print(f"추출한 text 값 : {text2}")
    self.assertEqual(text2, "Suprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.").is_displayed()
    errorText2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.']")
    contentDesc2 = errorText2.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc2}")
    self.assertEqual(contentDesc2, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.")

    passInput2.clear()
    print("--------------- 비밀번호 Suprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100! 완료")

    passInput3 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput3.click()
    passInput3.send_keys("suprema-100!")

    pass3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='suprema-100!']")
    text3 = pass3.get_attribute('text')
    print(f"추출한 text 값 : {text3}")
    self.assertEqual(text3, "suprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.").is_displayed()
    errorText3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.']")
    contentDesc3 = errorText3.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc3}")
    self.assertEqual(contentDesc3, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.")

    passInput3.clear()
    print("---------------  비밀번호 suprema-100! 완료")

    passInput4 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput4.click()
    passInput4.send_keys("SUPREMA-100!")

    pass4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='SUPREMA-100!']")
    text4 = pass4.get_attribute('text')
    print(f"추출한 text 값 : {text4}")
    self.assertEqual(text4, "SUPREMA-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.").is_displayed()
    errorText4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.']")
    contentDesc4 = errorText4.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc4}")
    self.assertEqual(contentDesc4, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.")

    passInput4.clear()
    print("--------------- 비밀번호 SUPREMA-100! 완료")

    passInput5 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput5.click()
    passInput5.send_keys("Suprema!")

    pass5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprema!']")
    text5 = pass5.get_attribute('text')
    print(f"추출한 text 값 : {text5}")
    self.assertEqual(text5, "Suprema!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.").is_displayed()
    errorText5 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.']")
    contentDesc5 = errorText5.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc5}")
    self.assertEqual(contentDesc5, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.")

    passInput5.clear()
    print("--------------- 비밀번호 Suprema! 완료")

    passInput6 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput6.click()
    passInput6.send_keys("Suprema100")

    pass6 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprema100']")
    text6 = pass6.get_attribute('text')
    print(f"추출한 text 값 : {text6}")
    self.assertEqual(text6, "Suprema100")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.").is_displayed()
    errorText6 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.']")
    contentDesc6 = errorText6.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc6}")
    self.assertEqual(contentDesc6, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.")

    passInput6.clear()
    print("--------------- 비밀번호 Suprema100 완료")

    passInput7 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput7.click()
    passInput7.send_keys("Suprema-123!")

    pass7 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprema-123!']")
    text7 = pass7.get_attribute('text')
    print(f"추출한 text 값 : {text7}")
    self.assertEqual(text7, "Suprema-123!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)").is_displayed()
    errorText7 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)']")
    contentDesc7 = errorText7.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc7}")
    self.assertEqual(contentDesc7, "연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)")

    passInput7.clear()
    print("--------------- 비밀번호 Suprema-123! 완료")

    passInput8 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput8.click()
    passInput8.send_keys("ABCSuprema-100!")

    pass8 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='ABCSuprema-100!']")
    text8 = pass8.get_attribute('text')
    print(f"추출한 text 값 : {text8}")
    self.assertEqual(text8, "ABCSuprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)").is_displayed()
    errorText8 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)']")
    contentDesc8 = errorText8.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc8}")
    self.assertEqual(contentDesc8, "연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)")

    passInput8.clear()
    print("--------------- 비밀번호 ABCSuprema-100! 완료")

    passInput9 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput9.click()
    passInput9.send_keys("abcSuprema-100!")

    pass9 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='abcSuprema-100!']")
    text9 = pass9.get_attribute('text')
    print(f"추출한 text 값 : {text9}")
    self.assertEqual(text9, "abcSuprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)").is_displayed()
    errorText9 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)']")
    contentDesc9 = errorText9.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc9}")
    self.assertEqual(contentDesc9, "연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)")

    passInput9.clear()
    print("--------------- 비밀번호 abcSuprema-100! 완료")

    passInput10 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput10.click()
    passInput10.send_keys("SSSuprema-100!")

    pass10 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='SSSuprema-100!']")
    text10 = pass10.get_attribute('text')
    print(f"추출한 text 값 : {text10}")
    self.assertEqual(text10, "SSSuprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "동일 문자 3번 이상 연속 반복할 수 없습니다.").is_displayed()
    errorText10 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='동일 문자 3번 이상 연속 반복할 수 없습니다.']")
    contentDesc10 = errorText10.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc10}")
    self.assertEqual(contentDesc10, "동일 문자 3번 이상 연속 반복할 수 없습니다.")

    passInput10.clear()
    print("--------------- 비밀번호 SSSuprema-100! 완료")

    passInput11 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput11.click()
    passInput11.send_keys("Suprema-111!")

    pass11 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprema-111!']")
    text11 = pass11.get_attribute('text')
    print(f"추출한 text 값 : {text11}")
    self.assertEqual(text11, "Suprema-111!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "동일 문자 3번 이상 연속 반복할 수 없습니다.").is_displayed()
    errorText11 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='동일 문자 3번 이상 연속 반복할 수 없습니다.']")
    contentDesc11 = errorText11.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc11}")
    self.assertEqual(contentDesc11, "동일 문자 3번 이상 연속 반복할 수 없습니다.")

    passInput11.clear()
    print("--------------- 비밀번호 Suprema-111! 완료")

    passInput12 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput12.click()
    passInput12.send_keys("sssSuprema-100!")

    pass12 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='sssSuprema-100!']")
    text12 = pass12.get_attribute('text')
    print(f"추출한 text 값 : {text12}")
    self.assertEqual(text12, "sssSuprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "동일 문자 3번 이상 연속 반복할 수 없습니다.").is_displayed()
    errorText12 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='동일 문자 3번 이상 연속 반복할 수 없습니다.']")
    contentDesc12 = errorText12.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc12}")
    self.assertEqual(contentDesc12, "동일 문자 3번 이상 연속 반복할 수 없습니다.")

    passInput12.clear()
    print("--------------- 비밀번호 sssSuprema-100! 완료")

def RePasswordValidtion(self):

    input2 = "//android.widget.ScrollView/android.widget.EditText[3]"

    passInput1 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput1.click()
    passInput1.send_keys("Suprem!")

    lookBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='•••••••']/following-sibling::*[1][self::android.widget.ImageView]")
    lookBtn.click()
    pass1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprem!']")
    text1 = pass1.get_attribute('text')
    print(f"추출한 text 값 : {text1}")
    self.assertEqual(text1, "Suprem!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.").is_displayed()
    errorText1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.']")
    contentDesc1 = errorText1.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc1}")
    self.assertEqual(contentDesc1, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.")

    passInput1.clear()
    print("--------------- 비밀번호 Suprem! 완료")

    passInput2 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput2.click()
    passInput2.send_keys("Suprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!")

    pass2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!']")
    text2 = pass2.get_attribute('text')
    print(f"추출한 text 값 : {text2}")
    self.assertEqual(text2, "Suprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.").is_displayed()
    errorText2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.']")
    contentDesc2 = errorText2.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc2}")
    self.assertEqual(contentDesc2, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.")

    passInput2.clear()
    print("--------------- 비밀번호 Suprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100! 완료")

    passInput3 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput3.click()
    passInput3.send_keys("suprema-100!")

    pass3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='suprema-100!']")
    text3 = pass3.get_attribute('text')
    print(f"추출한 text 값 : {text3}")
    self.assertEqual(text3, "suprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.").is_displayed()
    errorText3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.']")
    contentDesc3 = errorText3.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc3}")
    self.assertEqual(contentDesc3, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.")

    passInput3.clear()
    print("---------------  비밀번호 suprema-100! 완료")

    passInput4 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput4.click()
    passInput4.send_keys("SUPREMA-100!")

    pass4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='SUPREMA-100!']")
    text4 = pass4.get_attribute('text')
    print(f"추출한 text 값 : {text4}")
    self.assertEqual(text4, "SUPREMA-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.").is_displayed()
    errorText4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.']")
    contentDesc4 = errorText4.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc4}")
    self.assertEqual(contentDesc4, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.")

    passInput4.clear()
    print("--------------- 비밀번호 SUPREMA-100! 완료")

    passInput5 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput5.click()
    passInput5.send_keys("Suprema!")

    pass5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprema!']")
    text5 = pass5.get_attribute('text')
    print(f"추출한 text 값 : {text5}")
    self.assertEqual(text5, "Suprema!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.").is_displayed()
    errorText5 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.']")
    contentDesc5 = errorText5.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc5}")
    self.assertEqual(contentDesc5, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.")

    passInput5.clear()
    print("--------------- 비밀번호 Suprema! 완료")

    passInput6 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput6.click()
    passInput6.send_keys("Suprema100")

    pass6 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprema100']")
    text6 = pass6.get_attribute('text')
    print(f"추출한 text 값 : {text6}")
    self.assertEqual(text6, "Suprema100")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.").is_displayed()
    errorText6 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.']")
    contentDesc6 = errorText6.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc6}")
    self.assertEqual(contentDesc6, "8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.")

    passInput6.clear()
    print("--------------- 비밀번호 Suprema100 완료")

    passInput7 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput7.click()
    passInput7.send_keys("Suprema-123!")

    pass7 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprema-123!']")
    text7 = pass7.get_attribute('text')
    print(f"추출한 text 값 : {text7}")
    self.assertEqual(text7, "Suprema-123!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)").is_displayed()
    errorText7 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)']")
    contentDesc7 = errorText7.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc7}")
    self.assertEqual(contentDesc7, "연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)")

    passInput7.clear()
    print("--------------- 비밀번호 Suprema-123! 완료")

    passInput8 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput8.click()
    passInput8.send_keys("ABCSuprema-100!")

    pass8 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='ABCSuprema-100!']")
    text8 = pass8.get_attribute('text')
    print(f"추출한 text 값 : {text8}")
    self.assertEqual(text8, "ABCSuprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)").is_displayed()
    errorText8 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)']")
    contentDesc8 = errorText8.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc8}")
    self.assertEqual(contentDesc8, "연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)")

    passInput8.clear()
    print("--------------- 비밀번호 ABCSuprema-100! 완료")

    passInput9 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput9.click()
    passInput9.send_keys("abcSuprema-100!")

    pass9 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='abcSuprema-100!']")
    text9 = pass9.get_attribute('text')
    print(f"추출한 text 값 : {text9}")
    self.assertEqual(text9, "abcSuprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)").is_displayed()
    errorText9 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)']")
    contentDesc9 = errorText9.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc9}")
    self.assertEqual(contentDesc9, "연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)")

    passInput9.clear()
    print("--------------- 비밀번호 abcSuprema-100! 완료")

    passInput10 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput10.click()
    passInput10.send_keys("SSSuprema-100!")

    pass10 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='SSSuprema-100!']")
    text10 = pass10.get_attribute('text')
    print(f"추출한 text 값 : {text10}")
    self.assertEqual(text10, "SSSuprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "동일 문자 3번 이상 연속 반복할 수 없습니다.").is_displayed()
    errorText10 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='동일 문자 3번 이상 연속 반복할 수 없습니다.']")
    contentDesc10 = errorText10.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc10}")
    self.assertEqual(contentDesc10, "동일 문자 3번 이상 연속 반복할 수 없습니다.")

    passInput10.clear()
    print("--------------- 비밀번호 SSSuprema-100! 완료")

    passInput11 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput11.click()
    passInput11.send_keys("Suprema-111!")

    pass11 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprema-111!']")
    text11 = pass11.get_attribute('text')
    print(f"추출한 text 값 : {text11}")
    self.assertEqual(text11, "Suprema-111!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "동일 문자 3번 이상 연속 반복할 수 없습니다.").is_displayed()
    errorText11 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='동일 문자 3번 이상 연속 반복할 수 없습니다.']")
    contentDesc11 = errorText11.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc11}")
    self.assertEqual(contentDesc11, "동일 문자 3번 이상 연속 반복할 수 없습니다.")

    passInput11.clear()
    print("--------------- 비밀번호 Suprema-111! 완료")

    passInput12 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput12.click()
    passInput12.send_keys("sssSuprema-100!")

    pass12 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='sssSuprema-100!']")
    text12 = pass12.get_attribute('text')
    print(f"추출한 text 값 : {text12}")
    self.assertEqual(text12, "sssSuprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "동일 문자 3번 이상 연속 반복할 수 없습니다.").is_displayed()
    errorText12 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='동일 문자 3번 이상 연속 반복할 수 없습니다.']")
    contentDesc12 = errorText12.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc12}")
    self.assertEqual(contentDesc12, "동일 문자 3번 이상 연속 반복할 수 없습니다.")

    passInput12.clear()
    print("--------------- 비밀번호 sssSuprema-100! 완료")

def resetPasswordValidtion(self):

    element = self.driver.find_element(AppiumBy.XPATH,  "//android.view.View[contains(@content-desc, '휴대폰 번호') and contains(@content-desc, '비밀번호')and contains(@content-desc, '비밀번호 재입력')]")

    content = element.get_attribute('contentDescription')

    match = re.search(r'휴대폰 번호\n(\d+)\n비밀번호\n비밀번호 재입력', content)
    if  match:
        phone_number = match.group(1)
        print(f"추출한 휴대폰 번호: {phone_number}")

    input = f"//android.view.View[@content-desc='휴대폰 번호\n{phone_number}\n비밀번호\n비밀번호 재입력']/android.widget.EditText[1]"

    passInput1 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput1.click()
    passInput1.send_keys("Suprem!")

    lookBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='•••••••']/following-sibling::*[1][self::android.widget.ImageView]")
    lookBtn.click()
    pass1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprem!']")
    text1 = pass1.get_attribute('text')
    print(f"추출한 text 값 : {text1}")
    self.assertEqual(text1, "Suprem!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.\n비밀번호 재입력").is_displayed()

    passInput1.clear()

    print("--------------- 비밀번호 Suprem! 완료")

    passInput2 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput2.click()
    passInput2.send_keys("Suprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!")

    pass2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!']")
    text2 = pass2.get_attribute('text')
    print(f"추출한 text 값 : {text2}")
    self.assertEqual(text2, "Suprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.\n비밀번호 재입력").is_displayed()

    passInput2.clear()

    print("--------------- 비밀번호 Suprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100! 완료")

    passInput3 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput3.click()
    passInput3.send_keys("suprema-100!")

    pass3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='suprema-100!']")
    text3 = pass3.get_attribute('text')
    print(f"추출한 text 값 : {text3}")
    self.assertEqual(text3, "suprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.\n비밀번호 재입력").is_displayed()

    passInput3.clear()

    print("---------------  비밀번호 suprema-100! 완료")

    passInput4 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput4.click()
    passInput4.send_keys("SUPREMA-100!")

    pass4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='SUPREMA-100!']")
    text4 = pass4.get_attribute('text')
    print(f"추출한 text 값 : {text4}")
    self.assertEqual(text4, "SUPREMA-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.\n비밀번호 재입력").is_displayed()

    passInput4.clear()

    print("--------------- 비밀번호 SUPREMA-100! 완료")

    passInput5 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput5.click()
    passInput5.send_keys("Suprema!")

    pass5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprema!']")
    text5 = pass5.get_attribute('text')
    print(f"추출한 text 값 : {text5}")
    self.assertEqual(text5, "Suprema!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.\n비밀번호 재입력").is_displayed()

    passInput5.clear()

    print("--------------- 비밀번호 Suprema! 완료")

    passInput6 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput6.click()
    passInput6.send_keys("Suprema100")

    pass6 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprema100']")
    text6 = pass6.get_attribute('text')
    print(f"추출한 text 값 : {text6}")
    self.assertEqual(text6, "Suprema100")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.\n비밀번호 재입력").is_displayed()

    passInput6.clear()
    print("--------------- 비밀번호 Suprema100 완료")

    passInput7 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput7.click()
    passInput7.send_keys("Suprema-123!")

    pass7 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprema-123!']")
    text7 = pass7.get_attribute('text')
    print(f"추출한 text 값 : {text7}")
    self.assertEqual(text7, "Suprema-123!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)\n비밀번호 재입력").is_displayed()

    passInput7.clear()

    print("--------------- 비밀번호 Suprema-123! 완료")

    passInput8 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput8.click()
    passInput8.send_keys("ABCSuprema-100!")

    pass8 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='ABCSuprema-100!']")
    text8 = pass8.get_attribute('text')
    print(f"추출한 text 값 : {text8}")
    self.assertEqual(text8, "ABCSuprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)\n비밀번호 재입력").is_displayed()

    passInput8.clear()

    print("--------------- 비밀번호 ABCSuprema-100! 완료")

    passInput9 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput9.click()
    passInput9.send_keys("abcSuprema-100!")

    pass9 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='abcSuprema-100!']")
    text9 = pass9.get_attribute('text')
    print(f"추출한 text 값 : {text9}")
    self.assertEqual(text9, "abcSuprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)\n비밀번호 재입력").is_displayed()

    passInput9.clear()

    print("--------------- 비밀번호 abcSuprema-100! 완료")

    passInput10 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput10.click()
    passInput10.send_keys("SSSuprema-100!")

    pass10 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='SSSuprema-100!']")
    text10 = pass10.get_attribute('text')
    print(f"추출한 text 값 : {text10}")
    self.assertEqual(text10, "SSSuprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n동일 문자 3번 이상 연속 반복할 수 없습니다.\n비밀번호 재입력").is_displayed()

    passInput10.clear()

    print("--------------- 비밀번호 SSSuprema-100! 완료")

    passInput11 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput11.click()
    passInput11.send_keys("Suprema-111!")

    pass11 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprema-111!']")
    text11 = pass11.get_attribute('text')
    print(f"추출한 text 값 : {text11}")
    self.assertEqual(text11, "Suprema-111!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n동일 문자 3번 이상 연속 반복할 수 없습니다.\n비밀번호 재입력").is_displayed()

    passInput11.clear()

    print("--------------- 비밀번호 Suprema-111! 완료")

    passInput12 = self.driver.find_element(AppiumBy.XPATH, input)
    passInput12.click()
    passInput12.send_keys("sssSuprema-100!")

    pass12 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='sssSuprema-100!']")
    text12 = pass12.get_attribute('text')
    print(f"추출한 text 값 : {text12}")
    self.assertEqual(text12, "sssSuprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n동일 문자 3번 이상 연속 반복할 수 없습니다.\n비밀번호 재입력").is_displayed()

    passInput12.clear()

    print("--------------- 비밀번호 sssSuprema-100! 완료")

def resetRePasswordValidtion(self):

    element = self.driver.find_element(AppiumBy.XPATH,  "//android.view.View[contains(@content-desc, '휴대폰 번호') and contains(@content-desc, '비밀번호')and contains(@content-desc, '비밀번호 재입력')]")

    content = element.get_attribute('contentDescription')

    match = re.search(r'휴대폰 번호\n(\d+)\n비밀번호\n비밀번호 재입력', content)
    if  match:
        phone_number = match.group(1)
        print(f"추출한 휴대폰 번호: {phone_number}")

    input2 = f"//android.view.View[@content-desc='휴대폰 번호\n{phone_number}\n비밀번호\n비밀번호 재입력']/android.widget.EditText[2]"
    passInput1 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput1.click()
    passInput1.send_keys("Suprem!")

    lookBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='•••••••']/following-sibling::*[1][self::android.widget.ImageView]")
    lookBtn.click()
    pass1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprem!']")
    text1 = pass1.get_attribute('text')
    print(f"추출한 text 값 : {text1}")
    self.assertEqual(text1, "Suprem!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n비밀번호 재입력\n8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.").is_displayed()

    passInput1.clear()

    print("--------------- 비밀번호 Suprem! 완료")

    passInput2 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput2.click()
    passInput2.send_keys("Suprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!")

    pass2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!']")
    text2 = pass2.get_attribute('text')
    print(f"추출한 text 값 : {text2}")
    self.assertEqual(text2, "Suprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n비밀번호 재입력\n8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.").is_displayed()

    passInput2.clear()

    print("--------------- 비밀번호 Suprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100!uprema-100! 완료")

    passInput3 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput3.click()
    passInput3.send_keys("suprema-100!")

    pass3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='suprema-100!']")
    text3 = pass3.get_attribute('text')
    print(f"추출한 text 값 : {text3}")
    self.assertEqual(text3, "suprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n비밀번호 재입력\n8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.").is_displayed()

    passInput3.clear()

    print("---------------  비밀번호 suprema-100! 완료")

    passInput4 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput4.click()
    passInput4.send_keys("SUPREMA-100!")

    pass4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='SUPREMA-100!']")
    text4 = pass4.get_attribute('text')
    print(f"추출한 text 값 : {text4}")
    self.assertEqual(text4, "SUPREMA-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n비밀번호 재입력\n8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.").is_displayed()

    passInput4.clear()

    print("--------------- 비밀번호 SUPREMA-100! 완료")

    passInput5 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput5.click()
    passInput5.send_keys("Suprema!")

    pass5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprema!']")
    text5 = pass5.get_attribute('text')
    print(f"추출한 text 값 : {text5}")
    self.assertEqual(text5, "Suprema!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n비밀번호 재입력\n8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.").is_displayed()

    passInput5.clear()

    print("--------------- 비밀번호 Suprema! 완료")

    passInput6 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput6.click()
    passInput6.send_keys("Suprema100")

    pass6 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprema100']")
    text6 = pass6.get_attribute('text')
    print(f"추출한 text 값 : {text6}")
    self.assertEqual(text6, "Suprema100")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n비밀번호 재입력\n8-32자, 대,소문자 영문, 숫자, 특수문자를 조합해주세요.").is_displayed()

    passInput6.clear()
    print("--------------- 비밀번호 Suprema100 완료")

    passInput7 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput7.click()
    passInput7.send_keys("Suprema-123!")

    pass7 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprema-123!']")
    text7 = pass7.get_attribute('text')
    print(f"추출한 text 값 : {text7}")
    self.assertEqual(text7, "Suprema-123!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n비밀번호 재입력\n연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)").is_displayed()

    passInput7.clear()

    print("--------------- 비밀번호 Suprema-123! 완료")

    passInput8 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput8.click()
    passInput8.send_keys("ABCSuprema-100!")

    pass8 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='ABCSuprema-100!']")
    text8 = pass8.get_attribute('text')
    print(f"추출한 text 값 : {text8}")
    self.assertEqual(text8, "ABCSuprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n비밀번호 재입력\n연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)").is_displayed()

    passInput8.clear()

    print("--------------- 비밀번호 ABCSuprema-100! 완료")

    passInput9 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput9.click()
    passInput9.send_keys("abcSuprema-100!")

    pass9 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='abcSuprema-100!']")
    text9 = pass9.get_attribute('text')
    print(f"추출한 text 값 : {text9}")
    self.assertEqual(text9, "abcSuprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n비밀번호 재입력\n연속된 문자를 사용할 수 없습니다. (예: 123, abc 등)").is_displayed()

    passInput9.clear()

    print("--------------- 비밀번호 abcSuprema-100! 완료")

    passInput10 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput10.click()
    passInput10.send_keys("SSSuprema-100!")

    pass10 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='SSSuprema-100!']")
    text10 = pass10.get_attribute('text')
    print(f"추출한 text 값 : {text10}")
    self.assertEqual(text10, "SSSuprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n비밀번호 재입력\n동일 문자 3번 이상 연속 반복할 수 없습니다.").is_displayed()

    passInput10.clear()

    print("--------------- 비밀번호 SSSuprema-100! 완료")

    passInput11 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput11.click()
    passInput11.send_keys("Suprema-111!")

    pass11 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Suprema-111!']")
    text11 = pass11.get_attribute('text')
    print(f"추출한 text 값 : {text11}")
    self.assertEqual(text11, "Suprema-111!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n비밀번호 재입력\n동일 문자 3번 이상 연속 반복할 수 없습니다.").is_displayed()

    passInput11.clear()

    print("--------------- 비밀번호 Suprema-111! 완료")

    passInput12 = self.driver.find_element(AppiumBy.XPATH, input2)
    passInput12.click()
    passInput12.send_keys("sssSuprema-100!")

    pass12 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='sssSuprema-100!']")
    text12 = pass12.get_attribute('text')
    print(f"추출한 text 값 : {text12}")
    self.assertEqual(text12, "sssSuprema-100!")

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_number}\n비밀번호\n비밀번호 재입력\n동일 문자 3번 이상 연속 반복할 수 없습니다.").is_displayed()

    passInput12.clear()

    print("--------------- 비밀번호 sssSuprema-100! 완료")


def leaveAdmin(self):

    print("------------- 테스트 시나리오 종료, 회원탈퇴 시도")

    leadbutton = self.driver.find_element(AppiumBy.XPATH, lead)
    leadbutton.click()

    csctBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터")
    csctBtn.click()

    leavMB = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='안녕하세요.\n슈프리마 CLUe 서비스 고객센터 입니다.\n무엇을 도와드릴까요?\n운영시간 09:00 ~ 17:00\n(주말, 공휴일 제외)']/android.view.View[2]/android.widget.ImageView[3]")
    leavMB.click()

    assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='회원탈퇴'])[1]").is_displayed()
    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원탈퇴하시기 전에 꼭 읽어 보세요.\n모든 개인 정보는 지정된 보유 기간 후 자동 삭제됩니다.\n계정이 삭제된 후에는 계정을 살리거나 데이터를 복구 할 수 없습니다.\n공간의 유일한 메인 관리자인 경우 다른 사람에게 이관 후 회원탈퇴가 가능합니다.").is_displayed()

    start_x = 135
    start_y = 2010

    end_x = 982
    end_y = 2010

    actions = ActionChains(self.driver)
    actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)  # 100ms 대기
    actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원탈퇴").is_displayed()
    deleteAccountMsg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='회원탈퇴 성공하였습니다.\n로그인 페이지로 이동합니다.']")
    contentDesc = deleteAccountMsg.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc}")
    self.assertEqual(contentDesc, "회원탈퇴 성공하였습니다.\n로그인 페이지로 이동합니다.")
    confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
    confirmBtn.click()

    print("------------------- 임의 폰번호로 회원가입된 계정 탈퇴 성공")

def email_login(self, emailInput, passwordInput):

    login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
    login_button.click()

    email_input_box = self.driver.find_element(AppiumBy.XPATH, emailInputBox)
    email_input_box.click()
    email_input_box.send_keys(emailInput)

    password_input_box = self.driver.find_element(AppiumBy.XPATH, emailPasswordInputBox)
    password_input_box.click()
    password_input_box.send_keys(passwordInput)

    login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
    login_button.click()
    time.sleep(2)

    authCode(self, emailInput)

    self.driver.hide_keyboard()

    authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
    authBtn.click()
    time.sleep(3)

def mobile_login(self, mobileInput, passwordInput):
    login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
    login_button.click()

    phone_input_box = self.driver.find_element(AppiumBy.XPATH, phoneNumberInputBox)
    phone_input_box.click()
    phone_input_box.send_keys(mobileInput)

    password_input_box = self.driver.find_element(AppiumBy.XPATH, passwordInputBox)
    password_input_box.click()
    password_input_box.send_keys(passwordInput)

    login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
    login_button.click()
    time.sleep(2)

def toggle_click(self, menuXpath):

    menu = self.driver.find_element(AppiumBy.XPATH, f"{menuXpath}")

    before_status = menu.get_attribute("checked")
    print("현재 토글 상태:", before_status)

    menu.click()
    print("클릭함")
    time.sleep(2)

    after_status = menu.get_attribute("checked")
    print("토글 클릭 후 상태:", after_status)

    #상태 검증 -> 활성화 이면 비활성화 / 비활성화 이면 활성화
    if before_status == "true" and after_status == "false":
        print("토글이 활성화 -> 비활성화로 변경 되었습니다.")
    elif before_status == "false" and after_status == "true":
        print("토글이 비활성화 -> 활성화로 변경 되었습니다.")
    else:
        print("토글 상태가 예상과 다릅니다. (변경 실패)")
        assert False, f"토글 상태 변경 실패: before={before_status}, after={after_status}"



def toggle_status(self, menuXpath1, menuXpath2, menuXpath3, menuXpath4, location):
    def get_status(xpath):
        try:
            el = self.driver.find_element(AppiumBy.XPATH, xpath)
            status = el.get_attribute("checked")
            print(f"[{xpath}] 상태 :", status)
            return  status
        except NoSuchElementException:
            print(f"[{xpath}] 화면에 없음 -> 다음 수행")
            return None

    status1 = get_status(menuXpath1) if menuXpath1 else None
    status2 = get_status(menuXpath2) if menuXpath2 else None
    status3 = get_status(menuXpath3) if menuXpath3 else None
    status4 = get_status(menuXpath4) if menuXpath4 else None

    backBtn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
    backBtn.click()

    alramMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, location)
    alramMenu.click()


    reStatus1 = get_status(menuXpath1) if menuXpath1 else None
    reStatus2 = get_status(menuXpath2) if menuXpath2 else None
    reStatus3 = get_status(menuXpath3) if menuXpath3 else None
    reStatus4 = get_status(menuXpath4) if menuXpath4 else None

    if status1 is not None: assert status1 == reStatus1
    if status2 is not None: assert status2 == reStatus2
    if status3 is not None: assert status3 == reStatus3
    if status4 is not None: assert status4 == reStatus4

def signUp_mobile(self, phoneNum, name, password, rePassword):

    signUpBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
    signUpBtn.click()

    agreeAll = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "약관 전체 동의")
    agreeAll.click()

    nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
    is_enabled = nextBtn.get_attribute("enabled")
    self.assertEqual(is_enabled, "true", "인증완료 버튼 활성화")
    nextBtn.click()

    #모바일 회원 가입
    mobileBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "모바일")
    mobileBtn.click()

    mobileInput = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
    mobileInput.click()
    mobileInput.send_keys(phoneNum)

    AuthReqestBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청")
    is_enabled = AuthReqestBtn.get_attribute("enabled")
    self.assertEqual(is_enabled, "true", "인증요청 버튼 활성화")
    AuthReqestBtn.click()
    time.sleep(1)

    authCode_mobile(self, phoneNum)
    time.sleep(0.5)

    atBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
    is_enabled = atBtn.get_attribute("enabled")
    self.assertEqual(is_enabled, "true", "인증완료 버튼 활성화")
    atBtn.click()

    nameInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[1]")
    nameInput.click()
    nameInput.send_keys(name)

    passwordInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[2]")
    passwordInput.click()
    passwordInput.send_keys(password)

    rePasswordInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[3]")
    rePasswordInput.click()
    rePasswordInput.send_keys(rePassword)

    self.driver.back()
    start_x1 = 519
    start_y1 = 1351
    end_x1 = 519
    end_y1 = 1305
    self.driver.swipe(start_x1, start_y1, end_x1, end_y1)

    signUpCompleteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "시작하기")
    is_enabled = signUpCompleteBtn.get_attribute("enabled")
    self.assertEqual(is_enabled, "true", "시작하기 버튼 활성화")
    signUpCompleteBtn.click()
    time.sleep(2)


def get_current_hour(self):
    return datetime.datetime.now().strftime('%H')

def get_current_min(self):
    return datetime.datetime.now().strftime('%M')

def backBtn(self):
    #뒤로가기 후 사용자 상세 재 진입
    self.driver.tap([(68, 174)])
    time.sleep(1)

def user_invite_phone(self, name, phone_num):

    inviteBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='초대하기']")
    inviteBtn.click()

    # 인증 수단 - 휴대폰 번호(QR)로 사용자 초대
    user_qr = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호")
    user_qr.click()

    add_user = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
    add_user.click()

    name_input = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.widget.EditText[1]")
    name_input.click()
    name_input.send_keys(name)

    phone_input = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.widget.EditText[2]")
    phone_input.click()
    phone_input.send_keys(phone_num)

    next_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
    next_Btn.click()

    invite_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대")
    invite_Btn.click()
    time.sleep(1)

    # 초대 결과(출입 권한) 화면의 '확인' → 사용자 목록으로 돌아올 때까지 재시도 (서버 응답 지연 대비)
    self.driver.implicitly_wait(2)
    try:
        for _ in range(5):
            if self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "사용자 목록"):
                break
            for btn in self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "확인"):
                if btn.is_displayed():
                    btn.click()
                    break
            time.sleep(1)
        else:
            raise NoSuchElementException("초대 후 사용자 목록 화면으로 돌아오지 못했습니다.")
    finally:
        self.driver.implicitly_wait(10)
    time.sleep(1)

def user_delete(self):

    user_modity = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
    user_modity.click()

    # 등록순 목록의 마지막 = 방금 초대한 테스트 사용자 (기존 [2]는 '정국진'이 첫 번째에 있다는 전제)
    user_delete = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[last()]")
    user_delete.click()

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 제외")
    delete_pop = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='해당 사용자를 이 공간에서 제외하시겠습니까?']")
    contentDesc = delete_pop.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc}")
    self.assertEqual(contentDesc, "해당 사용자를 이 공간에서 제외하시겠습니까?")

    confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
    confirm_Btn.click()
    time.sleep(1)


# ---------------------------------------------------------------------------
# 사용자 상세 - 출입문 목록
# content-desc 예: "출입문\nBS3_538200888\n...\n모든 출입문은 해당 공간에 ... 반영 합니다."
# 하위 ImageView 는 행마다 [출입문 아이콘, X 버튼] 순서 → ImageView[2] = 첫 번째 행의 X 버튼
# 출입문 이름/순서는 서버 설정에 따라 바뀌므로 하드코딩하지 않는다.
# ---------------------------------------------------------------------------

USER_DOOR_SECTION = "//android.view.View[starts-with(@content-desc, '출입문\n')]"
ALL_DOOR_NOTICE = "모든 출입문은"


def user_door_list(self):
    """사용자 상세 화면의 출입문 이름 목록을 반환한다. (출입문이 없으면 빈 리스트)"""
    sections = self.driver.find_elements(AppiumBy.XPATH, USER_DOOR_SECTION)
    if not sections:
        return []
    lines = sections[0].get_attribute("content-desc").split("\n")[1:]
    # 출입문이 모두 삭제되면 우측 '모든 출입문' 버튼 문구가 content-desc 에 남으므로 제외
    return [line for line in lines
            if line and line != "모든 출입문" and not line.startswith(ALL_DOOR_NOTICE)]


def user_door_delete_first(self):
    """첫 번째 출입문의 X 버튼을 눌러 삭제하고, 삭제한 출입문 이름을 반환한다."""
    doors = user_door_list(self)
    if not doors:
        raise NoSuchElementException("삭제할 출입문이 없습니다.")
    self.driver.find_element(AppiumBy.XPATH, f"{USER_DOOR_SECTION}/android.widget.ImageView[2]").click()
    time.sleep(0.5)
    return doors[0]


# ---------------------------------------------------------------------------
# 공간 이동
# 로그인 직후 공간은 고정이 아님 (ID가 높은 공간 또는 마지막 사용 공간) → 필요한 공간으로 직접 이동
# ---------------------------------------------------------------------------

PLACE_HEADER_MAX_Y = 500  # 메인 화면 상단 공간 이름 영역 (Visitor Place1 [56,266], 비디오 공간 [56,201])


def _current_place_header(self):
    """메인 화면 상단의 공간 이름 요소를 반환 (x=56 에서 시작하고 y < 500 인 첫 요소)."""
    for el in self.driver.find_elements(AppiumBy.XPATH, "//*[@content-desc!='' and starts-with(@bounds, '[56,')]"):
        if el.rect["y"] < PLACE_HEADER_MAX_Y and el.is_displayed():
            return el
    raise NoSuchElementException("메인 화면에서 공간 이름 영역을 찾을 수 없습니다.")


def move_place(self, place_name, restore_wait=10):
    """place_name 공간으로 이동한다. 이미 해당 공간이면 아무것도 하지 않는다.

    공간 이름 선택 → 공간 선택 화면 → 목록에 있으면 바로 선택 / 없으면 검색 후 선택
    """
    self.driver.implicitly_wait(2)
    try:
        # 로그인 직후 메인 화면 로딩이 늦을 수 있어 공간 이름 영역을 최대 약 10초 대기
        header = None
        for _ in range(5):
            try:
                header = _current_place_header(self)
                break
            except NoSuchElementException:
                time.sleep(1)
        if header is None:
            capture_screenshot(self.driver, "move_place_no_header")
            header = _current_place_header(self)
        current = header.get_attribute("content-desc")
        if current == place_name:
            print(f"현재 공간: {current} (이동 불필요)")
            return
        print(f"현재 공간: {current} → {place_name} 이동")

        header.click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 선택")

        item_xpath = f"//*[starts-with(@content-desc, '{place_name}\nID')]"
        items = [el for el in self.driver.find_elements(AppiumBy.XPATH, item_xpath) if el.is_displayed()]
        if not items:
            search = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            search.click()
            search.send_keys(place_name)
            time.sleep(1)
            items = [el for el in self.driver.find_elements(AppiumBy.XPATH, item_xpath) if el.is_displayed()]
        if not items:
            raise NoSuchElementException(f"공간 목록/검색 결과에 '{place_name}' 공간이 없습니다. (계정 소속 공간 확인 필요)")

        # 이름 라벨은 눌러도 이동하지 않음 → 라벨 바로 위의 공간 이미지 선택
        r = items[0].rect
        self.driver.tap([(r["x"] + r["width"] // 2, r["y"] - 100)])

        moved = None
        for _ in range(10):  # 공간 메인 화면 로딩 대기 (최대 약 10초)
            time.sleep(1)
            try:
                moved = _current_place_header(self).get_attribute("content-desc")
            except NoSuchElementException:
                continue
            if moved == place_name:
                return
        raise AssertionError(f"공간 이동 실패: 기대={place_name}, 현재={moved}")
    finally:
        self.driver.implicitly_wait(restore_wait)



# ---------------------------------------------------------------------------
# 스와이프하며 요소 찾기 / 방해 금지 시간 휠 피커
# ---------------------------------------------------------------------------

def swipe_until_found(self, by, value, swipe, duration=200, max_swipes=10, click=False, required=True, restore_wait=10):
    """요소가 보일 때까지 swipe=(x1, y1, x2, y2) 로 스와이프한다.

    탐색 중에는 implicit wait 를 0 으로 둔다. (기존 루프는 못 찾을 때마다 implicit wait 10초를
    기다려 스와이프 1회당 10초 이상 걸렸음) 종료 시 restore_wait(setUp 값과 동일하게 10초)로 복구한다.
    ※ Appium 1.22 에서는 driver.timeouts 로 현재 값을 읽을 수 없어 복구 값을 인자로 받음
    """
    self.driver.implicitly_wait(0)
    try:
        for _ in range(max_swipes + 1):
            for el in self.driver.find_elements(by, value):
                if el.is_displayed():
                    if click:
                        el.click()
                    return el
            self.driver.swipe(*swipe, duration)
            time.sleep(0.3)
    finally:
        self.driver.implicitly_wait(restore_wait)
    if required:
        raise NoSuchElementException(f"스와이프 {max_swipes}회 후에도 찾을 수 없습니다: {value}")
    return None


# 방해 금지 시간 피커(2.2.0): SeekBar 4개 = [시작 시, 시작 분, 종료 시, 종료 분]
# content-desc 에 현재 선택값이 들어 있음 ("11 o'clock", "1 minute", "50 minutes")
# 휠 1칸 = 91px, 위로 드래그하면 값 증가
DND_WHEEL_ROW_PX = 91
DND_WHEEL_MAX_ROWS = 7  # 드래그 1회에 굴릴 최대 칸 수 (휠 영역 높이 안에서 움직이도록)


def _wheel_value(self, index):
    desc = self.driver.find_element(AppiumBy.XPATH, f"(//android.widget.SeekBar)[{index}]").get_attribute("content-desc")
    found = re.search(r"\d+", desc or "")
    if not found:
        raise Exception(f"휠 값을 읽을 수 없습니다: {desc!r}")
    return int(found.group())


def _wheel_drag(self, x, y_from, y_to):
    """관성(fling) 없이 정확한 거리만큼 굴리기: 천천히 이동 후 잠시 멈췄다가 손을 뗀다."""
    actions = ActionChains(self.driver)
    actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput("touch", "touch"))
    pointer = actions.w3c_actions.pointer_action
    pointer.move_to_location(x, y_from)
    pointer.pointer_down()
    actions.w3c_actions.pointer_action._duration = 300
    pointer.move_to_location(x, y_to)
    pointer.pause(0.3)
    pointer.release()
    actions.perform()
    time.sleep(0.3)


def set_wheel(self, index, target, modulo, max_drags=10):
    """index 번째(1부터) SeekBar 휠을 target 값으로 맞춘다. 순환 휠이므로 가까운 방향으로 굴린다."""
    bar = self.driver.find_element(AppiumBy.XPATH, f"(//android.widget.SeekBar)[{index}]")
    rect = bar.rect
    x = rect["x"] + rect["width"] // 2
    top = rect["y"] + 60
    bottom = rect["y"] + rect["height"] - 60

    for _ in range(max_drags):
        current = _wheel_value(self, index)
        diff = (target - current) % modulo
        if diff > modulo // 2:
            diff -= modulo
        if diff == 0:
            return
        rows = max(-DND_WHEEL_MAX_ROWS, min(DND_WHEEL_MAX_ROWS, diff))
        if rows > 0:   # 값 증가 → 위로 드래그
            _wheel_drag(self, x, bottom, bottom - rows * DND_WHEEL_ROW_PX)
        else:          # 값 감소 → 아래로 드래그
            _wheel_drag(self, x, top, top - rows * DND_WHEEL_ROW_PX)

    raise Exception(f"휠 {index} 값을 {target} 로 맞추지 못했습니다. (현재 {_wheel_value(self, index)})")


def open_dnd_picker(self):
    """방해 금지 시간 화면에서 시간 피커를 연다. (행 요소 click() 으로는 열리지 않아 행 오른쪽을 탭)"""
    row = self.driver.find_element(AppiumBy.XPATH, "//*[starts-with(@content-desc,'시작 시간')]")
    r = row.rect
    self.driver.tap([(r["x"] + int(r["width"] * 0.8), r["y"] + r["height"] // 2)])
    self.driver.find_element(AppiumBy.XPATH, "(//android.widget.SeekBar)[4]")


def set_dnd_time(self, start_hour, start_min, end_hour, end_min, confirm=True):
    """방해 금지 시간 피커를 열어 시작/종료 시간(24시간제)을 맞춘다. confirm=True 면 '확인'까지 누른다."""
    open_dnd_picker(self)
    set_wheel(self, 1, start_hour, 24)
    set_wheel(self, 2, start_min, 60)
    set_wheel(self, 3, end_hour, 24)
    set_wheel(self, 4, end_min, 60)
    print(f"방해 금지 시간 설정: {start_hour:02d}:{start_min:02d} ~ {end_hour:02d}:{end_min:02d}")
    if confirm:
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인").click()
        time.sleep(0.5)

