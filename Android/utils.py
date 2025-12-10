import re
import time
import datetime
import requests
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import os

from setuptools.command.build_ext import if_dl

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
phoneNumberInputBox = "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]"
passwordInputBox = "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[2]"
emailInputBox = "//android.widget.ImageView[@content-desc=\"이메일 주소\n비밀번호\"]/android.widget.EditText[1]"
emailPasswordInputBox = "//android.widget.ImageView[@content-desc=\"이메일 주소\n비밀번호\"]/android.widget.EditText[2]"
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

def authCode(self):
    self.driver.press_keycode(3)
    # 홈화면
    time.sleep(2)

    while True:
        if "outlook" not in self.driver.current_package:
            print("앱이 종료되어 다시 실행")
            self.driver.activate_app("com.microsoft.office.outlook")
            time.sleep(2)

        accountBtn = self.driver.find_element(AppiumBy.ID, "com.microsoft.office.outlook:id/account_button")
        accountBtn.click()

        clueBtn = self.driver.find_element(AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView[@resource-id='com.microsoft.office.outlook:id/drawer_folder_composable']/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[1]")
        clueBtn.click()
        time.sleep(7)

        for _ in range(3):  # 새로고침
            start_x1 = 573
            start_y1 = 291
            end_x1 = 573
            end_y1 = 1320
            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
            time.sleep(3)

        self.driver.tap([(497, 358)])
        time.sleep(2)

        MAX_RETRIES = 3
        WAIT_TIME = 3
        retries = 0

        while retries < MAX_RETRIES:
            elements = self.driver.find_elements(AppiumBy.XPATH, "//android.view.View[@text][1]")
            count = len(elements)

            if count >= 16:
                print(f"요소 {count}개 찾음. 모든 요소의 텍스트값 추출 시작")
                for i, el in enumerate(elements, start=1):
                    text_value = el.get_attribute("text")
                    print(f"요소 {i}의 텍스트 값: {text_value}")
                time.sleep(0.1)
                break

            print(f"현재 요소 {count}개 찾음. 16개 이상 찾을 때까지 재시도 중...({retries + 1}/{MAX_RETRIES}")
            time.sleep(WAIT_TIME)
            retries += 1

        else:
            print("최대 시도 횟수를 초과하였습니다. 요소를 충분히 찾지 못하였습니다.")
            self.driver.press_keycode(4)
            time.sleep(2)
            self.driver.tap([(497, 358)])
            time.sleep(2)

        self.driver.press_keycode(3)
        # 홈화면
        time.sleep(1)

        outlook_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Outlook")
        outlook_button.click()
        time.sleep(1)

        elements2 = self.driver.find_elements(AppiumBy.XPATH, "//android.view.View[@text][1]")
        print(f"현재 요소 {len(elements2)}개 찾음.")
        for i, el in enumerate(elements2, start=1):
            text_value = el.get_attribute("text")
            print(f"요소 {i}의 텍스트 값: {text_value}")

        # if len(elements2) >= 15:
        #     text_value = elements2[14].get_attribute("text")
        #     print("인증번호:", text_value)
        #     break
        # else:
        #     print("인증번호 없음")
        #     self.driver.press_keycode(4)
        #     time.sleep(2)

            match = re.fullmatch(r"\d{6}", text_value.strip())
            if match:
                auth_code = match.group()
                print("인증번호:", auth_code)
                break
        if auth_code:
            print("최종 인증번호: ", auth_code)
            break
        else:
            print("인증번호를 찾지 못했습니다.")
            self.driver.press_keycode(4)
            time.sleep(2)
            return

    officeBack = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "닫기")
    officeBack.click()
    time.sleep(1)

    self.driver.press_keycode(3)
    # 홈화면
    time.sleep(1)

    clue_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Suprema CLUe")
    clue_button.click()
    time.sleep(0.5)

    auth_input_box = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
    auth_input_box.click()
    auth_input_box.send_keys(auth_code)

