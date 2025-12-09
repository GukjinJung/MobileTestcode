import re
import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import os
import random

from selenium.webdriver.remote.mobile import Mobile

import Android.User
from configuration.webDriver import AppiumConfig
from configuration.utill import capture_screenshot
from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import sys
sys.path.append('../Android')
from Android import utils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""
기본 테스트 계정
Standard Account
ID : 01020905304
Password : Kjstar36!!

유일한 관리자 계정
ID : 01000011111
Password : Kjstar36!!
"""

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

class IntroScreen(unittest.TestCase):

    def setUp(self):

        self.driver = AppiumConfig.get_driver()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_DQS_T13681(self):
        print("DQS_T13681 모바일로 로그인/로그아웃 기능 동작 확인")
        try:
            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            login_button.click()

            time.sleep(1)

            phone_input_box = self.driver.find_element(AppiumBy.XPATH, phoneNumberInputBox)
            phone_input_box.click()
            self.driver.press_keycode(7) #0
            self.driver.press_keycode(8) #1
            self.driver.press_keycode(7) #0
            self.driver.press_keycode(9) #2
            self.driver.press_keycode(7) #0
            self.driver.press_keycode(16) #9
            self.driver.press_keycode(7) #0
            self.driver.press_keycode(12) #5
            self.driver.press_keycode(10) #3
            self.driver.press_keycode(7) #0
            self.driver.press_keycode(11) #4

            password_input_box = self.driver.find_element(AppiumBy.XPATH, passwordInputBox)
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            login_button.click()

            time.sleep(3)

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            logout_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, logout)
            logout_button.click()

            logout_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='로그아웃 하시겠습니까?\n자동로그인 기능이 해제 됩니다.']")
            contentDesc = logout_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "로그아웃 하시겠습니까?\n자동로그인 기능이 해제 됩니다.")

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()

            pass

            print("DQS_T13681 로그인/로그아웃 기능 동작 확인 | Pass")
        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13682(self):
        try:
            print("DQS_T13682 모바일로 로그인에서 자동 로그인 기능 동작 확인")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            login_button.click()

            phone_input_box = self.driver.find_element(AppiumBy.XPATH, phoneNumberInputBox)
            phone_input_box.click()
            phone_input_box.send_keys("01000011111")

            password_input_box = self.driver.find_element(AppiumBy.XPATH, passwordInputBox)
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            login_button.click()

            time.sleep(3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "웹게이트비디오").is_displayed()

            self.driver.quit()

            time.sleep(3)

            options = UiAutomator2Options()
            options.platform_name = 'Android'
            options.device_name = 'R3CXB0MKLGP'
            options.app_package = 'com.suprema.moon'
            options.app_activity = 'com.suprema.moon.MainActivity'
            options.automation_name = 'UiAutomator2'
            options.auto_grant_permissions = True
            options.no_reset = True

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "웹게이트비디오").is_displayed()

            pass

            print("DQS_T13682 자동 로그인 기능 동작 확인 | Pass")
        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T13682 자동 로그인 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13683(self):
        try:
            print("DQS_T13683 모바일로 로그인 페이지에서 비밀번호가 틀린 경우 로그인 실패 동작 확인")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            login_button.click()

            phone_input_box = self.driver.find_element(AppiumBy.XPATH, phoneNumberInputBox)
            phone_input_box.click()
            phone_input_box.send_keys("01020905305")

            password_input_box = self.driver.find_element(AppiumBy.XPATH, passwordInputBox)
            password_input_box.click()
            password_input_box.send_keys("111111")

            for _ in range(2):

                login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
                login_button.click()

                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인 정보 오류").is_displayed()

                popUpTest1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "계정 혹은 비밀번호를\n다시 확인해 주세요.")
                self.assertIsNotNone(popUpTest1, "로그인 정보 오류 팝업이 출력되지 않았습니다.")

                loginFail_msg1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='계정 혹은 비밀번호를\n다시 확인해 주세요.']")
                contentDesc1 = loginFail_msg1.get_attribute('content-desc')
                print(f"추출한 content-desc 값 : {contentDesc1}")
                self.assertEqual(contentDesc1, "계정 혹은 비밀번호를\n다시 확인해 주세요.")

                confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
                confirmBtn.click()

            password_input_box.clear()
            time.sleep(0.1)
            password_input_box = self.driver.find_element(AppiumBy.XPATH, passwordInputBox)
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!@")

            for _ in range(2):

                login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
                login_button.click()

                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인 정보 오류").is_displayed()

                popUpTest2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000")
                self.assertIsNotNone(popUpTest2, "로그인 정보 오류 팝업이 출력되지 않았습니다.")

                loginFail_msg2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000']")
                contentDesc2 = loginFail_msg2.get_attribute('content-desc')
                print(f"추출한 content-desc 값 : {contentDesc2}")
                self.assertEqual(contentDesc2, "계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000")

                confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
                confirmBtn.click()

            # 해당 계정 로그인 후 로그아웃하여 계정 로그인 실패횟수 초기화
            password_input_box.clear()
            password_input_box = self.driver.find_element(AppiumBy.XPATH, passwordInputBox)
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            login_button.click()

            time.sleep(2)

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            logout_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, logout)
            logout_button.click()

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()
            time.sleep(1)

            pass
            print("DQS_T13683 모바일로 로그인 페이지에서 비밀번호가 틀린 경우 로그인 실패 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T13683 모바일로 로그인 페이지에서 비밀번호가 틀린 경우 로그인 실패 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_1(self):

        try:
            print("DQS_T99999 이메일로 로그인/로그아웃 기능 동작 확인")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            login_button.click()

            emailAdress = "kjjung+p1@suprema.co.kr"
            email_input_box = self.driver.find_element(AppiumBy.XPATH, emailInputBox)
            email_input_box.click()
            email_input_box.send_keys(emailAdress)

            password_input_box = self.driver.find_element(AppiumBy.XPATH, emailPasswordInputBox)
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            login_button.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\nkjjung+p1@suprema.co.kr\n인증번호").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "재전송").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "6 characters remaining").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete).is_displayed()

            utils.authCode(self)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "No characters remaining").is_displayed()

            self.driver.hide_keyboard()

            authApply = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authApply.click()

            time.sleep(5)

            leadbutton = self.driver.find_element(AppiumBy.XPATH, lead)
            leadbutton.click()

            logout_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, logout)
            logout_button.click()

            logout_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='로그아웃 하시겠습니까?\n자동로그인 기능이 해제 됩니다.']")
            contentDesc = logout_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "로그아웃 하시겠습니까?\n자동로그인 기능이 해제 됩니다.")

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()

            pass

            print("DQS_T99999 이메일로 로그인/로그아웃 기능 동작 확인 | Pass")
        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T99999 이메일로 로그인/로그아웃 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_2(self):
        try:
            print("DQS_T99999 이메일로 로그인 시 인증번호 입력 페이지에서 올바르지 않은 인증번호 입력 시 동작 확인")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            login_button.click()

            emailAdress = "kjjung+p1@suprema.co.kr"
            email_input_box = self.driver.find_element(AppiumBy.XPATH, emailInputBox)
            email_input_box.click()
            email_input_box.send_keys(emailAdress)

            password_input_box = self.driver.find_element(AppiumBy.XPATH, emailPasswordInputBox)
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            login_button.click()
            time.sleep(1)

            auth_input_box1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            auth_input_box1.click()
            auth_input_box1.send_keys("!@#$%^")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\nkjjung+p1@suprema.co.kr\n인증번호\n인증번호는 6자리 숫자입니다.").is_displayed()

            auth_input_box1.clear()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\nkjjung+p1@suprema.co.kr\n인증번호").is_displayed()

            auth_input_box2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            auth_input_box2.click()
            auth_input_box2.send_keys("가나다라마바")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\nkjjung+p1@suprema.co.kr\n인증번호\n인증번호는 6자리 숫자입니다.").is_displayed()

            auth_input_box2.clear()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\nkjjung+p1@suprema.co.kr\n인증번호").is_displayed()

            auth_input_box3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            auth_input_box3.click()
            auth_input_box3.send_keys("ABCDEF")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\nkjjung+p1@suprema.co.kr\n인증번호\n인증번호는 6자리 숫자입니다.").is_displayed()

            auth_input_box3.clear()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\nkjjung+p1@suprema.co.kr\n인증번호").is_displayed()

            auth_input_box4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            auth_input_box4.click()
            auth_input_box4.send_keys("abcdef")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\nkjjung+p1@suprema.co.kr\n인증번호\n인증번호는 6자리 숫자입니다.").is_displayed()

            auth_input_box4.clear()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\nkjjung+p1@suprema.co.kr\n인증번호").is_displayed()

            auth_input_box5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            auth_input_box5.click()
            auth_input_box5.send_keys("111111")

            self.driver.hide_keyboard()

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authBtn.click() # 활성화/비활성화 확인 - 인증완료 버튼이 활성화 상태이면 error팝업 출력/비활성이면 팝업 출력 없음(element 찾지 못함)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증코드 오류").is_displayed()

            authCodeErr1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증코드가 잘못되었습니다.\na1002']")
            contentDesc1 = authCodeErr1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "인증코드가 잘못되었습니다.\na1002")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm).is_displayed()
            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()

            resentBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "재전송")
            resentBtn.click()

            time.sleep(0.5)

            self.driver.hide_keyboard()
            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authBtn.click() # 활성화/비활성화 확인 - 인증완료 버튼이 활성화 상태이면 error팝업 출력/비활성이면 팝업 출력 없음(element 찾지 못함)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증코드 오류").is_displayed()

            authCodeErr2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증코드가 잘못되었습니다.\na1002']")
            contentDesc2 = authCodeErr2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "인증코드가 잘못되었습니다.\na1002")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm).is_displayed()
            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()

            pass

            print("DQS_T99999 이메일로 로그인 시 인증번호 입력 페이지에서 올바르지 않은 인증번호 입력 시 동작 확인 | Pass")
        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T99999 이메일로 로그인 시 인증번호 입력 페이지에서 올바르지 않은 인증번호 입력 시 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_3(self):
        try:
            print("DQS_T99999 이메일 로그인 시 인증번호 입력 페이지에서 인증번호 재전송 시 기능 동작 확인")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            login_button.click()

            emailAdress = "kjjung+p1@suprema.co.kr"
            email_input_box = self.driver.find_element(AppiumBy.XPATH, emailInputBox)
            email_input_box.click()
            email_input_box.send_keys(emailAdress)

            password_input_box = self.driver.find_element(AppiumBy.XPATH, emailPasswordInputBox)
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            login_button.click()
            time.sleep(0.5)

            resendBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "재전송")
            resendBtn.click()
            time.sleep(1)

            utils.authCode(self) #이메일 인증코드 동작

            self.driver.hide_keyboard()

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authBtn.click()

            time.sleep(5)

            leadbutton = self.driver.find_element(AppiumBy.XPATH, lead)
            leadbutton.click()

            logout_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, logout)
            logout_button.click()

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()

            pass

            print("DQS_T99999 이메일 로그인 시 인증번호 입력 페이지에서 인증번호 재전송 시 기능 동작 확인 | Pass")
        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T99999 이메일 로그인 시 인증번호 입력 페이지에서 인증번호 재전송 시 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_4(self):
        try:
            print("DQS_T999999 이메일로 로그인에서 자동 로그인 기능 동작 확인")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            login_button.click()

            emailAdress = "kjjung+p1@suprema.co.kr"
            email_input_box = self.driver.find_element(AppiumBy.XPATH, emailInputBox)
            email_input_box.click()
            email_input_box.send_keys(emailAdress)

            password_input_box = self.driver.find_element(AppiumBy.XPATH, emailPasswordInputBox)
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            login_button.click()
            time.sleep(0.5)

            utils.authCode(self) #이메일 인증코드 동작

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "No characters remaining").is_displayed()

            self.driver.hide_keyboard()

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authBtn.click()

            time.sleep(3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1").is_displayed()

            self.driver.quit()

            time.sleep(1)

            options = UiAutomator2Options()
            options.platform_name = 'Android'
            options.device_name = 'R3CXB0MKLGP'
            options.app_package = 'com.suprema.moon'
            options.app_activity = 'com.suprema.moon.MainActivity'
            options.automation_name = 'UiAutomator2'
            options.auto_grant_permissions = True
            options.no_reset = True

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1").is_displayed()

            pass

            print("DQS_T99999 이메일로 로그인/로그아웃 기능 동작 확인 | Pass")
        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T99999 이메일로 로그인/로그아웃 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_5(self):
        try:
            print("DQS_T999999 이메일로 로그인 페이지에서 비밀번호가 틀린 경우 로그인 실패 동작 확인")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            login_button.click()

            emailAdress = "kjjung+p1@suprema.co.kr"
            email_input_box = self.driver.find_element(AppiumBy.XPATH, emailInputBox)
            email_input_box.click()
            email_input_box.send_keys(emailAdress)

            password_input_box = self.driver.find_element(AppiumBy.XPATH, emailPasswordInputBox)
            password_input_box.click()
            password_input_box.send_keys("111111")

            for _ in range(2):

                login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
                login_button.click()

                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인 정보 오류").is_displayed()

                popUpTest1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "계정 혹은 비밀번호를\n다시 확인해 주세요.")
                self.assertIsNotNone(popUpTest1, "로그인 정보 오류 팝업이 출력되지 않았습니다.")

                loginFail_msg1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='계정 혹은 비밀번호를\n다시 확인해 주세요.']")
                contentDesc1 = loginFail_msg1.get_attribute('content-desc')
                print(f"추출한 content-desc 값 : {contentDesc1}")
                self.assertEqual(contentDesc1, "계정 혹은 비밀번호를\n다시 확인해 주세요.")

                confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
                confirmBtn.click()

            password_input_box.clear()

            password_input_box = self.driver.find_element(AppiumBy.XPATH, emailPasswordInputBox)
            password_input_box.click()
            password_input_box.send_keys("Wjdrnrwls170!!")

            for _ in range(2):

                login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
                login_button.click()

                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인 정보 오류").is_displayed()

                popUpTest2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000")
                self.assertIsNotNone(popUpTest2, "로그인 정보 오류 팝업이 출력되지 않았습니다.")

                loginFail_msg2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000']")
                contentDesc2 = loginFail_msg2.get_attribute('content-desc')
                print(f"추출한 content-desc 값 : {contentDesc2}")
                self.assertEqual(contentDesc2, "계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000")

                confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
                confirmBtn.click()

            # 해당 계정 로그인 후 로그아웃하여 계정 로그인 실패횟수 초기화
            password_input_box.clear()

            password_input_box = self.driver.find_element(AppiumBy.XPATH, emailPasswordInputBox)
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            login_button.click()
            time.sleep(0.5)

            utils.authCode(self) #이메일 인증코드 동작

            self.driver.hide_keyboard()

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authBtn.click()

            pass
            print("DQS_T999999 이메일로 로그인 페이지에서 비밀번호가 틀린 경우 로그인 실패 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T999999 이메일로 로그인 페이지에서 비밀번호가 틀린 경우 로그인 실패 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_6(self):
        try:
            print("DQS_T999999 공간 그룹 관리자로 이메일 로그인 시 동작 확인")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            login_button.click()

            emailAdress = "kjjung+pga@suprema.co.kr"
            email_input_box = self.driver.find_element(AppiumBy.XPATH, emailInputBox)
            email_input_box.click()
            email_input_box.send_keys(emailAdress)

            password_input_box = self.driver.find_element(AppiumBy.XPATH, emailPasswordInputBox)
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            login_button.click()
            time.sleep(0.5)

            utils.authCode(self) #이메일 인증코드 동작

            self.driver.hide_keyboard()

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1").is_displayed()
            placeSelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1")
            placeSelete.click()

            #입력박스에 문구 출력 element가 없어 공간 그룹에 등록된 임의 공간 출력 확인 케이스로 작성함
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 선택").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1\nID : 240").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "face 링크 공간\nID : 196").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "c 토르\nID : 112").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "b 안씀4\nID : 101").is_displayed()

            placeInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            placeInput.click()
            placeInput.send_keys("비디오 공간")
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간\nID : 22").is_displayed()

            self.driver.tap([(260, 644)])
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[7]").is_displayed()

            placeSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            placeSetting.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "알람\n공간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 통제").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대").is_displayed()

            pass
            print("DQS_T999999 공간 그룹 관리자로 이메일 로그인 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T999999 공간 그룹 관리자로 이메일 로그인 시 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13668_T13669(self):
        try:
            print("DQS-T13668 모바일로 회원가입 기능 동작 확인 || DQS_T13669 회원탈퇴(모바일) 기능 동작 확인")

            phone_Num = "010" + str(random.randint(0, 99999999)).zfill(8)
            print(phone_Num)

            utils.placeInvitePhone(self, "22","kr", phone_Num, "MANAGER")
            time.sleep(2)

            utils.signUpMobile(self, phone_Num)

            utils.mobile_login(self, phone_Num, "Kjstar36!!")

            utils.leaveAdmin(self)

            self.driver.quit()

            print("---------DQS-T14139 모바일로 로그인 페이지에서 당일 탈퇴한 계정으로 로그인 시도 시 로그인 실패 동작 확인 -> 사양변경으로 케이스가 동일하여 해당 케이스로 대체함  ")
            time.sleep(3)

            options = UiAutomator2Options()
            options.platform_name = 'Android'
            options.device_name = 'R3CXB0MKLGP'
            options.app_package = 'com.suprema.moon'
            options.app_activity = 'com.suprema.moon.MainActivity'
            options.automation_name = 'UiAutomator2'
            options.auto_grant_permissions = True
            options.no_reset = True

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

            time.sleep(1)

            utils.mobile_login(self, phone_Num, "Kjstar36!!")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인 정보 오류").is_displayed()
            loginErrorMsg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000']")
            contentDesc = loginErrorMsg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000")
            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()

            pass

            print("DQS-T13668 모바일로 회원가입 기능 동작 확인 || DQS_T13669 회원탈퇴(모바일) 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T13668 모바일로 회원가입 기능 동작 확인 || DQS_T13669 회원탈퇴(모바일) 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_30_T13669(self):
        try:
            print("DQS_999999_30 이메일로 회원가입 기능 동작 확인 || DQS_T13669 회원탈퇴(이메일) 기능 동작 확인")

            email_random = "kjjung+pp"+ str(random.randint(11, 9999)).zfill(3) + "@suprema.co.kr"
            print(email_random)

            utils.placeInviteEmail(self, "22",email_random, "MANAGER")
            time.sleep(5)

            utils.signUpEmail(self, email_random)
            time.sleep(3)

            utils.email_login(self, email_random, "Kjstar36!!")
            time.sleep(2)

            utils.leaveAdmin(self)

            self.driver.quit()

            print("---------DQS-T999999_15 이메일로 로그인 페이지에서 당일 탈퇴한 계정으로 로그인 시도 시 로그인 실패 동작 확인 -> 사양변경으로 케이스가 동일하여 해당 케이스로 대체함  ")
            time.sleep(3)

            options = UiAutomator2Options()
            options.platform_name = 'Android'
            options.device_name = 'R3CXB0MKLGP'
            options.app_package = 'com.suprema.moon'
            options.app_activity = 'com.suprema.moon.MainActivity'
            options.automation_name = 'UiAutomator2'
            options.auto_grant_permissions = True
            options.no_reset = True

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

            time.sleep(1)

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            login_button.click()

            email_input_box = self.driver.find_element(AppiumBy.XPATH, emailInputBox)
            email_input_box.click()
            email_input_box.send_keys(email_random)

            password_input_box = self.driver.find_element(AppiumBy.XPATH, emailPasswordInputBox)
            password_input_box.click()
            password_input_box.send_keys("kJstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            login_button.click()
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인 정보 오류").is_displayed()
            loginErrorMsg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000']")
            contentDesc = loginErrorMsg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000")
            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()

            pass

            print("DQS_999999_30 이메일로 회원가입 기능 동작 확인 || DQS_T13669 회원탈퇴(이메일) 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_999999_30 이메일로 회원가입 기능 동작 확인 || DQS_T13669 회원탈퇴(이메일) 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13670(self):
        try:
            print("DQS_T13670 모바일 로그인에서 비밀번호 찾기 기능 동작 확인")

            phone_num = "010" + str(random.randint(0, 99999999)).zfill(8)
            print(phone_num)

            utils.signUpMobile(self, phone_num)
            time.sleep(2)

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            login_button.click()

            resetPassword_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            resetPassword_button.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+82").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest).is_displayed()

            phone_input_box = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            phone_input_box.click()
            phone_input_box.send_keys(phone_num)

            authRequestBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            authRequestBtn.click()
            time.sleep(0.5)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_num}\n인증번호").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "재전송").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "6 characters remaining").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료").is_displayed()

            utils.authCode_mobile(self)
            time.sleep(0.5)

            authCompleteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authCompleteBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_num}\n비밀번호\n비밀번호 재입력").is_displayed()

            password1 = self.driver.find_element(AppiumBy.XPATH, f"//android.view.View[@content-desc='휴대폰 번호\n{phone_num}\n비밀번호\n비밀번호 재입력']/android.widget.EditText[1]")
            password1.click()
            password1.send_keys("Kjstar36!@")

            passwordInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='••••••••••']")
            text1 = passwordInput1.get_attribute('text')
            print(f"추출한 text 값 : {text1}")
            self.assertEqual(text1, "••••••••••")

            passwordLook1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='••••••••••']/android.widget.ImageView")
            passwordLook1.click()

            passwordInput2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Kjstar36!@']")
            text2 = passwordInput2.get_attribute('text')
            print(f"추출한 text 값 : {text2}")
            self.assertEqual(text2, "Kjstar36!@")

            rePassword1 = self.driver.find_element(AppiumBy.XPATH, f"//android.view.View[@content-desc='휴대폰 번호\n{phone_num}\n비밀번호\n비밀번호 재입력']/android.widget.EditText[2]")
            rePassword1.click()
            rePassword1.send_keys("Kjstar36!@")

            rePasswordInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='••••••••••']")
            text3 = rePasswordInput1.get_attribute('text')
            print(f"추출한 text 값 : {text3}")
            self.assertEqual(text3, "••••••••••")

            rePasswordLook2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='••••••••••']/android.widget.ImageView")
            rePasswordLook2.click()

            rePasswordInput2 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.EditText[@text='Kjstar36!@'])[2]")
            text4 = rePasswordInput2.get_attribute('text')
            print(f"추출한 text 값 : {text4}")
            self.assertEqual(text4, "Kjstar36!@")

            reSetBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "재설정")
            reSetBtn.click()
            time.sleep(0.5)

            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='확인']").is_displayed()
            resetMsg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='재설정 되었습니다.\n변경된 비밀번호로 로그인 해주세요.']")
            contentDesc = resetMsg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "재설정 되었습니다.\n변경된 비밀번호로 로그인 해주세요.")

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(1)

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            login_button.click()

            mobile_input_box = self.driver.find_element(AppiumBy.XPATH, phoneNumberInputBox)
            mobile_input_box.click()
            mobile_input_box.send_keys(phone_num)

            password_input_box = self.driver.find_element(AppiumBy.XPATH, passwordInputBox)
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            loginBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            loginBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인 정보 오류").is_displayed()
            loginError = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000']")
            contentDesc = loginError.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000")

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()

            password_input_box.clear()
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!@")

            loginBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            loginBtn.click()
            time.sleep(1.5)

            print("----- 시나리오 종료 - 회원 탈퇴----")
            utils.leaveAdmin(self)

            pass

            print("DQS_T13670 모바일 로그인에서 비밀번호 찾기 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T13670 모바일 로그인에서 비밀번호 찾기 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_22(self):
        try:
            print("DQS_T999999_22 이메일 로그인에서 비밀번호 찾기 기능 동작 확인")

            email_random = "kjjung+pp" + str(random.randint(11, 9999)).zfill(3) + "@suprema.co.kr"
            print(email_random)

            utils.signUpEmail(self, email_random)
            time.sleep(2)

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            login_button.click()

            resetPassword_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            resetPassword_button.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest).is_displayed()

            email_input_box = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            email_input_box.click()
            email_input_box.send_keys(email_random)

            authRequestBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            authRequestBtn.click()
            time.sleep(0.5)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"이메일 주소\n{email_random}\n인증번호").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "재전송").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "6 characters remaining").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료").is_displayed()

            utils.authCode(self)
            time.sleep(0.5)

            authCompleteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authCompleteBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"이메일\n{email_random}\n비밀번호\n비밀번호 재입력").is_displayed()

            password1 = self.driver.find_element(AppiumBy.XPATH, f"//android.view.View[@content-desc='이메일\n{email_random}\n비밀번호\n비밀번호 재입력']/android.widget.EditText[1]")
            password1.click()
            password1.send_keys("Kjstar36!@")

            passwordInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='••••••••••']")
            text1 = passwordInput1.get_attribute('text')
            print(f"추출한 text 값 : {text1}")
            self.assertEqual(text1, "••••••••••")

            passwordLook1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='••••••••••']/android.widget.ImageView")
            passwordLook1.click()

            passwordInput2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Kjstar36!@']")
            text2 = passwordInput2.get_attribute('text')
            print(f"추출한 text 값 : {text2}")
            self.assertEqual(text2, "Kjstar36!@")

            rePassword1 = self.driver.find_element(AppiumBy.XPATH, f"//android.view.View[@content-desc='이메일\n{email_random}\n비밀번호\n비밀번호 재입력']/android.widget.EditText[2]")
            rePassword1.click()
            rePassword1.send_keys("Kjstar36!@")

            rePasswordInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='••••••••••']")
            text3 = rePasswordInput1.get_attribute('text')
            print(f"추출한 text 값 : {text3}")
            self.assertEqual(text3, "••••••••••")

            rePasswordLook2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='••••••••••']/android.widget.ImageView")
            rePasswordLook2.click()

            rePasswordInput2 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.EditText[@text='Kjstar36!@'])[2]")
            text4 = rePasswordInput2.get_attribute('text')
            print(f"추출한 text 값 : {text4}")
            self.assertEqual(text4, "Kjstar36!@")

            reSetBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "재설정")
            reSetBtn.click()
            time.sleep(0.5)

            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='확인']").is_displayed()
            resetMsg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='재설정 되었습니다.\n변경된 비밀번호로 로그인 해주세요.']")
            contentDesc = resetMsg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "재설정 되었습니다.\n변경된 비밀번호로 로그인 해주세요.")

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(1)

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            login_button.click()

            email_input_box = self.driver.find_element(AppiumBy.XPATH, emailInputBox)
            email_input_box.click()
            email_input_box.send_keys(email_random)

            password_input_box = self.driver.find_element(AppiumBy.XPATH, emailPasswordInputBox)
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            loginBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            loginBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인 정보 오류").is_displayed()
            loginError = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000']")
            contentDesc = loginError.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000")

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()

            password_input_box.clear()
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!@")

            loginBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            loginBtn.click()
            time.sleep(1.5)

            utils.authCode(self)
            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authBtn.click()
            time.sleep(1)

            print("----- 시나리오 종료 - 회원 탈퇴----")
            utils.leaveAdmin(self)

            pass

            print("DQS_T999999_20 이메일 로그인에서 비밀번호 찾기 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T999999_20 이메일 로그인에서 비밀번호 찾기 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13671(self):
        try:
            print("DQS_T13671 공간의 유일한 관리자 회원 탈퇴 시도 시 동작 확인")

            phone_num = "010" + str(random.randint(0, 99999999)).zfill(8)
            print(phone_num)

            utils.placeInvitePhone(self, "27","kr", phone_num, "MASTER")

            utils.signUpMobile(self, phone_num)

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            login_button.click()

            phone_input_box = self.driver.find_element(AppiumBy.XPATH, phoneNumberInputBox)
            phone_input_box.click()
            phone_input_box.send_keys(phone_num)

            password_input_box = self.driver.find_element(AppiumBy.XPATH, passwordInputBox)
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            login_button.click()
            time.sleep(2)

            leadbutton = self.driver.find_element(AppiumBy.XPATH, lead)
            leadbutton.click()

            csctBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터")
            csctBtn.click()

            leavMB = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='안녕하세요.\n슈프리마 CLUe 서비스 고객센터 입니다.\n무엇을 도와드릴까요?\n운영시간 09:00 ~ 17:00\n(주말, 공휴일 제외)']/android.view.View[2]/android.widget.ImageView[3]")
            leavMB.click()

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

            self.driver.quit()

            print("---------DQS-T14139 모바일로 로그인 페이지에서 당일 탈퇴한 계정으로 로그인 시도 시 로그인 실패 동작 확인 -> 사양변경으로 케이스가 동일하여 해당 케이스로 대체함  ")
            time.sleep(3)

            options = UiAutomator2Options()
            options.platform_name = 'Android'
            options.device_name = 'R3CXB0MKLGP'
            options.app_package = 'com.suprema.moon'
            options.app_activity = 'com.suprema.moon.MainActivity'
            options.automation_name = 'UiAutomator2'
            options.auto_grant_permissions = True
            options.no_reset = True

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

            time.sleep(1)

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            login_button.click()

            phone_input_box = self.driver.find_element(AppiumBy.XPATH, phoneNumberInputBox)
            phone_input_box.click()
            phone_input_box.send_keys(phone_num)

            password_input_box = self.driver.find_element(AppiumBy.XPATH, passwordInputBox)
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            login_button.click()
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인 정보 오류").is_displayed()
            loginErrorMsg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000']")
            contentDesc = loginErrorMsg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000")
            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()

            pass

            print("DQS_T13671 공간의 유일한 관리자 회원 탈퇴 시도 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T13683 로그인 실패 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13677(self):
        try:
            print("DQS_T13677 회원가입 휴대폰 번호 입력 페이지에서 올바르지 않은 번호 입력시 동작 확인")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "약관 전체 동의").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "만 14세 이상입니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이용 약관 동의").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 수집 및 이용 동의").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음").is_displayed()

            agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "약관 전체 동의")
            agree.click()

            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            nextBtn.click()

            mobileSel = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "모바일")
            mobileSel.click()

            phoNo = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            phoNo.click()

            text_to_input = "~!@#$%^&*("
            os.system(f"adb shell input text '{text_to_input}'")
            cl1 = phoNo.text
            self.assertEqual("", cl1)

            text_to_input1 = "가나다라마바사아"
            os.system(f"adb shell input text '{text_to_input1}'")
            cl2 = phoNo.text
            self.assertEqual("", cl2)

            text_to_input2 = "ABCDEFGH"
            os.system(f"adb shell input text '{text_to_input2}'")
            cl3 = phoNo.text
            self.assertEqual("", cl3)

            text_to_input3 = "abcdefgh"
            os.system(f"adb shell input text '{text_to_input3}'")
            cl4 = phoNo.text
            self.assertEqual("", cl4)

            phoNo.send_keys("123456789")
            #cl5 = phoNo.text
            cl5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123 456 789']")
            numtext = cl5.get_attribute('text')
            print(f"추출한 content-desc 값 : {numtext}")
            self.assertEqual("123 456 789", numtext)

            wrongPhoNum = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.']")
            contentDesc = wrongPhoNum.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.")

            # next = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청")
            # next.click()
            # assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청").is_displayed()

            nextDisabled = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            isNext = nextDisabled.is_enabled()
            self.assertFalse(isNext, "인증요청 버튼이 비활성화되어 있습니다.")

            pass

            print("DQS_T13677 회원가입 휴대폰 번호 입력 페이지에서 올바르지 않은 번호 입력시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T13677 회원가입 휴대폰 번호 입력 페이지에서 올바르지 않은 번호 입력시 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_11(self):
        try:
            print("DQS_T1999999_11 회원가입 이메일 입력 페이지에서 올바르지 않은 이메일 입력시 동작 확인")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "약관 전체 동의").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "만 14세 이상입니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이용 약관 동의").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 수집 및 이용 동의").is_displayed()
            #assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 처리업무 위수탁 계약").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음").is_displayed()

            agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "약관 전체 동의")
            agree.click()

            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            nextBtn.click()

            emailInput1 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            emailInput1.click()

            emailInput1.send_keys("가나다@suprema.co.kr")
            cl1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='가나다@suprema.co.kr']")
            emailtext1 = cl1.get_attribute('text')
            print(f"추출한 content-desc 값 : {emailtext1}")
            self.assertEqual("가나다@suprema.co.kr", emailtext1)

            wrongEmail1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='이메일 주소\n입력 형식이 맞지 않습니다.']")
            contentDesc1 = wrongEmail1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "이메일 주소\n입력 형식이 맞지 않습니다.")

            inputDel1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='가나다@suprema.co.kr']/android.widget.ImageView")
            inputDel1.click()

            emailInput2 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            emailInput2.click()

            emailInput2.send_keys("123456789")
            cl2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123456789']")
            emailtext2 = cl2.get_attribute('text')
            print(f"추출한 content-desc 값 : {emailtext2}")
            self.assertEqual("123456789", emailtext2)

            wrongEmail2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='이메일 주소\n입력 형식이 맞지 않습니다.']")
            contentDesc2 = wrongEmail2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "이메일 주소\n입력 형식이 맞지 않습니다.")

            inputDel2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123456789']/android.widget.ImageView")
            inputDel2.click()

            emailInput3 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            emailInput3.click()

            emailInput3.send_keys("ABCDEFGH")
            cl3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='ABCDEFGH']")
            emailtext3 = cl3.get_attribute('text')
            print(f"추출한 content-desc 값 : {emailtext3}")
            self.assertEqual("ABCDEFGH", emailtext3)

            wrongEmail3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='이메일 주소\n입력 형식이 맞지 않습니다.']")
            contentDesc3 = wrongEmail3.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc3}")
            self.assertEqual(contentDesc3, "이메일 주소\n입력 형식이 맞지 않습니다.")

            inputDel3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='ABCDEFGH']/android.widget.ImageView")
            inputDel3.click()

            emailInput4 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            emailInput4.click()

            emailInput4.send_keys("abcdefgh")
            cl4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='abcdefgh']")
            emailtext4 = cl4.get_attribute('text')
            print(f"추출한 content-desc 값 : {emailtext4}")
            self.assertEqual("abcdefgh", emailtext4)

            wrongEmail4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='이메일 주소\n입력 형식이 맞지 않습니다.']")
            contentDesc4 = wrongEmail4.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc4}")
            self.assertEqual(contentDesc4, "이메일 주소\n입력 형식이 맞지 않습니다.")

            inputDel4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='abcdefgh']/android.widget.ImageView")
            inputDel4.click()

            emailInput5 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            emailInput5.click()

            emailInput5.send_keys("kjjung+p1@suprema.")
            cl5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='kjjung+p1@suprema.']")
            emailtext5 = cl5.get_attribute('text')
            print(f"추출한 content-desc 값 : {emailtext5}")
            self.assertEqual("kjjung+p1@suprema.", emailtext5)

            wrongEmail5 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='이메일 주소\n입력 형식이 맞지 않습니다.']")
            contentDesc5 = wrongEmail5.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc5}")
            self.assertEqual(contentDesc5, "이메일 주소\n입력 형식이 맞지 않습니다.")

            inputDel5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='kjjung+p1@suprema.']/android.widget.ImageView")
            inputDel5.click()

            emailInput6 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            emailInput6.click()

            emailInput6.send_keys("kjjung+p1@suprema.co.kr.")
            cl6 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='kjjung+p1@suprema.co.kr.']")
            emailtext6 = cl6.get_attribute('text')
            print(f"추출한 content-desc 값 : {emailtext6}")
            self.assertEqual("kjjung+p1@suprema.co.kr.", emailtext6)

            wrongEmail6 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='이메일 주소\n입력 형식이 맞지 않습니다.']")
            contentDesc6 = wrongEmail6.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc6}")
            self.assertEqual(contentDesc6, "이메일 주소\n입력 형식이 맞지 않습니다.")

            inputDel6 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='kjjung+p1@suprema.co.kr.']/android.widget.ImageView")
            inputDel6.click()

            nextDisabled = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            isNext = nextDisabled.is_enabled()
            self.assertFalse(isNext, "인증요청 버튼이 비활성화되어 있습니다.")

            pass

            print("DQS_T13677 회원가입 휴대폰 번호 입력 페이지에서 올바르지 않은 번호 입력시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T13677 회원가입 휴대폰 번호 입력 페이지에서 올바르지 않은 번호 입력시 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13685(self):
        try:
            print("DQS_T13685 회원가입 휴대폰 번호 입력 페이지에서 존재하는 번호 입력 시 동작 확인")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            agree.click()

            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            nextBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()
            mobileSelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "모바일")
            mobileSelete.click()

            phoNo = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            phoNo.click()
            phoNo.send_keys("01020905304")

            authButton = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            authButton.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인 정보 오류").is_displayed()
            emailDeplicate_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='이미 가입된 계정입니다.\na1001']")
            contentDesc = emailDeplicate_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "이미 가입된 계정입니다.\na1001")

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()

            pass

            print("DQS_T13685 회원가입 휴대폰 번호 입력 페이지에서 존재하는 번호 입력 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T13685 회원가입 휴대폰 번호 입력 페이지에서 존재하는 번호 입력 시 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_7(self):
        try:
            print("DQS_T999999 회원가입 이메일 주소 입력 페이지에서 존재하는 번호 입력 시 동작 확인")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            agree.click()

            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            nextBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소").is_displayed()

            emailinput = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            emailinput.click()
            emailinput.send_keys("kjjung+p1@suprema.co.kr")

            authButton = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            authButton.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인 정보 오류").is_displayed()
            emailDeplicate_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='이미 가입된 계정입니다.\na1001']")
            contentDesc = emailDeplicate_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "이미 가입된 계정입니다.\na1001")

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()

            pass

            print("DQS_T999999 회원가입 이메일 주소 입력 페이지에서 존재하는 번호 입력 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T999999 회원가입 이메일 주소 입력 페이지에서 존재하는 번호 입력 시 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_10(self):
        try:
            print("DQS_T999999 브랜치, 대리점, 공간 그룹 관리자 계정으로 회원 가입 시 동작 확인 ")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            agree.click()

            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            nextBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소").is_displayed()

            emailinput1 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            emailinput1.click()
            emailinput1.send_keys("kjjung+ba@suprema.co.kr")

            authButton = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            authButton.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인 정보 오류").is_displayed()
            emailDeplicate_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='이미 가입된 계정입니다.\na1001']")
            contentDesc = emailDeplicate_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "이미 가입된 계정입니다.\na1001")

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()

            emailDel = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='kjjung+ba@suprema.co.kr']/android.widget.ImageView")
            emailDel.click()

            emailinput2 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            emailinput2.click()
            emailinput2.send_keys("kjjung+dist1@suprema.co.kr")

            authButton = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            authButton.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인 정보 오류").is_displayed()
            emailDeplicate_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='이미 가입된 계정입니다.\na1001']")
            contentDesc = emailDeplicate_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "이미 가입된 계정입니다.\na1001")

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()

            pass

            print("DQS_T999999 브랜치, 대리점, 공간 그룹 관리자 계정으로 회원 가입 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T999999 브랜치, 대리점, 공간 그룹 관리자 계정으로 회원 가입 시 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13718(self):
        try:

            print("DQS_T13718 회원가입 페이지의 약관 동의 기능 동작 확인")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "약관 전체 동의").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "만 14세 이상입니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이용 약관 동의").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 수집 및 이용 동의").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음").is_displayed()

            agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            isagree = agree.is_enabled()
            self.assertTrue(isagree,"약관 전체 동의 버튼이 활성화되어 있습니다.")
            print("-----------------------------약관 전체 동의 확인 완료")

            fourtteenAgree= self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "만 14세 이상입니다.")
            isagreeAge = fourtteenAgree.is_enabled()
            self.assertTrue(isagreeAge,"만 14세 이상입니다. 버튼이 활성화되어 있습니다.")
            fourtteenAgree.click()

            nextDisabled1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            isNext1 = nextDisabled1.is_enabled()
            self.assertFalse(isNext1, "다음 버튼이 비활성화되어 있습니다.")
            fourtteenAgree.click()

            print("----------------------------- 만 14세 이상입니다. 확인 완료")

            agree1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이용 약관 동의")
            isagree1 = agree1.is_enabled()
            self.assertTrue(isagree1,"이용 약관 동의 버튼이 활성화되어 있습니다.")
            agree1.click()

            nextDisabled1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            isNext1 = nextDisabled1.is_enabled()
            self.assertFalse(isNext1, "다음 버튼이 비활성화되어 있습니다.")

            self.driver.tap([(980, 1154)])
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이용약관").is_displayed() #이용 약관 페이지의 타이틀 명 확인, 본문 내용은 확인 하지 못함

            collapse = self.driver.find_element(AppiumBy.CLASS_NAME, widgetImage)
            collapse.click()
            agree1.click()

            print("----------------------------- 이용 약관 동의 확인 완료")

            agree2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 수집 및 이용 동의")
            isagree2 = agree2.is_enabled()
            self.assertTrue(isagree2,"개인정보 수집 및 이용 동의 버튼이 활성화되어 있습니다.")
            agree2.click()

            nextDisabled2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            isNext2 = nextDisabled2.is_enabled()
            self.assertFalse(isNext2, "다음 버튼이 비활성화되어 있습니다.")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 수집 및 이용에 동의합니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 수집·이용 항목: 아이디(App: 국가코드, 휴대폰번호, Web: 이메일주소), 비밀번호, 이름").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "※ 프로필 사진, 닉네임은 서비스 이용 과정에서 수집되는 선택정보로 언제든 입력/수정/삭제 가능합니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 수집·이용 목적: CLUe 서비스 가입처리 및 서비스 제공").is_displayed()

            stat_x1 = 550
            stat_y1 = 1765
            end_x1 = 550
            end_y1 = 1400
            self.driver.swipe(stat_x1, stat_y1, end_x1, end_y1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 보유·이용 기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "메인 관리자 정보: 탈퇴 시 또는 계약 등 서비스 이용 종료 시까지").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "서브 관리자 정보: 탈퇴 시 또는 메인 관리자가 삭제 시까지").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "※ CLUe 서비스 내 “사용자”로 등록되는 정보주체의 개인정보 수집에 대한 책임은 “메인관리자”인 고객에게 있습니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "※ 위 개인정보 수집·이용에 대한 동의를 거부할 권리가 있습니다. 그러나 동의를 거부할 경우 CLUe 서비스 이용이 불가합니다.").is_displayed()

            print("----------------------------- 개인정보 수집 및 이용 동의 확인 완료, 문서 이슈 있음")

            stat_x1 = 537
            stat_y1 = 1016
            end_x1 = 537
            end_y1 = 877
            self.driver.swipe(stat_x1, stat_y1, end_x1, end_y1)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 처리업무 위수탁 계약").is_displayed()

            agree3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 처리업무 위수탁 계약")
            isagree3 = agree3.is_enabled()
            self.assertTrue(isagree3,"개인정보 처리업무 위수탁 계약 버튼이 활성화되어 있습니다.")
            agree3.click()

            nextDisabled3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            isNext3 = nextDisabled3.is_enabled()
            self.assertFalse(isNext3, "다음 버튼이 비활성화되어 있습니다.")

            self.driver.tap([(980, 1861)])
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 처리업무 위수탁 계약").is_displayed() #개인정보 처리업무 위수탁 계약 타이틀 명 확인, 본문 내용은 확인 하지 못함 - 이슈있음
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='CLUe서비스 이용에 따른 개인정보 처리업무 위수탁 계약']").is_displayed()

            collapse = self.driver.find_element(AppiumBy.CLASS_NAME, widgetImage)
            collapse.click()
            agree3.click()

            print("----------------------------- 개인정보 처리업무 위수탁 계약 확인 완료")

            stat_x1 = 537
            stat_y1 = 877
            end_x1 = 537
            end_y1 = 1016
            self.driver.swipe(stat_x1, stat_y1, end_x1, end_y1)

            agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            agree.click()

            nextEnabled1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            isNext4 = nextEnabled1.is_enabled()
            self.assertTrue(isNext4, "다음 버튼이 활성화되어 있습니다.")

            agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            agree.click()

            nextDisabled4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            isNext5 = nextDisabled4.is_enabled()
            self.assertFalse(isNext5, "다음 버튼이 비활성화되어 있습니다.")
            print("------------------ 약관 전체 동의 체크/미체크 확인")

            fourtteenAgree.click()
            time.sleep(0.1)

            agree1.click()
            time.sleep(0.1)

            agree2.click()
            time.sleep(0.1)

            stat_x1 = 537
            stat_y1 = 1016
            end_x1 = 537
            end_y1 = 877
            self.driver.swipe(stat_x1, stat_y1, end_x1, end_y1)
            agree3.click()
            time.sleep(0.1)

            nextEnabled2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            isNext6 = nextEnabled2.is_enabled()
            self.assertTrue(isNext6, "다음 버튼이 활성화되어 있습니다.")

            nextEnabled2.click()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "모바일").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청").is_displayed()

            pass

            print("DQS_T13718 회원가입 페이지의 약관 동의 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T13718 회원가입 페이지의 약관 동의 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14133(self):
        try:

            print("DQS_T14133 로그인 페이지 휴대폰 번호 인풋 박스 유효성 검사")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.XPATH, phoneNumberInputBox)
            st2.click()
            st2.send_keys("1234567890123450000")
            st2Input = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123 4567 8901']")
            text1 =st2Input.get_attribute('text')
            print(f"추출한 text 값 : {text1}")
            self.assertEqual(text1, "123 4567 8901")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.\n비밀번호").is_displayed()

            st2clear = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123 4567 8901']/android.widget.ImageView")
            st2clear.click()

            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.\n비밀번호']/android.widget.EditText[1]")
            st3.click()
            text_to_input = "ABCDEFG"
            er3 = st3.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er3)
            st3.clear()

            st4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.\n비밀번호']/android.widget.EditText[1]")
            st4.click()
            text_to_input = "abcdefg"
            er4 = st4.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er4)
            st4.clear()

            st5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.\n비밀번호']/android.widget.EditText[1]")
            st5.click()
            text_to_input = "가나다라마바사"
            er5 = st5.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er5)
            st5.clear()

            st6 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.\n비밀번호']/android.widget.EditText[1]")
            st6.click()
            text_to_input = "!@#$%^&*()"
            er6 = st6.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er6)
            st6.clear()

            time.sleep(0.2)
            st7 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.\n비밀번호']/android.widget.EditText[1]")
            st7.click()
            st7.send_keys("123456789")
            st7Input = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123 456 789']")
            text2 =st7Input.get_attribute('text')
            print(f"추출한 text 값 : {text2}")
            self.assertEqual(text2, "123 456 789")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.\n비밀번호").is_displayed()

            st7clear = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123 456 789']/android.widget.ImageView")
            st7clear.click()

            st8 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.\n비밀번호']/android.widget.EditText[1]")
            st8.click()
            st8.send_keys("01012345678")
            st8Input = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010 1234 5678']")
            text3 =st8Input.get_attribute('text')
            print(f"추출한 text 값 : {text3}")
            self.assertEqual(text3, "010 1234 5678")

            pass

            print("DQS_T14133 로그인 페이지 휴대폰 번호 인풋 박스 유효성 검사 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T14133 로그인 페이지 휴대폰 번호 인풋 박스 유효성 검사 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14134(self):
        try:
            print("DQS_T14134 로그인 페이지 휴대폰/이메일 인풋 박스 X 버튼 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.XPATH, phoneNumberInputBox)
            st2.click()
            st2.send_keys("01011112222")

            self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010 1111 2222']/android.widget.ImageView").is_displayed()
            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010 1111 2222']/android.widget.ImageView")
            st3.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.\n비밀번호").is_displayed()

            try:
                self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010 1111 2222']/android.widget.ImageView")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                #assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            backBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.\n비밀번호']/android.view.View/android.widget.ImageView")
            backBtn.click()
            st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            st5.click()

            st6 = self.driver.find_element(AppiumBy.XPATH, emailInputBox)
            st6.click()
            st6.send_keys("kjjung+p3@suprema.co.kr")

            self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='kjjung+p3@suprema.co.kr']/android.widget.ImageView").is_displayed()
            st7 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='kjjung+p3@suprema.co.kr']/android.widget.ImageView")
            st7.click()

            try:
                self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='kjjung+p3@suprema.co.kr']/android.widget.ImageView")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                # assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            pass

            print("DQS_T14134 로그인 페이지 휴대폰/이메일 인풋 박스 X 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T14134 로그인 페이지 휴대폰/이메일 인풋 박스 X 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14137(self):
        try:
            print("DQS-T14137 모바일로 로그인 페이지에서 비밀번호만 입력한 경우 로그인 실패 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.XPATH, passwordInputBox)
            st2.click()
            st2.send_keys("Kjstar36!!")

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            st3.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "계정 혹은 비밀번호를\n다시 확인해 주세요.").is_displayed()
            onlyPass_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='계정 혹은 비밀번호를\n다시 확인해 주세요.']")
            contentDesc = onlyPass_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "계정 혹은 비밀번호를\n다시 확인해 주세요.")

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            st4.click()

            pass

            print("DQS-T14137 로그인 페이지에서 비밀번호만 입력한 경우 로그인 실패 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14137 로그인 페이지에서 비밀번호만 입력한 경우 로그인 실패 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_13(self):
        try:
            print("DQS-T1999999_13 이메일로 로그인 페이지에서 비밀번호만 입력한 경우 로그인 실패 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.XPATH, emailPasswordInputBox)
            st2.click()
            st2.send_keys("Kjstar36!!")

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            st3.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "계정 혹은 비밀번호를\n다시 확인해 주세요.").is_displayed()
            onlyPass_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='계정 혹은 비밀번호를\n다시 확인해 주세요.']")
            contentDesc = onlyPass_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "계정 혹은 비밀번호를\n다시 확인해 주세요.")

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            st4.click()

            pass

            print("DQS-T1999999_13 이메일로 로그인 페이지에서 비밀번호만 입력한 경우 로그인 실패 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T999999_13 이메일로 로그인 페이지에서 비밀번호만 입력한 경우 로그인 실패 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14138(self):
        try:
            print("DQS-T14138 모바일로 로그인 페이지에서 휴대폰 번호만 입력한 경우 로그인 실패 동작 확인")
            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.XPATH, phoneNumberInputBox)
            st2.click()
            st2.send_keys("01000011111")

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            st3.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "계정 혹은 비밀번호를\n다시 확인해 주세요.").is_displayed()
            onlyPho_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='계정 혹은 비밀번호를\n다시 확인해 주세요.']")
            contentDesc = onlyPho_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "계정 혹은 비밀번호를\n다시 확인해 주세요.")

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            st4.click()

            pass

            print("DQS-T14138 모바일로 로그인 페이지에서 휴대폰 번호만 입력한 경우 로그인 실패 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14138 모바일로 로그인 페이지에서 휴대폰 번호만 입력한 경우 로그인 실패 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_14(self):
        try:
            print("DQS-T999999_14 이메일로 로그인 페이지에서 이메일 주소만 입력한 경우 로그인 실패 동작 확인")
            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.XPATH, emailInputBox)
            st2.click()
            st2.send_keys("kjjung+p2@suprema.co.kr")

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            st3.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "계정 혹은 비밀번호를\n다시 확인해 주세요.").is_displayed()
            onlyEmail_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='계정 혹은 비밀번호를\n다시 확인해 주세요.']")
            contentDesc = onlyEmail_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "계정 혹은 비밀번호를\n다시 확인해 주세요.")

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            st4.click()

            pass

            print("DQS-T999999_14 이메일로 로그인 페이지에서 이메일 주소만 입력한 경우 로그인 실패 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T999999_14 이메일로 로그인 페이지에서 이메일 주소만 입력한 경우 로그인 실패 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14140(self):
        try:
            print("DQS-T14140 모바일로 회원가입 휴대폰 번호 입력 페이지에서 당일 탈퇴한 계정 입력 시 동작 확인")

            phone_num = "010" + str(random.randint(10000000, 99999999)).zfill(8)
            print(phone_num)

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            agree.click()

            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            nextBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()
            mobileSelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "모바일")
            mobileSelete.click()

            phoNo = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            phoNo.click()
            phoNo.send_keys(phone_num)

            authButton = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            authButton.click()

            formatted_phone_num = f"{phone_num[:3]} {phone_num[3:7]} {phone_num[7:]}"
            print(formatted_phone_num)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{formatted_phone_num}\n인증번호").is_displayed()

            pass

            print("DQS-T14140 모바일로 회원가입 휴대폰 번호 입력 페이지에서 당일 탈퇴한 계정 입력 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14140 모바일로 회원가입 휴대폰 번호 입력 페이지에서 당일 탈퇴한 계정 입력 시 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_16(self):
        try:
            print("DQS-T999999_16 이메일로 회원가입 휴대폰 번호 입력 페이지에서 당일 탈퇴한 계정 입력 시 동작 확인")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            agree.click()

            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            nextBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()

            emailInput = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            emailInput.click()
            emailInput.send_keys("kjjung+pp1001@suprema.co.kr")

            authButton = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            authButton.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\nkjjung+pp1001@suprema.co.kr\n인증번호").is_displayed()

            pass

            print("DQS-T14140 모바일로 회원가입 휴대폰 번호 입력 페이지에서 당일 탈퇴한 계정 입력 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14140 모바일로 회원가입 휴대폰 번호 입력 페이지에서 당일 탈퇴한 계정 입력 시 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14141(self):
        try:
            print("DQS-T14141 로그인 페이지에서 가입되지 않은 휴대폰 번호로 로그인 시도 시 로그인 실패 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.XPATH, phoneNumberInputBox)
            st2.click()
            st2.send_keys("01045614689")
            #가입되지 않는 폰번호 입력

            st3 = self.driver.find_element(AppiumBy.XPATH, passwordInputBox)
            st3.click()
            st3.send_keys("Kjstar36!!")

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            st4.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인 정보 오류").is_displayed()
            notRegister_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000']")
            contentDesc = notRegister_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000")

            st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            st5.click()

            pass

            print("DQS-T14141 로그인 페이지에서 가입되지 않은 휴대폰 번호로 로그인 시도 시 로그인 실패 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14141 로그인 페이지에서 가입되지 않은 휴대폰 번호로 로그인 시도 시 로그인 실패 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_17(self):
        try:
            print("DQS-T999999_17 로그인 페이지에서 가입되지 않은 이메일 주소로 로그인 시도 시 로그인 실패 동작 확인")

            email_random = "kjjung+pp" + str(random.randint(1000, 9999)).zfill(3) + "@suprema.co.kr"
            print(email_random)

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.XPATH, emailInputBox)
            st2.click()
            st2.send_keys(email_random)
            #가입되지 않는 이메일 입력

            st3 = self.driver.find_element(AppiumBy.XPATH, emailPasswordInputBox)
            st3.click()
            st3.send_keys("Kjstar36!!")

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            st4.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인 정보 오류").is_displayed()
            notRegister_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000']")
            contentDesc = notRegister_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000")

            st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            st5.click()

            pass

            print("DQS-T14141 로그인 페이지에서 가입되지 않은 이메일 주소로 로그인 시도 시 로그인 실패 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14141 로그인 페이지에서 가입되지 않은 이메일 주소로 로그인 시도 시 로그인 실패 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14142(self):
        try:
            print("DQS-T14142 회원가입 페이지의 휴대폰 번호 인풋 박스 유효성 검사")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            st2.click()

            mobileSel = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "모바일")
            mobileSel.click()

            st3 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st3.click()
            text_to_input = "ABCDEFG"
            er3 = st3.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er3)
            st3.clear()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st4.click()
            text_to_input = "abcdefg"
            er4 = st4.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er4)
            st4.clear()

            st5 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st5.click()
            text_to_input = "가나다라마바사"
            er5 = st5.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er5)
            st5.clear()

            st6 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st6.click()
            text_to_input = "!@#$%^&*()"
            er6 = st6.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er6)
            st6.clear()

            st7 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st7.click()
            st7.send_keys("123456789")
            textKey1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123 456 789']")
            text1 = textKey1.get_attribute('text')
            print(f"추출한 text 값 : {text1}")
            self.assertEqual("123 456 789", text1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.").is_displayed()
            phoNum1_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.']")
            contentDesc1 = phoNum1_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.")
            st7.clear()

            st8 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st8.click()
            st8.send_keys("1234567890123450000")
            textKey2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123 4567 8901']")
            text2 = textKey2.get_attribute('text')
            print(f"추출한 text 값 : {text2}")
            self.assertEqual("123 4567 8901", text2)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.").is_displayed()

            deleteBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123 4567 8901']/android.widget.ImageView")
            deleteBtn.click()

            st9 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st9.click()
            st9.send_keys("123456789")
            textKey3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123 456 789']")
            text3 = textKey3.get_attribute('text')
            print(f"추출한 text 값 : {text3}")
            self.assertEqual("123 456 789", text3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.").is_displayed()

            deleteBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123 456 789']/android.widget.ImageView")
            deleteBtn.click()

            st10 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st10.click()
            st10.send_keys("01012345678")
            textKey4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010 1234 5678']")
            text4 = textKey4.get_attribute('text')
            print(f"추출한 text 값 : {text4}")
            self.assertEqual("010 1234 5678", text4)
            st10.clear()
            pass

            print("DQS-T14142 회원가입 페이지의 휴대폰 번호 인풋 박스 유효성 검사 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14142 회원가입 페이지의 휴대폰 번호 인풋 박스 유효성 검사 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_18(self):
        try:
            print("DQS-T14142 회원가입 페이지의 이메일 주소 인풋 박스 유효성 검사")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            st2.click()

            st3 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st3.click()
            st3.send_keys("가나다@suprema.co.kr")
            textKey1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='가나다@suprema.co.kr']")
            text1 = textKey1.get_attribute('text')
            print(f"추출한 text 값 : {text1}")
            self.assertEqual("가나다@suprema.co.kr", text1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\n입력 형식이 맞지 않습니다.").is_displayed()
            email1_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='이메일 주소\n입력 형식이 맞지 않습니다.']")
            contentDesc1 = email1_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "이메일 주소\n입력 형식이 맞지 않습니다.")
            st3.clear()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st4.click()
            st4.send_keys("123456789")
            textKey2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123456789']")
            text2 = textKey2.get_attribute('text')
            print(f"추출한 text 값 : {text2}")
            self.assertEqual("123456789", text2)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\n입력 형식이 맞지 않습니다.").is_displayed()
            st4.clear()

            st5 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st5.click()
            st5.send_keys("abcdefg")
            textKey3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='abcdefg']")
            text3 = textKey3.get_attribute('text')
            print(f"추출한 text 값 : {text3}")
            self.assertEqual("abcdefg", text3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\n입력 형식이 맞지 않습니다.").is_displayed()
            st5.clear()

            st7 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st7.click()
            st7.send_keys("kjjung@suprema.co.kr.")
            textKey5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='kjjung@suprema.co.kr.']")
            text5 = textKey5.get_attribute('text')
            print(f"추출한 text 값 : {text5}")
            self.assertEqual("kjjung@suprema.co.kr.", text5)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\n입력 형식이 맞지 않습니다.").is_displayed()
            st7.clear()

            pass

            print("DQS-T14142 회원가입 페이지의 이메일 주소 인풋 박스 유효성 검사 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14142 회원가입 페이지의 휴대폰 번호 인풋 박스 유효성 검사 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14144(self):
        try:

            print("DQS-T14144 회원가입 페이지의 휴대폰 번호 인풋 박스 X버튼 기능 동작 확인")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            st2.click()

            mobileSel = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "모바일")
            mobileSel.click()

            st3 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st3.click()
            st3.send_keys("01022221111")

            self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010 2222 1111']/android.widget.ImageView").is_displayed()
            st4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010 2222 1111']/android.widget.ImageView")
            st4.click()

            assert self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput).is_displayed()

            pass

            print("DQS-T14144 회원가입 페이지의 휴대폰 번호 인풋 박스 X버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14144 회원가입 페이지의 휴대폰 번호 인풋 박스 X버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_19(self):
        try:

            print("DQS-T14144 회원가입 페이지의 이메일 주소 인풋 박스 X버튼 기능 동작 확인")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            st2.click()

            st2 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st2.click()
            st2.send_keys("kjjung+p2@suprema.co.kr")

            self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='kjjung+p2@suprema.co.kr']/android.widget.ImageView").is_displayed()
            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='kjjung+p2@suprema.co.kr']/android.widget.ImageView")
            st3.click()

            assert self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput).is_displayed()

            pass

            print("DQS-T14144 회원가입 페이지의 이메일 주소 인풋 박스 X버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14144 회원가입 페이지의 이메일 주소 인풋 박스 X버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14145(self):
        try:
            print("DQS-T14145 모바일로 회원가입 인증번호 입력 페이지의 인증번호 인풋 박스 유효성 검사")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            st2.click()

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            st3.click()

            mobileSel = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "모바일")
            mobileSel.click()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st4.click()
            st4.send_keys("01087561455")

            st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            st5.click()

            time.sleep(3)

            st6 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st6.click()
            st6.send_keys("ABCDEFG")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n010 8756 1455\n인증번호\n인증번호는 6자리 숫자입니다.").is_displayed()

            authDisabledBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            isAuthBtn = authDisabledBtn.is_enabled()
            self.assertFalse(isAuthBtn, "인증완료 버튼이이 비활성화되어 있습니다.")
            st6.clear()

            st7 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st7.click()
            st7.send_keys("abcdefg")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n010 8756 1455\n인증번호\n인증번호는 6자리 숫자입니다.").is_displayed()

            authDisabledBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            isAuthBtn = authDisabledBtn.is_enabled()
            self.assertFalse(isAuthBtn, "인증완료 버튼이이 비활성화되어 있습니다.")
            st7.clear()

            st8 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st8.click()
            st8.send_keys("가나다라마바사")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n010 8756 1455\n인증번호\n인증번호는 6자리 숫자입니다.").is_displayed()

            authDisabledBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            isAuthBtn = authDisabledBtn.is_enabled()
            self.assertFalse(isAuthBtn, "인증완료 버튼이이 비활성화되어 있습니다.")
            st8.clear()

            st9 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st9.click()
            st9.send_keys("!@#$%^&*()")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n010 8756 1455\n인증번호\n인증번호는 6자리 숫자입니다.").is_displayed()

            authDisabledBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            isAuthBtn = authDisabledBtn.is_enabled()
            self.assertFalse(isAuthBtn, "인증완료 버튼이이 비활성화되어 있습니다.")
            st9.clear()

            st10 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st10.click()
            st10.send_keys("123")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n010 8756 1455\n인증번호\n인증번호는 6자리 숫자입니다.").is_displayed()

            authDisabledBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            isAuthBtn = authDisabledBtn.is_enabled()
            self.assertFalse(isAuthBtn, "인증완료 버튼이이 비활성화되어 있습니다.")
            st10.clear()

            st11 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st11.click()
            st11.send_keys("9876543210")
            er11 = st11.text
            print(er11)
            self.assertEqual("987654", er11)
            time.sleep(1)
            st11.clear()

            st12 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st12.click()
            st12.send_keys("123456")

            authEnabledBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            isAuthBtn = authEnabledBtn.is_enabled()
            self.assertTrue(isAuthBtn, "인증완료 버튼이 활성화되어 있습니다.")

            st12 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            st12.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증 코드 오류").is_displayed()

            authError_Pop = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증 코드가 일치하지 않습니다. \n다시 입력해 주세요.\na1005']")
            contentDesc = authError_Pop.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "인증 코드가 일치하지 않습니다. \n다시 입력해 주세요.\na1005")
            st13 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            st13.click()

            pass

            print("DQS-T14145 모바일로 회원가입 인증번호 입력 페이지의 인증번호 인풋 박스 유효성 검사 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("모바일로 회원가입 인증번호 입력 페이지의 인증번호 인풋 박스 유효성 검사 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_12(self):
        try:
            print("DQS-T1999999_12 이메일로 회원가입 인증번호 입력 페이지의 인증번호 인풋 박스 유효성 검사")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            st2.click()

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            st3.click()


            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st4.click()
            st4.send_keys("kjjung+pp2002@suprema.co.kr")

            st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            st5.click()

            time.sleep(3)

            st6 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st6.click()
            st6.send_keys("ABCDEFG")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\nkjjung+pp2002@suprema.co.kr\n인증번호\n인증번호는 6자리 숫자입니다.").is_displayed()

            authDisabledBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            isAuthBtn = authDisabledBtn.is_enabled()
            self.assertFalse(isAuthBtn, "인증완료 버튼이이 비활성화되어 있습니다.")
            st6.clear()

            st7 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st7.click()
            st7.send_keys("abcdefg")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\nkjjung+pp2002@suprema.co.kr\n인증번호\n인증번호는 6자리 숫자입니다.").is_displayed()

            authDisabledBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            isAuthBtn = authDisabledBtn.is_enabled()
            self.assertFalse(isAuthBtn, "인증완료 버튼이이 비활성화되어 있습니다.")
            st7.clear()

            st8 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st8.click()
            st8.send_keys("가나다라마바사")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\nkjjung+pp2002@suprema.co.kr\n인증번호\n인증번호는 6자리 숫자입니다.").is_displayed()

            authDisabledBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            isAuthBtn = authDisabledBtn.is_enabled()
            self.assertFalse(isAuthBtn, "인증완료 버튼이이 비활성화되어 있습니다.")
            st8.clear()

            st9 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st9.click()
            st9.send_keys("!@#$%^&*()")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\nkjjung+pp2002@suprema.co.kr\n인증번호\n인증번호는 6자리 숫자입니다.").is_displayed()

            authDisabledBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            isAuthBtn = authDisabledBtn.is_enabled()
            self.assertFalse(isAuthBtn, "인증완료 버튼이이 비활성화되어 있습니다.")
            st9.clear()

            st10 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st10.click()
            st10.send_keys("123")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\nkjjung+pp2002@suprema.co.kr\n인증번호\n인증번호는 6자리 숫자입니다.").is_displayed()

            authDisabledBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            isAuthBtn = authDisabledBtn.is_enabled()
            self.assertFalse(isAuthBtn, "인증완료 버튼이 비활성화되어 있습니다.")
            st10.clear()

            st11 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st11.click()
            st11.send_keys("1234567890123450000")
            er11 = st11.text
            print(er11)
            self.assertEqual("123456", er11)
            time.sleep(1)
            st11.clear()

            st12 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st12.click()
            st12.send_keys("123456")

            authEnabledBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            isAuthBtn = authEnabledBtn.is_enabled()
            self.assertTrue(isAuthBtn, "인증완료 버튼이 활성화되어 있습니다.")

            st12 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            st12.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증 코드 오류").is_displayed()

            authError_Pop = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증 코드가 일치하지 않습니다. \n다시 입력해 주세요.\na1005']")
            contentDesc = authError_Pop.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "인증 코드가 일치하지 않습니다. \n다시 입력해 주세요.\na1005")
            st13 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            st13.click()

            pass

            print("DQS-T999999_12 이메일로 회원가입 인증번호 입력 페이지의 인증번호 인풋 박스 유효성 검사 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("이메일로 회원가입 인증번호 입력 페이지의 인증번호 인풋 박스 유효성 검사 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14146(self):
        try:
            print("DQS-T14146 모바일 회원가입 인증번호 입력 페이지에서 인증번호 재전송 시 기능 동작 확인")

            phone_num = "010" + str(random.randint(10000000, 99999999)).zfill(8)
            print(phone_num)

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            st2.click()

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            st3.click()

            moblieSel = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "모바일")
            moblieSel.click()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st4.click()
            st4.send_keys(phone_num)

            st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            st5.click()

            time.sleep(3)

            resendBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "재전송")
            resendBtn.click()
            time.sleep(1)

            utils.authCode_mobile(self)

            self.driver.hide_keyboard()

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authBtn.click()

            formatted_phone = f"{phone_num[:3]} {phone_num[3:7]} {phone_num[7:]}"
            print(formatted_phone)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "프로필 입력").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"{formatted_phone}").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이름").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재입력").is_displayed()

            pass

            print("DQS-T14146 모바일 회원가입 인증번호 입력 페이지에서 인증번호 재전송 시 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14146 모바일 회원가입 인증번호 입력 페이지에서 인증번호 재전송 시 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_20(self):
        try:
            print("DQS-T999999_20 이메일 회원가입 인증번호 입력 페이지에서 인증번호 재전송 시 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            st2.click()

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            st3.click()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st4.click()
            st4.send_keys("kjjung+pp2002@suprema.co.kr")

            st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            st5.click()

            time.sleep(3)

            resendBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "재전송")
            resendBtn.click()
            time.sleep(1)

            utils.authCode(self)

            self.driver.hide_keyboard()

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "프로필 입력").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung+pp2002@suprema.co.kr").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이름").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재입력").is_displayed()

            pass

            print("DQS-T14146 이메일 회원가입 인증번호 입력 페이지에서 인증번호 재전송 시 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14146 이메일 회원가입 인증번호 입력 페이지에서 인증번호 재전송 시 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14147(self):
        try:
            print("DQS-T14147 회원가입에 프로필 입력 페이지의 이름 인풋 박스 유효성 검사")

            phome_num = "010" + str(random.randint(10000000, 99999999)).zfill(8)
            print(phome_num)

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            st2.click()

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            st3.click()

            moblieSel = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "모바일")
            moblieSel.click()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st4.click()
            st4.send_keys(phome_num)

            st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            st5.click()

            time.sleep(1)

            utils.authCode_mobile(self)

            self.driver.hide_keyboard()

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authBtn.click()

            nameInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[1]")
            nameInput1.click()
            nameInput1.send_keys("Ab")

            name1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Ab']")
            text1 = name1.get_attribute('text')
            print(f"추출한 text 값 : {text1}")
            self.assertEqual(text1, "Ab")

            delete1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Ab']/android.widget.ImageView")
            delete1.click() #DQS-T14149 회원가입에 프로필 입력 이름 인풋 박스 X 버튼 기능 동작 확인 포함됨
            print("------------------- Ab 완료")

            nameInput2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[1]")
            nameInput2.click()
            nameInput2.send_keys("12")

            name2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='12']")
            text2 = name2.get_attribute('text')
            print(f"추출한 text 값 : {text2}")
            self.assertEqual(text2, "12")

            delete2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='12']/android.widget.ImageView")
            delete2.click()
            print("------------------- 12 완료")

            nameInput3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[1]")
            nameInput3.click()
            nameInput3.send_keys("-_")

            name3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='-_']")
            text3 = name3.get_attribute('text')
            print(f"추출한 text 값 : {text3}")
            self.assertEqual(text3, "-_")

            delete3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='-_']/android.widget.ImageView")
            delete3.click()
            print("------------------- -_ 완료")

            nameInput4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[1]")
            nameInput4.click()
            nameInput4.send_keys("!@#$%^&*()")

            name4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='!@#$%^&*()']")
            text4 = name4.get_attribute('text')
            print(f"추출한 text 값 : {text4}")
            self.assertEqual(text4, "!@#$%^&*()")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.")
            errorText1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='공백,-,_, 외의 특수문자는 사용할 수 없습니다.']")
            contentDesc1 = errorText1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.")

            delete4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='!@#$%^&*()']/android.widget.ImageView")
            delete4.click()
            print("------------------- !@#$%^&*() 완료")

            nameInput5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[1]")
            nameInput5.click()
            nameInput5.send_keys("Ab1")

            name5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Ab1']")
            text5 = name5.get_attribute('text')
            print(f"추출한 text 값 : {text5}")
            self.assertEqual(text5, "Ab1")

            delete5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Ab1']/android.widget.ImageView")
            delete5.click()
            print("------------------- Ab1 완료")

            nameInput6 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[1]")
            nameInput6.click()
            nameInput6.send_keys("Ab가")

            name6 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Ab가']")
            text6 = name6.get_attribute('text')
            print(f"추출한 text 값 : {text6}")
            self.assertEqual(text6, "Ab가")

            delete6 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Ab가']/android.widget.ImageView")
            delete6.click()
            print("------------------- Ab가 완료")

            nameInput7 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[1]")
            nameInput7.click()
            nameInput7.send_keys("Ab-_")

            name7 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Ab-_']")
            text7 = name7.get_attribute('text')
            print(f"추출한 text 값 : {text7}")
            self.assertEqual(text7, "Ab-_")

            delete7 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Ab-_']/android.widget.ImageView")
            delete7.click()
            print("------------------- Ab-_ 완료")

            nameInput8 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[1]")
            nameInput8.click()
            nameInput8.send_keys("Ab!")

            name8 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Ab!']")
            text8 = name8.get_attribute('text')
            print(f"추출한 text 값 : {text8}")
            self.assertEqual(text8, "Ab!")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.")
            errorText2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='공백,-,_, 외의 특수문자는 사용할 수 없습니다.']")
            contentDesc2 = errorText2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.")

            delete8 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Ab!']/android.widget.ImageView")
            delete8.click()
            print("------------------- Ab! 완료")


            nameInput9 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[1]")
            nameInput9.click()
            nameInput9.send_keys("1가")

            name9 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='1가']")
            text9 = name9.get_attribute('text')
            print(f"추출한 text 값 : {text9}")
            self.assertEqual(text9, "1가")

            delete9 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='1가']/android.widget.ImageView")
            delete9.click()
            print("------------------- 1가 완료")

            nameInput10 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[1]")
            nameInput10.click()
            nameInput10.send_keys("1-_")

            name10 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='1-_']")
            text10 = name10.get_attribute('text')
            print(f"추출한 text 값 : {text10}")
            self.assertEqual(text10, "1-_")

            delete10 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='1-_']/android.widget.ImageView")
            delete10.click()
            print("------------------- 1-_ 완료")

            nameInput11 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[1]")
            nameInput11.click()
            nameInput11.send_keys("가-_")

            name11 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='가-_']")
            text11 = name11.get_attribute('text')
            print(f"추출한 text 값 : {text11}")
            self.assertEqual(text11, "가-_")

            delete11 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='가-_']/android.widget.ImageView")
            delete11.click()
            print("------------------- 가-_ 완료")

            nameInput12 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[1]")
            nameInput12.click()
            nameInput12.send_keys("가!@#$%^&*()")

            name12 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='가!@#$%^&*()']")
            text12 = name12.get_attribute('text')
            print(f"추출한 text 값 : {text12}")
            self.assertEqual(text12, "가!@#$%^&*()")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.")
            errorText3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='공백,-,_, 외의 특수문자는 사용할 수 없습니다.']")
            contentDesc3 = errorText3.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc3}")
            self.assertEqual(contentDesc3, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.")

            delete12 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='가!@#$%^&*()']/android.widget.ImageView")
            delete12.click()
            print("------------------- 가!@#$%^&*() 완료")

            nameInput13 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[1]")
            nameInput13.click()
            nameInput13.send_keys("ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789012345678901234567890123456789012345678901234567890123456")

            name13 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789012345678901234567890123456789012345678901234567890123456']")
            text13 = name13.get_attribute('text')
            print(f"추출한 text 값 : {text13}")
            self.assertEqual(text13, "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789012345678901234567890123456789012345678901234567890123456")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.")
            errorText4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='공백,-,_, 외의 특수문자는 사용할 수 없습니다.']")
            contentDesc4 = errorText4.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc4}")
            self.assertEqual(contentDesc4, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.")

            print("-------------------- ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789012345678901234567890123456789012345678901234567890123456 완료")

            pass

            print("DQS-T14147 회원가입에 프로필 입력 페이지의 이름 인풋 박스 유효성 검사 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14147 회원가입에 프로필 입력 페이지의 이름 인풋 박스 유효성 검사 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14151_T14213_T14152(self):
        try:
            print("DQS-T14151 회원가입에 프로필 입력 페이지의 비밀번호 인풋 박스 유효성 검사 || DQS-T14213 회원가입에서 프로필 입력 페이지의 비밀번호 재입력 인풋 박스 유효성 검사 || DQS-T14152 회원가입에 프로필 입력 페이지에서 비밀번호 와 비밀번호 재입력 값이 다른 경우 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            st2.click()

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            st3.click()

            moblieSel = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "모바일")
            moblieSel.click()

            phone_Num = "010" + str(random.randint(0, 99999999)).zfill(8)
            print(phone_Num)
            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st4.click()
            st4.send_keys(phone_Num)

            st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            st5.click()

            time.sleep(1)

            utils.authCode_mobile(self)

            self.driver.hide_keyboard()

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authBtn.click()

            nameInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[1]")
            nameInput.click()
            nameInput.send_keys("TestName")

            utils.passwordValidtion(self)

            time.sleep(0.5)
            print("------------------- DQS-T14213 시작")
            utils.RePasswordValidtion(self)

            print("------------------- DQS-T14152 시작")
            passInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[2]")
            passInput.click()
            passInput.send_keys("Kjstar36!!")

            rePassInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[3]")
            rePassInput.click()
            rePassInput.send_keys("Kjstar36!@")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호가 일치하지 않습니다.").is_displayed()
            errorText = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='비밀번호가 일치하지 않습니다.']")
            contentDesc = errorText.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "비밀번호가 일치하지 않습니다.")

            print("------------------- DQS-T14152 완료")


            pass

            print("DQS-T14151 회원가입에 프로필 입력 페이지의 비밀번호 인풋 박스 유효성 검사 || DQS-T14213 회원가입에서 프로필 입력 페이지의 비밀번호 재입력 인풋 박스 유효성 검사 || DQS-T14152 회원가입에 프로필 입력 페이지에서 비밀번호 와 비밀번호 재입력 값이 다른 경우 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14151 DQS-T14151 회원가입에 프로필 입력 페이지의 비밀번호 인풋 박스 유효성 검사 || DQS-T14213 회원가입에서 프로필 입력 페이지의 비밀번호 재입력 인풋 박스 유효성 검사 || DQS-T14152 회원가입에 프로필 입력 페이지에서 비밀번호 와 비밀번호 재입력 값이 다른 경우 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14153(self):
        try:
            print("DQS-T14153 비밀번호 찾기 페이지의 휴대폰 번호 인풋 박스 유효성 검사")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            st2.click()

            st3 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st3.click()
            text_to_input = "ABCDEFG"
            er3 = st3.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er3)
            st3.clear()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st4.click()
            text_to_input = "abcdefg"
            er4 = st4.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er4)
            st4.clear()

            st5 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st5.click()
            text_to_input = "가나다라마바사"
            er5 = st5.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er5)
            st5.clear()

            st6 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st6.click()
            text_to_input = "!@#$%^&*()"
            er6 = st6.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er6)
            st6.clear()

            st7 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st7.click()
            st7.send_keys("123456789")
            er7 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123 456 789']")
            text1 = er7.get_attribute('text')
            print(f"추출한 text 값 : {text1}")
            time.sleep(3)
            self.assertEqual("123 456 789", text1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.").is_displayed()
            wrongPho_Text = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.']")
            contentDesc1 = wrongPho_Text.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.")
            st7.clear()

            st8 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st8.click()
            st8.send_keys("1234567890123450000")
            er8 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123 4567 8901']")
            text2 = er8.get_attribute('text')
            print(f"추출한 text 값 : {text2}")
            self.assertEqual("123 4567 8901", text2)

            authRequset1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            isNext1 = authRequset1.is_enabled()
            self.assertFalse(isNext1, "인증요청 버튼이 비활성화되어 있습니다.")

            deleteBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123 4567 8901']/android.widget.ImageView")
            deleteBtn.click()

            st9 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st9.click()
            st9.send_keys("01012345678")
            er9 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010 1234 5678']")
            text3 = er9.get_attribute('text')
            print(f"추출한 text 값 : {text3}")
            self.assertEqual("010 1234 5678", text3)

            authRequset2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            isNext2 = authRequset2.is_enabled()
            self.assertTrue(isNext2, "인증요청 버튼이 활성화되어 있습니다.")

            pass

            print("DQS-T14153 비밀번호 찾기 페이지의 휴대폰 번호 인풋 박스 유효성 검사 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14153 비밀번호 찾기 페이지의 휴대폰 번호 인풋 박스 유효성 검사 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_23(self):
        try:
            print("DQS-T999999_23 비밀번호 찾기 페이지의 이메일 주소 인풋 박스 유효성 검사")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            st2.click()

            st3 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st3.click()
            st3.send_keys("가나다@suprema.co.kr")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\n입력 형식이 맞지 않습니다.").is_displayed()
            st3.clear()
            print("----------------- 가나다@suprema.co.kr 완료")

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st4.click()
            st4.send_keys("123456789")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\n입력 형식이 맞지 않습니다.").is_displayed()
            st4.clear()
            print("----------------- 123456789 완료")

            st5 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st5.click()
            st5.send_keys("abcdefg")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\n입력 형식이 맞지 않습니다.").is_displayed()
            st5.clear()
            print("----------------- abcdefg 완료")

            st6 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st6.click()
            st6.send_keys("kjjung@suprema.")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\n입력 형식이 맞지 않습니다.").is_displayed()
            st6.clear()
            print("----------------- kjjung@suprema. 완료")

            st7 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st7.click()
            st7.send_keys("kjjung@suprema.co.kr.")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소\n입력 형식이 맞지 않습니다.").is_displayed()
            print("----------------- kjjung@suprema.co.kr. 완료")

            authRequset1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            isNext1 = authRequset1.is_enabled()
            self.assertFalse(isNext1, "인증요청 버튼이 비활성화되어 있습니다.")
            st7.clear()

            st8 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st8.click()
            st8.send_keys("kjjung@suprema.co.kr")

            authRequset2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            isNext2 = authRequset2.is_enabled()
            self.assertTrue(isNext2, "인증요청 버튼이 활성화되어 있습니다.")
            print("----------------- kjjung@suprema.co.kr 완료")
            pass

            print("DQS-T999999_23 비밀번호 찾기 페이지의 이메일 주소 인풋 박스 유효성 검사 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T999999_23 비밀번호 찾기 페이지의 이메일 주소 인풋 박스 유효성 검사 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14154(self):
        try:
            print("DQS-T14154 비밀번호 찾기 페이지의 휴대폰 번호 인풋 박스 X 버튼 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            st2.click()

            st3 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st3.click()
            st3.send_keys("01022221111")

            self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010 2222 1111']/android.widget.ImageView").is_displayed()
            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010 2222 1111']/android.widget.ImageView")
            st3.click()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            re = st4.text
            print(re)
            self.assertEqual("", re)

            try:
                self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010 2222 1111']/android.widget.ImageView")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                #assert True, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            pass

            print("DQS-T14154 비밀번호 찾기 페이지의 휴대폰 번호 인풋 박스 X 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14154 비밀번호 찾기 페이지의 휴대폰 번호 인풋 박스 X 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_24(self):
        try:
            print("DQS-T999999_24 비밀번호 찾기 페이지의 이메일 주소 인풋 박스 X 버튼 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            st2.click()

            st3 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            st3.click()
            st3.send_keys("kjjung@suprema.co.kr")

            self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='kjjung@suprema.co.kr']/android.widget.ImageView").is_displayed()
            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='kjjung@suprema.co.kr']/android.widget.ImageView")
            st3.click()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            re = st4.text
            print(re)
            self.assertEqual("", re)

            try:
                self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='kjjung@suprema.co.kr']/android.widget.ImageView")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                #assert True, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            pass

            print("DQS-T999999_24 비밀번호 찾기 페이지의 이메일 주소 인풋 박스 X 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T999999_24 비밀번호 찾기 페이지의 이메일 주소 인풋 박스 X 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14156(self):
        try:
            print("DQS_T14156 비밀번호 찾기 기능 중 당일 탈퇴 휴대폰 번호 입력 시 동작 확인")

            phone_num = "010" + str(random.randint(0, 99999999)).zfill(8)
            print(phone_num)

            utils.signUpMobile(self, phone_num)

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            login_button.click()

            phone_input_box = self.driver.find_element(AppiumBy.XPATH, phoneNumberInputBox)
            phone_input_box.click()
            phone_input_box.send_keys(phone_num)

            password_input_box = self.driver.find_element(AppiumBy.XPATH, passwordInputBox)
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            login_button.click()
            time.sleep(2)

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

            self.driver.quit()

            print("--------- 비밀번호 찾기에서 회원탈퇴한 전화번호 입력 후 팝업 동작 시작")
            time.sleep(3)

            options = UiAutomator2Options()
            options.platform_name = 'Android'
            options.device_name = 'R3CXB0MKLGP'
            options.app_package = 'com.suprema.moon'
            options.app_activity = 'com.suprema.moon.MainActivity'
            options.automation_name = 'UiAutomator2'
            options.auto_grant_permissions = True
            options.no_reset = True

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

            time.sleep(1)

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            login_button.click()

            resetPassword = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            resetPassword.click()

            phone_input_box = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            phone_input_box.click()
            phone_input_box.send_keys(phone_num)

            authRequest_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            authRequest_Btn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인 정보 오류").is_displayed()
            loginErrorMsg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000']")
            contentDesc = loginErrorMsg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000")
            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()

            pass

            print("DQS_T14156 비밀번호 찾기 기능 중 당일 탈퇴 휴대폰 번호 입력 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T14156 비밀번호 찾기 기능 중 당일 탈퇴 휴대폰 번호 입력 시 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_25(self):
        try:
            print("DQS_T999999_25 비밀번호 찾기 기능 중 당일 탈퇴 이메일 주소 입력 시 동작 확인")

            email_random = "kjjung+pp" +str(random.randint(1000, 9999)).zfill(3) + "@suprema.co.kr"
            print(email_random)

            utils.signUpEmail(self, email_random)
            time.sleep(3)

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            login_button.click()

            email_input_box = self.driver.find_element(AppiumBy.XPATH, emailInputBox)
            email_input_box.click()
            email_input_box.send_keys(email_random)

            password_input_box = self.driver.find_element(AppiumBy.XPATH, emailPasswordInputBox)
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            login_button.click()
            time.sleep(2)

            utils.authCode(self)

            self.driver.hide_keyboard()

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authBtn.click()

            leadbutton = self.driver.find_element(AppiumBy.XPATH, lead)
            leadbutton.click()

            csctBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터")
            csctBtn.click()
            time.sleep(0.3)

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

            self.driver.quit()

            print("--------- 비밀번호 찾기에서 회원탈퇴한 이메일 입력 후 팝업 동작 시작")
            time.sleep(3)

            options = UiAutomator2Options()
            options.platform_name = 'Android'
            options.device_name = 'R3CXB0MKLGP'
            options.app_package = 'com.suprema.moon'
            options.app_activity = 'com.suprema.moon.MainActivity'
            options.automation_name = 'UiAutomator2'
            options.auto_grant_permissions = True
            options.no_reset = True

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

            time.sleep(1)

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            login_button.click()

            resetPassword = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            resetPassword.click()

            email_input_box = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            email_input_box.click()
            email_input_box.send_keys(email_random)

            authRequest_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            authRequest_Btn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인 정보 오류").is_displayed()
            loginErrorMsg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000']")
            contentDesc = loginErrorMsg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000")
            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()

            pass

            print("DQS_T999999_25 비밀번호 찾기 기능 중 당일 탈퇴 이메일 주소 입력 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T999999_25 비밀번호 찾기 기능 중 당일 탈퇴 이메일 주소 입력 시 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14216_T14217_T14163(self):
        try:
            print("DQS-T14216 비밀번호 찾기 비밀번호 재설정 페이지의 비밀번호 입력 인풋 박스 유효성 검사 || DQS-T14217 비밀번호 찾기 비밀번호 재설정 페이지의 비밀번호 재입력 인풋 박스 유효성 검사 || DQS-T14163 비밀번호 찾기 비밀번호 재설정 페이지에서 비밀번호 와 비밀번호 재입력 값이 다른 경우 확인")

            phone_num = "010" + str(random.randint(0, 99999999)).zfill(8)
            print(phone_num)

            utils.signUpMobile(self, phone_num)

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            login_button.click()

            resetPassword = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            resetPassword.click()

            phone_input = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            phone_input.click()
            phone_input.send_keys(phone_num)

            authReBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            authReBtn.click()
            time.sleep(1)

            utils.authCode_mobile(self)

            self.driver.hide_keyboard()

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authBtn.click()

            utils.resetPasswordValidtion(self)

            time.sleep(0.5)
            print("------------------- DQS-T14217 시작")
            utils.resetRePasswordValidtion(self)

            print("------------------- DQS-T14163 시작")
            passInput = self.driver.find_element(AppiumBy.XPATH, f"//android.view.View[@content-desc='휴대폰 번호\n{phone_num}\n비밀번호\n비밀번호 재입력']/android.widget.EditText[1]")
            passInput.click()
            passInput.send_keys("Kjstar36!!")

            rePassInput = self.driver.find_element(AppiumBy.XPATH, f"//android.view.View[@content-desc='휴대폰 번호\n{phone_num}\n비밀번호\n비밀번호 재입력']/android.widget.EditText[2]")
            rePassInput.click()
            rePassInput.send_keys("Kjstar36!@")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_num}\n비밀번호\n비밀번호 재입력\n비밀번호가 일치하지 않습니다.").is_displayed()

            print("------------------- DQS-T14152 완료")

            print("------------------- 임의 폰번호로 회원가입된 계정 탈퇴 시작")

            self.driver.tap([(72, 166)])
            time.sleep(1)
            # backBtn = self.driver.find_element(AppiumBy.XPATH, f"//android.view.View[@content-desc='휴대폰 번호\n({phone_num})\n비밀번호\n비밀번호 재입력\n비밀번호가 알치하지 않습니다.']/android.view.View/android.widget.ImageView")
            # backBtn.click()

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            login_button.click()

            phone_input_box = self.driver.find_element(AppiumBy.XPATH, phoneNumberInputBox)
            phone_input_box.click()
            phone_input_box.send_keys(phone_num)

            password_input_box = self.driver.find_element(AppiumBy.XPATH, passwordInputBox)
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            login_button.click()
            time.sleep(2)

            utils.leaveAdmin(self)
            print("------------------- 임의 폰번호로 회원가입된 계정 탈퇴 성공")

            pass

            print("DQS-T14151 회원가입에 프로필 입력 페이지의 비밀번호 인풋 박스 유효성 검사 || DQS-T14213 회원가입에서 프로필 입력 페이지의 비밀번호 재입력 인풋 박스 유효성 검사 || DQS-T14152 회원가입에 프로필 입력 페이지에서 비밀번호 와 비밀번호 재입력 값이 다른 경우 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14151 DQS-T14151 회원가입에 프로필 입력 페이지의 비밀번호 인풋 박스 유효성 검사 || DQS-T14213 회원가입에서 프로필 입력 페이지의 비밀번호 재입력 인풋 박스 유효성 검사 || DQS-T14152 회원가입에 프로필 입력 페이지에서 비밀번호 와 비밀번호 재입력 값이 다른 경우 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14223(self):
        try:
            print("DQS-T14223 회원가입 휴대폰 번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "약관 전체 동의")
            agree.click()

            next = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next.click()

            mobileSel = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "모바일")
            mobileSel.click()

            backBtn = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='휴대폰 번호']/android.view.View/android.widget.ImageView")
            backBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()

            pass

            print("DQS-T14223 회원가입 휴대폰 번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14223 회원가입 휴대폰 번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_27(self):
        try:
            print("DQS-T999999_27 회원가입 이메일 주소 입력 페이지의 뒤로가기 버튼 기능 동작 확인")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "약관 전체 동의")
            agree.click()

            next = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next.click()

            emailSel = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일")
            emailSel.click()

            backBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            backBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()

            pass

            print("DQS-T999999_27 회원가입 이메일 주소 입력 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T999999_27 회원가입 이메일 주소 입력 페이지의 뒤로가기 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14224(self):
        try:
            print("DQS-T14224 회원가입 휴대폰 인증번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "약관 전체 동의")
            agree.click()

            next = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next.click()

            mobileSel = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "모바일")
            mobileSel.click()

            mobile_input = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            mobile_input.click()
            mobile_input.send_keys("01079461346")

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            authBtn.click()

            time.sleep(3)

            backBtn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
            backBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()

            pass

            print("DQS-T14224 회원가입 휴대폰 인증번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14224 회원가입 휴대폰 인증번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_28(self):
        try:
            print("DQS-T999999_28 회원가입 이메일 인증번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "약관 전체 동의")
            agree.click()

            next = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next.click()

            emailSel = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일")
            emailSel.click()

            email_input = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            email_input.click()
            email_input.send_keys("kjjung+back1@suprema.co.kr")

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            authBtn.click()

            time.sleep(3)

            backBtn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
            backBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()

            pass

            print("DQS-T999999_28 회원가입 이메일 인증번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T999999_28 회원가입 이메일 인증번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14222(self):
        try:
            print("DQS-T14222 회원가입 약관 동의 페이지의 뒤로가기 버튼 기능 동작 확인")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            backBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='고객님 \n환영합니다.']/android.view.View[1]/android.widget.ImageView")
            backBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()

            pass

            print("DQS-T14222 회원가입 약관 동의 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14222 회원가입 약관 동의 페이지의 뒤로가기 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14220(self):
        try:
            print("DQS-T14220 비밀번호 찾기 인증번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인")

            print("----- PreCondition: 이메일, 모바일 회원가입-----")
            email_random = "kjjung+pp" + str(random.randint(11,9999)).zfill(3) + "@suprema.co.kr"
            print(email_random)
            time.sleep(2)

            mobile_random = "010" + str(random.randint(0, 99999999)).zfill(8)
            print(mobile_random)
            time.sleep(2)

            utils.signUpEmail(self,email_random)
            time.sleep(2)

            utils.signUpMobile(self, mobile_random)
            time.sleep(2)

            print("----- PreCondition 완료(회원가입 완료)-----")

            loginBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            loginBtn.click()

            resetPassword = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            resetPassword.click()

            emailInput = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            emailInput.click()
            emailInput.send_keys(email_random)

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청")
            st3.click()
            time.sleep(3)

            backBtn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
            backBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()

            mobile_login = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            mobile_login.click()

            resetPassword = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            resetPassword.click()

            mobileInput = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            mobileInput.click()
            mobileInput.send_keys(mobile_random)

            authReBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            authReBtn.click()
            time.sleep(3)

            backBtn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
            backBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()

            print("----- 회원가입된 이메일/모바일 계정 회원 틸퇴 -----")
            print("----- 1. 이메일계정 회원 틸퇴 시작 -----")

            utils.email_login(self, email_random, "Kjstar36!!")

            utils.leaveAdmin(self)
            print("----- 1. 이메일계정 회원 틸퇴 완료-----")

            print("----- 1. 모바일계정 회원 틸퇴 시작 -----")

            utils.mobile_login(self, mobile_random, "Kjstar36!!")

            utils.leaveAdmin(self)
            print("----- 1. 모바일계정 회원 틸퇴 완료-----")

            pass

            print("DQS-T14220 비밀번호 찾기 인증번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14220 비밀번호 찾기 인증번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14221(self):
        try:
            print("DQS-T14221 비밀번호 찾기 비밀번호 재설정 페이지의 뒤로가기 버튼 기능 동작 확인")

            print("----- PreCondition: 이메일, 모바일 회원가입-----")
            email_random = "kjjung+pp" + str(random.randint(11,9999)).zfill(3) + "@suprema.co.kr"
            print(email_random)
            time.sleep(2)

            mobile_random = "010" + str(random.randint(0, 99999999)).zfill(8)
            print(mobile_random)
            time.sleep(2)

            utils.signUpEmail(self,email_random)
            time.sleep(2)

            utils.signUpMobile(self, mobile_random)
            time.sleep(2)

            print("----- PreCondition 완료(회원가입 완료)-----")

            email_login = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            email_login.click()

            resetPassword = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            resetPassword.click()

            emailInput = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            emailInput.click()
            emailInput.send_keys(email_random)

            authReBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            authReBtn.click()
            time.sleep(3)

            utils.authCode(self)

            authComBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authComBtn.click()

            backBtn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
            backBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()


            mobile_login = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            mobile_login.click()

            resetPassword = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            resetPassword.click()

            emailInput = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            emailInput.click()
            emailInput.send_keys(mobile_random)

            authReBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            authReBtn.click()
            time.sleep(3)

            utils.authCode_mobile(self)

            authComBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authComBtn.click()

            backBtn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
            backBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()

            print("----- 회원가입된 이메일/모바일 계정 회원 틸퇴 -----")
            print("----- 1. 이메일계정 회원 틸퇴 시작 -----")

            utils.email_login(self, email_random, "Kjstar36!!")

            utils.leaveAdmin(self)
            print("----- 1. 이메일계정 회원 틸퇴 완료-----")

            print("----- 1. 모바일계정 회원 틸퇴 시작 -----")

            utils.mobile_login(self, mobile_random, "Kjstar36!!")

            utils.leaveAdmin(self)
            print("----- 1. 모바일계정 회원 틸퇴 완료-----")

            pass

            print("DQS-T14221 비밀번호 찾기 비밀번호 재설정 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14221 비밀번호 찾기 비밀번호 재설정 페이지의 뒤로가기 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14219(self):
        try:
            print("DQS-T14219 비밀번호 찾기 휴대폰 번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인")

            email_login = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            email_login.click()

            resetPassword = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            resetPassword.click()

            backBtn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
            backBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()


            mobile_login = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            mobile_login.click()

            resetPassword = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            resetPassword.click()

            backBtn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
            backBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()

            pass

            print("DQS-T14219 비밀번호 찾기 휴대폰 번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14219 비밀번호 찾기 휴대폰 번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14218(self):
        try:
            print("DQS-T14218 로그인 페이지에서 뒤로가기 버튼 기능 동작 확인")
            email_login = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            email_login.click()

            backBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='이메일 주소\n비밀번호']/android.view.View/android.widget.ImageView")
            backBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()

            mobile_login = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            mobile_login.click()

            backBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='휴대폰 번호\n비밀번호']/android.view.View/android.widget.ImageView")
            backBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin).is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()

            pass

            print("DQS-T14218 로그인 페이지에서 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14218 로그인 페이지에서 뒤로가기 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14157(self):
        try:
            print("DQS-T14157 비밀번호 찾기 인증번호 입력 페이지의 인증번호 인풋 박스 유효성 검사")

            phone_num = "010" + str(random.randint(0, 99999999)).zfill(8)
            print(phone_num)

            utils.signUpMobile(self, phone_num)

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            st2.click()

            st2 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st2.click()
            st2.send_keys(phone_num)

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청")
            st3.click()
            time.sleep(3)

            st3 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st3.click()
            st3.send_keys("ABCDEFG")
            input1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='ABCDEF']")
            er3 = input1.text
            self.assertEqual("ABCDEF", er3)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_num}\n인증번호\n인증번호는 6자리 숫자입니다.").is_displayed()

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            isNext1 = authBtn.is_enabled()
            self.assertFalse(isNext1, "인증요청 버튼이 비활성화되어 있습니다.")
            st3.clear()
            print(" --------- ABCDCDEFG 입력 후 가이드 문구 및 인증요청 버튼 비활성화 확인")

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st4.click()
            st4.send_keys("abcdef")
            er4 = st4.text
            self.assertEqual("abcdef", er4)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_num}\n인증번호\n인증번호는 6자리 숫자입니다.").is_displayed()

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            isNext1 = authBtn.is_enabled()
            self.assertFalse(isNext1, "인증요청 버튼이 비활성화되어 있습니다.")
            st4.clear()
            print(" --------- abcdef 입력 후 가이드 문구 및 인증요청 버튼 비활성화 확인")

            st5 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st5.click()
            st5.send_keys("가나다라마바")
            er5 = st5.text
            self.assertEqual("가나다라마바", er5)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_num}\n인증번호\n인증번호는 6자리 숫자입니다.").is_displayed()

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            isNext1 = authBtn.is_enabled()
            self.assertFalse(isNext1, "인증요청 버튼이 비활성화되어 있습니다.")
            st5.clear()
            print(" --------- 가나다라마바 입력 후 가이드 문구 및 인증요청 버튼 비활성화 확인")

            st6 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st6.click()
            st6.send_keys("!@#$%^&*()")
            input2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='!@#$%^']")
            er6 = input2.text
            self.assertEqual("!@#$%^", er6)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_num}\n인증번호\n인증번호는 6자리 숫자입니다.").is_displayed()

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            isNext1 = authBtn.is_enabled()
            self.assertFalse(isNext1, "인증요청 버튼이 비활성화되어 있습니다.")
            st6.clear()
            print(" --------- !@#$%^&*() 입력 후 가이드 문구 및 인증요청 버튼 비활성화 확인")

            st7 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st7.click()
            st7.send_keys("123")
            er7 = st7.text
            self.assertEqual("123", er7)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_num}\n인증번호\n인증번호는 6자리 숫자입니다.").is_displayed()

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            isNext1 = authBtn.is_enabled()
            self.assertFalse(isNext1, "인증요청 버튼이 비활성화되어 있습니다.")
            st7.clear()
            print(" --------- 123 입력 후 가이드 문구 및 인증요청 버튼 비활성화 확인")

            st8 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st8.click()
            st8.send_keys("9876543210")
            er8 = st8.text
            self.assertEqual("987654", er8)
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_num}\n인증번호").is_displayed()

            authBtn2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            isNext2 = authBtn2.is_enabled()
            self.assertTrue(isNext2, "인증요청 버튼이 활성화되어 있습니다.")
            st8.clear()
            print(" --------- 9876543210 입력 후 가이드 문구 및 인증요청 버튼 활성화 확인")

            st9 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st9.click()
            st9.send_keys("123456")

            authBtn2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            isNext2 = authBtn2.is_enabled()
            self.assertTrue(isNext2, "인증요청 버튼이 활성화되어 있습니다.")

            pass

            print("DQS-T14157 비밀번호 찾기 인증번호 입력 페이지의 인증번호 인풋 박스 유효성 검사| Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14157 비밀번호 찾기 인증번호 입력 페이지의 인증번호 인풋 박스 유효성 검사 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14159(self):
        try:
            print("DQS_T14159 모바일로 로그인에서 비밀번호 찾기 인증번호 입력 페이지의 인증번호 재전송 버튼 기능 동작 확인")

            phone_Num = "010" + str(random.randint(0, 99999999)).zfill(8)
            print(phone_Num) #랜덤 폰번호로 회원가입 -> 비밀번호 찾기 테스트 시 잦은 시도 팝업 발생으로 신규 가입 후 테스트 시나리오 진행

            utils.signUpMobile(self, phone_Num)

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            st2.click()

            st2 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st2.click()
            st2.send_keys(phone_Num)

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청")
            st3.click()
            time.sleep(3)

            utils.authCode_mobile(self)

            resendBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "재전송")
            resendBtn.click()
            time.sleep(3)

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authBtn.click()
            time.sleep(0.5)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증코드 오류").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다른 코드가 입력 되었네요. \n다시 확인 후 시도해보세요.\na1021").is_displayed()
            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st4.click()
            st4.clear()
            time.sleep(1)

            utils.authCode_mobile(self)

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authBtn.click()
            time.sleep(0.5)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"휴대폰 번호\n{phone_Num}\n비밀번호\n비밀번호 재입력").is_displayed()

            print("------------- 테스트 시나리오 종료, 회원탈퇴 시도")

            self.driver.quit()

            time.sleep(1)

            options = UiAutomator2Options()
            options.platform_name = 'Android'
            options.device_name = 'R3CXB0MKLGP'
            options.app_package = 'com.suprema.moon'
            options.app_activity = 'com.suprema.moon.MainActivity'
            options.automation_name = 'UiAutomator2'
            options.auto_grant_permissions = True
            options.no_reset = True

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

            time.sleep(1)

            utils.mobile_login(self, phone_Num, "Kjstar36!!")

            utils.leaveAdmin(self)

            pass

            print("DQS_T14159 모바일로 로그인에서 비밀번호 찾기 인증번호 입력 페이지의 인증번호 재전송 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T14159 모바일로 로그인에서 비밀번호 찾기 인증번호 입력 페이지의 인증번호 재전송 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_26(self):
        try:
            print("DQS_T999999_26 이메일로 로그인에서 비밀번호 찾기 인증번호 입력 페이지의 인증번호 재전송 버튼 기능 동작 확인")

            email_random = "kjjung+pp" + str(random.randint(11,9999)).zfill(3) + "@suprema.co.kr"
            print(email_random)

            utils.signUpEmail(self, email_random)

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            st2.click()

            st2 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st2.click()
            st2.send_keys(email_random)

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청")
            st3.click()
            time.sleep(3)

            utils.authCode(self)

            resendBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "재전송")
            resendBtn.click()
            time.sleep(3)

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authBtn.click()
            time.sleep(0.5)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증코드 오류").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다른 코드가 입력 되었네요. \n다시 확인 후 시도해보세요.\na1021").is_displayed()
            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st4.click()
            st4.clear()
            time.sleep(1)

            utils.authCode(self)

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authBtn.click()
            time.sleep(0.5)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"이메일\n{email_random}\n비밀번호\n비밀번호 재입력").is_displayed()

            print("------------- 테스트 시나리오 종료, 회원탈퇴 시도")

            self.driver.quit()

            time.sleep(1)

            options = UiAutomator2Options()
            options.platform_name = 'Android'
            options.device_name = 'R3CXB0MKLGP'
            options.app_package = 'com.suprema.moon'
            options.app_activity = 'com.suprema.moon.MainActivity'
            options.automation_name = 'UiAutomator2'
            options.auto_grant_permissions = True
            options.no_reset = True

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

            time.sleep(1)

            utils.email_login(self, email_random, "Kjstar36!!")

            utils.leaveAdmin(self)

            pass

            print("DQS_T999999_26 이메일로 로그인에서 비밀번호 찾기 인증번호 입력 페이지의 인증번호 재전송 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T999999_26 이메일로 로그인에서 비밀번호 찾기 인증번호 입력 페이지의 인증번호 재전송 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14160(self):
        try:
            print("DQS-T14160 비밀번호 찾기 인증번호 입력 페이지의 인증시간 만료 시 기능 동작 확인")

            phone_Num = "010" + str(random.randint(0, 99999999)).zfill(8)
            print(phone_Num) #랜덤 폰번호로 회원가입 -> 비밀번호 찾기 테스트 시 잦은 시도 팝업 발생으로 신규 가입 후 테스트 시나리오 진행

            utils.signUpMobile(self, phone_Num)

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            st2.click()

            st2 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st2.click()
            st2.send_keys(phone_Num)

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청")
            st3.click()
            time.sleep(0.5)

            utils.authCode_mobile(self)

            print("인증 코드 만료를 위해 5분 대기중.......................")
            time.sleep(302)  # 인증시간 만료를 위해 5분 대기


            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 초기화 오류").is_displayed()
            authError_Pop = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초기화 인증 코드 유효 시간이 만료 되었습니다. \na1022']")
            contentDesc = authError_Pop.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "초기화 인증 코드 유효 시간이 만료 되었습니다. \na1022")

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()

            print("------------- 테스트 시나리오 종료, 회원탈퇴 시도")
            self.driver.quit()

            time.sleep(1)

            options = UiAutomator2Options()
            options.platform_name = 'Android'
            options.device_name = 'R3CXB0MKLGP'
            options.app_package = 'com.suprema.moon'
            options.app_activity = 'com.suprema.moon.MainActivity'
            options.automation_name = 'UiAutomator2'
            options.auto_grant_permissions = True
            options.no_reset = True

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

            time.sleep(1)

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            login_button.click()

            phone_input_box = self.driver.find_element(AppiumBy.XPATH, phoneNumberInputBox)
            phone_input_box.click()
            phone_input_box.send_keys(phone_Num)

            password_input_box = self.driver.find_element(AppiumBy.XPATH, passwordInputBox)
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, login)
            login_button.click()
            time.sleep(2)

            utils.leaveAdmin(self)

            pass

            print("DQS-T14160 비밀번호 찾기 인증번호 입력 페이지의 인증시간 만료 시 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14160 비밀번호 찾기 인증번호 입력 페이지의 인증시간 만료 시 기능 동작 확인  | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14161(self):
        try:
            print("DQS-T14161 회원가입 인증번호 입력 페이지의 인증시간 만료 시 기능 동작 확인")

            signUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            signUp.click()

            agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            agree.click()

            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
            nextBtn.click()
            time.sleep(0.5)

            emailInput = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
            emailInput.click()
            emailInput.send_keys("kjjung+auth1@suprema.co.kr")

            authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            authBtn.click()
            time.sleep(2)

            utils.authCode(self)

            print("인증 코드 만료를 위해 5분 대기중.......................")
            time.sleep(302)  # 인증시간 만료를 위해 5분 대기

            authComBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authComBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증번호 오류").is_displayed()
            authError_Pop = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증 시간이 초과되었습니다.\n다시 시도해 주세요.\na1017']")
            contentDesc = authError_Pop.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "인증 시간이 초과되었습니다.\n다시 시도해 주세요.\na1017")

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()

            pass

            print("DQS-T14161 회원가입 인증번호 입력 페이지의 인증시간 만료 시 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14161 회원가입 인증번호 입력 페이지의 인증시간 만료 시 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13684(self):
        try:
            print("DQS-T13684 비밀번호 찾기 기능 중 가입하지 않은 휴대폰 번호 입력 시 동작 확인")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mobileLogin)
            login_button.click()

            resetPassword = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            resetPassword.click()

            mobile_input = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            mobile_input.click()
            mobile_input.send_keys("01078965412") #회원가입이 안된 전화번호 입력

            authReBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
            authReBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인 정보 오류").is_displayed()
            wrongPhoneNum_Msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000']")
            contentDesc = wrongPhoneNum_Msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000")

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()

            pass

            print("DQS-T13684 비밀번호 찾기 기능 중 가입하지 않은 휴대폰 번호 입력 시 동작 확인| Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T13684 비밀번호 찾기 기능 중 가입하지 않은 휴대폰 번호 입력 시 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_8(self):
        try:
            print("DQS-T999999_8 비밀번호 찾기 기능 중 가입되지 않은 이메일 주소 입력 시 동작 확인")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            login_button.click()

            resetPassword = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            resetPassword.click()

            email_input = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            email_input.click()
            email_input.send_keys("kjjung@suprema.com") # 가입되지 않은 이메일 주소 입력

            authRequestBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청")
            authRequestBtn.click()
            time.sleep(0.5)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인 정보 오류").is_displayed()
            loginMsg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000']")
            contentDesc = loginMsg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인").is_displayed()
            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()

            pass

            print("DQS-T999999 비밀번호 찾기 기능 중 가입되지 않은 이메일 주소 입력 시 동작 확인| Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T999999 비밀번호 찾기 기능 중 가입하지 않은 이메일 주소 입력 시 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_9(self):
        try:
            print("DQS_T999999_9 공간 초대/미초대 된 브랜치 관리자로 이메일 로그인 동작 확인")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            login_button.click()

            emailAdress1 = "kjjung+ba@suprema.co.kr"
            email_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"이메일 주소\n비밀번호\"]/android.widget.EditText[1]")
            email_input_box.click()
            email_input_box.send_keys(emailAdress1)

            password_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"이메일 주소\n비밀번호\"]/android.widget.EditText[2]")
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            login_button.click()
            time.sleep(0.5)

            utils.authCode(self)
            time.sleep(1)

            authComBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authComBtn.click()
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간").is_displayed()

            leadbutton = self.driver.find_element(AppiumBy.XPATH, lead)
            leadbutton.click()

            logout_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, logout)
            logout_button.click()

            logout_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='로그아웃 하시겠습니까?\n자동로그인 기능이 해제 됩니다.']")
            contentDesc = logout_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "로그아웃 하시겠습니까?\n자동로그인 기능이 해제 됩니다.")

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()

            time.sleep(3)

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            login_button.click()

            emailAdress1 = "kjjung+ba222@suprema.co.kr"
            email_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"이메일 주소\n비밀번호\"]/android.widget.EditText[1]")
            email_input_box.click()
            email_input_box.send_keys(emailAdress1)

            password_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"이메일 주소\n비밀번호\"]/android.widget.EditText[2]")
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            login_button.click()
            time.sleep(0.5)

            utils.authCode(self)
            time.sleep(1)

            authComBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authComBtn.click()
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "할당된 공간이 없습니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대된 공간이 없습니다\n관리자에게 연락하여 초대 여부를 확인하세요.").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[1]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대 후에 자동으로 이동합니다.").is_displayed()

            pass
            print("DQS_T999999 공간 초대/미초대 된 브랜치 관리자로 이메일 로그인 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T999999 공간 초대/미초대 된 브랜치 관리자로 이메일 로그인 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_29(self):
        try:
            print("DQS_T999999_29 공간 초대/미초대 된 대리점 관리자로 이메일 로그인 동작 확인")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            login_button.click()

            emailAdress1 = "kjjung+dist1@suprema.co.kr"
            email_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"이메일 주소\n비밀번호\"]/android.widget.EditText[1]")
            email_input_box.click()
            email_input_box.send_keys(emailAdress1)

            password_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"이메일 주소\n비밀번호\"]/android.widget.EditText[2]")
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            login_button.click()
            time.sleep(0.5)

            utils.authCode(self)
            time.sleep(1)

            authComBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authComBtn.click()
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간").is_displayed()

            leadbutton = self.driver.find_element(AppiumBy.XPATH, lead)
            leadbutton.click()

            logout_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, logout)
            logout_button.click()

            logout_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='로그아웃 하시겠습니까?\n자동로그인 기능이 해제 됩니다.']")
            contentDesc = logout_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "로그아웃 하시겠습니까?\n자동로그인 기능이 해제 됩니다.")

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirmBtn.click()

            time.sleep(3)

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, emailLogin)
            login_button.click()

            emailAdress1 = "kjjung+dist2@suprema.co.kr"
            email_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"이메일 주소\n비밀번호\"]/android.widget.EditText[1]")
            email_input_box.click()
            email_input_box.send_keys(emailAdress1)

            password_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"이메일 주소\n비밀번호\"]/android.widget.EditText[2]")
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            login_button.click()
            time.sleep(0.5)

            utils.authCode(self)
            time.sleep(1)

            authComBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
            authComBtn.click()
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "할당된 공간이 없습니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대된 공간이 없습니다\n관리자에게 연락하여 초대 여부를 확인하세요.").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[1]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대 후에 자동으로 이동합니다.").is_displayed()

            pass
            print("DQS_T999999 공간 초대/미초대 된 대리점 관리자로 이메일 로그인 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T999999 공간 초대/미초대 된 대리점 관리자로 이메일 로그인 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T999999_999(self):
        try:
            print("DQS_T999999_999 네트워크 차단된 경우 App 실행 시 예외처리 동작 확인")

            self.driver.press_keycode(4)

            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "종료").is_displayed()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "앱을 정말 종료 하시겠습니까?").is_displayed()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소").is_displayed()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인").is_displayed()

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()

            self.driver.set_network_connection(0)
            time.sleep(0.5)

            clueBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Suprema CLUe")
            clueBtn.click()

            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Network").is_displayed()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Network not found\n\nPlease check your network connection").is_displayed()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "OK").is_displayed()

            okBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "OK")
            okBtn.click()

            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Suprema CLUe").is_displayed()

            self.driver.set_network_connection(2)
            time.sleep(0.5)

            pass
            print("DQS_T999999_999 네트워크 차단된 경우 App 실행 시 예외처리 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T999999_999 네트워크 차단된 경우 App 실행 시 예외처리 동작 확인 | Failed")
            print(str(e))
            self.fail()



if __name__ == '__main__':
    unittest.main()
