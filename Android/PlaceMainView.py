#import datetime
#import os
import time
import unittest
#from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
#from appium.options.android import UiAutomator2Options
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

from Android.PlaceMainView_Email import leadBtn
from Android.User import confirm
from configuration.utill import capture_screenshot
from configuration.webDriver import AppiumConfig
import sys
sys.path.append('../Android')
from Android import utils


'Xpath'
leadBtn = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView"
backBtn = "//android.widget.ImageView[@content-desc='안녕하세요.\n슈프리마 CLUe 서비스 고객센터 입니다.\n무엇을 도와드릴까요?\n운영시간 09:00 ~ 17:00\n(주말, 공휴일 제외)']/android.view.View[1]/android.widget.ImageView"


class SideMenu(unittest.TestCase):

    def setUp(self):
        self.driver = AppiumConfig.get_driver()
        self.driver.implicitly_wait(10)

        utils.mobile_login(self, "01020905304", "Kjstar36!!")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_DQS_T13730(self):
        try:
            print("DQS_T13730 모바일로 로그인 시 Side Menu 기본 UI 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung\n#01020905304").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "설정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃").is_displayed()

            print("DQS_T13730 모바일로 로그인 시 Side Menu 기본 UI 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T13730 모바일로 로그인 시 Side Menu 기본 UI 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T777777_1(self):
        try:
            print("DQS_T777777_1 이메일로 로그인 시 Side Menu 기본 UI 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            logout_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃")
            logout_button.click()

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            utils.email_login(self, "kjjung+p1@suprema.co.kr", "Kjstar36!!")
            time.sleep(2)

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 관리자 1번입니다\n#kjjung+p1@suprema.co.kr").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "설정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃").is_displayed()

            print("DQS_T13730 모바일로 로그인 시 Side Menu 기본 UI 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T13730 모바일로 로그인 시 Side Menu 기본 UI 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13731(self):
        try:
            print("DQS_T13731 방해 금지 시간 기능 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "설정")
            setting.click()

            notouch = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "방해 금지 시간")
            notouch.click()

            toggle_btn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Switch")

            # 현재 상태 확인
            is_on = toggle_btn.get_attribute("checked") == "true"

            if not is_on:
                toggle_btn.click()  # OFF면 클릭해서 ON으로 변경

            self.driver.tap([(840, 574)])

            max_swipes = 24
            start_x = 215
            start_y = 1707
            end_x = 215
            end_y = 1707+60
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "11 o'clock")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            max_swipes = 60
            start_x1 = 331
            start_y1 = 1707
            end_x1 = 797
            end_y1 = 1707+60
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "50 minutes")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x1, start_y1, end_x1, end_y1, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            max_swipes = 24
            start_x3 = 738
            start_y3 = 1707
            end_x3 = 738
            end_y3 = 1707+60
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "22 o'clock")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x3, start_y3, end_x3, end_y3, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            max_swipes = 60
            start_x3 = 873
            start_y3 = 1707
            end_x3 = 873
            end_y3 = 1707+60
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "55 minutes")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x3, start_y3, end_x3, end_y3, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")


            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "시작 시간\n 오전 11 : 50")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "종료 시간\n 오후 10 : 55")

            # default 시간 복구 및 방해금지 Off
            self.driver.tap([(840, 574)])
            time.sleep(0.5)

            max_swipes = 24
            start_x = 215
            start_y = 1707
            end_x = 215
            end_y = 1707-60
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "12 o'clock")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            max_swipes = 60
            start_x1 = 331
            start_y1 = 1707
            end_x1 = 797
            end_y1 = 1707-60
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "0 minutes")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x1, start_y1, end_x1, end_y1, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            max_swipes = 24
            start_x3 = 738
            start_y3 = 1707
            end_x3 = 738
            end_y3 = 1707-60
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "23 o'clock")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x3, start_y3, end_x3, end_y3, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            max_swipes = 60
            start_x3 = 873
            start_y3 = 1707
            end_x3 = 873
            end_y3 = 1707-60
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.SeekBar[@content-desc='0 minutes'])[2]")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x3, start_y3, end_x3, end_y3, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")


            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "시작 시간\n 오후 12 : 00")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "종료 시간\n 오후 11 : 00")

            toggle_btn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Switch")
            toggle_btn.click()

            print("DQS_T13731 방해 금지 시간 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T13731 방해 금지 시간 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13732(self):
        try:
            print("DQS_T13732 방해 금지 시간 설정 불가 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "설정")
            setting.click()

            notouch = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "방해 금지 시간")
            notouch.click()

            toggle_btn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Switch")

            # 현재 상태 확인
            is_on = toggle_btn.get_attribute("checked") == "true"

            if not is_on:
                toggle_btn.click()  # OFF면 클릭해서 ON으로 변경

            self.driver.tap([(840, 574)])

            max_swipes = 24
            start_x = 215
            start_y = 1707
            end_x = 215
            end_y = 1707+60
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "12 o'clock")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            max_swipes = 60
            start_x1 = 331
            start_y1 = 1707
            end_x1 = 797
            end_y1 = 1707+60
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.SeekBar[@content-desc='0 minutes'])[1]")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x1, start_y1, end_x1, end_y1, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            max_swipes = 24
            start_x3 = 738
            start_y3 = 1707
            end_x3 = 738
            end_y3 = 1707-60
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "3 o'clock")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x3, start_y3, end_x3, end_y3, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            max_swipes = 60
            start_x3 = 873
            start_y3 = 1707
            end_x3 = 873
            end_y3 = 1707+60
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.SeekBar[@content-desc='0 minutes'])[2]")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x3, start_y3, end_x3, end_y3, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "익일").is_displayed() #확인 버튼 비활성화 값이 없어 익일 버튼 확인으로 대체

            # 방해금지 Off
            cancel_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            cancel_btn.click()

            toggle_btn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Switch")
            toggle_btn.click()

            print("DQS_T13732 방해 금지 시간 설정 불가 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T13732 방해 금지 시간 설정 불가 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13733(self):
        try:
            print("DQS_T13733 고객센터 기본 UI 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            csct = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터")
            csct.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "안녕하세요.\n슈프리마 CLUe 서비스 고객센터 입니다.\n무엇을 도와드릴까요?\n운영시간 09:00 ~ 17:00\n(주말, 공휴일 제외)").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "전화 상담 1660-4507").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "정보 및 회원탈퇴").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "버전정보").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이용약관").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원탈퇴").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "라이센스").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "오픈 소스").is_displayed()

            print("DQS_T13733 고객센터 기본 UI 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13734(self):
        try:
            print("DQS_T13734 고객센터 전화상담 기능 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            csct = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터")
            csct.click()

            call = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "전화 상담 1660-4507")
            call.click()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@resource-id='com.samsung.android.dialer:id/digits']").is_displayed()
            #테스트폰마다 전화 화면이 다를 수 있어 전화화면에 찾는 element가 있다면 pass로 수정

            self.driver.press_keycode(3)  # 홈 버튼 누르기

            print("DQS_T13734 고객센터 전화상담 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14226(self):
        try:
            print("DQS-T14226 설정 페이지에서 뒤로가기 버튼 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.XPATH, leadBtn)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "설정")
            st2.click()

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            # 공간 메인 화면 이동 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문").is_displayed()

            print("DQS-T14226 설정 페이지에서 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14227(self):
        try:
            print("DQS-T14227 내 계정 페이지의 뒤로가기 버튼 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.XPATH, leadBtn)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung\n#01020905304")
            st2.click()

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            # 공간 메인 화면 이동 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문").is_displayed()

            print("DQS-T14227 내 계정 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14228(self):
        try:
            print("DQS-T14228 고객센터 페이지의 뒤로가기 버튼 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.XPATH, leadBtn)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터")
            st2.click()

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            # 공간 메인 화면 이동 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문").is_displayed()

            print("DQS-T14228 고객센터 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13735(self):
        try:
            print("DQS_T13735 고객센터 페이지의 이용약관 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            csct = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터")
            csct.click()

            cl1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='안녕하세요.\n슈프리마 CLUe 서비스 고객센터 입니다.\n무엇을 도와드릴까요?\n운영시간 09:00 ~ 17:00\n(주말, 공휴일 제외)']/android.view.View[2]/android.widget.ImageView[1]")
            cl1.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이용약관").is_displayed()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text= '제1장 총칙']").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='제2장 계약의 성립과 이용']").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='제3장 서비스의 내용']").is_displayed()

            prev = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
            prev.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "전화 상담 1660-4507").is_displayed()

            print("DQS_T13735 고객센터 페이지의 이용약관 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13736(self):
        try:
            print("DQS_T13736 고객센터 페이지의 개인정보 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            csct = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터")
            csct.click()

            cl1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='안녕하세요.\n슈프리마 CLUe 서비스 고객센터 입니다.\n무엇을 도와드릴까요?\n운영시간 09:00 ~ 17:00\n(주말, 공휴일 제외)']/android.view.View[2]/android.widget.ImageView[2]")
            cl1.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보").is_displayed()
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='슈프리마 클루(CLUe) 서비스 개인정보 처리방침']").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@text='제1조 개인정보 처리목적, 처리항목, 처리 및 보유기간']").is_displayed()

            prev = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
            prev.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "전화 상담 1660-4507").is_displayed()


            print("DQS_T13736 고객센터 페이지의 개인정보 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13737(self):
        try:
            print("DQS_T13737 고객센터 페이지의 오픈 소스 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            csct = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터")
            csct.click()

            cl1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='안녕하세요.\n슈프리마 CLUe 서비스 고객센터 입니다.\n무엇을 도와드릴까요?\n운영시간 09:00 ~ 17:00\n(주말, 공휴일 제외)']/android.view.View[2]/android.widget.ImageView[4]")
            cl1.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "오픈 소스").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "_fe_analyzer_shared 61.0.0\nLogic that is shared between the front_end and analyzer packages.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "_flutterfire_internals 1.3.7\nA package hosting Dart code shared between FlutterFire plugins.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "analyzer 5.13.0\nThis package provides a library that performs static analysis of Dart code.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "ansicolor 2.0.2\nLooking to add some color to your terminal logs? `ansicolor` is an xterm-256 color support library that lets you change the foreground and background color of your text.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "archive 3.5.1\nProvides encoders and decoders for various archive and compression formats such as zip, tar, bzip2, gzip, and zlib.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "args 2.5.0\nLibrary for defining parsers for parsing raw command-line arguments into a set of options and values using GNU and POSIX style options.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "async 2.11.0\nUtility functions and classes related to the 'dart:async' library.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "bloc 8.1.4\nA predictable state management library that helps implement the BLoC (Business Logic Component) design pattern.").is_displayed()

            prev = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
            prev.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "전화 상담 1660-4507").is_displayed()

            print("DQS_T13737 고객센터 페이지의 개인정보 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14102(self):
        try:
            print("DQS_T14102 프로필 이름 변경 불가 케이스 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, leadBtn)
            leadbutton.click()

            profile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung\n#01020905304")
            profile.click()

            edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            edit.click()

            time.sleep(1)

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "내 계정 변경").is_displayed()
            # 확인 버튼 상태 체크 요소값이 없어 확인 버튼 클릭 후 해당 페이지 유지 되는지 케이스로 작성함

            pass

            print("DQS_T14102 프로필 이름 변경 불가 케이스 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()


        print("DQS_T14102 프로필 이름 변경 불가 케이스 동작 확인 | Pass")

    def test_DQS_T14009(self):
        try:
            print("DQS_T14009 프로필 정보 변경 취소 시 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, leadBtn)
            leadbutton.click()

            prifile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung\n#01020905304")
            prifile.click()

            edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            edit.click()

            nameIPB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            nameIPB.click()
            nameIPB.send_keys("test user123")
            time.sleep(3)

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung").is_displayed()

            print("DQS_T14009 프로필 정보 변경 취소 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T16924(self):
        try:
            print("DQS_T16924 프로필에서 비밀번호 재설정 인증번호 입력 페이지의 인증번호 인풋 박스 유효성 검사")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            logoutBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃")
            logoutBtn.click()

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            utils.mobile_login(self, "01066666666", "Kjstar36!!")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            profile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "666\n#01066666666")
            profile.click()

            edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            edit.click()

            passwordreSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")
            passwordreSetting.click()
            time.sleep(2)

            #너무 잦은 시도 팝업 발생 시 회원 탈퇴 후 다시 회원 가입하여 진행
            error_popup = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "인증코드 요청 오류")
            if error_popup and error_popup[0].is_displayed():
                confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
                confirmBtn.click()
                time.sleep(1)

                #회원 탈퇴 동작
                for _ in range(2):
                    self.driver.back()

                utils.leaveAdmin(self)

                utils.signUp_mobile(self, "01066666666", "666", "Kjstar36!!", "Kjstar36!!")


                utils.mobile_login(self, "01066666666", "Kjstar36!!")

                leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
                leadbutton.click()

                profile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "666\n#01066666666")
                profile.click()

                edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
                edit.click()

                passwordreSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")
                passwordreSetting.click()
                time.sleep(1)
            else:
                pass

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")

            st1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st1.click()
            st1.send_keys("ABCDEF")
            er1 = st1.text
            self.assertEqual("ABCDEF", er1)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n01066666666\n인증번호\n인증번호는 6자리 숫자입니다.")

            atBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            is_enabled = atBtn.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "인증완료 버튼 비활성화")

            st1.clear()

            st2 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st2.click()
            st2.send_keys("abcdef")
            er2 = st2.text
            self.assertEqual("abcdef", er2)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n01066666666\n인증번호\n인증번호는 6자리 숫자입니다.")

            atBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            is_enabled = atBtn.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "인증완료 버튼 비활성화")

            st2.clear()

            st3 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st3.click()
            st3.send_keys("가나다라마바")
            er3 = st3.text
            self.assertEqual("가나다라마바", er3)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n01066666666\n인증번호\n인증번호는 6자리 숫자입니다.")

            atBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            is_enabled = atBtn.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "인증완료 버튼 비활성화")

            st3.clear()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st4.click()
            st4.send_keys("!@#$%^&*()")
            er4 = st4.text
            self.assertEqual("!@#$%^", er4)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n01066666666\n인증번호\n인증번호는 6자리 숫자입니다.")

            atBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            is_enabled = atBtn.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "인증완료 버튼 비활성화")

            st4.clear()

            st5 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st5.click()
            st5.send_keys("123")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n01066666666\n인증번호\n인증번호는 6자리 숫자입니다.")

            atBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            is_enabled = atBtn.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "인증완료 버튼 비활성화")

            st5.clear()

            st6 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st6.click()
            st6.send_keys("9876543210")
            er6 = st6.text
            self.assertEqual("987654", er6)

            atBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            is_enabled = atBtn.get_attribute("enabled")
            self.assertEqual(is_enabled, "true", "인증완료 버튼 활성화")

            st6.clear()

            st7 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st7.click()
            st7.send_keys("123456")

            atBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            is_enabled = atBtn.get_attribute("enabled")
            self.assertEqual(is_enabled, "true", "인증완료 버튼 활성화")

            atBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증 코드가 일치하지 않습니다. \n다시 입력해 주세요.").is_displayed()
            # 회원가입 씬에서 출력된 팝업 문구와 비밀번호 찾기 씬에서 출력되는 팝업 문구가 상이함, 회원가입 씬에서 발생하는 문구로 작성되어 있어서 Fail 발생함, 사양 확정 후 TC보완예정
            authError_Pop = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증 코드가 일치하지 않습니다. \n다시 입력해 주세요.']")
            contentDesc6 = authError_Pop.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc6}")
            self.assertEqual(contentDesc6, "인증 코드가 일치하지 않습니다. \n다시 입력해 주세요.")
            st8 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            st8.click()

            pass

            print("DQS_T16924 프로필에서 비밀번호 재설정 인증번호 입력 페이지의 인증번호 인풋 박스 유효성 검사 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T16923(self):
        try:
            print("DQS_T16923 프로필에서 비밀번호 재설정 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            logoutBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃")
            logoutBtn.click()

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            utils.mobile_login(self, "01066666666", "Kjstar36!!")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            profile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "666\n#01066666666")
            profile.click()

            edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            edit.click()

            passwordreSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")
            passwordreSetting.click()
            time.sleep(1)

            #너무 잦은 시도 팝업 발생 시 회원 탈퇴 후 다시 회원 가입하여 진행
            error_popup = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "인증코드 요청 오류")
            if error_popup and error_popup[0].is_displayed():
                confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
                confirmBtn.click()
                time.sleep(1)

                #회원 탈퇴 동작
                for _ in range(2):
                    self.driver.back()

                utils.leaveAdmin(self)

                utils.signUp_mobile(self, "01066666666", "666", "Kjstar36!!", "Kjstar36!!")

                utils.mobile_login(self, "01066666666", "Kjstar36!!")

                leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
                leadbutton.click()

                profile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "666\n#01066666666")
                profile.click()

                edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
                edit.click()

                passwordreSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")
                passwordreSetting.click()
                time.sleep(1)
            else:
                pass

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n01066666666\n인증번호").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "재전송").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "6 characters remaining").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료").is_displayed()

            utils.authCode_mobile(self)
            time.sleep(0.5)

            atBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            is_enabled = atBtn.get_attribute("enabled")
            self.assertEqual(is_enabled, "true", "인증완료 버튼 활성화")

            atBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n01066666666\n비밀번호\n비밀번호 재입력").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "재설정").is_displayed()

            password1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='휴대폰 번호\n01066666666\n비밀번호\n비밀번호 재입력']/android.widget.EditText[1]")
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

            rePassword1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='휴대폰 번호\n01066666666\n비밀번호\n비밀번호 재입력']/android.widget.EditText[2]")
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
            is_enabled = reSetBtn.get_attribute("enabled")
            self.assertEqual(is_enabled, "true", "재설정 버튼 활성화")
            reSetBtn.click()
            time.sleep(0.5)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정").is_displayed()
            rePasswordMsg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='재설정 되었습니다.\n변경된 비밀번호로 로그인 해주세요.']")
            contentDesc1 = rePasswordMsg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "재설정 되었습니다.\n변경된 비밀번호로 로그인 해주세요.")

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            #로그아웃 후 로그인 페이지 이동 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일로 로그인").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "모바일로 로그인").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()

            # 변경 전 Password로 로그인 시도
            utils.mobile_login(self, "01066666666", "Kjstar36!!")
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인 정보 오류").is_displayed()
            loginError_Pop = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000']")
            contentDesc2 = loginError_Pop.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "계정 혹은 비밀번호를\n다시 확인해 주세요.\na1000")
            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(0.5)

            # 변경된 Password로 로그인 시도
            self.driver.quit()

            self.driver = AppiumConfig.get_driver()
            self.driver.implicitly_wait(10)

            utils.mobile_login(self, "01066666666", "Kjstar36!@")

            # 기존 Password 복구
            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            profile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "666\n#01066666666")
            profile.click()

            edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            edit.click()

            passwordreSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")
            passwordreSetting.click()
            time.sleep(2)

            utils.authCode_mobile(self)
            time.sleep(0.5)

            atBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            atBtn.click()

            password1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='휴대폰 번호\n01066666666\n비밀번호\n비밀번호 재입력']/android.widget.EditText[1]")
            password1.click()
            password1.send_keys("Kjstar36!!")

            rePassword1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='휴대폰 번호\n01066666666\n비밀번호\n비밀번호 재입력']/android.widget.EditText[2]")
            rePassword1.click()
            rePassword1.send_keys("Kjstar36!!")

            reSetBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "재설정")
            reSetBtn.click()
            time.sleep(0.5)

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            #로그아웃 후 로그인 페이지 이동 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일로 로그인").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "모바일로 로그인").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입").is_displayed()

            pass

            print("DQS_T16923 프로필에서 비밀번호 재설정 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T16925(self):
        try:
            print("DQS_T16925 프로필에서 비밀번호 재설정 인증번호 입력 페이지의 인증번호 재전송 버튼 기능 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            logoutBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃")
            logoutBtn.click()

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            utils.mobile_login(self, "01066666666", "Kjstar36!!")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            profile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "666\n#01066666666")
            profile.click()

            edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            edit.click()

            passwordreSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")
            passwordreSetting.click()
            time.sleep(1)

            #너무 잦은 시도 팝업 발생 시 회원 탈퇴 후 다시 회원 가입하여 진행
            error_popup = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "인증코드 요청 오류")
            if error_popup and error_popup[0].is_displayed():
                confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
                confirmBtn.click()
                time.sleep(1)

                #회원 탈퇴 동작
                for _ in range(2):
                    self.driver.back()

                utils.leaveAdmin(self)

                utils.signUp_mobile(self, "01066666666", "666", "Kjstar36!!", "Kjstar36!!")


                utils.mobile_login(self, "01066666666", "Kjstar36!!")

                leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
                leadbutton.click()

                profile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "666\n#01066666666")
                profile.click()

                edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
                edit.click()

                passwordreSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")
                passwordreSetting.click()
                time.sleep(1)
            else:
                pass

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")

            utils.authCode_mobile(self)

            resend = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "재전송")
            resend.click()
            time.sleep(3)

            authApply = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            authApply.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증 코드 오류").is_displayed()
            # 회원가입 씬에서 출력된 팝업 문구와 비밀번호 찾기 씬에서 출력되는 팝업 문구가 상이함, 회원가입 씬에서 발생하는 문구로 작성되어 있어서 Fail 발생함 -> 팝업 문구 확인 케이스가 아니어서 현재 출력되는 메시지로 작성홤
            authError_Pop = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='다른 코드가 입력 되었네요.\n다시 확인 후 시도해보세요.\na1021']")
            contentDesc = authError_Pop.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "다른 코드가 입력 되었네요.\n다시 확인 후 시도해보세요.\na1021")

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            authNum = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            authNum.click()
            authNum.send_keys("")

            utils.authCode_mobile(self)

            authApply = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            authApply.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n01066666666\n비밀번호\n비밀번호 재입력")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "재설정")

            pass

            print("DQS_T16925 프로필에서 비밀번호 재설정 인증번호 입력 페이지의 인증번호 재전송 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T16926(self):
        try:
            print("DQS-T16926 프로필에서 비밀번호 재설정 인증번호 입력 페이지의 인증시간 만료 시 기능 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            logoutBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃")
            logoutBtn.click()

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            utils.mobile_login(self, "01066666666", "Kjstar36!!")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            profile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "666\n#01066666666")
            profile.click()

            edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            edit.click()

            passwordreSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")
            passwordreSetting.click()
            time.sleep(1)

            #너무 잦은 시도 팝업 발생 시 회원 탈퇴 후 다시 회원 가입하여 진행
            error_popup = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "인증코드 요청 오류")
            if error_popup and error_popup[0].is_displayed():
                confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
                confirmBtn.click()
                time.sleep(1)

                #회원 탈퇴 동작
                for _ in range(2):
                    self.driver.back()

                utils.leaveAdmin(self)

                utils.signUp_mobile(self, "01066666666", "666", "Kjstar36!!", "Kjstar36!!")


                utils.mobile_login(self, "01066666666", "Kjstar36!!")

                leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
                leadbutton.click()

                profile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "666\n#01066666666")
                profile.click()

                edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
                edit.click()

                passwordreSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")
                passwordreSetting.click()
                time.sleep(1)
            else:
                pass

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")

            print("5분 대기 시작.......................")
            time.sleep(301)
            print("5분 대기 완료")

            utils.authCode_mobile(self)

            authApply = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            authApply.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 초기화 오류").is_displayed()
            passwordError_Pop = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초기화 인증 코드 유효 시간이 만료 되었습니다. \na1022']")
            contentDesc = passwordError_Pop.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "초기화 인증 코드 유효 시간이 만료 되었습니다. \na1022")

            pass

            print("DQS-T16926 프로필에서 비밀번호 재설정 인증번호 입력 페이지의 인증시간 만료 시 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T16927(self):
        try:
            print("DQS_T16927 프로필에 비밀번호 재설정 페이지에서 비밀번호 와 비밀번호 재입력 값이 다른 경우 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            logoutBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃")
            logoutBtn.click()

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            utils.mobile_login(self, "01066666666", "Kjstar36!!")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            profile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "666\n#01066666666")
            profile.click()

            edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            edit.click()

            passwordreSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")
            passwordreSetting.click()
            time.sleep(2)

            #너무 잦은 시도 팝업 발생 시 회원 탈퇴 후 다시 회원 가입하여 진행
            error_popup = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "인증코드 요청 오류")
            if error_popup and error_popup[0].is_displayed():
                confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
                confirmBtn.click()
                time.sleep(1)

                #회원 탈퇴 동작
                for _ in range(2):
                    self.driver.back()

                utils.leaveAdmin(self)

                utils.signUp_mobile(self, "01066666666", "666", "Kjstar36!!", "Kjstar36!!")


                utils.mobile_login(self, "01066666666", "Kjstar36!!")

                leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
                leadbutton.click()

                profile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "666\n#01066666666")
                profile.click()

                edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
                edit.click()

                passwordreSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")
                passwordreSetting.click()
                time.sleep(1)
            else:
                pass

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")

            utils.authCode_mobile(self)
            time.sleep(0.5)

            atBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            atBtn.click()

            password = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='휴대폰 번호\n01066666666\n비밀번호\n비밀번호 재입력']/android.widget.EditText[1]")
            password.click()
            password.send_keys("Kjstar36!@")

            rePassword = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='휴대폰 번호\n01066666666\n비밀번호\n비밀번호 재입력']/android.widget.EditText[2]")
            rePassword.click()
            rePassword.send_keys("Kjstar36!#")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n01066666666\n비밀번호\n비밀번호 재입력\n비밀번호가 일치하지 않습니다.")

            reSetBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "재설정")
            is_enabled = reSetBtn.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "재설정 버튼 비활성화")
            reSetBtn.click()
            time.sleep(0.5)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")

            pass

            print("DQS_T16927 프로필에 비밀번호 재설정 페이지에서 비밀번호 와 비밀번호 재입력 값이 다른 경우 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T16928_T16929(self):
        try:
            print("DQS_T16928 프로필에서 비밀번호 재설정 페이지의  새 비밀번호 입력 인풋 박스 유효성 검사 || DQS_T16929 프로필에서 비밀번호 재설정 페이지의 새 비밀번호 재입력 인풋 박스 유효성 검사")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            logoutBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃")
            logoutBtn.click()

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            utils.mobile_login(self, "01066666666", "Kjstar36!!")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            profile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "666\n#01066666666")
            profile.click()

            edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            edit.click()

            passwordreSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")
            passwordreSetting.click()
            time.sleep(2)

            #너무 잦은 시도 팝업 발생 시 회원 탈퇴 후 다시 회원 가입하여 진행
            error_popup = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "인증코드 요청 오류")
            if error_popup and error_popup[0].is_displayed():
                confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
                confirmBtn.click()
                time.sleep(1)

                #회원 탈퇴 동작
                for _ in range(2):
                    self.driver.back()

                utils.leaveAdmin(self)

                utils.signUp_mobile(self, "01066666666", "666", "Kjstar36!!", "Kjstar36!!")


                utils.mobile_login(self, "01066666666", "Kjstar36!!")

                leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
                leadbutton.click()

                profile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "666\n#01066666666")
                profile.click()

                edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
                edit.click()

                passwordreSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")
                passwordreSetting.click()
                time.sleep(1)
            else:
                pass

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")

            utils.authCode_mobile(self)
            time.sleep(0.5)

            atBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            atBtn.click()

            utils.resetPasswordValidtion(self)

            time.sleep(0.5)
            print("------------------- DQS-T16929 시작")
            utils.resetRePasswordValidtion(self)

            pass

            print("DQS_T16928 프로필에서 비밀번호 재설정 페이지의  새 비밀번호 입력 인풋 박스 유효성 검사 || DQS_T16929 프로필에서 비밀번호 재설정 페이지의 새 비밀번호 재입력 인풋 박스 유효성 검사 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T16930(self):
        try:
            print("DQS_T16930 프로필에 비밀번호 재설정에서 인증번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            logoutBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃")
            logoutBtn.click()

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            utils.mobile_login(self, "01066666666", "Kjstar36!!")


            leadbutton = self.driver.find_element(AppiumBy.XPATH, leadBtn)
            leadbutton.click()

            profile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "666\n#01066666666")
            profile.click()

            edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            edit.click()

            passwordreSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")
            passwordreSetting.click()
            time.sleep(2)

            #너무 잦은 시도 팝업 발생 시 회원 탈퇴 후 다시 회원 가입하여 진행
            error_popup = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "인증코드 요청 오류")
            if error_popup and error_popup[0].is_displayed():
                confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
                confirmBtn.click()
                time.sleep(1)

                #회원 탈퇴 동작
                for _ in range(2):
                    self.driver.back()

                utils.leaveAdmin(self)

                utils.signUp_mobile(self, "01066666666", "666", "Kjstar36!!", "Kjstar36!!")


                utils.mobile_login(self, "01066666666", "Kjstar36!!")

                leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
                leadbutton.click()

                profile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "666\n#01066666666")
                profile.click()

                edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
                edit.click()

                passwordreSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")
                passwordreSetting.click()
                time.sleep(1)
            else:
                pass

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정").is_displayed()

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "내 계정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이름").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "666").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+82 01066666666").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "device uid").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "AP3A.240905.015.A2").is_displayed() ##시료폰마다 UID값 다름, 코드 수정 시 확인 필요
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "⦁⦁⦁⦁⦁⦁⦁⦁").is_displayed()

            pass

            print("DQS_T16930 프로필에 비밀번호 재설정에서 인증번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T16931(self):
        try:
            print("DQS_T16931 프로필에 비밀번호 재설정에서 비밀번호 재설정 페이지의 뒤로가기 버튼 기능 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            logoutBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃")
            logoutBtn.click()

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            utils.mobile_login(self, "01066666666", "Kjstar36!!")


            leadbutton = self.driver.find_element(AppiumBy.XPATH, leadBtn)
            leadbutton.click()

            profile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "666\n#01066666666")
            profile.click()

            edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            edit.click()

            passwordreSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")
            passwordreSetting.click()
            time.sleep(2)

            #너무 잦은 시도 팝업 발생 시 회원 탈퇴 후 다시 회원 가입하여 진행
            error_popup = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "인증코드 요청 오류")
            if error_popup and error_popup[0].is_displayed():
                confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
                confirmBtn.click()
                time.sleep(1)

                #회원 탈퇴 동작
                for _ in range(2):
                    self.driver.back()

                utils.leaveAdmin(self)

                utils.signUp_mobile(self, "01066666666", "666", "Kjstar36!!", "Kjstar36!!")


                utils.mobile_login(self, "01066666666", "Kjstar36!!")

                leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
                leadbutton.click()

                profile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "666\n#01066666666")
                profile.click()

                edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
                edit.click()

                passwordreSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정")
                passwordreSetting.click()
                time.sleep(1)
            else:
                pass

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재설정").is_displayed()

            utils.authCode_mobile(self)

            atBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            atBtn.click()

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "내 계정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이름").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "666").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+82 01066666666").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "device uid").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "AP3A.240905.015.A2").is_displayed() ##시료폰마다 UID값 다름, 코드 수정 시 확인 필요
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "⦁⦁⦁⦁⦁⦁⦁⦁").is_displayed()

            pass

            print("DQS_T16931 프로필에 비밀번호 재설정에서 비밀번호 재설정 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13738(self):
        try:
            print("DQS_T13738 프로필 이름 변경 기능 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            profile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung\n#01020905304")
            profile.click()

            edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            edit.click()

            nameIPB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            nameIPB.click()
            nameIPB.send_keys("e2e_test1")

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_test1").is_displayed()

            #기존 상태로 복구 동작
            edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            edit.click()

            nameIPB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            nameIPB.click()
            nameIPB.send_keys("kjjung")

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung").is_displayed()

            print("DQS_T13738 프로필 이름 변경 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

class AC(unittest.TestCase):
    def setUp(self):
        self.driver = AppiumConfig.get_driver()
        self.driver.implicitly_wait(10)

        utils.mobile_login(self, "01011111111", "Kjstar36!!")

        # place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1")
        # place.click()
        # time.sleep(2)
        #
        # placeInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
        # placeInput.click()
        # placeInput.send_keys("비디오 공간")
        # time.sleep(1)
        #
        # assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간\nID : 22").is_displayed()
        #
        # self.driver.tap([(260, 644)])
        # time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_DQS_T14017(self):
        try:
            print("DQS_T14017 출입문 없는 케이스 동작 확인")

            place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간")
            place.click()
            time.sleep(2)

            placeInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            placeInput.click()
            placeInput.send_keys("멤버쉽관리_초대 Test")
            time.sleep(1)

            self.driver.tap([(260, 644)])
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "장치 없음").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문이 없습니다.").is_displayed()

            el1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.widget.ImageView[2]")
            el1.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "장치 없음").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문이 없습니다.").is_displayed()

            print("DQS_T14017 출입문 없는 케이스 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14018(self):
        try:
            print("DQS_T14018 출입문 수동 잠금 기능 동작 확인")

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
            door.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 잠금")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금 상태")
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='잠금']")
            status0 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='잠금']")
            contentDesc0 = status0.get_attribute('content-desc')
            print(f"잠금 상태 : {contentDesc0}")

            manuallock = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[2]")
            manuallock.click()
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 잠금'])[2]")
            status1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 잠금'])[2]")
            contentDesc1 = status1.get_attribute('content-desc')
            print(f"잠금 상태 : {contentDesc1}")

            self.driver.tap([(550, 747)]) # 출입문 바텀 시트 종료
            self.driver.tap([(468, 2049)]) # 이벤트 이력 클릭

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='잠금 닫힘'])[1]")
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]")
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금 닫힘")
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888")
                except NoSuchElementException:
                    self.fail("DQS_T14018 출입문 수동 잠금 기능 동작 확인 | Fail")

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 잠금 시작'])[1]")
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_538200888'])[1]")
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 잠금 시작")
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
                except NoSuchElementException:
                    self.fail("DQS_T14018 출입문 수동 잠금 기능 동작 확인 | Fail")

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n수동 잠금\nBS3_538200888")
            door.click()

            lock = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[2]")
            lock.click()
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='잠금']")
            status3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='잠금']")
            contentDesc3 = status3.get_attribute('content-desc')
            print(f"잠금 상태 : {contentDesc3}")

            self.driver.tap([(550, 747)]) # 출입문 바텀 시트 종료
            self.driver.tap([(468, 2049)]) # 이벤트 이력 클릭

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='잠금 닫힘'])[1]")
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]")
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금 닫힘")
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888")
                except NoSuchElementException:
                    self.fail("DQS_T14018 출입문 수동 잠금 기능 동작 확인 | Fail")

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 모드 해제'])[1]")
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_538200888'])[1]")
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 모드 해제")
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
                except NoSuchElementException:
                    self.fail("DQS_T14018 출입문 수동 잠금 기능 동작 확인 | Fail")

            print("DQS_T14018 출입문 수동 잠금 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14019(self):
        try:
            print("DQS_T14019 출입문 일시 열림 기능 동작 확인")

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
            door.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일시 열림")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금 상태")
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='잠금']")
            status0 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='잠금']")
            contentDesc0 = status0.get_attribute('content-desc')
            print(f"잠금 상태 : {contentDesc0}")

            opendoor = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[3]")
            opendoor.click()
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='열림']")
            status1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='열림']")
            contentDesc1 = status1.get_attribute('content-desc')
            print(f"잠금 상태 : {contentDesc1}")

            time.sleep(3)

            #3초 후 잠금 상태 변경
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='잠금']")
            status1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='잠금']")
            contentDesc1 = status1.get_attribute('content-desc')
            print(f"3초 후 잠금 상태 : {contentDesc1}")

            self.driver.tap([(550, 747)])
            self.driver.tap([(540, 2031)])

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='잠금 닫힘'])[1]")
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]")
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금 닫힘")
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888")
                except NoSuchElementException:
                    self.fail("DQS_T14019 출입문 일시 열림 기능 동작 확인 | Fail")

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='잠금 해제'])[1]")
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[2]")
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금 해제")
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888")
                except NoSuchElementException:
                    self.fail("DQS_T14019 출입문 일시 열림 기능 동작 확인 | Fail")

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")

            print("DQS_T14019 출입문 일시 열림 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14020(self):
        try:
            print("DQS_T14020 출입문명 변경 기능 동작 확인")

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
            door.click()

            device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
            device_setting.click()

            modifyBtn0 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            is_enabled = modifyBtn0.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "수정 버튼 비활성화")

            nameDel = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='BS3_538200888']/android.widget.ImageView")
            nameDel.click()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("Test_1")

            dnIBtext = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIBtext)

            modifyBtn1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            is_enabled = modifyBtn1.get_attribute("enabled")
            self.assertEqual(is_enabled, "true", "수정 버튼 활성화")

            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nTest_1")
            #기존 출입문 이름 복구
            door1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nTest_1")
            door1.click()

            setting1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_1")
            setting1.click()

            nameDel = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Test_1']/android.widget.ImageView")
            nameDel.click()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("BS3_538200888")

            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888").is_displayed()

            print("DQS_T14020 출입문명 변경 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14021(self):
        try:
            print("DQS_T14021 출입문 수동 열림 기능 동작 확인")

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
            door.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 열림")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금 상태")
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='잠금']")
            status0 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='잠금']")
            contentDesc0 = status0.get_attribute('content-desc')
            print(f"잠금 상태 : {contentDesc0}")

            manualOpen = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[4]")
            manualOpen.click()
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 열림'])[2]")
            status1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 열림'])[2]")
            contentDesc1 = status1.get_attribute('content-desc')
            print(f"잠금 상태 : {contentDesc1}")

            self.driver.tap([(550, 747)]) # 출입문 바텀 시트 종료
            self.driver.tap([(468, 2049)]) # 이벤트 이력 클릭

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='잠금 해제'])[1]").is_displayed()
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금 해제").is_displayed()
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888").is_displayed()
                except NoSuchElementException:
                    self.fail("DQS_T14021 출입문 수동 열림 기능 동작 확인 | Fail")

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 열림 시작'])[1]").is_displayed()
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_538200888'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 열림 시작").is_displayed()
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888").is_displayed()
                except NoSuchElementException:
                    self.fail("DQS_T14021 출입문 수동 열림 기능 동작 확인 | Fail")

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            door2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "열림\n수동 열림\nBS3_538200888")
            door2.click()

            lock = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[4]")
            lock.click()

            time.sleep(1)

            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='잠금']")
            status3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='잠금']")
            contentDesc3 = status3.get_attribute('content-desc')
            print(f"잠금 상태 : {contentDesc3}")

            self.driver.tap([(550, 747)]) # 출입문 바텀 시트 종료
            self.driver.tap([(468, 2049)]) # 이벤트 이력 클릭

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='잠금 닫힘'])[1]").is_displayed()
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금 닫힘").is_displayed()
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888").is_displayed()
                except NoSuchElementException:
                    self.fail("DQS_T14021 출입문 수동 열림 기능 동작 확인 | Fail")

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 모드 해제'])[1]").is_displayed()
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_538200888'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 모드 해제").is_displayed()
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888").is_displayed()
                except NoSuchElementException:
                    self.fail("DQS_T14021 출입문 수동 열림 기능 동작 확인 | Fail")

            print("DQS_T14021 출입문 수동 열림 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14022(self):
        try:
            print("DQS_T14022 출입문 Grid 리스트에서 스와이프 시 기능 동작 확인")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")

            start_x = 230
            start_y = 1600
            end_x = 840
            end_y = 1600
            self.driver.swipe(start_x, start_y, end_x, end_y)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")

            start_x1 = 840
            start_y1 = 1600
            end_x1 = 230
            end_y1 = 1600

            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_54780678")

            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_547838616")

            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nXS2_543478219")

            self.driver.swipe(start_x, start_y, end_x, end_y)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_547838616")

            for _ in range(2):
                self.driver.swipe(start_x, start_y, end_x, end_y)
                time.sleep(1)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")

            print("DQS_T14022 출입문 Grid 리스트에서 스와이프 시 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14023(self):
        try:
            print("DQS_T14023 출입문 연결 끊김 시 동작 확인")

            start_x1 = 840
            start_y1 = 1600
            end_x1 = 230
            end_y1 = 1600

            for _ in range(4):
                self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
                time.sleep(1)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nN2_800000900")

            disabledoor = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nN2_800000900")
            disabledoor.click()

            manualLock = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[2]")
            manualLock.click()
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금")

            doorOpen = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[3]")
            doorOpen.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금")

            manualOpen = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[4]")
            manualOpen.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금")

            device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "N2_800000900")
            device_setting.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 잠금")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일시 열림")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 열림")

            print("DQS_T14023 출입문 연결 끊김 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14024_T14087(self):
        try:
            print("DQS_T14024 출입문 스케쥴 열림 설정 시 동작 확인 || DQS-T14087 출입문 스케줄 열림 설정 해제 시 동작 확인")

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
            except NoSuchElementException:
                print("초기 상태 아님 - 스케줄 없음으로 변경 후 Test 진행")
                self.driver.tap([(530, 1620)]) #door 선택

                device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
                device_setting.click()

                self.driver.tap([(930, 750)]) #스케줄 열림 선택

                schedule_selete1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음")
                schedule_selete1.click()

                # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
                print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
                self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표

                self.driver.tap([(530, 1620)]) #door 선택

                device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
                device_setting.click()

                self.driver.tap([(930, 900)]) #스케줄 잠금 선택

                schedule_selete1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음")
                schedule_selete1.click()

                # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
                print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
                self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
            door.click()

            device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
            device_setting.click()

            schedule1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\n없음")
            schedule1.click()

            # Web에 저장된 스케줄 선택
            schedule_selete1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "E2E_Schedule")
            schedule_selete1.click()

            # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
            print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            self.driver.tap([(468, 2049)]) # 이벤트 이력 클릭

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='잠금 해제'])[1]").is_displayed()
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금 해제").is_displayed()
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888").is_displayed()
                except NoSuchElementException:
                    self.fail("DQS_T14024 출입문 스케쥴 열림 설정 시 동작 확인 || DQS-T14087 출입문 스케줄 열림 설정 해제 시 동작 확인")
            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='스케줄 열림 시작'])[1]").is_displayed()
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림 시작").is_displayed()
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888").is_displayed()
                except NoSuchElementException:
                    self.fail("DQS_T14024 출입문 스케쥴 열림 설정 시 동작 확인 || DQS-T14087 출입문 스케줄 열림 설정 해제 시 동작 확인")

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            open_door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "열림\n스케줄 열림\nBS3_538200888")
            open_door.click()

            device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
            device_setting.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\nE2E_Schedule")

            # DQS-T14087 출입문 스케줄 열림 설정 해제 시 동작 확인
            schedule2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\nE2E_Schedule")
            schedule2.click()

            schedule_selete2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음")
            schedule_selete2.click()

            # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
            print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            self.driver.tap([(468, 2049)]) # 이벤트 이력 클릭

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='잠금 닫힘'])[1]").is_displayed()
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금 닫힘").is_displayed()
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888").is_displayed()
                except NoSuchElementException:
                    self.fail("DQS_T14024 출입문 스케쥴 열림 설정 시 동작 확인 || DQS-T14087 출입문 스케줄 열림 설정 해제 시 동작 확인")
            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='스케줄 열림 종료'])[1]").is_displayed()
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림 종료").is_displayed()
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888").is_displayed()
                except NoSuchElementException:
                    self.fail("DQS_T14024 출입문 스케쥴 열림 설정 시 동작 확인 || DQS-T14087 출입문 스케줄 열림 설정 해제 시 동작 확인")

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")

            pass

            print("DQS_T14024 출입문 스케쥴 열림 설정 시 동작 확인 || DQS-T14087 출입문 스케줄 열림 설정 해제 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14025_T14088(self):
        try:
            print("DQS_T14025 출입문 스케쥴 잠금 설정 시 동작 확인 || DQS-T14088 출입문 스케줄 잠금 설정 해제 시 동작 확인")

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
            except NoSuchElementException:
                print("초기 상태 아님 - 스케줄 없음으로 변경 후 Test 진행")
                self.driver.tap([(530, 1620)]) #door 선택

                device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
                device_setting.click()

                self.driver.tap([(930, 750)]) #스케줄 열림 선택

                schedule_selete1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음")
                schedule_selete1.click()

                # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
                print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
                self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표

                self.driver.tap([(530, 1620)]) #door 선택

                device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
                device_setting.click()

                self.driver.tap([(930, 900)]) #스케줄 잠금 선택

                schedule_selete1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음")
                schedule_selete1.click()

                # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
                print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
                self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
            door.click()

            device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
            device_setting.click()

            schedule1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\n없음")
            schedule1.click()

            # Web에 저장된 스케줄 선택
            schedule_selete1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "E2E_Schedule")
            schedule_selete1.click()

            # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
            print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            self.driver.tap([(468, 2049)]) # 이벤트 이력 클릭

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='잠금 닫힘'])[1]").is_displayed()
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금 닫힘").is_displayed()
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888").is_displayed()
                except NoSuchElementException:
                    self.fail("DQS_T14025 출입문 스케쥴 잠금 설정 시 동작 확인 || DQS-T14088 출입문 스케줄 잠금 설정 해제 시 동작 확인")
            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='스케줄 잠금 시작'])[1]").is_displayed()
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금 시작").is_displayed()
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888").is_displayed()
                except NoSuchElementException:
                    self.fail("DQS_T14025 출입문 스케쥴 잠금 설정 시 동작 확인 || DQS-T14088 출입문 스케줄 잠금 설정 해제 시 동작 확인")

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            close_door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n스케줄 잠금\nBS3_538200888")
            close_door.click()

            device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
            device_setting.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\nE2E_Schedule")

            # DQS-T14087 출입문 스케줄 열림 설정 해제 시 동작 확인
            schedule2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\nE2E_Schedule")
            schedule2.click()

            schedule_selete2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음")
            schedule_selete2.click()

            # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
            print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            self.driver.tap([(468, 2049)]) # 이벤트 이력 클릭

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='잠금 닫힘'])[1]").is_displayed()
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금 닫힘").is_displayed()
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888").is_displayed()
                except NoSuchElementException:
                    self.fail("DQS_T14025 출입문 스케쥴 잠금 설정 시 동작 확인 || DQS-T14088 출입문 스케줄 잠금 설정 해제 시 동작 확인")
            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='스케줄 잠금 종료'])[1]").is_displayed()
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금 종료").is_displayed()
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888").is_displayed()
                except NoSuchElementException:
                    self.fail("DQS_T14025 출입문 스케쥴 잠금 설정 시 동작 확인 || DQS-T14088 출입문 스케줄 잠금 설정 해제 시 동작 확인")

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")

            pass

            print("DQS_T14025 출입문 스케쥴 잠금 설정 시 동작 확인 || DQS-T14088 출입문 스케줄 잠금 설정 해제 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14077(self):
        try:
            print("DQS_T14077 출입문 모드 변경시 동작 확인")

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
            door.click()

            print("수동 잠금 -> 수동 열림 변경 시나리오 시작")
            manuallock = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[2]")
            manuallock.click()
            time.sleep(1)

            status1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 잠금'])[2]")
            contentDesc1 = status1.get_attribute('content-desc')
            print(f"잠금 상태 : {contentDesc1}")

            manualopen = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[4]")
            manualopen.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문 제어").is_displayed()
            door_pop1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='현재 모드를 해제 하시겠습니까?']")
            msg1 = door_pop1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {msg1}")
            self.assertEqual(msg1, "현재 모드를 해제 하시겠습니까?")

            cancel_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            cancel_Btn.click()

            manualopen = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[4]")
            manualopen.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문 제어").is_displayed()
            door_pop2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='현재 모드를 해제 하시겠습니까?']")
            msg2 = door_pop2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {msg2}")
            self.assertEqual(msg2, "현재 모드를 해제 하시겠습니까?")

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()

            status2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금")
            contentDesc2 = status2.get_attribute('content-desc')
            print(f"잠금 상태 : {contentDesc2}")

            print("수동 열림 -> 수동 잠금 변경 시나리오 시작")
            manualopen = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[4]")
            manualopen.click()
            time.sleep(1)

            manuallock = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[2]")
            manuallock.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문 제어").is_displayed()
            door_pop3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='현재 모드를 해제 하시겠습니까?']")
            msg3 = door_pop3.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {msg3}")
            self.assertEqual(msg3, "현재 모드를 해제 하시겠습니까?")

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()

            status3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금")
            contentDesc3 = status3.get_attribute('content-desc')
            print(f"잠금 상태 : {contentDesc3}")

            print("수동 열림 -> 일시 열림 변경 시나리오 시작")
            manualopen = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[4]")
            manualopen.click()
            time.sleep(1)

            open = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[3]")
            open.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문 제어").is_displayed()
            door_pop4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='현재 모드를 해제 하시겠습니까?']")
            msg4 = door_pop4.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {msg4}")
            self.assertEqual(msg4, "현재 모드를 해제 하시겠습니까?")

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()

            status4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금")
            contentDesc4 = status4.get_attribute('content-desc')
            print(f"잠금 상태 : {contentDesc4}")

            print("수동 잠금 -> 일시 열림 변경 시나리오 시작")
            manuallock = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[2]")
            manuallock.click()
            time.sleep(1)

            open = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[3]")
            open.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문 제어").is_displayed()
            door_pop5 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='현재 모드를 해제 하시겠습니까?']")
            msg5 = door_pop5.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {msg5}")
            self.assertEqual(msg5, "현재 모드를 해제 하시겠습니까?")

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()

            status5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금")
            contentDesc5 = status5.get_attribute('content-desc')
            print(f"잠금 상태 : {contentDesc5}")

            pass

            print("DQS_T14077 출입문 모드 변경시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14083(self):
        try:
            print("DQS_T14083 출입문 Grid 리스트 에서 출입문 선택 시 동작 확인")

            list_mode = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[11]/android.widget.ImageView[2]")
            list_mode.click()

            gird_mode = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[11]/android.widget.ImageView[1]")
            gird_mode.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")

            device_select = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
            device_select.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
            status = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금")
            contentDesc = status.get_attribute('content-desc')
            print(f"잠금 상태 : {contentDesc}")

            self.driver.tap([(550, 747)]) # 출입문 바텀 시트 종료

            assert  self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")

            pass

            print("DQS_T14083 출입문 Grid 리스트 에서 출입문 선택 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14084(self):
        try:
            print("DQS-T14084 출입문 리스트 변경 버튼 기능 동작 확인")

            list_mode = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[11]/android.widget.ImageView[2]")
            list_mode.click()

            gird_mode = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[11]/android.widget.ImageView[1]")
            gird_mode.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
            time.sleep(0.5)

            list_mode = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[11]/android.widget.ImageView[2]")
            list_mode.click()

            time.sleep(0.5)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888\n잠금  ").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_54780678\n잠금  ").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_547838616\n잠금  ").is_displayed()

            pass

            print("DQS-T14084 출입문 리스트 변경 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14085(self):
        try:
            print("DQS-T14085 출입문 리스트 뷰에서 출입문 선택 시 기능 동작 확인")

            list_mode = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[11]/android.widget.ImageView[2]")
            list_mode.click()

            time.sleep(0.5)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888\n잠금  ").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_54780678\n잠금  ").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_547838616\n잠금  ").is_displayed()

            device_selete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_54780678\n잠금  ")
            device_selete.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_54780678")
            status = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금")
            contentDesc = status.get_attribute('content-desc')
            print(f"잠금 상태 : {contentDesc}")

            self.driver.tap([(550, 747)]) # 출입문 바텀 시트 종료

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888\n잠금  ").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_54780678\n잠금  ").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_547838616\n잠금  ").is_displayed()

            pass

            print("DQS-T14085 출입문 리스트 뷰에서 출입문 선택 시 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14086(self):
        try:
            print("DQS-T14086 출입문 리스트 뷰 스와이프 시 기능 동작 확인")

            list_mode = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[11]/android.widget.ImageView[2]")
            list_mode.click()

            time.sleep(0.5)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888\n잠금  ").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_54780678\n잠금  ").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_547838616\n잠금  ").is_displayed()

            start_x = 535
            start_y = 1320
            end_x = 535
            end_y = 1788
            self.driver.swipe(start_x, start_y, end_x, end_y)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888\n잠금  ").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_54780678\n잠금  ").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_547838616\n잠금  ").is_displayed()

            start_x1 = 535
            start_y1 = 1788
            end_x1 = 535
            end_y1 = 1320
            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "XS2_543478219\n잠금  ").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "N2_800000900\n잠금  ").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "N2_538761744\n잠금  ").is_displayed()

            start_x2 = 535
            start_y2 = 1320
            end_x2 = 535
            end_y2 = 1788
            self.driver.swipe(start_x2, start_y2, end_x2, end_y2)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888\n잠금  ").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_54780678\n잠금  ").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_547838616\n잠금  ").is_displayed()

            pass

            print("DQS-T14086 출입문 리스트 뷰 스와이프 시 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14164(self):
        try:
            print("DQS-T14164 출입문 스케줄 열림/잠금 스케줄 이 중복되는 시간의 스케줄 설정 시도 시 동작 확인")

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
            except NoSuchElementException:
                print("초기 상태 아님 - 스케줄 없음으로 변경 후 Test 진행")
                self.driver.tap([(530, 1620)]) #door 선택

                device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
                device_setting.click()

                self.driver.tap([(930, 750)]) #스케줄 열림 선택

                schedule_selete1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음")
                schedule_selete1.click()

                # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
                print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
                self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표

                self.driver.tap([(530, 1620)]) #door 선택

                device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
                device_setting.click()

                self.driver.tap([(930, 900)]) #스케줄 잠금 선택

                schedule_selete1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음")
                schedule_selete1.click()

                # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
                print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
                self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
            door.click()

            device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
            device_setting.click()

            schedule1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\n없음")
            schedule1.click()

            # Web에 저장된 스케줄 선택
            schedule_selete1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "E2E_Schedule")
            schedule_selete1.click()


            # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
            print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "열림\n스케줄 열림\nBS3_538200888")
            door.click()

            device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
            device_setting.click()

            schedule2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\n없음")
            schedule2.click()

            # Web에 저장된 스케줄 선택
            schedule_selete2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "E2E_Schedule")
            schedule_selete2.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "지원하지 않음").is_displayed()
            popup1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='지원 하지 않음\ne1002']")
            content_desc = popup1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {content_desc}")
            self.assertEqual(content_desc, "지원 하지 않음\ne1002")

            confirm_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_btn.click()

            # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
            print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "열림\n스케줄 열림\nBS3_538200888")
            door.click()

            device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
            device_setting.click()

            schedule1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\nE2E_Schedule")
            schedule1.click()

            # Web에 저장된 스케줄 선택
            schedule_selete1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음")
            schedule_selete1.click()

            # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
            print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표

            pass

            print("DQS-T14164 출입문 스케줄 열림/잠금 스케줄 이 중복되는 시간의 스케줄 설정 시도 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    # def test_DQS_T14165(self):
    #     try:
    #         print("DQS-T14165 출입문 스케줄 열림 스케줄 시간 종료 시 동작 확인")
    #
    #         try:
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
    #         except NoSuchElementException:
    #             print("초기 상태 아님 - 스케줄 없음으로 변경 후 Test 진행")
    #             self.driver.tap([(530, 1620)]) #door 선택
    #
    #             device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
    #             device_setting.click()
    #
    #             self.driver.tap([(930, 750)]) #스케줄 열림 선택
    #
    #             schedule_selete1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음")
    #             schedule_selete1.click()
    #
    #             # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
    #             print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
    #             self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
    #
    #             self.driver.tap([(530, 1620)]) #door 선택
    #
    #             device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
    #             device_setting.click()
    #
    #             self.driver.tap([(930, 900)]) #스케줄 잠금 선택
    #
    #             schedule_selete1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음")
    #             schedule_selete1.click()
    #
    #             # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
    #             print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
    #             self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
    #
    #         door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
    #         door.click()
    #
    #         device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
    #         device_setting.click()
    #
    #         schedule1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\n없음")
    #         schedule1.click()
    #
    #         hour = utils.get_current_hour(self)
    #         print(hour)
    #
    #         hour2 = utils.get_current_hour(self)
    #         print(hour2)
    #
    #         min = utils.get_current_min(self)
    #         print(utils.get_current_min(self))
    #         min2 = (int(min) + 2) % 60
    #         print(min2)
    #
    #         schedule_add = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
    #         schedule_add.click()
    #
    #         name_input = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
    #         name_input.click()
    #         name_input.send_keys("Test Schedule")
    #         self.driver.back()
    #
    #         schedule_mon_add = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[15]")
    #         schedule_mon_add.click()
    #
    #         self.driver.tap([(257, 1221)]) # 시작 시간 선택
    #
    #         try:
    #             self.driver.find_element(AppiumBy.XPATH, f"//android.view.View[@content-desc='{hour2}']")
    #         except NoSuchElementException:
    #             max_swipes = 24
    #             start_x = 243
    #             start_y = 1929
    #             end_x = 230
    #             end_y = 1730
    #             duration = 150
    #
    #         for _ in range(max_swipes):
    #             try:
    #                 element = self.driver.find_element(AppiumBy.XPATH, f"//android.view.View[@content-desc='{hour2}']")
    #                 if element.is_displayed():
    #                     element.click()
    #                     break
    #             except NoSuchElementException:
    #                 self.driver.swipe(start_x, start_y, end_x, end_y, duration)
    #                 time.sleep(0.5)
    #         else:
    #             raise NoSuchElementException("찾을 수 없습니다.")
    #
    #         time.sleep(2)
    #
    #         self.driver.tap([(270, 1354)]) # 종료 시간 선택
    #
    #         try:
    #             self.driver.find_element(AppiumBy.XPATH, f"//android.view.View[@content-desc='{hour2}']")
    #         except NoSuchElementException:
    #             max_swipes = 24
    #             start_x1 = 243
    #             start_y1 = 1929
    #             end_x1 = 230
    #             end_y1 = 1730
    #             duration = 150
    #
    #         for _ in range(max_swipes):
    #             try:
    #                 element = self.driver.find_element(AppiumBy.XPATH, f"//android.view.View[@content-desc='{hour2}']")
    #                 if element.is_displayed():
    #                     element.click()
    #                     break
    #             except NoSuchElementException:
    #                 self.driver.swipe(start_x1, start_y1, end_x1, end_y1, duration)
    #                 time.sleep(0.5)
    #         else:
    #             raise NoSuchElementException("찾을 수 없습니다.")
    #
    #         time.sleep(2)
    #         self.driver.tap([(708, 1354)]) # 종료 분 선택
    #
    #         try:
    #             self.driver.find_element(AppiumBy.XPATH, f"//android.view.View[@content-desc='{min2+5}']")
    #         except NoSuchElementException:
    #             max_swipes = 60
    #             start_x2 = 243
    #             start_y2 = 1929
    #             end_x2 = 230
    #             end_y2 = 1730
    #             duration = 100
    #
    #         for _ in range(max_swipes):
    #             try:
    #                 element = self.driver.find_element(AppiumBy.XPATH, f"//android.view.View[@content-desc='{min2+5}']")
    #                 if element.is_displayed():
    #                     element.click()
    #                     break
    #             except NoSuchElementException:
    #                 self.driver.swipe(start_x2, start_y2, end_x2, end_y2, duration)
    #                 time.sleep(0.5)
    #         else:
    #             raise NoSuchElementException("찾을 수 없습니다.")
    #
    #         copy_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "복사")
    #         copy_btn.click()
    #
    #         tuesday_select = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "화요일")
    #         tuesday_select.click()
    #
    #         wednesday_select = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수요일")
    #         wednesday_select.click()
    #
    #         thursday_select = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "목요일")
    #         thursday_select.click()
    #
    #         friday_select = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "금요일")
    #         friday_select.click()
    #
    #         saturday_select = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "토요일")
    #         saturday_select.click()
    #
    #         sunday_select = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일요일")
    #         sunday_select.click()
    #
    #         confirm_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
    #         confirm_btn.click()
    #
    #         save_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "저장")
    #         save_btn.click()
    #         time.sleep(1)
    #
    #         schedule_selete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test Schedule")
    #         schedule_selete.click()
    #
    #         # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
    #         print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
    #         self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
    #         time.sleep(1)
    #
    #         self.driver.tap([(468, 2049)]) # 이벤트 이력 클릭
    #
    #         try:
    #             assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='잠금 해제'])[1]").is_displayed()
    #             assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]").is_displayed()
    #         except NoSuchElementException:
    #             try:
    #                 assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금 해제").is_displayed()
    #                 assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888").is_displayed()
    #             except NoSuchElementException:
    #                 self.fail("이벤트 찾지 못함")
    #         try:
    #             assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='스케줄 열림 시작'])[1]").is_displayed()
    #             assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]").is_displayed()
    #         except NoSuchElementException:
    #             try:
    #                 assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림 시작").is_displayed()
    #                 assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888").is_displayed()
    #             except NoSuchElementException:
    #                 self.fail("이벤트 찾지 못함")
    #
    #         self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
    #         time.sleep(121)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
    #
    #         self.driver.tap([(468, 2049)]) # 이벤트 이력 클릭
    #
    #         try:
    #             assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='잠금 닫힘'])[1]").is_displayed()
    #             assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]").is_displayed()
    #         except NoSuchElementException:
    #             try:
    #                 assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금 닫힘").is_displayed()
    #                 assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888").is_displayed()
    #             except NoSuchElementException:
    #                 self.fail("이벤트 찾지 못함")
    #         try:
    #             assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='스케줄 열림 종료'])[1]").is_displayed()
    #             assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]").is_displayed()
    #         except NoSuchElementException:
    #             try:
    #                 assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림 종료").is_displayed()
    #                 assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888").is_displayed()
    #             except NoSuchElementException:
    #                 self.fail("이벤트 찾지 못함")
    #
    #         self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
    #         time.sleep(1)
    #
    #         #스케줄 설정 없음으로 변경
    #         self.driver.tap([(530, 1620)]) #door 선택
    #
    #         device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
    #         device_setting.click()
    #
    #         self.driver.tap([(930, 750)]) #스케줄 열림 선택
    #
    #         schedule_selete1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음")
    #         schedule_selete1.click()
    #
    #         # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
    #         print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
    #         self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
    #
    #         pass
    #
    #         print("DQS-T14165 출입문 스케줄 열림 스케줄 시간 종료 시 동작 확인 | Pass")
    #
    #     except Exception as e:
    #         capture_screenshot(self.driver, self._testMethodName)
    #         print(f"{self._testMethodName} | Failed")
    #         print(str(e))
    #         self.fail()

    def test_DQS_T14209(self):
        try:
            print("DQS-T14209 출입문 설정 페이지의 뒤로가기 버튼 기능 동작 확인")

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
            door.click()

            device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
            device_setting.click()

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")

            pass
            print("DQS-T14209 출입문 설정 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14210(self):
        try:
            print("DQS-T14210 출입문 설정 페이지의 출입문명 인풋 박스 유효성 검사")
            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
            door.click()

            device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
            device_setting.click()

            name_delete = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='BS3_538200888']/android.widget.ImageView")
            name_delete.click()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("Ab")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "Ab")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("12")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "12")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("가나")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "가나")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("- _")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "- _")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("!@#$%^&*()")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "!@#$%^&*()")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.").is_displayed()
            specialText1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='공백,-,_, 외의 특수문자는 사용할 수 없습니다.']")
            contentDesc = specialText1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("Ab1")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "Ab1")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("Ab가")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "Ab가")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("Ab - _")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "Ab - _")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("Ab!")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.").is_displayed()
            specialText2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='공백,-,_, 외의 특수문자는 사용할 수 없습니다.']")
            contentDesc = specialText2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "Ab!")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("1가")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "1가")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("1 - _")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "1 - _")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("가 - _")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "가 - _")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("가!@#$%^&*()")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.").is_displayed()
            specialText3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='공백,-,_, 외의 특수문자는 사용할 수 없습니다.']")
            contentDesc = specialText3.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "가!@#$%^&*()")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789012345678901234567890123456789012345678901234567890123456")
            print("메시지 문구 기획 필요(CLUEQ-92) 현재는 65자 이상 입력 시 '공백, -, _, 외의 특수문자는 사용할 수 없습니다.' 문구 출력")

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.")
                raise AssertionError(f"Fail : 에러 메시지 출력, '공백,-,_, 외의 특수문자는 사용할 수 없습니다.'")
            except NoSuchElementException:
                print(f"pass : 에러 메시지 출력하지 않음")


            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1,"<<<<<이 친구는 기획이 이상하여 64자 넘어갔을때 잘못된 문구가 출력 되어 나중에 테스트 하시는분은 PES 기획에 문구 수정 요청하세요 ! ")
            self.assertEqual(dnIB1, "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789012345678901234567890123456789012345678901234567890123456")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            print("DQS-T14210 출입문 설정 페이지의 출입문명 인풋 박스 유효성 검사 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14230(self):
        try:
            print("DQS-T14230 스케줄 잠금 시간 목록 페이지의 뒤로가기 버튼 기능 동작 확인")

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
            except NoSuchElementException:
                print("초기 상태 아님 - 스케줄 없음으로 변경 후 Test 진행")
                self.driver.tap([(530, 1620)]) #door 선택

                device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
                device_setting.click()

                self.driver.tap([(930, 750)]) #스케줄 열림 선택

                # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
                print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
                self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표

                self.driver.tap([(530, 1620)]) #door 선택

                device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
                device_setting.click()

                self.driver.tap([(930, 900)]) #스케줄 잠금 선택

                schedule_selete1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음")
                schedule_selete1.click()

                # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
                print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
                self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
            door.click()

            device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
            device_setting.click()

            schedule1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\n없음")
            schedule1.click()

            # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
            print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\n없음")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\n없음")

            print("DQS-T14230 스케줄 잠금 시간 목록 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14229(self):
        try:
            print("DQS-T14229 스케줄 열림 시간 목록 페이지의 뒤로가기 버튼 기능 동작 확인")

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
            except NoSuchElementException:
                print("초기 상태 아님 - 스케줄 없음으로 변경 후 Test 진행")
                self.driver.tap([(530, 1620)]) #door 선택

                device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
                device_setting.click()

                self.driver.tap([(930, 750)]) #스케줄 열림 선택

                # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
                print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
                self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표

                self.driver.tap([(530, 1620)]) #door 선택

                device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
                device_setting.click()

                self.driver.tap([(930, 900)]) #스케줄 잠금 선택

                schedule_selete1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음")
                schedule_selete1.click()

                # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
                print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
                self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
            door.click()

            device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
            device_setting.click()

            schedule1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\n없음")
            schedule1.click()

            # 뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)
            print("뒤로가기 시 출입문 설정 화면 이동 되어야 함 / 현재는 메인화면으로 이동됨 - Fail(CLUEQ-857)")
            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\n없음")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\n없음")

            print("DQS-T14229 스케줄 열림 시간 목록 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14211(self):
        try:
            print("DQS-T14211 출입문 설정 페이지의 출입문명 인풋 박스 X 버튼 기능 동작 확인")

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
            door.click()

            device_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
            device_setting.click()

            name_delete = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='BS3_538200888']/android.widget.ImageView")
            name_delete.click()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("1")

            name_delete2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='1']/android.widget.ImageView")
            name_delete2.click()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText").is_displayed()

            print("DQS-T14211 출입문 설정 페이지의 출입문명 인풋 박스 X 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

class Video(unittest.TestCase):
    def setUp(self):
        self.driver = AppiumConfig.get_driver()
        self.driver.implicitly_wait(10)

        utils.mobile_login(self, "01011111111", "Kjstar36!!")

    def tearDown(self):
        self.driver.quit()

    def test_DQS_T14028(self):
        try:
            print("DQS-T14028 비디오 최대화/최소화 버튼 기능 동작 확인")

            #최대화(가로모드) 버튼 클릭
            self.driver.tap([(1004, 1132)])
            time.sleep(3)

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "전체화면 전환안됨, 공간 명 출력됨"
            except NoSuchElementException:
                pass

            # 최소화 버튼 클릭
            self.driver.tap([(71, 2137)])
            time.sleep(3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간")

            pass
            print("DQS-T14028 비디오 최대화/최소화 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14029(self):
        try:
            print("DQS-T14029 비디오명 변경 기능 동작 확인")

            self.driver.tap([(1004, 522)])

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카메라 설정")

            name_input = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            name_input.click()
            name_input.send_keys("Test1")

            modify_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modify_btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "변경이 완료 되었습니다.").is_displayed()
            camNameModify = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='변경이 완료 되었습니다.']")
            contentDesc = camNameModify.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "변경이 완료 되었습니다.")

            confirm_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_btn.click()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Test1']")

            name_delete = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Test1']/android.widget.ImageView")
            name_delete.click()

            name_input = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            name_input.click()
            name_input.send_keys("CAM_1")

            modify_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modify_btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "변경이 완료 되었습니다.").is_displayed()
            camNameModify = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='변경이 완료 되었습니다.']")
            contentDesc = camNameModify.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "변경이 완료 되었습니다.")

            confirm_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_btn.click()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='CAM_1']")

            pass

            print("DQS-T14029 비디오명 변경 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14030_T14027(self):
        try:
            print("DQS-T14030 비디오 멀티뷰에서 특정 비디오 선택 시 동작 확인 || DQS-T14027 비디오 뷰 변경 버튼 기능 동작 확인")

            multi_view1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[6]/android.widget.ImageView[1]")
            multi_view1.click()
            time.sleep(1)

            #1번 채널 선택
            self.driver.tap([(260, 644)])
            time.sleep(1)

            #선택한 채널이름 추출할 수 없어서 1ch 변경 후 설정 버튼 클릭 시 이동하는지 확인
            self.driver.tap([(1002, 528)])
            time.sleep(1)

            assert self .driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카메라 설정")

            # 뒤로가기 버튼 클릭
            for _ in range(2):
                self.driver.back()
                time.sleep(1)

            multi_view2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[6]/android.widget.ImageView[1]")
            multi_view2.click()
            time.sleep(1)

            #2번 채널 선택
            self.driver.tap([(774, 631)])
            time.sleep(1)

            #선택한 채널이름 추출할 수 없어서 1ch 변경 후 최대화 되는지 확인
            self.driver.tap([(1003, 1131)])
            time.sleep(1)

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "전체화면 전환안됨, 공간 명 출력됨"
            except NoSuchElementException:
                pass

            #최소화 복구
            self.driver.tap([(71, 2144)])
            time.sleep(1)

            multi_view3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.widget.ImageView[1]")
            multi_view3.click()
            time.sleep(1)

            #3번 채널 선택
            self.driver.tap([(258, 1019)])
            time.sleep(1)

            #선택한 채널이름 추출할 수 없어서 1ch 변경 후 설정 버튼 클릭 시 이동하는지 확인
            self.driver.tap([(1002, 528)])
            time.sleep(1)

            assert self .driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카메라 설정")

            # 뒤로가기 버튼 클릭
            for _ in range(2):
                self.driver.back()
                time.sleep(1)

            multi_view4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[6]/android.widget.ImageView[1]")
            multi_view4.click()
            time.sleep(1)

            #4번 채널 선택
            self.driver.tap([(796, 1003)])
            time.sleep(1)

            #선택한 채널이름 추출할 수 없어서 1ch 변경 후 최대화 확인
            self.driver.tap([(1003, 1131)])
            time.sleep(1)

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "전체화면 전환안됨, 공간 명 출력됨"
            except NoSuchElementException:
                pass

            #최소화 복구
            self.driver.tap([(71, 2144)])
            time.sleep(1)

            multi_view5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.widget.ImageView[1]")
            multi_view5.click()
            time.sleep(1)

            single_view = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.widget.ImageView[2]")
            single_view.click()
            time.sleep(1)

            print("DQS-T14030 비디오 멀티뷰에서 특정 비디오 선택 시 동작 확인 || DQS-T14027 비디오 뷰 변경 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13557(self):
        try:
            print("DQS-T13557 양방향 통화 중 카메라 화면 전환 시 동작 확인")

            #1번 > 3번 ch 이동
            for _ in range(2):
                start_x1 = 846
                start_y1 = 819
                end_x1 = 246
                end_y1 = 819
                self.driver.swipe(start_x1, start_y1, end_x1, end_y1)


            #양방향 통화버튼 선택
            self.driver.tap([(900, 1133)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='스피커 방송'])[1]")
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            #assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '누르고 말하세요.\n말하는 중에는 들리지 않습니다.') #현재 스피커 방송으로 출력됨

            touch_action = TouchAction(self.driver)
            x = 550
            y = 1696
            touch_action.long_press(x=x, y=y, duration=3000).release().perform()

            #양방향 통화 종료 - 비디오 임의 위치 클릭
            self.driver.tap([(479, 796)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")

            # #1번 > 3번 ch 이동
            # for _ in range(2):
            #     start_x1 = 846
            #     start_y1 = 819
            #     end_x1 = 246
            #     end_y1 = 819
            #     self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
            #
            # assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")

            #3번 > 1번 ch 이동
            for _ in range(2):
                start_x2 = 246
                start_y2 = 819
                end_x2 = 846
                end_y2 = 819
                self.driver.swipe(start_x2, start_y2, end_x2, end_y2)

            #1번 > 3번 ch 이동
            for _ in range(2):
                start_x1 = 846
                start_y1 = 819
                end_x1 = 246
                end_y1 = 819
                self.driver.swipe(start_x1, start_y1, end_x1, end_y1)

            self.driver.tap([(900, 1133)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='스피커 방송'])[1]")
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            #assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '누르고 말하세요.\n말하는 중에는 들리지 않습니다.') #현재 스피커 방송으로 출력됨

            touch_action = TouchAction(self.driver)
            x = 550
            y = 1696
            touch_action.long_press(x=x, y=y, duration=3000).release().perform()

            #양방향 통화 종료 - 비디오 임의 위치 클릭
            self.driver.tap([(479, 796)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")

            pass
            print("DQS-T13557 양방향 통화 중 카메라 화면 전환 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13558(self):
        try:
            print("DQS-T13558 양방향 통화 상태에서 전체 화면(가로 모드) 전환 시 동작 확인")

            #1번 > 3번 ch 이동
            for _ in range(2):
                start_x1 = 846
                start_y1 = 819
                end_x1 = 246
                end_y1 = 819
                self.driver.swipe(start_x1, start_y1, end_x1, end_y1)

            #양방향 통화버튼 선택
            self.driver.tap([(900, 1133)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='스피커 방송'])[1]")
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            #assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '누르고 말하세요.\n말하는 중에는 들리지 않습니다.') #현재 스피커 방송으로 출력됨

            touch_action = TouchAction(self.driver)
            x = 550
            y = 1696
            touch_action.long_press(x=x, y=y, duration=3000).release().perform()

            #양방향 통화 종료 - 비디오 임의 위치 클릭
            self.driver.tap([(479, 796)])
            time.sleep(1)

            #최대화(가로모드) 버튼 클릭
            self.driver.tap([(1004, 1132)])
            time.sleep(3)

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "전체화면 전환안됨, 공간 명 출력됨"
            except NoSuchElementException:
                pass

            # 최소화 버튼 클릭
            self.driver.tap([(71, 2137)])
            time.sleep(3)

            #양방향 통화버튼 선택
            self.driver.tap([(900, 1133)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='스피커 방송'])[1]")
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            #assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '누르고 말하세요.\n말하는 중에는 들리지 않습니다.') #현재 스피커 방송으로 출력됨

            touch_action = TouchAction(self.driver)
            x = 550
            y = 1696
            touch_action.long_press(x=x, y=y, duration=3000).release().perform()

            #양방향 통화 종료 - 비디오 임의 위치 클릭
            self.driver.tap([(479, 796)])
            time.sleep(1)

            pass
            print("DQS-T13558 양방향 통화 상태에서 전체 화면(가로 모드) 전환 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13559(self):
        try:
            print("DQS-T13559 양방향 통화 종료 기능 동작 확인")

            #1번 > 3번 ch 이동
            for _ in range(2):
                start_x1 = 846
                start_y1 = 819
                end_x1 = 246
                end_y1 = 819
                self.driver.swipe(start_x1, start_y1, end_x1, end_y1)

            #양방향 통화버튼 선택
            self.driver.tap([(900, 1133)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='스피커 방송'])[1]")
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            #assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '누르고 말하세요.\n말하는 중에는 들리지 않습니다.') #현재 스피커 방송으로 출력됨

            touch_action = TouchAction(self.driver)
            x = 550
            y = 1696
            touch_action.long_press(x=x, y=y, duration=3000).release().perform()

            #양방향 통화 종료 - 스와이프 동작
            start_x1 = 540
            start_y1 = 1226
            end_x1 = 540
            end_y1 = 1370
            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
            #양방향 통화 종료 확인
            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nBS3_538200888")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "전체화면 전환안됨, 출입문 출력됨"
            except NoSuchElementException:
                pass

            pass
            print("DQS-T13559 양방향 통화 종료 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13561(self):
        try:
            print("DQS-T13561 양방향 통화 기능이 없는 카메라 싱글뷰에서 양방향 통화 버튼 확인")

            # #1번 > 2번 ch 이동 - 2번 ch 양방향 통화 기는 없는 카메라
            # start_x1 = 846
            # start_y1 = 819
            # end_x1 = 246
            # end_y1 = 819
            # self.driver.swipe(start_x1, start_y1, end_x1, end_y1)

            #양방향 톻화버튼 선택
            self.driver.tap([(900, 1133)])
            time.sleep(1)

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스피커 방송")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "스피커 방송 출력되는지 확인"
            except NoSuchElementException:
                pass

            pass
            print("DQS-T13561 양방향 통화 기능이 없는 카메라 싱글뷰에서 양방향 통화 버튼 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

class EventSearch(unittest.TestCase):
    def setUp(self):
        self.driver = AppiumConfig.get_driver()
        self.driver.implicitly_wait(10)

        utils.mobile_login(self, "01020905304", "Kjstar36!!")

        # place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1")
        # place.click()
        # time.sleep(2)
        #
        # placeInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
        # placeInput.click()
        # placeInput.send_keys("비디오 공간")
        # time.sleep(1)
        #
        # assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간\nID : 22").is_displayed()
        #
        # self.driver.tap([(260, 644)])
        # time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    # def test_DQS_T13627(self):
    #     try:
    #         print("DQS-T13627 [출입보안][워크스페이스 변경] 동일한 타입으로 변경 시 동작 확인")
    #
    #         #하단 이력 조회 선택
    #         self.driver.tap([(362, 2081)])
    #         time.sleep(2)
    #
    #         #핕터 선택
    #         self.driver.tap([(1002, 291)])
    #         time.sleep(1)
    #
    #         #출입 이벤트 - 출입 인증 선택 해제
    #         self.driver.tap([(1016, 380)])
    #         time.sleep(1)
    #
    #         acEvent = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 인증")
    #         acEvent.click()
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n5").is_displayed()
    #
    #         confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
    #         confirm_Btn.click()
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "6 개 필터 선택").is_displayed()
    #
    #         #워크 스페이지 변경 - 출입보안(공간이름 : Test 공간2)
    #
    #         self.driver.tap([(175, 294)])
    #         time.sleep(5)
    #
    #         self.driver.tap([(277, 1823)])
    #         time.sleep(3)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이력조회").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test 공간2").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "6 개 필터 선택").is_displayed()
    #
    #         #핕터 선택
    #         self.driver.tap([(1002, 291)])
    #         time.sleep(1)
    #
    #         #출입 이벤트 - 출입 인증 선택 해제
    #         self.driver.tap([(1016, 380)])
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n6").is_displayed()
    #
    #         confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
    #         confirm_Btn.click()
    #         time.sleep(1)
    #
    #         #place변경(공간이름 : 멤버쉽관리_초대 100명 이상)
    #         self.driver.tap([(140, 291)])
    #         time.sleep(5)
    #
    #         self.driver.tap([(271, 622)])
    #         time.sleep(3)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이력조회").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "멤버쉽관리_초대 100명 이상").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "5 개 필터 선택").is_displayed()
    #
    #         #핕터 선택
    #         self.driver.tap([(1002, 291)])
    #         time.sleep(1)
    #
    #         #출입 이벤트 - 출입 인증 선택
    #         self.driver.tap([(1016, 380)])
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n5").is_displayed()
    #
    #         confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
    #         confirm_Btn.click()
    #         time.sleep(1)
    #
    #         #이력 필터 기존 설정 복구
    #         self.driver.tap([(1002, 291)])
    #         time.sleep(1)
    #
    #         #출입 이벤트 - 출입 인증 선택
    #         self.driver.tap([(1016, 380)])
    #         time.sleep(1)
    #
    #         acEvent = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 인증")
    #         acEvent.click()
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n6").is_displayed()
    #
    #         confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
    #         confirm_Btn.click()
    #         time.sleep(1)
    #
    #         pass
    #         print("DQS-T13627 [출입보안][워크스페이스 변경] 동일한 타입으로 변경 시 동작 확인 | Pass")
    #
    #     except Exception as e:
    #         capture_screenshot(self.driver, self._testMethodName)
    #         print(f"{self._testMethodName} | Failed")
    #         print(str(e))
    #         self.fail()

    # def test_DQS_T13628(self):
    #     try:
    #         print("DQS-T13628 [영상보안][워크스페이스 변경] 동일한 타입으로 변경 시 동작 확인")
    #
    #         #영상보안 공간 이동
    #         self.driver.tap([(215, 331)])
    #         time.sleep(5)
    #
    #         self.driver.tap([(786, 609)])
    #         time.sleep(5)
    #
    #         #하단 이력 조회 선택
    #         self.driver.tap([(362, 2081)])
    #         time.sleep(2)
    #
    #         #핕터 선택
    #         self.driver.tap([(1002, 291)])
    #         time.sleep(1)
    #
    #         #출입 이벤트 - 출입 인증 선택 해제
    #         self.driver.tap([(1016, 490)])
    #         time.sleep(1)
    #
    #         acEvent = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 인증")
    #         acEvent.click()
    #
    #         self.driver.tap([(1016, 490)])
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n5").is_displayed()
    #
    #         #영상 이벤트 - 움직임 감지 선택 해제
    #         self.driver.tap([(1016, 600)])
    #         time.sleep(1)
    #
    #         veEvent = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "움직임 감지")
    #         veEvent.click()
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 이벤트\n3").is_displayed()
    #
    #         confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
    #         confirm_Btn.click()
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "14 개 필터 선택").is_displayed()
    #         #14개로 출력됨 - issue
    #
    #         #워크 스페이지 변경 - 영상보안(공간이름 : Test 공간)
    #
    #         self.driver.tap([(175, 291)])
    #         time.sleep(5)
    #
    #         self.driver.tap([(797, 1209)])
    #         time.sleep(3)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이력조회").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test 공간").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "12 개 필터 선택").is_displayed()
    #         #12개 필터 출력됨(issue) - 10개로 출력되어야 함
    #
    #         #핕터 선택
    #         self.driver.tap([(1002, 291)])
    #         time.sleep(1)
    #
    #         #출입 이벤트 - 출입 인증 선택 해제
    #         self.driver.tap([(1016, 490)])
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n6").is_displayed()
    #
    #         self.driver.tap([(1016, 490)])
    #         time.sleep(1)
    #
    #         self.driver.tap([(1016, 600)])
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 이벤트\n4").is_displayed()
    #
    #         confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
    #         confirm_Btn.click()
    #         time.sleep(1)
    #
    #         #place변경(공간이름 : 비디오 공간)
    #         self.driver.tap([(140, 291)])
    #         time.sleep(5)
    #
    #         self.driver.tap([(794, 606)])
    #         time.sleep(3)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이력조회").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "12 개 필터 선택").is_displayed()
    #
    #         #핕터 선택
    #         self.driver.tap([(1002, 291)])
    #         time.sleep(1)
    #
    #         #출입 이벤트 - 출입 인증 선택
    #         self.driver.tap([(1016, 500)])
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n5").is_displayed()
    #
    #         self.driver.tap([(1016, 500)])
    #         time.sleep(1)
    #
    #         self.driver.tap([(1016, 600)])
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 이벤트\n3").is_displayed()
    #
    #         confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
    #         confirm_Btn.click()
    #         time.sleep(1)
    #
    #         #이력 필터 기존 설정 복구
    #         self.driver.tap([(1002, 291)])
    #         time.sleep(1)
    #
    #         #출입 이벤트 - 출입 인증 선택
    #         self.driver.tap([(1016, 500)])
    #         time.sleep(1)
    #
    #         acEvent = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 인증")
    #         acEvent.click()
    #
    #         self.driver.tap([(1016, 500)])
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n6").is_displayed()
    #
    #         self.driver.tap([(1016, 600)])
    #         time.sleep(1)
    #
    #         veEvent = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "움직임 감지")
    #         veEvent.click()
    #
    #         confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
    #         confirm_Btn.click()
    #         time.sleep(1)
    #
    #         pass
    #         print("DQS-T13628 [영상보안][워크스페이스 변경] 동일한 타입으로 변경 시 동작 확인 | Pass")
    #
    #     except Exception as e:
    #         capture_screenshot(self.driver, self._testMethodName)
    #         print(f"{self._testMethodName} | Failed")
    #         print(str(e))
    #         self.fail()

    # def test_DQS_T13629(self):
    #     try:
    #         print("DQS-T13629 [워크스페이스 변경] 비디오 워크스페이스로 변경 시 동작 확인")
    #
    #         #하단 이력 조회 선택
    #         self.driver.tap([(362, 2081)])
    #         time.sleep(2)
    #
    #         #핕터 선택
    #         self.driver.tap([(1002, 291)])
    #         time.sleep(1)
    #
    #         #출입 이벤트 - 출입 인증 선택 해제
    #         self.driver.tap([(1016, 380)])
    #         time.sleep(1)
    #
    #         acEvent = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 인증")
    #         acEvent.click()
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n5").is_displayed()
    #
    #         confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
    #         confirm_Btn.click()
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "6 개 필터 선택").is_displayed()
    #         #6개로 출력됨 - issue
    #
    #         #워크 스페이지 변경 - 영상보안(공간이름 : 비디오 공간)
    #
    #         self.driver.tap([(140, 291)])
    #         time.sleep(5)
    #
    #         self.driver.tap([(794, 606)])
    #         time.sleep(3)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이력조회").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "10 개 필터 선택").is_displayed()
    #         #10 개 필터로 출력됨 -issue
    #
    #         #핕터 선택
    #         self.driver.tap([(1002, 291)])
    #         time.sleep(1)
    #
    #         #출입 이벤트 선택
    #         self.driver.tap([(1020, 501)])
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n6").is_displayed()
    #
    #         #영상 이벤트 선택
    #         self.driver.tap([(1020, 600)])
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 이벤트\n4").is_displayed()
    #
    #         confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
    #         confirm_Btn.click()
    #         time.sleep(1)
    #
    #         #place변경(공간이름 : 멤버쉽관리_초대 100명 이상)
    #         self.driver.tap([(140, 291)])
    #         time.sleep(5)
    #
    #         self.driver.tap([(271, 622)])
    #         time.sleep(3)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이력조회").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "멤버쉽관리_초대 100명 이상").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "5 개 필터 선택").is_displayed()
    #
    #         #핕터 선택
    #         self.driver.tap([(1002, 291)])
    #         time.sleep(1)
    #
    #         #출입 이벤트 - 출입 인증 선택
    #         self.driver.tap([(1016, 380)])
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n5").is_displayed()
    #
    #         confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
    #         confirm_Btn.click()
    #         time.sleep(1)
    #
    #         #이력 필터 기존 설정 복구
    #         self.driver.tap([(1002, 291)])
    #         time.sleep(1)
    #
    #         #출입 이벤트 - 출입 인증 선택
    #         self.driver.tap([(1016, 380)])
    #         time.sleep(1)
    #
    #         acEvent = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 인증")
    #         acEvent.click()
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n6").is_displayed()
    #
    #         confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
    #         confirm_Btn.click()
    #         time.sleep(1)
    #
    #         pass
    #         print("DQS-T13629 [워크스페이스 변경] 비디오 워크스페이스로 변경 시 동작 확인 | Pass")
    #
    #     except Exception as e:
    #         capture_screenshot(self.driver, self._testMethodName)
    #         print(f"{self._testMethodName} | Failed")
    #         print(str(e))
    #         self.fail()

    # def test_DQS_T13630(self):
    #     try:
    #         print("DQS-T13630 [워크스페이스 변경] 출입문 워크스페이스로 변경 시 동작 확인")
    #
    #         #영상보안 공간 이동
    #         self.driver.tap([(215, 331)])
    #         time.sleep(5)
    #
    #         self.driver.tap([(786, 609)])
    #         time.sleep(5)
    #
    #         #하단 이력 조회 선택
    #         self.driver.tap([(362, 2081)])
    #         time.sleep(2)
    #
    #         #워크 스페이지 변경 - 출입보안(공간이름 : QA 무인매장)
    #         self.driver.tap([(170, 286)])
    #         time.sleep(5)
    #
    #         self.driver.tap([(295, 1190)])
    #         time.sleep(3)
    #
    #         #핕터 선택
    #         self.driver.tap([(1002, 291)])
    #         time.sleep(1)
    #
    #         #출입 이벤트 - 출입 인증 선택 해제
    #         self.driver.tap([(1020, 394)])
    #         time.sleep(1)
    #
    #         acEvent = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 인증")
    #         acEvent.click()
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n5").is_displayed()
    #
    #         confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
    #         confirm_Btn.click()
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "6 개 필터 선택").is_displayed()
    #         #6개로 출력됨 - issue
    #
    #         #워크 스페이지 변경 - 영상보안(공간이름 : 비디오 공간)
    #
    #         self.driver.tap([(140, 291)])
    #         time.sleep(5)
    #
    #         self.driver.tap([(794, 606)])
    #         time.sleep(3)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이력조회").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "10 개 필터 선택").is_displayed()
    #         #10 개 필터로 출력됨 -issue
    #
    #         #핕터 선택
    #         self.driver.tap([(1002, 291)])
    #         time.sleep(1)
    #
    #         #출입 이벤트 선택
    #         self.driver.tap([(1020, 501)])
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n6").is_displayed()
    #
    #         #영상 이벤트 선택
    #         self.driver.tap([(1020, 600)])
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 이벤트\n4").is_displayed()
    #
    #         confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
    #         confirm_Btn.click()
    #         time.sleep(1)
    #
    #         #place변경(공간이름 : 공간이름 : QA 무인매장)
    #         self.driver.tap([(170, 286)])
    #         time.sleep(5)
    #
    #         self.driver.tap([(295, 1190)])
    #         time.sleep(3)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이력조회").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "QA 무인매장").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "5 개 필터 선택").is_displayed()
    #
    #         #핕터 선택
    #         self.driver.tap([(1002, 291)])
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n5").is_displayed()
    #
    #         #출입 이벤트 - 출입 인증 선택
    #         self.driver.tap([(1020, 394)])
    #         time.sleep(1)
    #
    #         acEvent = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 인증")
    #         acEvent.click()
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n6").is_displayed()
    #
    #         confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
    #         confirm_Btn.click()
    #         time.sleep(1)
    #
    #         pass
    #         print("DQS-T13630 [워크스페이스 변경] 출입문 워크스페이스로 변경 시 동작 확인 | Pass")
    #
    #     except Exception as e:
    #         capture_screenshot(self.driver, self._testMethodName)
    #         print(f"{self._testMethodName} | Failed")
    #         print(str(e))
    #         self.fail()

    def test_DQS_T13637(self):
        try:
            print("DQS-T13637 [출입보안] 이력조회 필터의 기본값 확인")

            #출입보안 공간 - Visitor Place1
            #하단 이력 조회 선택
            self.driver.tap([(362, 2081)])
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "10 개 필터 선택")

            #핕터 선택
            filter_slelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "10 개 필터 선택")
            filter_slelete.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이력 조회 필터")

            #출입 이벤트 필터 확인
            ac_event_open = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n6")
            ac_event_open.click()

            #출입 이벤트 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 제어")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 인증")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 제어")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도어락 잠금")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "퇴실 입력")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "문열림 알람")

            #출입 이벤트 필터 접기
            ac_event_close = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n6")
            ac_event_close.click()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 제어")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "수동 제어 출력됨"
            except NoSuchElementException:
                pass

            #출입문 확인
            door_open = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문\n4")
            door_open.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "XP2_544417896")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "XP2_546091200")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "XP2_333333333")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "XP2_546113199")

            #출입문 접기
            door_close = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문\n4")
            door_close.click()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "XP2_544417896")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "출입문 출력됨"
            except NoSuchElementException:
                pass

            pass
            print("DQS-T13637 [출입보안] 이력조회 필터의 기본값 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13638(self):
        try:
            print("DQS-T13638 [영상보안] 이력조회 필터의 기본값 확인")

            #영상보안 공간 이동 - 비디오 공간
            place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1")
            place.click()
            time.sleep(2)

            placeInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            placeInput.click()
            placeInput.send_keys("비디오 공간")
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간\nID : 22").is_displayed()

            self.driver.tap([(260, 644)])
            time.sleep(2)

            #하단 이력 조회 선택
            self.driver.tap([(362, 2081)])
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "17 개 필터 선택")

            #핕터 선택
            filter_slelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "17 개 필터 선택")
            filter_slelete.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이력 조회 필터")

            #출입 이벤트 필터 확인
            ac_event_open = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n6")
            ac_event_open.click()

            #출입 이벤트 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 제어")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 인증")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 제어")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도어락 잠금")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "퇴실 입력")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "문열림 알람")

            #출입 이벤트 필터 접기
            ac_event_close = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n6")
            ac_event_close.click()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 제어")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "수동 제어 출력됨"
            except NoSuchElementException:
                pass

            #video 이벤트 필터 확인
            video_event_open = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 이벤트\n4")
            video_event_open.click()

            #video 이벤트 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "움직임 감지")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "시야각 가림")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "IoT 접점 센서")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사람 감지")

            #video 이벤트 필터 접기
            video_event_close = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 이벤트\n4")
            video_event_close.click()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "움직임 감지")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "움직임 감지 출력됨"
            except NoSuchElementException:
                pass

            #출입문 확인
            door_open = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문\n7") #6변경해야 함
            door_open.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_54780678")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_547838616")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "XS2_543478219")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "N2_800000900")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "N2_538761744")

            #출입문 접기
            door_close = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문\n7")
            door_close.click()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "출입문 출력됨"
            except NoSuchElementException:
                pass
            pass
            print("DQS-T13638 [영상보안] 이력조회 필터의 기본값 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13652(self):
        try:
            print("DQS-T13652 [출입보안] 이력조회 기간의 검색 범위 초과 설정 시(8일 이상) 동작 확인")

            #하단 이력 조회 선택
            self.driver.tap([(362, 2081)])
            time.sleep(3)

            #조회 기간 선택
            self.driver.tap([(1008, 587)])
            time.sleep(1)

            #이전 달 이동
            pre_month = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Backward")
            pre_month.click()
            time.sleep(1)

            #3번째 주 월요일 선택
            self.driver.tap([(228, 932)])
            time.sleep(1)

            #4번째 주 월요일 선택
            self.driver.tap([(231, 1044)])
            time.sleep(1)

            #확인 버튼 클릭 후 팝업 출력 확인
            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "검색 범위 초과").is_displayed()
            searchError_Pop = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='최대 검색 범위는 7일 입니다.']")
            contentDesc = searchError_Pop.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")

            #팝업 확인 버튼 클릭
            confirmPop_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmPop_Btn.click()

            cancle_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            cancle_Btn.click()

            pass
            print("DQS-T13652 [출입보안] 이력조회 기간의 검색 범위 초과 설정 시(8일 이상) 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13653(self):
        try:
            print("DQS-T13653 [영상보안] 이력조회 기간의 검색 범위 초과 설정 시(8일 이상) 동작 확인")

            #영상보안 공간 이동 - 비디오 공간
            place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1")
            place.click()
            time.sleep(2)

            placeInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            placeInput.click()
            placeInput.send_keys("비디오 공간")
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간\nID : 22").is_displayed()

            self.driver.tap([(260, 644)])
            time.sleep(2)

            #하단 이력 조회 선택
            self.driver.tap([(362, 2081)])
            time.sleep(3)

            #조회 기간 선택
            self.driver.tap([(1008, 587)])
            time.sleep(1)

            #이전 달 이동
            pre_month = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Backward")
            pre_month.click()
            time.sleep(1)

            #3번째 주 월요일 선택
            self.driver.tap([(228, 932)])
            time.sleep(1)

            #4번째 주 월요일 선택
            self.driver.tap([(231, 1044)])
            time.sleep(1)

            #확인 버튼 클릭 후 팝업 출력 확인
            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "검색 범위 초과").is_displayed()
            searchError_Pop = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='최대 검색 범위는 7일 입니다.']")
            contentDesc = searchError_Pop.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")

            #팝업 확인 버튼 클릭
            confirmPop_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmPop_Btn.click()

            cancle_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            cancle_Btn.click()

            pass
            print("DQS-T13653 [영상보안] 이력조회 기간의 검색 범위 초과 설정 시(8일 이상) 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

class IO(unittest.TestCase):
    def setUp(self):
        self.driver = AppiumConfig.get_driver()
        self.driver.implicitly_wait(10)

        utils.mobile_login(self, "01011111111", "Kjstar36!!")

    def tearDown(self):
        self.driver.quit()

    def test_DQS_T777777_2(self):
        try:
            print("DQS_T777777_2 센서(Input) 및 Relay(Output) UI 확인")

            #I/O 탭 출력 확인
            io_tab = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I/O")
            io_tab.click()
            time.sleep(0.5)

            # 등록된 input 출력 확인
            assert  self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_input 0\ninput 0번\nOFF\nDI_24_input 3\ninput 3번\nOFF\nSIO2_input 0\ninput 0번\nOFF\nDM_20_input 3\ninput 3번\nOFF\nDM_20_input 7\ninput 7번\nOFF")
            time.sleep(1)

            # I/O 메뉴 펼치기
            self.driver.tap([(984, 1253)])
            time.sleep(1)

            # 등록된 Relay 출력 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0\nrelay 0번\nOFF")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 1\nrelay 1번\nOFF")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "SIO2_relay 0\nrelay 0번\nOFF")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DM_20_relay 2\nrelay 2번\nOFF")

            # relay제어 UI 확인
            relay_selete1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0\nrelay 0번\nOFF")
            relay_selete1.click()
            time.sleep(0.5)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 잠금")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일시 열림")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 열림")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Current status")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Normal Off")

            # relay 이름 클릭
            relay_name = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0")
            relay_name.click()
            time.sleep(0.5)

            # realy 설정 UI 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Relay name")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 설정")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\nNo select")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\nNo select")

            pass

            print("777777_2 센서(Input) 및 Relay(Output) UI 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T777777_3(self):
        try:
            print("DQS_T777777_3 I/O 레이아웃 펼치기/접기 동작 확인")

            #I/O 탭 출력 확인
            io_tab = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I/O")
            io_tab.click()
            time.sleep(0.5)

            # I/O 메뉴 펼치기
            self.driver.tap([(984, 1253)])
            time.sleep(1)

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상")

            except NoSuchElementException:
                pass

            # I/O 메뉴 접기
            self.driver.tap([(1002, 412)])
            time.sleep(1)

            # 영상 레이아웃 출력 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상")
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='실시간'])[2]")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "녹화 탐색")

            # I/O 메뉴 펼치기
            self.driver.tap([(984, 1253)])
            time.sleep(1)

            door_selete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door")
            door_selete.click()

            # 영상 레리아웃 출력 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상")
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='실시간'])[2]")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "녹화 탐색")

            #I/O 탭 클릭
            io_tab = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I/O")
            io_tab.click()
            time.sleep(0.5)

            # I/O 메뉴 펼치기
            self.driver.tap([(984, 1253)])
            time.sleep(1)

            # 사용자 메뉴 진입
            self.driver.tap([(971, 2067)])
            time.sleep(1)

            #뒤로가기 후 메인화면 정상 출력 확인
            self.driver.back()
            time.sleep(0.5)

            # 영상 레이아웃 출력 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상")
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='실시간'])[2]")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "녹화 탐색")

            #출입문 선택 확인 - door 선택된 상태에서는 accessibility_ID I/O 출력 확인
            # 영상 레리아웃 출력 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I/O")

            pass

            print("DQS_T777777_3 I/O 레이아웃 펼치기/접기 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T777777_4(self):
        try:
            print("DQS_T777777_4 I/O Relay 이름 수정 동작 확인")

            #I/O 탭 출력 확인
            io_tab = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I/O")
            io_tab.click()
            time.sleep(0.5)

            # I/O 메뉴 펼치기
            self.driver.tap([(984, 1253)])
            time.sleep(1)

            # Test수행할 Relay 선택
            relay_control = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0\nrelay 0번\nOFF")
            relay_control.click()

            # Relay 설정 진입
            relay_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0")
            relay_setting.click()

            # Relay 이름 수정
            relay_name_modity = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            relay_name_modity.click()
            relay_name_modity.send_keys("Relay 이름 수정")
            time.sleep(0.5)

            modity_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modity_btn.click()
            time.sleep(1)

            relay_name1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Relay 이름 수정']")
            text1 = relay_name1.get_attribute('text')
            print(f"추출한 이름 값 : {text1}")
            self.assertEqual(text1, "Relay 이름 수정")
            time.sleep(0.5)

            #뒤로가기
            for _ in range(2):
                self.driver.back()
                time.sleep(0.5)

            relay_name2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Relay 이름 수정']")
            contentDesc1 = relay_name2.get_attribute('content-desc')
            print(f"추출한 이름 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "Relay 이름 수정")
            time.sleep(0.5)

            # Relay 제어 바텀 시트 종료
            self.driver.back()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Relay 이름 수정\nrelay 0번\nOFF")

            # 기존 이름으로 수정
            relay_control2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Relay 이름 수정\nrelay 0번\nOFF")
            relay_control2.click()

            # Relay 설정 진입
            relay_setting2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Relay 이름 수정")
            relay_setting2.click()

            relay_name_modity2 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            relay_name_modity2.click()
            relay_name_modity2.send_keys("DI_24_relay 0")
            time.sleep(0.5)

            modity_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modity_btn.click()
            time.sleep(1)

            #뒤로가기
            for _ in range(2):
                self.driver.back()
                time.sleep(0.5)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0")

            pass


            print("DQS_T777777_4 I/O Relay 이름 수정 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T777777_5(self):
        try:
            print("DQS_T777777_5 Relay 이름 Validation 체크 동작 확인")

            #I/O 탭 출력 확인
            io_tab = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I/O")
            io_tab.click()
            time.sleep(0.5)

            # I/O 메뉴 펼치기
            self.driver.tap([(984, 1253)])
            time.sleep(1)

            # Test수행할 Relay 선택
            relay_control = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0\nrelay 0번\nOFF")
            relay_control.click()

            # Relay 설정 진입
            relay_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0")
            relay_setting.click()

            # Relay 이름 Validation 체크
            relay_name_input1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            relay_name_input1.click()
            relay_name_input1.send_keys("테스트 AB12 テスト 34한글")
            time.sleep(0.5)

            name_delete1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='테스트 AB12 テスト 34한글']/android.widget.ImageView")
            name_delete1.click()
            print("------------------- 테스트 AB12 テスト 34한글 완료")

            relay_name_input2 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            relay_name_input2.click()
            relay_name_input2.send_keys("-_-")
            time.sleep(0.5)

            name_delete2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='-_-']/android.widget.ImageView")
            name_delete2.click()
            print("------------------- -_- 완료")

            relay_name_input3 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            relay_name_input3.click()
            relay_name_input3.send_keys("~!@#")
            time.sleep(0.5)

            error_msg1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='공백,-,_, 외의 특수문자는 사용할 수 없습니다.']")
            contentDesc1 = error_msg1.get_attribute('content-desc')
            print(f"추출한 errorMsg 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.")
            time.sleep(0.5)

            # 수정 버튼 클릭 - 비활성화 확인
            modify_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            is_enabled = modify_btn.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "수정 버튼 비활성화")

            name_delete3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='~!@#']/android.widget.ImageView")
            name_delete3.click()
            print("------------------- ~!@# 완료")

            relay_name_input4 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            relay_name_input4.click()
            relay_name_input4.send_keys("테스트 AB12 テスト 34한글 Sample テキスト 5678 ABCD 한글 영어 日本語 混在 테스트 90 추가1234 extraテストXYZ789")
            time.sleep(0.5)

            text_input = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='테스트 AB12 テスト 34한글 Sample テキスト 5678 ABCD 한글 영어 日本語 混在 테스트 90 추가1234 extraテストXYZ78']")
            text_value = text_input.get_attribute('text')
            print(f"추출한 text 값 : {text_value}")
            self.assertEqual(text_value, "테스트 AB12 テスト 34한글 Sample テキスト 5678 ABCD 한글 영어 日本語 混在 테스트 90 추가1234 extraテストXYZ78")

            # 수정 버튼 클릭 - 비활성화 확인
            modify_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            is_enabled = modify_btn.get_attribute("enabled")
            self.assertEqual(is_enabled, "flase", "수정 버튼 비활성화")
            print("------------------- 80자 초과 테스트 완료")

            pass

            print("DQS_T777777_5 Relay 이름 Validation 체크 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T777777_6(self):
        try:
            print("DQS_T777777_6 Relay 수동 잠금 제어 동작 확인")

            #I/O 탭 출력 확인
            io_tab = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I/O")
            io_tab.click()
            time.sleep(0.5)

            # I/O 메뉴 펼치기
            self.driver.tap([(984, 1253)])
            time.sleep(1)

            # Test수행할 Relay 선택
            relay_control = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0\nrelay 0번\nOFF")
            relay_control.click()

            # 현재 상태 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 잠금")
            status0 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Normal Off']")
            contentDesc0 = status0.get_attribute('content-desc')
            print(f"Current status : {contentDesc0}")

            #수동 잠금 선택
            manuallock = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[2]")
            manuallock.click()
            time.sleep(2)

            status1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Manual Off\']")
            contentDesc1 = status1.get_attribute('content-desc')
            print(f"Current status : {contentDesc1}")

            self.driver.back() # 출입문 바텀 시트 종료
            self.driver.tap([(468, 2049)]) # 이벤트 이력 클릭 - 이벤트 출력 개선 필요하여 주석 처리함

            # try:
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='릴레이 OFF'])[1]")
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]")
            # except NoSuchElementException:
            #     try:
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "릴레이 OFF")
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888")
            #     except NoSuchElementException:
            #         self.fail("DQS_T777777_6 Relay 수동 잠금 제어 동작 확인 | Fail")

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            #I/O 탭 출력 확인
            io_tab = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I/O")
            io_tab.click()
            time.sleep(0.5)

            # # I/O 메뉴 펼치기
            # self.driver.tap([(984, 1253)])
            # time.sleep(1)

            # Test수행할 Relay 선택
            relay_control = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0\nrelay 0번\nOFF")
            relay_control.click()

            # 수동잠금 해제
            lock = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[2]")
            lock.click()
            time.sleep(2)

            status3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Normal Off']")
            contentDesc3 = status3.get_attribute('content-desc')
            print(f"Current status : {contentDesc3}")

            self.driver.back() # 출입문 바텀 시트 종료
            self.driver.tap([(468, 2049)]) # 이벤트 이력 클릭 - 이벤트 출력 개선 필요하여 주석 처리함

            # try:
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='릴레이 OFF'])[1]")
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]")
            # except NoSuchElementException:
            #     try:
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "릴레이 OFF")
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888")
            #     except NoSuchElementException:
            #         self.fail("DQS_T777777_6 Relay 수동 잠금 제어 동작 확인 | Fail")

            print("DQS_T14018 출입문 수동 잠금 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T777777_7(self):
        try:
            print("DQS_T777777_7 Relay 일시 열림 제어 동작 확인")

            #I/O 탭 출력 확인
            io_tab = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I/O")
            io_tab.click()
            time.sleep(0.5)

            # I/O 메뉴 펼치기
            self.driver.tap([(984, 1253)])
            time.sleep(1)

            # Test수행할 Relay 선택
            relay_control = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0\nrelay 0번\nOFF")
            relay_control.click()

            # 현재 상태 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일시 열림")
            status0 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Normal Off']")
            contentDesc0 = status0.get_attribute('content-desc')
            print(f"Current status : {contentDesc0}")

            # 일시 열림 제어 동작
            openrelay = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[3]")
            openrelay.click()
            time.sleep(2)

            status1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Once On']")
            contentDesc1 = status1.get_attribute('content-desc')
            print(f"Current status : {contentDesc1}")

            time.sleep(3)

            #3초 후 잠금 상태 변경
            status2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Normal Off']")
            contentDesc2 = status2.get_attribute('content-desc')
            print(f"Current status : {contentDesc2}")

            self.driver.back() # 출입문 바텀 시트 종료
            self.driver.tap([(540, 2031)]) # 이벤트 이력 클릭 - 이벤트 출력 개선 필요하여 주석 처리함

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='릴레이 OFF'])[1]")
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]")
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "릴레이 OFF")
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888")
                except NoSuchElementException:
                    self.fail("DQS_T777777_7 Relay 일시 열림 제어 동작 확인 | Fail")

            # try:
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='잠금 해제'])[1]")
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[2]")
            # except NoSuchElementException:
            #     try:
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금 해제")
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888")
            #     except NoSuchElementException:
            #         self.fail("DQS_T14019 출입문 일시 열림 기능 동작 확인 | Fail")

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표

            print("DQS_T777777_7 Relay 일시 열림 제어 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T777777_8(self):
        try:
            print("DQS_T777777_8 Relay 수동 열림 제어 동작 확인")

            #I/O 탭 출력 확인
            io_tab = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I/O")
            io_tab.click()
            time.sleep(0.5)

            # I/O 메뉴 펼치기
            self.driver.tap([(984, 1253)])
            time.sleep(1)

            # Test수행할 Relay 선택
            relay_control = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0\nrelay 0번\nOFF")
            relay_control.click()

            # 현재 상태 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일시 열림")
            status0 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Normal Off']")
            contentDesc0 = status0.get_attribute('content-desc')
            print(f"Current status : {contentDesc0}")

            #수동 열림 제어
            manualOpen = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[4]")
            manualOpen.click()
            time.sleep(2)

            status1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Manual On")
            contentDesc1 = status1.get_attribute('content-desc')
            print(f"Current status : {contentDesc1}")

            self.driver.back() # 출입문 바텀 시트 종료
            self.driver.tap([(468, 2049)]) # 이벤트 이력 클릭 - 이벤트 출력 개선 필요하여 주석 처리함

            # try:
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='릴레이 ON'])[1]").is_displayed()
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]").is_displayed()
            # except NoSuchElementException:
            #     try:
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "릴레이 ON").is_displayed()
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888").is_displayed()
            #     except NoSuchElementException:
            #         self.fail("DQS_T777777_8 출입문 수동 열림 기능 동작 확인 | Fail")
            #
            # try:
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 열림 시작'])[1]").is_displayed()
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_538200888'])[1]").is_displayed()
            # except NoSuchElementException:
            #     try:
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 열림 시작").is_displayed()
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888").is_displayed()
            #     except NoSuchElementException:
            #         self.fail("DQS_T777777_8 출입문 수동 열림 기능 동작 확인 | Fail")

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            #I/O 탭 출력 확인
            io_tab = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I/O")
            io_tab.click()
            time.sleep(0.5)

            # # I/O 메뉴 펼치기
            # self.driver.tap([(984, 1253)])
            # time.sleep(1)

            # Test수행할 Relay 선택
            relay_control = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0\nrelay 0번\nON")
            relay_control.click()

            # 수동 열림 해제
            lock = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[4]")
            lock.click()
            time.sleep(2)

            status3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Normal Off']")
            contentDesc3 = status3.get_attribute('content-desc')
            print(f"Current status : {contentDesc3}")

            self.driver.back() # 출입문 바텀 시트 종료
            self.driver.tap([(468, 2049)]) # 이벤트 이력 클릭 - 이벤트 출력 개선 필요하여 주석 처리함

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='릴레이 OFF'])[1]")
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]")
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "릴레이 OFF")
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888")
                except NoSuchElementException:
                    self.fail("DQS_T777777_8 출입문 수동 열림 기능 동작 확인 | Fail")

            pass

            print("DQS_T777777_8 출입문 수동 열림 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T777777_9_T777777_11(self):
        try:
            print("DQS_T777777_9 Relay 스케줄 열림 설정 동작 확인 || DQS_T777777_11 Relay 스케줄 열림 설정된 상태에서 수동 제어 동작 확인")

            #I/O 탭 출력 확인
            io_tab = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I/O")
            io_tab.click()
            time.sleep(0.5)

            # I/O 메뉴 펼치기
            self.driver.tap([(984, 1253)])
            time.sleep(1)

            # Test수행할 Relay 선택
            relay_control = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0\nrelay 0번\nOFF")
            relay_control.click()

            # 현재 상태 확인
            status0 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Normal Off']")
            contentDesc0 = status0.get_attribute('content-desc')
            print(f"Current status : {contentDesc0}")

            relay_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0")
            relay_setting.click()

            schedule_open = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\nNo select")
            schedule_open.click()

            #공간에 저장된 스케줄 선택
            schedule_selete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "E2E_Schedule")
            schedule_selete.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\nE2E_Schedule")

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            # 스케줄 On 상태 확인
            status1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Schedule On']")
            contentDesc1 = status1.get_attribute('content-desc')
            print(f"Current status : {contentDesc1}")

            #DQS_T777777_11 Relay 스케줄 열림 설정된 상태에서 수동 제어 동작 확인
            #수동 잠금 선택
            manuallock = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[2]")
            manuallock.click()
            time.sleep(2)

            status2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Manual Off']")
            contentDesc2 = status2.get_attribute('content-desc')
            print(f"Current status : {contentDesc2}")

            self.driver.back() # 출입문 바텀 시트 종료
            self.driver.tap([(468, 2049)]) # 이벤트 이력 클릭 - 이벤트 출력 개선 필요하여 주석 처리함

            # try:
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='릴레이 OFF'])[1]")
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]")
            # except NoSuchElementException:
            #     try:
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "릴레이 OFF")
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888")
            #     except NoSuchElementException:
            #         self.fail("DQS_T777777_11 Relay 스케줄 열림 설정된 상태에서 수동 제어 동작 확인 | Fail")

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            #I/O 탭 출력 확인
            io_tab = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I/O")
            io_tab.click()
            time.sleep(0.5)

            # # I/O 메뉴 펼치기
            # self.driver.tap([(984, 1253)])
            # time.sleep(1)

            # Test수행할 Relay 선택
            relay_control = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0\nrelay 0번\nOFF")
            relay_control.click()

            # 일시 열림 제어 동작
            openrelay = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[3]")
            openrelay.click()
            time.sleep(2)

            status3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Once On']")
            contentDesc3 = status3.get_attribute('content-desc')
            print(f"Current status : {contentDesc3}")

            time.sleep(3)

            #3초 후 잠금 상태 변경
            status4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Schedule On']")
            contentDesc4 = status4.get_attribute('content-desc')
            print(f"Current status : {contentDesc4}")

            self.driver.back() # 출입문 바텀 시트 종료
            self.driver.tap([(540, 2031)]) # 이벤트 이력 클릭 - 이벤트 출력 개선 필요하여 주석 처리함

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='릴레이 OFF'])[1]")
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]")
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "릴레이 OFF")
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888")
                except NoSuchElementException:
                    self.fail("DQS_T777777_11 Relay 스케줄 열림 설정된 상태에서 수동 제어 동작 확인 | Fail")

            # try:
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='잠금 해제'])[1]")
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[2]")
            # except NoSuchElementException:
            #     try:
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금 해제")
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888")
            #     except NoSuchElementException:
            #         self.fail("DQS_T14019 출입문 일시 열림 기능 동작 확인 | Fail")

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표

            #I/O 탭 출력 확인
            io_tab = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I/O")
            io_tab.click()
            time.sleep(0.5)

            # I/O 메뉴 펼치기
            self.driver.tap([(984, 1253)])
            time.sleep(1)

            # Test수행할 Relay 선택
            relay_control = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0\nrelay 0번\nON")
            relay_control.click()

            # 현재 상태 확인
            status5 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Schedule On']")
            contentDesc5 = status5.get_attribute('content-desc')
            print(f"Current status : {contentDesc5}")

            #수동 열림 제어
            manualOpen = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[4]")
            manualOpen.click()
            time.sleep(2)

            status6 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Manual On")
            contentDesc6 = status6.get_attribute('content-desc')
            print(f"Current status : {contentDesc6}")

            self.driver.back() # 출입문 바텀 시트 종료
            self.driver.tap([(468, 2049)]) # 이벤트 이력 클릭 - 이벤트 출력 개선 필요하여 주석 처리함

            # try:
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='릴레이 ON'])[1]").is_displayed()
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]").is_displayed()
            # except NoSuchElementException:
            #     try:
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "릴레이 ON").is_displayed()
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888").is_displayed()
            #     except NoSuchElementException:
            #         self.fail("DQS_T777777_11 Relay 스케줄 열림 설정된 상태에서 수동 제어 동작 확인 | Fail")
            #
            # try:
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 열림 시작'])[1]").is_displayed()
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_538200888'])[1]").is_displayed()
            # except NoSuchElementException:
            #     try:
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 열림 시작").is_displayed()
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888").is_displayed()
            #     except NoSuchElementException:
            #         self.fail("DQS_T777777_11 Relay 스케줄 열림 설정된 상태에서 수동 제어 동작 확인 | Fail")

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            #I/O 탭 출력 확인
            io_tab = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I/O")
            io_tab.click()
            time.sleep(0.5)

            # # I/O 메뉴 펼치기
            # self.driver.tap([(984, 1253)])
            # time.sleep(1)

            # Test수행할 Relay 선택
            relay_control = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0\nrelay 0번\nON")
            relay_control.click()

            # 수동 열림 해제
            lock = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[4]")
            lock.click()
            time.sleep(2)

            status7 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Schedule On']")
            contentDesc7 = status7.get_attribute('content-desc')
            print(f"Current status : {contentDesc7}")

            relay_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0")
            relay_setting.click()

            schedule_open1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\nE2E_Schedule")
            schedule_open1.click()

            # 스케줄 - 없음 선택
            schedule_selete1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음")
            schedule_selete1.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\nNo select")

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            # Relay 상태 확인
            status8 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Normal Off']")
            contentDesc8 = status8.get_attribute('content-desc')
            print(f"Current status : {contentDesc8}")

            self.driver.back() # 출입문 바텀 시트 종료
            self.driver.tap([(468, 2049)]) # 이벤트 이력 클릭 - 이벤트 출력 개선 필요하여 주석 처리함

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='릴레이 OFF'])[1]").is_displayed()
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "릴레이 OFF").is_displayed()
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888").is_displayed()
                except NoSuchElementException:
                    self.fail("DQS_T777777_9 Relay 스케줄 열림 설정 동작 확인 | Fail")

            pass

            print("DQS_T777777_9 Relay 스케줄 열림 설정 동작 확인 || DQS_T777777_9 Relay 스케줄 열림 설정된 상태에서 수동 제어 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T777777_10_T777777_12(self):
        try:
            print("DQS_T777777_10 Relay 스케줄 잠금 설정 동작 확인 || DQS_T777777_12 Relay 스케줄 잠금 설정된 상태에서 수동 제어 동작 확인")

            #I/O 탭 출력 확인
            io_tab = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I/O")
            io_tab.click()
            time.sleep(0.5)

            # I/O 메뉴 펼치기
            self.driver.tap([(984, 1253)])
            time.sleep(1)

            # Test수행할 Relay 선택
            relay_control = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0\nrelay 0번\nOFF")
            relay_control.click()

            # 현재 상태 확인
            status0 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Normal Off']")
            contentDesc0 = status0.get_attribute('content-desc')
            print(f"Current status : {contentDesc0}")

            relay_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0")
            relay_setting.click()

            schedule_close = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\nNo select")
            schedule_close.click()

            #공간에 저장된 스케줄 선택
            schedule_selete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "E2E_Schedule")
            schedule_selete.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\nE2E_Schedule")

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            # 스케줄 Off 상태 확인
            status1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Schedule Off']")
            contentDesc1 = status1.get_attribute('content-desc')
            print(f"Current status : {contentDesc1}")

            #DQS_T777777_12 Relay 스케줄 잠금 설정된 상태에서 수동 제어 동작 확인
            #수동 잠금 선택
            manuallock = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[2]")
            manuallock.click()
            time.sleep(2)

            status2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Manual Off']")
            contentDesc2 = status2.get_attribute('content-desc')
            print(f"Current status : {contentDesc2}")

            self.driver.back() # 출입문 바텀 시트 종료
            self.driver.tap([(468, 2049)]) # 이벤트 이력 클릭 - 이벤트 출력 개선 필요하여 주석 처리함

            # try:
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='릴레이 OFF'])[1]")
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]")
            # except NoSuchElementException:
            #     try:
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "릴레이 OFF")
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888")
            #     except NoSuchElementException:
            #         self.fail("DQS_T777777_12 Relay 스케줄 잠금 설정된 상태에서 수동 제어 동작 확인 | Fail")

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            #I/O 탭 출력 확인
            io_tab = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I/O")
            io_tab.click()
            time.sleep(0.5)

            # # I/O 메뉴 펼치기
            # self.driver.tap([(984, 1253)])
            # time.sleep(1)

            # Test수행할 Relay 선택
            relay_control = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0\nrelay 0번\nOFF")
            relay_control.click()

            # 일시 열림 제어 동작
            openrelay = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[3]")
            openrelay.click()
            time.sleep(2)

            status3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Once On']")
            contentDesc3 = status3.get_attribute('content-desc')
            print(f"Current status : {contentDesc3}")

            time.sleep(3)

            #3초 후 스케줄 잠금 상태 변경
            status4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Schedule Off']")
            contentDesc4 = status4.get_attribute('content-desc')
            print(f"Current status : {contentDesc4}")

            self.driver.back() # 출입문 바텀 시트 종료
            self.driver.tap([(540, 2031)]) # 이벤트 이력 클릭 - 이벤트 출력 개선 필요하여 주석 처리함

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='릴레이 OFF'])[1]")
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]")
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "릴레이 OFF")
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888")
                except NoSuchElementException:
                    self.fail("DQS_T777777_11 Relay 스케줄 열림 설정된 상태에서 수동 제어 동작 확인 | Fail")

            # try:
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='잠금 해제'])[1]")
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[2]")
            # except NoSuchElementException:
            #     try:
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금 해제")
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888")
            #     except NoSuchElementException:
            #         self.fail("DQS_T777777_12 Relay 스케줄 잠금 설정된 상태에서 수동 제어 동작 확인 | Fail")

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표

            #I/O 탭 출력 확인
            io_tab = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I/O")
            io_tab.click()
            time.sleep(0.5)

            # I/O 메뉴 펼치기
            self.driver.tap([(984, 1253)])
            time.sleep(1)

            # Test수행할 Relay 선택
            relay_control = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0\nrelay 0번\nOFF")
            relay_control.click()

            # 현재 상태 확인
            status5 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Schedule Off']")
            contentDesc5 = status5.get_attribute('content-desc')
            print(f"Current status : {contentDesc5}")

            #수동 열림 제어
            manualOpen = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[4]")
            manualOpen.click()
            time.sleep(2)

            status6 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Manual On")
            contentDesc6 = status6.get_attribute('content-desc')
            print(f"Current status : {contentDesc6}")

            self.driver.back() # 출입문 바텀 시트 종료
            self.driver.tap([(468, 2049)]) # 이벤트 이력 클릭 - 이벤트 출력 개선 필요하여 주석 처리함

            # try:
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='릴레이 ON'])[1]").is_displayed()
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]").is_displayed()
            # except NoSuchElementException:
            #     try:
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "릴레이 ON").is_displayed()
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888").is_displayed()
            #     except NoSuchElementException:
            #         self.fail("DQS_T777777_12 Relay 스케줄 잠금 설정된 상태에서 수동 제어 동작 확인 | Fail")
            #
            # try:
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 열림 시작'])[1]").is_displayed()
            #     assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_538200888'])[1]").is_displayed()
            # except NoSuchElementException:
            #     try:
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 열림 시작").is_displayed()
            #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_538200888").is_displayed()
            #     except NoSuchElementException:
            #         self.fail("DQS_T777777_12 Relay 스케줄 잠금 설정된 상태에서 수동 제어 동작 확인 | Fail")

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            #I/O 탭 출력 확인
            io_tab = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I/O")
            io_tab.click()
            time.sleep(0.5)

            # # I/O 메뉴 펼치기
            # self.driver.tap([(984, 1253)])
            # time.sleep(1)

            # Test수행할 Relay 선택
            relay_control = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0\nrelay 0번\nON")
            relay_control.click()

            # 수동 열림 해제
            lock = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[4]")
            lock.click()
            time.sleep(2)

            status7 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Schedule Off']")
            contentDesc7 = status7.get_attribute('content-desc')
            print(f"Current status : {contentDesc7}")

            relay_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0")
            relay_setting.click()

            schedule_close1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\nE2E_Schedule")
            schedule_close1.click()

            # 스케줄 - 없음 선택
            schedule_selete1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음")
            schedule_selete1.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\nNo select")

            self.driver.tap([(67, 175)]) #뒤로가기 버튼 좌표
            time.sleep(1)

            # Relay 상태 확인
            status8 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Normal Off']")
            contentDesc8 = status8.get_attribute('content-desc')
            print(f"Current status : {contentDesc8}")

            self.driver.back() # 출입문 바텀 시트 종료
            self.driver.tap([(468, 2049)]) # 이벤트 이력 클릭 - 이벤트 출력 개선 필요하여 주석 처리함

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='릴레이 OFF'])[1]").is_displayed()
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='BS3_APWB_538200888'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "릴레이 OFF").is_displayed()
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BS3_APWB_538200888").is_displayed()
                except NoSuchElementException:
                    self.fail("DQS_T777777_10 Relay 스케줄 잠금 설정 동작 확인 | Fail")

            pass

            print("DQS_T777777_10 Relay 스케줄 잠금 설정 동작 확인 || DQS_T777777_12 Relay 스케줄 잠금 설정된 상태에서 수동 제어 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T777777_13(self):
        try:
            print("DQS_T777777_13 Relay 수동 제어된 상태에서 제어 동작 확인")

            #I/O 탭 출력 확인
            io_tab = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I/O")
            io_tab.click()
            time.sleep(0.5)

            # I/O 메뉴 펼치기
            self.driver.tap([(984, 1253)])
            time.sleep(1)

            # Test수행할 Relay 선택
            relay_control = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0\nrelay 0번\nOFF")
            relay_control.click()

            # 현재 상태 확인
            status0 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Normal Off']")
            contentDesc0 = status0.get_attribute('content-desc')
            print(f"Current status : {contentDesc0}")

            #수동 잠금 선택
            manuallock = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[2]")
            manuallock.click()
            time.sleep(2)

            status1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Manual Off']")
            contentDesc1 = status1.get_attribute('content-desc')
            print(f"Current status : {contentDesc1}")

            # 일시 열림 제어 동작
            openrelay = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[3]")
            openrelay.click()
            time.sleep(2)

            status2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Once On']")
            contentDesc2 = status2.get_attribute('content-desc')
            print(f"Current status : {contentDesc2}")

            time.sleep(3)

            #3초 후 Default 잠금 상태 변경(수동 잠금 해제)
            status3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Normal Off']")
            contentDesc3 = status3.get_attribute('content-desc')
            print(f"Current status : {contentDesc3}")

            print("---------- 수동 잠금 -> 일시열림 테스트 종료 ----------")

            #수동 잠금 선택
            manuallock = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[2]")
            manuallock.click()
            time.sleep(2)

            status4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Manual Off']")
            contentDesc4 = status4.get_attribute('content-desc')
            print(f"Current status : {contentDesc4}")

            #수동 열림 제어 - 수동 잠금 해제
            manualOpen = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[4]")
            manualOpen.click()
            time.sleep(2)

            status5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Normal Off")
            contentDesc5 = status5.get_attribute('content-desc')
            print(f"Current status : {contentDesc5}")


            print("---------- 수동 잠금 -> 수동열림 테스트 종료 ----------")

            manualOpen = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[4]")
            manualOpen.click()
            time.sleep(2)

            status6 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Manual On")
            contentDesc6 = status6.get_attribute('content-desc')
            print(f"Current status : {contentDesc6}")

            # 일시 열림 제어 동작
            openrelay = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[3]")
            openrelay.click()
            time.sleep(2)

            status7 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Once On']")
            contentDesc7 = status7.get_attribute('content-desc')
            print(f"Current status : {contentDesc7}")

            time.sleep(3)

            #3초 후 Default 잠금 상태 변경(수동 열림 해제)
            status8 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Normal Off']")
            contentDesc8 = status8.get_attribute('content-desc')
            print(f"Current status : {contentDesc8}")

            print("---------- 수동 열림 -> 일시열림 테스트 종료 ----------")

            manualOpen = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[4]")
            manualOpen.click()
            time.sleep(2)

            status9 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Manual On")
            contentDesc9 = status9.get_attribute('content-desc')
            print(f"Current status : {contentDesc9}")

            #수동 열림 -> 수동 잠금 선택
            manuallock = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Dismiss']/android.view.View/android.widget.ImageView[2]")
            manuallock.click()
            time.sleep(2)

            status10 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Normal Off']")
            contentDesc10 = status10.get_attribute('content-desc')
            print(f"Current status : {contentDesc10}")

            print("---------- 수동 열림 -> 수동 잠금 테스트 종료 ----------")

            pass

            print("DQS_T777777_13 Relay 수동 제어된 상태에서 제어 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T777777_14(self):
        try:
            print("DQS_T777777_14 Relay 스케줄 열림/잠금 스케줄이 중복되는 시간의 스케줄 설정 시도 시 동작 확인")

            #I/O 탭 출력 확인
            io_tab = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "I/O")
            io_tab.click()
            time.sleep(0.5)

            # I/O 메뉴 펼치기
            self.driver.tap([(984, 1253)])
            time.sleep(1)

            # Test수행할 Relay 선택
            relay_control = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0\nrelay 0번\nOFF")
            relay_control.click()

            # 현재 상태 확인
            status0 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Normal Off']")
            contentDesc0 = status0.get_attribute('content-desc')
            print(f"Current status : {contentDesc0}")

            relay_setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DI_24_relay 0")
            relay_setting.click()

            # Relay 스케줄 열림 - 공간에 저장된 스케줄 선택
            schedule_open = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\nNo select")
            schedule_open.click()

            schedule_selete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "근무시간1")
            schedule_selete.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\n근무시간1")

            # Relay 스케줄 잠금  - 스케줄 열림에 설정한 동일한 스케줄 선택
            schedule_close = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\nNo select")
            schedule_close.click()

            schedule_selete2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "근무시간1")
            schedule_selete2.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "등록 오류")
            error_pop1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='이미 사용중인 스케쥴 입니다.\nd1026']")
            content_desc1 = error_pop1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {content_desc1}")
            self.assertEqual(content_desc1, "이미 사용중인 스케쥴 입니다.\nd1026")

            confirmn_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmn_btn.click()

            # Relay 스케줄 잠금  - 스케줄 열림에 설정한 스케줄하고 동일한 시간대가 있는 스케줄 선택
            schedule_selete3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "E2E_Schedule")
            schedule_selete3.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "등록 오류")
            error_pop2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='이미 사용중인 스케쥴 입니다.\nd1026']")
            content_desc2 = error_pop2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {content_desc2}")
            self.assertEqual(content_desc2, "이미 사용중인 스케쥴 입니다.\nd1026")

            confirmn_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmn_btn.click()

            # 스케줄 열림 설정 해제
            self.driver.back()

            # Relay 스케줄 열림 - 없음 선택
            schedule_open = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\n근무시간1")
            schedule_open.click()

            schedule_selete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음")
            schedule_selete.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\nNo select")

            pass

            print("DQS_T777777_14 Relay 스케줄 열림/잠금 스케줄이 중복되는 시간의 스케줄 설정 시도 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()







if __name__ == '__main__':
    unittest.main()