def authCode_mobile(self):
    self.driver.press_keycode(3)
    #홈화면
    time.sleep(1)

    teamsApp_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Teams")
    teamsApp_button.click()

    for _ in range(2): #새로고침
        start_x1 = 573
        start_y1 = 291
        end_x1 = 573
        end_y1 = 559
        self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
        time.sleep(1)

    chSelete = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.microsoft.teams:id/textView' and @text='채널']")
    chSelete.click()

    mobileAuthCh = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.microsoft.teams:id/teams_channel_text' and @text='CLUe 인증 코드 수신채널']")
    mobileAuthCh.click()
    time.sleep(2)

    elements = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@content-desc]")

    for i, el in enumerate(elements, start=1):
        text_value1 = el.get_attribute("text")
        print(f"요소 {i}의 텍스트 값: {text_value1}")

    if elements:
        last_value = elements[-1].get_attribute("content-desc")
        print(f"마지막 요소의 content-desc 값: {last_value}")

        num_value = last_value[25:31]
        print(f"추출한 값: {num_value}")

    else:
        last_value = None
        print("요소가 없습니다..")

    teamsBack = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "뒤로")
    teamsBack.click()
    time.sleep(0.3)

    chSelete2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.microsoft.teams:id/textView' and @text='채널']")
    chSelete2.click()
    time.sleep(0.1)

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

    self.driver.press_keycode(3)
    # 홈화면
    time.sleep(1)

    while True:
        if "outlook" not in self.driver.current_package:
            print("앱이 종료되어 다시 실행")
            self.driver.activate_app("com.microsoft.office.outlook")
            time.sleep(2)

        accountBtn = self.driver.find_element(AppiumBy.ID, "com.microsoft.office.outlook:id/account_button")
        accountBtn.click()

        clueBtn = self.driver.find_element(AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView[@resource-id='com.microsoft.office.outlook:id/drawer_folder_composable']/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[1]")
        clueBtn.click()
        time.sleep(7)

        for _ in range(3):  # 새로고침
            start_x1 = 573
            start_y1 = 291
            end_x1 = 573
            end_y1 = 1320
            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
            time.sleep(3)

        self.driver.tap([(497, 358)])
        time.sleep(2)

        MAX_RETRIES = 3
        WAIT_TIME = 3
        retries = 0

        while retries < MAX_RETRIES:
            elements = self.driver.find_elements(AppiumBy.XPATH, "//android.view.View[@text][1]")
            count = len(elements)

            if count >= 16:
                print(f"요소 {count}개 찾음. 모든 요소의 텍스트값 추출 시작")
                time.sleep(0.1)
                break

            print(f"현재 요소 {count}개 찾음. 16개 이상 찾을 때까지 재시도 중...({retries + 1}/{MAX_RETRIES}")
            time.sleep(WAIT_TIME)
            retries += 1
        else:
            print("최대 시도 횟수를 초과하였습니다. 요소를 충분히 찾지 못하였습니다.")

        self.driver.press_keycode(3)
        # 홈화면
        time.sleep(1)

        outlook_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Outlook")
        outlook_button.click()
        time.sleep(1)

        elements2 = self.driver.find_elements(AppiumBy.XPATH, "//android.view.View[@text][1]")
        print(f"현재 요소 {len(elements2)}개 찾음.")
        for i, el in enumerate(elements2, start=1):
            text_value = el.get_attribute("text")
            print(f"요소 {i}의 텍스트 값: {text_value}")

        # if len(elements2) >= 15:
        #     text_value = elements2[14].get_attribute("text")
        #     print("인증번호:", text_value)
        #     break
        # else:
        #     print("인증번호 없음")
        #     self.driver.press_keycode(4)
        #     time.sleep(2)
            match = re.fullmatch(r"\d{6}", text_value.strip())
            if match:
                auth_code2 = match.group()
                print("인증번호:", auth_code2)
                break
        if auth_code2:
            print("최종 인증번호: ", auth_code2)
            break
        else:
            print("인증번호를 찾지 못했습니다.")
            self.driver.press_keycode(4)
            time.sleep(2)
            return

    officeBack = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "닫기")
    officeBack.click()
    time.sleep(1)

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

    self.driver.press_keycode(3)
    # 홈화면
    time.sleep(1)

    while True:
        if "outlook" not in self.driver.current_package:
            print("앱이 종료되어 다시 실행")
            self.driver.activate_app("com.microsoft.office.outlook")
            time.sleep(2)

        accountBtn = self.driver.find_element(AppiumBy.ID, "com.microsoft.office.outlook:id/account_button")
        accountBtn.click()

        clueBtn = self.driver.find_element(AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView[@resource-id='com.microsoft.office.outlook:id/drawer_folder_composable']/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[1]")
        clueBtn.click()
        time.sleep(7)

        for _ in range(3):  # 새로고침
            start_x1 = 573
            start_y1 = 291
            end_x1 = 573
            end_y1 = 1320
            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
            time.sleep(3)

        self.driver.tap([(497, 358)])
        time.sleep(2)

        MAX_RETRIES = 3
        WAIT_TIME = 3
        retries = 0

        while retries < MAX_RETRIES:
            elements = self.driver.find_elements(AppiumBy.XPATH, "//android.view.View[@text][1]")
            count = len(elements)

            if count >= 16:
             print(f"요소 {count}개 찾음. 모든 요소의 텍스트값 추출 시작")
             time.sleep(0.1)
             break

            print(f"현재 요소 {count}개 찾음. 16개 이상 찾을 때까지 재시도 중...({retries + 1}/{MAX_RETRIES}")
            time.sleep(WAIT_TIME)
            retries += 1
        else:
            print("최대 시도 횟수를 초과하였습니다. 요소를 충분히 찾지 못하였습니다.")

        self.driver.press_keycode(3)
        # 홈화면
        time.sleep(1)

        outlook_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Outlook")
        outlook_button.click()
        time.sleep(1)

        elements2 = self.driver.find_elements(AppiumBy.XPATH, "//android.view.View[@text][1]")
        print(f"현재 요소 {len(elements2)}개 찾음.")
        for i, el in enumerate(elements2, start=1):
            text_value = el.get_attribute("text")
            print(f"요소 {i}의 텍스트 값: {text_value}")

        # if len(elements2) >= 15:
        #     text_value = elements2[14].get_attribute("text")
        #     print("인증번호:", text_value)
        #     break
        # else:
        #     print("인증번호 없음")
        #     self.driver.press_keycode(4)
        #     time.sleep(2)
            match = re.fullmatch(r"\d{6}", text_value.strip())
            if match:
                auth_code = match.group()
                print("인증번호:", auth_code)
                break
        if auth_code:
            print("최종 인증번호: ", auth_code)
            break
        else:
            print("인증번호를 찾지 못했습니다.")
            self.driver.press_keycode(4)
            time.sleep(2)
            return

    officeBack = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "닫기")
    officeBack.click()
    time.sleep(1)

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

    authCode(self)

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

    authCode_mobile(self)

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

    placeSeachBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='비디오 공간']/android.widget.ImageView")
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

    email_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"이메일 주소\n비밀번호\"]/android.widget.EditText[1]")
    email_input_box.click()
    email_input_box.send_keys("kjjung+p1@suprema.co.kr")

    password_input_box = self.driver.find_element(AppiumBy.XPATH, emailPasswordInputBox)
    password_input_box.click()
    password_input_box.send_keys("Kjstar36!!")

    login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
    login_button.click()

    authCode(self)

    self.driver.hide_keyboard()

    authApply = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
    authApply.click()

    placeMove = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "지문 카드 테스트")
    placeMove.click()
    time.sleep(0.5)

    placeInput = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
    placeInput.click()
    placeInput.send_keys("비디오 공간")

    placeSeachBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='비디오 공간']/android.widget.ImageView")
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

    lookBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='•••••••']/android.widget.ImageView")
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

    lookBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='•••••••']/android.widget.ImageView")
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

    lookBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='•••••••']/android.widget.ImageView")
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

    lookBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='•••••••']/android.widget.ImageView")
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

    authCode(self)

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

    authCode_mobile(self)
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

    confirm_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
    confirm_btn.click()
    time.sleep(1)

def user_delete(self):

    user_modity = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
    user_modity.click()

    user_delete = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]")
    user_delete.click()

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 제외")
    delete_pop = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='해당 사용자를 이 공간에서 제외하시겠습니까?']")
    contentDesc = delete_pop.get_attribute('content-desc')
    print(f"추출한 content-desc 값 : {contentDesc}")
    self.assertEqual(contentDesc, "해당 사용자를 이 공간에서 제외하시겠습니까?")

    confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
    confirm_Btn.click()
    time.sleep(1)

def swipe_and_select_time(self, target_value, start_x, start_y, end_x, end_y, max_swipes=10, duration=100, xpath_selector=None):
    """
    스와이프하면서 특정 시간 값을 찾아서 선택하는 헬퍼 함수
    
    Args:
        target_value: 찾을 시간 값 (예: "08", "17")
        start_x, start_y, end_x, end_y: 스와이프 좌표
        max_swipes: 최대 스와이프 횟수 (기본값: 10)
        duration: 스와이프 지속 시간 (기본값: 100ms, 최적화됨)
        xpath_selector: XPath 선택자 (None이면 ACCESSIBILITY_ID 사용)
    """
    for _ in range(max_swipes):
        try:
            if xpath_selector:
                element = self.driver.find_element(AppiumBy.XPATH, xpath_selector)
            else:
                element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, target_value)
            
            if element.is_displayed():
                element.click()
                return True
        except NoSuchElementException:
            self.driver.swipe(start_x, start_y, end_x, end_y, duration)
    
    raise NoSuchElementException(f"'{target_value}' 값을 찾을 수 없습니다.")

def quick_swipe_down(self, start_x=779, start_y=1920, end_x=779, end_y=390, duration=100):
    """빠른 아래 방향 스크롤"""
    self.driver.swipe(start_x, start_y, end_x, end_y, duration)

def wait_and_click(self, locator_type, locator_value, timeout=3):
    """
    명시적 대기를 사용하여 요소를 찾고 클릭
    time.sleep() 대신 WebDriverWait 사용
    """
    try:
        if locator_type == "ACCESSIBILITY_ID":
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, locator_value))
            )
        elif locator_type == "XPATH":
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((AppiumBy.XPATH, locator_value))
            )
        element.click()
        return element
    except:
        # fallback to immediate find
        if locator_type == "ACCESSIBILITY_ID":
            element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, locator_value)
        else:
            element = self.driver.find_element(AppiumBy.XPATH, locator_value)
        element.click()
        return element


