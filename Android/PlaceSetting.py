#import datetime
import os
import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.common import NoSuchElementException

#from Android.User import backBtn, modify, delete
#from selenium.webdriver.common.action_chains import ActionChains
#from configuration.utill import capture_screenshot
from configuration.webDriver import AppiumConfig
#from configuration.utill import swipe_until_element_found, swipe_up, capture_screenshot, extract_verification_code
from configuration.utill import capture_screenshot
import sys
sys.path.append('../Android')
from Android import utils
import random


checkFalse = "false"
checkTrue = "true"


class AlramMenu(unittest.TestCase):

    def setUp(self):
        self.driver = AppiumConfig.get_driver()
        self.driver.implicitly_wait(10)

        utils.mobile_login(self, "01020905304", "Kjstar36!!")
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

    def test_DQS_T15894(self):
        try:
            print("DQS_T15894 [출입보안] 공간 설정에 알람 설정 UI 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            acMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 통제")
            acMenu.click()

            #출입문 이벤트 출력 확인 - 기본값 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문 이벤트\n시스템 이벤트").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증 성공").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증 성공']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증 실패").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증 실패']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "장시간 문열림").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='장시간 문열림']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "강제 문열림").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='강제 문열림']/android.widget.Switch").is_displayed()

            #시스템 이벤트 출력 확인 - 기본값 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "서버 연결 해제").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='서버 연결 해제']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "템퍼 발생").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='템퍼 발생']/android.widget.Switch").is_displayed()

            pass
            print("DQS_T15894 [출입보안] 공간 설정에 알람 설정 UI 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15894 [출입보안] 공간 설정에 알람 설정 UI 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15895(self):
        try:
            print("DQS_T15895 [영상보안] 공간 설정에 알람 설정 UI 확인")

            place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1")
            place.click()
            time.sleep(3)

            placeInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            placeInput.click()
            placeInput.send_keys("비디오 공간")
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간\nID : 22").is_displayed()

            self.driver.tap([(260, 644)])
            time.sleep(2)

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            acMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 통제")
            acMenu.click()

            #출입문 이벤트 출력 확인 - 기본값 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문 이벤트\n시스템 이벤트").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증 성공").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증 성공']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증 실패").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증 실패']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "장시간 문열림").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='장시간 문열림']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "강제 문열림").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='강제 문열림']/android.widget.Switch").is_displayed()

            #시스템 이벤트 출력 확인 - 기본값 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "서버 연결 해제").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='서버 연결 해제']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "템퍼 발생").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='템퍼 발생']/android.widget.Switch").is_displayed()

            #뒤로가기 클릭
            backBtn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
            backBtn.click()

            # self.driver.tap([(54, 158)])
            # time.sleep(1)

            videoMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 감시")
            videoMenu.click()

            #영상 감시 이벤트 출력 확인 - 기본값 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 이벤트\n영상 이벤트 순서 오류\nIoT 이벤트 순서 오류").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "움직임 감지").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='움직임 감지']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "시야각 가림").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='시야각 가림']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "IoT 접점 센서").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='IoT 접점 센서']/android.widget.Switch").is_displayed()

            #영상 이벤트 순서 오류 출력 확인 - 기본값 확인

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "내부 오류").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='내부 오류']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "연결 해제").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='연결 해제']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "디스크 공간 없음").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='디스크 공간 없음']/android.widget.Switch").is_displayed()

            #IoT 이벤트 순서 오류 출력 확인 - 기본값 확인

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "센서 분리").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='센서 분리']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "배터리 얼마남지 않음").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='배터리 얼마남지 않음']/android.widget.Switch").is_displayed()

            pass
            print("DQS_T15895 [영상보안] 공간 설정에 알람 설정 UI 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15895 [영상보안] 공간 설정에 알람 설정 UI 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15896(self):
        try:
            print("DQS_T15896 출입 통제에 출입문 이벤트 알람 설정 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            acMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 통제")
            acMenu.click()

            acXpath1 = "//android.view.View[@content-desc='인증 성공']/android.widget.Switch"
            acXpath2 = "//android.view.View[@content-desc='인증 실패']/android.widget.Switch"
            acXpath3 = "//android.view.View[@content-desc='장시간 문열림']/android.widget.Switch"
            acXpath4 = "//android.view.View[@content-desc='강제 문열림']/android.widget.Switch"


            print("----- #인증 성공 알람 이벤트만 설정 - 나머지 미설정 -----")
            utils.toggle_click(self, acXpath2)

            utils.toggle_click(self, acXpath3)

            utils.toggle_click(self, acXpath4)

            utils.toggle_status(self, acXpath1, acXpath2, acXpath3, acXpath4, "출입 통제")

            print("----- 인증 성공 토글 버튼 확인 완료-----")

            time.sleep(1)
            print("----- #인증 실패 알람 이벤트만 설정 - 나머지 미설정 -----")

            utils.toggle_click(self, acXpath1)

            utils.toggle_click(self, acXpath2)

            utils.toggle_status(self, acXpath1, acXpath2, acXpath3, acXpath4, "출입 통제")

            print("----- 인증 실패 토글 버튼 확인 완료-----")

            time.sleep(1)
            print("----- #장시간 문열림 알람 이벤트만 설정 - 나머지 미설정 -----")

            utils.toggle_click(self, acXpath2)

            utils.toggle_click(self, acXpath3)

            utils.toggle_status(self, acXpath1, acXpath2, acXpath3, acXpath4, "출입 통제")

            print("----- 장시간 문열림 토글 버튼 확인 완료-----")

            time.sleep(1)
            print("----- #강제 문열림 알람 이벤트만 설정 - 나머지 미설정 -----")

            utils.toggle_click(self, acXpath3)

            utils.toggle_click(self, acXpath4)

            utils.toggle_status(self, acXpath1, acXpath2, acXpath3, acXpath4, "출입 통제")

            print("----- 강제 문열림 토글 버튼 확인 완료-----")

            time.sleep(1)
            print("----- #모두 설정으로 복구 -----")

            authSuccess = self.driver.find_element(AppiumBy.XPATH, acXpath1)
            authSuccess.click()
            time.sleep(2)

            authFail = self.driver.find_element(AppiumBy.XPATH, acXpath2)
            authFail.click()
            time.sleep(2)

            longDoor = self.driver.find_element(AppiumBy.XPATH, acXpath3)
            longDoor.click()
            time.sleep(2)

            pass
            print("DQS_T15896 출입 통제에 출입문 이벤트 알람 설정 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15896 출입 통제에 출입문 이벤트 알람 설정 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15897(self):
        try:
            print("DQS_T15897 출입 통제에 시스템 이벤트 알람 설정 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            acMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 통제")
            acMenu.click()

            acXpath1 = "//android.view.View[@content-desc='서버 연결 해제']/android.widget.Switch"
            acXpath2 = "//android.view.View[@content-desc='템퍼 발생']/android.widget.Switch"

            print("----- #서버 연결 해제 이벤트만 설정 - 나머지 미설정 -----")
            utils.toggle_click(self, acXpath2)

            utils.toggle_status(self, acXpath1, acXpath2, None, None, "출입 통제")

            print("----- 서버 연결 해제 토글 버튼 확인 완료-----")

            time.sleep(1)
            print("----- #템퍼 발생 알람 이벤트만 설정 - 나머지 미설정 -----")

            utils.toggle_click(self, acXpath1)

            utils.toggle_click(self, acXpath2)

            utils.toggle_status(self, acXpath1, acXpath2, None, None, "출입 통제")

            print("----- 템퍼 발생 토글 버튼 확인 완료-----")

            time.sleep(1)
            print("----- #모두 설정으로 복구 -----")

            serverDis = self.driver.find_element(AppiumBy.XPATH, acXpath1)
            serverDis.click()
            time.sleep(2)

            pass
            print("DQS_T15897 출입 통제에 시스템 이벤트 알람 설정 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15897 출입 통제에 시스템 이벤트 알람 설정 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15898(self):
        try:
            print("DQS_T15898 영상 감시에 영상 이벤트 알람 설정 동작 확인")

            place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1")
            place.click()
            time.sleep(5)

            placeInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            placeInput.click()
            placeInput.send_keys("비디오 공간")
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간\nID : 22").is_displayed()

            self.driver.tap([(260, 644)])
            time.sleep(2)

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            videoMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 감시")
            videoMenu.click()

            videoXpath1 = "//android.view.View[@content-desc='움직임 감지']/android.widget.Switch"
            videoXpath2 = "//android.view.View[@content-desc='시야각 가림']/android.widget.Switch"
            videoXpath3 = "//android.view.View[@content-desc='IoT 접점 센서']/android.widget.Switch"

            print("----- #움직임 감지 이벤트만 설정 - 나머지 미설정 -----")
            utils.toggle_click(self, videoXpath2)
            utils.toggle_click(self, videoXpath3)

            utils.toggle_status(self, videoXpath1, videoXpath2, videoXpath3, None, "영상 감시")

            print("----- 움직임 감지 토글 버튼 확인 완료-----")

            time.sleep(1)
            print("----- #시야각 가림 이벤트만 설정 - 나머지 미설정 -----")

            utils.toggle_click(self, videoXpath1)

            utils.toggle_click(self, videoXpath2)

            utils.toggle_status(self, videoXpath1, videoXpath2, videoXpath3, None, "영상 감시")

            print("----- 시야각 가림 토글 버튼 확인 완료-----")

            time.sleep(1)
            print("----- #IoT 접점 센서 이벤트만 설정 - 나머지 미설정 -----")

            utils.toggle_click(self, videoXpath2)

            utils.toggle_click(self, videoXpath3)

            utils.toggle_status(self, videoXpath1, videoXpath2, videoXpath3, None, "영상 감시")

            print("----- IoT 접점 센서 토글 버튼 확인 완료-----")

            time.sleep(1)

            print("----- #모두 설정으로 복구 -----")

            move = self.driver.find_element(AppiumBy.XPATH, videoXpath1)
            move.click()
            time.sleep(2)

            tampering = self.driver.find_element(AppiumBy.XPATH, videoXpath2)
            tampering.click()
            time.sleep(2)

            pass
            print("DQS_T15898 영상 감시에 영상 이벤트 알람 설정 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15898 영상 감시에 영상 이벤트 알람 설정 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15899(self):
        try:
            print("DQS_T15899 영상 감시에 영상 이벤트 순서 오류 알람 설정 동작 확인")

            place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1")
            place.click()
            time.sleep(5)

            placeInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            placeInput.click()
            placeInput.send_keys("비디오 공간")
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간\nID : 22").is_displayed()

            self.driver.tap([(260, 644)])
            time.sleep(2)

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            videoMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 감시")
            videoMenu.click()

            videoXpath1 = "//android.view.View[@content-desc='내부 오류']/android.widget.Switch"
            videoXpath2 = "//android.view.View[@content-desc='연결 해제']/android.widget.Switch"
            videoXpath3 = "//android.view.View[@content-desc='디스크 공간 없음']/android.widget.Switch"

            print("----- #내부 오류 이벤트만 설정 - 나머지 미설정 -----")
            utils.toggle_click(self, videoXpath2)
            utils.toggle_click(self, videoXpath3)

            utils.toggle_status(self, videoXpath1, videoXpath2, videoXpath3, None, "영상 감시")

            print("----- 내부 오류 토글 버튼 확인 완료-----")

            time.sleep(1)
            print("----- #연결 해제 이벤트만 설정 - 나머지 미설정 -----")

            utils.toggle_click(self, videoXpath1)

            utils.toggle_click(self, videoXpath2)

            utils.toggle_status(self, videoXpath1, videoXpath2, videoXpath3, None, "영상 감시")

            print("----- 연결 해제 토글 버튼 확인 완료-----")

            time.sleep(1)
            print("----- #디스크 공간 없음 이벤트만 설정 - 나머지 미설정 -----")

            utils.toggle_click(self, videoXpath2)

            utils.toggle_click(self, videoXpath3)

            utils.toggle_status(self, videoXpath1, videoXpath2, videoXpath3, None, "영상 감시")

            print("----- 디스크 공간 없음 토글 버튼 확인 완료-----")

            time.sleep(1)

            print("----- #모두 설정으로 복구 -----")

            internalError= self.driver.find_element(AppiumBy.XPATH, videoXpath1)
            internalError.click()
            time.sleep(2)

            disconnect = self.driver.find_element(AppiumBy.XPATH, videoXpath2)
            disconnect.click()
            time.sleep(2)

            pass
            print("DQS_T15899 영상 감시에 영상 이벤트 순서 오류 알람 설정 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15899 영상 감시에 영상 이벤트 순서 오류 알람 설정 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15900(self):
        try:
            print("DQS_T15900 영상 감시에 IoT 이벤트 순서 오류 알람 설정 동작 확인")

            place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1")
            place.click()
            time.sleep(5)

            placeInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            placeInput.click()
            placeInput.send_keys("비디오 공간")
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간\nID : 22").is_displayed()

            self.driver.tap([(260, 644)])
            time.sleep(2)

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            videoMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 감시")
            videoMenu.click()

            videoXpath1 = "//android.view.View[@content-desc='센서 분리']/android.widget.Switch"
            videoXpath2 = "//android.view.View[@content-desc='배터리 얼마남지 않음']/android.widget.Switch"

            print("----- #센서 분리 이벤트만 설정 - 나머지 미설정 -----")
            utils.toggle_click(self, videoXpath2)

            utils.toggle_status(self, videoXpath1, videoXpath2, None, None, "영상 감시")

            print("----- 센서 분리 토글 버튼 확인 완료-----")

            time.sleep(1)
            print("----- #배터리 얼마남지 않음 이벤트만 설정 - 나머지 미설정 -----")

            utils.toggle_click(self, videoXpath1)

            utils.toggle_click(self, videoXpath2)

            utils.toggle_status(self, videoXpath1, videoXpath2, None, None, "영상 감시")

            print("----- 베터리 얼마남지 않음 토글 버튼 확인 완료-----")


            time.sleep(1)

            print("----- #모두 설정으로 복구 -----")

            sersor = self.driver.find_element(AppiumBy.XPATH, videoXpath1)
            sersor.click()
            time.sleep(2)

            pass
            print("DQS_T15900 영상 감시에 IoT 이벤트 순서 오류 알람 설정 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15900 영상 감시에 IoT 이벤트 순서 오류 알람 설정 동작 확인 | Failed")
            print(str(e))
            self.fail()

class adminMenu_Mobile(unittest.TestCase):

    def setUp(self):
        self.driver = AppiumConfig.get_driver()
        self.driver.implicitly_wait(10)

        utils.mobile_login(self, "01020905304", "Kjstar36!!")
        time.sleep(2)

        place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1")
        if place.get_attribute("content-desc") != "Visitor Place1":
            # "Visitor Place1"이 아닐 경우 다시 찾기
            self.driver.tap([(125, 277)])
            time.sleep(2)

            placeInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            placeInput.click()
            placeInput.send_keys("Visitor Place1")
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1\nID : 240").is_displayed()
            self.driver.tap([(260, 644)])
            time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_DQS_T15901(self):
        try:
            print("DQS_T15901 모바일로 로그인 시 관리자 초대 메뉴 UI 출력 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            # 관리자 초대 메뉴 UI 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "주소록").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 리스트").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정").is_displayed()

            #Visitor Place1 관리자 계정 확인
            #Email 계정 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 관리자 1번입니다").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kj*******@suprema.co.kr").is_displayed()

            #Mobile 계정 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "010****5304").is_displayed()

            pass
            print("DQS_T15901 모바일로 로그인 시 관리자 초대 메뉴 UI 출력 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15901 모바일로 로그인 시 관리자 초대 메뉴 UI 출력 확인| Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15902(self):
        try:
            print("DQS_T15902 모바일로 로그인 시 관리자 초대에 직접 입력 메뉴 UI 출력 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력")
            manualInput.click()

            # 직접 입력 UI 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대 받는 사람").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+82").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 처리 방침 안내").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기").is_displayed()

            # 초대하기 버튼 클릭 - 비활성화 확인
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            is_enabled = inviteBtn.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "초대하기 버튼 비활성화")

            # 지역 코드 확인
            countryNum = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+82")
            countryNum.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "지역 코드").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "대한민국\n+82").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81").is_displayed()

            start_x1 = 539
            start_y1 = 223
            end_x1 = 539
            end_y1 = 932
            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)

            personalData = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 처리 방침 안내")
            personalData.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대 기능 개인 정보 처리 방침 안내").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대 기능 사용시 개인 정보의 보관 및 삭제 등 법규에 따른 관리 책임은 고객(이하 관리자)에게 있습니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대에 응하지 않은 사용자 정보의 보관 및 삭제는 관리자가 진행해야 합니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "따라서 관리자는 사용자 개인의 요청이 있을 경우 혹은 해당 개인 정보가 더 이상 필요치 않을 경우 삭제를 진행해야 하며 외부에 노출되지 않도록 관리 해야 합니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인").is_displayed()

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()

            pass
            print("DQS_T15902 모바일로 로그인 시 관리자 초대에 직접 입력 메뉴 UI 출력 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15902 모바일로 로그인 시 관리자 초대에 직접 입력 메뉴 UI 출력 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15903(self):
        try:
            print("DQS_T15903 모바일 로그인 환경에서 관리자 초대에 직접 입력 설정 Validation 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력")
            manualInput.click()

            # 지역 코드 유효성 체크
            countryNum = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+82")
            countryNum.click()

            st1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st1.click()
            st1.send_keys("123456")
            searchBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            searchBtn.click()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "대한민국\n+82").is_displayed()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81").is_displayed()
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "지역코드가 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            st1.clear()

            st2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st2.click()
            st2.send_keys("Korea")
            searchBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            searchBtn.click()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "대한민국\n+82").is_displayed()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81").is_displayed()
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "지역코드가 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            st2.clear()

            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st3.click()
            st3.send_keys("!@#$")
            searchBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            searchBtn.click()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "대한민국\n+82").is_displayed()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81").is_displayed()
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "지역코드가 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            st3.clear()

            st4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st4.click()
            st4.send_keys("가나다")
            searchBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            searchBtn.click()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "대한민국\n+82").is_displayed()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81").is_displayed()
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "지역코드가 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            st4.clear()

            st5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st5.click()
            st5.send_keys("+81")
            searchBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            searchBtn.click()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "대한민국\n+82").is_displayed()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81").is_displayed()
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "지역코드가 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            st5.clear()

            st6 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st6.click()
            st6.send_keys("ㄷ")
            searchBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            searchBtn.click()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "대한민국\n+82").is_displayed()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81").is_displayed()
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "지역코드가 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            st6.clear()

            st7 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st7.click()
            st7.send_keys("ㅇ")
            searchBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            searchBtn.click()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "대한민국\n+82").is_displayed()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81").is_displayed()
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "지역코드가 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            st7.clear()

            st8 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st8.click()
            st8.send_keys("대한")
            searchBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            searchBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "대한민국\n+82").is_displayed()

            st8.clear()

            st9 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st9.click()
            st9.send_keys("일")
            searchBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            searchBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81").is_displayed()

            seleteCountry = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81")
            seleteCountry.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+81").is_displayed()

            #전화번호 유효성 체크
            phoneInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput1.click()
            text_to_input = "ABCDEFG"
            er1 = phoneInput1.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er1)
            phoneInput1.clear()

            phoneInput2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput2.click()
            text_to_input = "abcdefg"
            er2 = phoneInput2.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er2)
            phoneInput2.clear()

            phoneInput3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput3.click()
            text_to_input = "가나다라마바사"
            er3 = phoneInput3.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er3)
            phoneInput3.clear()

            phoneInput4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput4.click()
            text_to_input = "!@#$%^&*()"
            er4 = phoneInput4.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er4)
            phoneInput4.clear()

            phoneInput5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput5.click()
            phoneInput5.send_keys("012345678")
            time.sleep(1)

            # 초대하기 버튼 클릭 - 비활성화 확인
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            is_enabled = inviteBtn.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "초대하기 버튼 비활성화")

            phoneInput5.clear()
            time.sleep(1)

            phoneInput6 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput6.click()
            phoneInput6.send_keys("012345678901234567890123456789")
            time.sleep(1)

            # 초대하기 버튼 클릭 - 비활성화 확인
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            is_enabled = inviteBtn.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "초대하기 버튼 비활성화")

            phoneInput6.clear()
            time.sleep(1)

            phoneInput7 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput7.click()
            phoneInput7.send_keys("012345678901")
            time.sleep(1)

            # 초대하기 버튼 클릭 - 비활성화 확인
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            is_enabled = inviteBtn.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "초대하기 버튼 비활성화")

            phoneInput7.clear()
            time.sleep(1)

            phoneInput8 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput8.click()
            phoneInput8.send_keys("01023235454")
            time.sleep(1)

            # 초대하기 버튼 클릭 - 활성화 확인(초대 동작 확인 및 리스트 '회원가입 전' 출력 확인)
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입 전").is_displayed()

            #초대한 관리자 삭제
            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            adminDelete = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]") #3번째 등록된 관리자 삭제
            adminDelete.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(3)

            pass
            print("DQS_T15903 모바일 로그인 환경에서 관리자 초대에 직접 입력 설정 Validation 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15903 모바일 로그인 환경에서 관리자 초대에 직접 입력 설정 Validation 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15904(self):
        try:
            print("DQS_T15904 모바일 로그인 환경에서 직접 입력으로 관리자 초대 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력")
            manualInput.click()

            #관리자 초대
            phoneInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput1.click()
            phoneInput1.send_keys("01000011111")
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            #최초 회원가입 시 '회원가입 전'으로 출력 되지만 회원가입 후 확인하는 케이스를 진행할 수 없어 이미 가입된 관리자로 테스트 진행함
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "테스트1").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "010****1111").is_displayed()

            #테스트한 관리자 삭제
            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            adminDelete1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]") #3번째 등록된 관리자 삭제
            adminDelete1.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(3)

            pass
            print("DQS_T15904 모바일 로그인 환경에서 직접 입력으로 관리자 초대 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15904 모바일 로그인 환경에서 직접 입력으로 관리자 초대 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T888888_1(self):
        try:
            print("DQS_T888888_1 모바일 로그인 환경에서 이미 초대된 휴대폰 번호로 관리자 초대 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력")
            manualInput.click()

            #관리자 초대 - 로그인 중인 계정
            phoneInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput1.click()
            phoneInput1.send_keys("01020905304")
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            #관리자 초대 오류 팝업 발생
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대 오류").is_displayed()
            adminInvite_Error1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='이미 해당 관리자가 등록되어 있습니다. \np1003']")
            errorDesc1 = adminInvite_Error1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {errorDesc1}")
            self.assertEqual(errorDesc1, "이미 해당 관리자가 등록되어 있습니다. \np1003")
            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            phoneInput1.clear()
            time.sleep(1)

            #관리자 초대
            phoneInput2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput2.click()
            phoneInput2.send_keys("01000011111")
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            #관리자 초대 - 초대한 계정으로 초대 시도
            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력")
            manualInput.click()

            phoneInput3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput3.click()
            phoneInput3.send_keys("01000011111")
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            #관리자 초대 오류 팝업 발생
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대 오류").is_displayed()
            adminInvite_Error2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='이미 해당 관리자가 등록되어 있습니다. \np1003']")
            errorDesc2 = adminInvite_Error2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {errorDesc2}")
            self.assertEqual(errorDesc2, "이미 해당 관리자가 등록되어 있습니다. \np1003")
            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            for _ in range(2):
                self.driver.back()
            time.sleep(1)

            #테스트한 관리자 삭제
            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            adminDelete1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]") #2번째 등록된 관리자 삭제
            adminDelete1.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(3)

            pass
            print("DQS_T888888_1 모바일 로그인 환경에서 이미 초대된 휴대폰 번호로 관리자 초대 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T888888_1 모바일 로그인 환경에서 이미 초대된 휴대폰 번호로 관리자 초대 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15905(self):
        try:
            print("DQS_T15905 모바일 로그인 환경에서 직접 입력으로 다수의 관리자 초대 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력")
            manualInput.click()

            #관리자 초대
            phoneInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput1.click()
            phoneInput1.send_keys("01000088888")
            time.sleep(1)

            addBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn.click()

            phoneInput2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[1]/android.widget.EditText[2]")
            phoneInput2.click()
            phoneInput2.send_keys("01023235455")
            time.sleep(1)

            deleteAdmin = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[1]/android.widget.ImageView[3]")
            deleteAdmin.click()
            time.sleep(1)

            addBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn.click()

            phoneInput3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[1]/android.widget.EditText[2]")
            phoneInput3.click()
            phoneInput3.send_keys("01023235455")
            time.sleep(1)

            addBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn.click()

            phoneInput4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[3]")
            phoneInput4.click()
            phoneInput4.send_keys("01023235456")
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            #최초 회원가입 시 '회원가입 전'으로 출력 되지만 회원가입 후 확인하는 케이스를 진행할 수 없어 이미 가입된 관리자로 테스트 진행함
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_sub").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "010****8888").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='회원가입 전'])[1]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='회원가입 전'])[2]").is_displayed()

            #회원가입 전 관리자 삭제
            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            adminDelete1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[4]") #4번째 등록된 관리자 삭제
            adminDelete1.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(1)

            adminDelete2 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[3]") #3번째 등록된 관리자 삭제
            adminDelete2.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(1)

            adminDelete3 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]") #2번째 등록된 관리자 삭제
            adminDelete3.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(1)

            pass
            print("DQS_T15905 모바일 로그인 환경에서 직접 입력으로 다수의 관리자 초대 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15905 모바일 로그인 환경에서 직접 입력으로 다수의 관리자 초대 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T888888_2(self):
        try:
            print("DQS_T888888_2 모바일 로그인 환경에서 다수의 모바일 관리자 초대 시 이미 초대된 모바일로 관리자 초대 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력")
            manualInput.click()

            #관리자 초대 - 초대 안된 계정
            phoneInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput1.click()
            phoneInput1.send_keys("01023235457")
            time.sleep(1)

            addBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn.click()

            phoneInput2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[1]/android.widget.EditText[2]")
            phoneInput2.click()
            phoneInput2.send_keys("01020905304")
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            #관리자 초대 오류 팝업 발생
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대 오류").is_displayed()
            adminInvite_Error1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='이미 해당 관리자가 등록되어 있습니다. \np1003']")
            errorDesc1 = adminInvite_Error1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {errorDesc1}")
            self.assertEqual(errorDesc1, "이미 해당 관리자가 등록되어 있습니다. \np1003")
            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            #테스트한 관리자 삭제
            for _ in range(2):
                self.driver.back()
            time.sleep(1)

            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            adminDelete1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]") #2번째 등록된 관리자 삭제
            adminDelete1.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(3)

            pass
            print("DQS_T888888_2 모바일 로그인 환경에서 다수의 모바일 관리자 초대 시 이미 초대된 모바일로 관리자 초대 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T888888_2 모바일 로그인 환경에서 다수의 모바일 관리자 초대 시 이미 초대된 모바일로 관리자 초대 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T888888_3(self):
        try:
            print("DQS_T888888_3 모바일 로그인 환경에서 다수의 휴대폰 번호 관리자 초대 시 동일한 휴대폰 번호로 관리자 초대 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력")
            manualInput.click()

            #관리자 초대 - 초대 안된 계정
            phoneInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput1.click()
            phoneInput1.send_keys("01023235451")
            time.sleep(1)

            addBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn.click()

            phoneInput2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[1]/android.widget.EditText[2]")
            phoneInput2.click()
            phoneInput2.send_keys("01023235452")
            time.sleep(1)

            addBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn.click()

            phoneInput3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[3]")
            phoneInput3.click()
            phoneInput3.send_keys("01023235451")
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            #오류 팝업 발생
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "에러").is_displayed()
            adminInvite_Error = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='중복된 항목이 있습니다.']")
            errorDesc = adminInvite_Error.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {errorDesc}")
            self.assertEqual(errorDesc, "중복된 항목이 있습니다.")
            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            pass
            print("DQS_T888888_3 모바일 로그인 환경에서 다수의 휴대폰 번호 관리자 초대 시 동일한 휴대폰 번호로 관리자 초대 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T888888_3 모바일 로그인 환경에서 다수의 휴대폰 번호 관리자 초대 시 동일한 휴대폰 번호로 관리자 초대 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15906(self):
        try:
            print("DQS_T15906 관리자 초대에 주소록 메뉴 UI 출력 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            seleteAdress = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "주소록")
            seleteAdress.click()

            # 주소록 UI 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "주소록").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대 받는 사람").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 처리 방침 안내").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기").is_displayed()

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "주소록").is_displayed() #버튼 비활성화 확인 - 주소록 화면 유지 확인

            personalData = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 처리 방침 안내")
            personalData.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대 기능 개인 정보 처리 방침 안내").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대 기능 사용시 개인 정보의 보관 및 삭제 등 법규에 따른 관리 책임은 고객(이하 관리자)에게 있습니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대에 응하지 않은 사용자 정보의 보관 및 삭제는 관리자가 진행해야 합니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "따라서 관리자는 사용자 개인의 요청이 있을 경우 혹은 해당 개인 정보가 더 이상 필요치 않을 경우 삭제를 진행해야 하며 외부에 노출되지 않도록 관리 해야 합니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인").is_displayed()

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            pass
            print("DQS_T15906 관리자 초대에 주소록 메뉴 UI 출력 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15906 관리자 초대에 주소록 메뉴 UI 출력 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15907(self):
        try:
            print("DQS_T15907 모바일 로그인 환경에서 주소록으로 관리자 초대 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            seleteAdress = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "주소록")
            seleteAdress.click()

            #관리자 초대
            addBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn.click()
            time.sleep(1)

            #사용자1 - 01000044444
            seleteAdmin1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자1")
            seleteAdmin1.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@text='01000044444']").is_displayed()

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자1").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "010****4444").is_displayed()

            #테스트한 관리자 삭제
            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            adminDelete1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]") #2번째 등록된 관리자 삭제
            adminDelete1.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(3)

            pass
            print("DQS_T15907 모바일 로그인 환경에서 주소록으로 관리자 초대 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15907 모바일 로그인 환경에서 주소록으로 관리자 초대 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15908(self):
        try:
            print("DQS_T15908 모바일 로그인 환경에서 주소록으로 다수의 관리자 초대 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            seleteAdress = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "주소록")
            seleteAdress.click()

            #관리자 초대
            addBtn1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn1.click()
            time.sleep(1)

            seleteAdmin1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자1")
            seleteAdmin1.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@text='01000044444']").is_displayed()

            addBtn2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn2.click()
            time.sleep(1)

            seleteAdmin2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자A")
            seleteAdmin2.click()
            time.sleep(1)

            #2번째 관리자 삭제
            deleteAdmin = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[1]/android.widget.ImageView[4]")
            deleteAdmin.click()

            addBtn2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn2.click()
            time.sleep(1)

            seleteAdmin3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자A")
            seleteAdmin3.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@text='01035478960']").is_displayed()

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            #최초 회원가입 시 '회원가입 전'으로 출력 되지만 회원가입 후 확인하는 케이스를 진행할 수 없어 이미 가입된 관리자로 테스트 진행함
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자1").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "010****4444").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입 전").is_displayed()

            #테스트한 관리자 삭제
            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            adminDelete1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[3]") #3번째 등록된 관리자 삭제
            adminDelete1.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(1)

            adminDelete1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]") #2번째 등록된 관리자 삭제
            adminDelete1.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(1)

            pass
            print("DQS_T15908 모바일 로그인 환경에서 주소록으로 다수의 관리자 초대 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15908 모바일 로그인 환경에서 주소록으로 다수의 관리자 초대 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15909(self):
        try:
            print("DQS_T15909 메인 관리자 계정 접속된 경우 초대된 관리자 수정 기능 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[1]").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "나가기").is_displayed()

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력")
            manualInput.click()

            #관리자 초대
            phoneInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput1.click()
            phoneInput1.send_keys("01000099999") # name : e2e_main
            time.sleep(1)

            addBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn.click()

            phoneInput2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[1]/android.widget.EditText[2]")
            phoneInput2.click()
            phoneInput2.send_keys("01000088888") # name : e2e_sub
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(3)

            #메인 관리자 권한 이관 동작
            permission = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='권한 이관'])[1]")
            permission.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "권한 이행").is_displayed()
            permission_Msg = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "메인 관리자 권한을 변경 하시겠습니까?")
            contentDesc1 = permission_Msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "메인 관리자 권한을 변경 하시겠습니까?")

            cancelBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            cancelBtn.click()

            permission = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='권한 이관'])[1]")
            permission.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(1)

            # 메인 관리자 변경 확인 - 프로필 이미지의 왕관 표시 확인
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='관리자 리스트']/android.view.View[4]/android.widget.ImageView[6]").is_displayed()

            # 메인 관리자 삭제
            adminDelete1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]") #2번째 등록된 관리자 삭제
            adminDelete1.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "내보내기").is_displayed()
            delete_Msg1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "해당 관리자를 공간에서 내보내시겠습니까?")
            contentDesc2 = delete_Msg1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "해당 관리자를 공간에서 내보내시겠습니까?")

            cancelBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            cancelBtn.click()

            adminDelete2 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]") #2번째 등록된 관리자 삭제
            adminDelete2.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(2)

            # 서브 관리자 삭제
            adminDelete3 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]") #2번째 등록된 관리자 삭제
            adminDelete3.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "내보내기").is_displayed()
            delete_Msg2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "해당 관리자를 공간에서 내보내시겠습니까?")
            contentDesc3 = delete_Msg2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc3}")
            self.assertEqual(contentDesc3, "해당 관리자를 공간에서 내보내시겠습니까?")

            cancelBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            cancelBtn.click()

            adminDelete2 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]") #2번째 등록된 관리자 삭제
            adminDelete2.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(3)

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")

            try:
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[1]").is_displayed()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "나가기").is_displayed()
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "나가기 버튼 및 삭제 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            pass
            print("DQS_T15909 메인 관리자 계정 접속된 경우 초대된 관리자 수정 기능 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15909 메인 관리자 계정 접속된 경우 초대된 관리자 수정 기능 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15910(self):
        try:
            print("DQS_T15910 서브 관리자 계정 접속된 경우 초대된 관리자 수정 기능 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력")
            manualInput.click()

            #관리자 초대
            phoneInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput.click()
            phoneInput.send_keys("01000088888") # name : e2e_sub
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(1)

            for _ in range(2):
                self.driver.back()
                time.sleep(1)

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            logout_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃")
            logout_button.click()

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            utils.mobile_login(self, "01000088888", "Kjstar36!!")
            time.sleep(2)

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            # 나가기 버튼 출력 확인 / 삭제 버튼 미출력 확인
            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "나가기").is_displayed()

            try:
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[1]").is_displayed()
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]").is_displayed()
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "삭제 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력")
            manualInput.click()

            #관리자 초대
            phoneInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput.click()
            phoneInput.send_keys("01000022222") # name : test2
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            #서브 관리자 삭제 동작
            adminDelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "삭제") #본인 계정외 서브 관리자만 삭제버튼 출력
            adminDelete.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "내보내기").is_displayed()
            delete_Msg = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "해당 관리자를 공간에서 내보내시겠습니까?")
            contentDesc = delete_Msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "해당 관리자를 공간에서 내보내시겠습니까?")

            cancelBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            cancelBtn.click()

            adminDelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "삭제") #본인 계정외 서브 관리자만 삭제버튼 출력
            adminDelete.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(1)

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "나가기")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "나가기 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            # 테스트 환경 복구 - 서브 관리자 나가기
            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            outBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "나가기")
            outBtn.click()

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            pass
            print("DQS_T15910 서브 관리자 계정 접속된 경우 초대된 관리자 수정 기능 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15910 서브 관리자 계정 접속된 경우 초대된 관리자 수정 기능 확인 | Failed")
            print(str(e))
            self.fail()

class adminMenu_Email(unittest.TestCase):

    def setUp(self):
        self.driver = AppiumConfig.get_driver()
        self.driver.implicitly_wait(10)

        utils.email_login(self, "kjjung+p1@suprema.co.kr", "Kjstar36!!")
        time.sleep(3)

        place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1")
        if place.get_attribute("content-desc") != "Visitor Place1":
            # "Visitor Place1"이 아닐 경우 다시 찾기
            self.driver.tap([(125, 277)])
            time.sleep(2)

            placeInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            placeInput.click()
            placeInput.send_keys("Visitor Place1")
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1\nID : 240").is_displayed()
            self.driver.tap([(260, 644)])
            time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_DQS_T888888_4(self):
        try:
            print("DQS_T888888_4 이메일로 로그인 시 관리자 초대 메뉴 UI 출력 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            # 관리자 초대 메뉴 UI 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 리스트").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정").is_displayed()

            #Visitor Place1 관리자 계정 확인
            #Email 계정 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 관리자 1번입니다").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kj*******@suprema.co.kr").is_displayed()

            #Mobile 계정 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "010****5304").is_displayed()

            pass
            print("DQS_T888888_4 이메일로 로그인 시 관리자 초대 메뉴 UI 출력 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T888888_4 이메일로 로그인 시 관리자 초대 메뉴 UI 출력 확인| Failed")
            print(str(e))
            self.fail()

    def test_DQS_T888888_5(self):
        try:
            print("DQS_T888888_5 이메일 로그인 환경에서 관리자 초대에 + 이메일 메뉴 UI 출력 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일")
            manualInput.click()

            # 직접 입력 UI 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대 받는 사람").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 처리 방침 안내").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기").is_displayed()

            # 초대하기 버튼 클릭 - 비활성화 확인
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            is_enabled = inviteBtn.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "초대하기 버튼 비활성화")

            personalData = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 처리 방침 안내")
            personalData.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대 기능 개인 정보 처리 방침 안내").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대 기능 사용시 개인 정보의 보관 및 삭제 등 법규에 따른 관리 책임은 고객(이하 관리자)에게 있습니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대에 응하지 않은 사용자 정보의 보관 및 삭제는 관리자가 진행해야 합니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "따라서 관리자는 사용자 개인의 요청이 있을 경우 혹은 해당 개인 정보가 더 이상 필요치 않을 경우 삭제를 진행해야 하며 외부에 노출되지 않도록 관리 해야 합니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인").is_displayed()

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()

            pass
            print("DQS_T888888_5 이메일 로그인 환경에서 관리자 초대에 + 이메일 메뉴 UI 출력 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T888888_5 이메일 로그인 환경에서 관리자 초대에 + 이메일 메뉴 UI 출력 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T888888_6(self):
        try:
            print("DQS_T888888_6 이메일 로그인 환경에서 관리자 초대에 이메일 입력 Validation 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일")
            manualInput.click()

            st1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st1.click()
            st1.send_keys("가나다@suprema.co.kr")

            # 초대하기 버튼 클릭 - 비활성화 확인
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            is_enabled = inviteBtn.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "초대하기 버튼 비활성화")

            st1.clear()
            time.sleep(1)

            st2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st2.click()
            st2.send_keys("123456789")

            # 초대하기 버튼 클릭 - 비활성화 확인
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            is_enabled = inviteBtn.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "초대하기 버튼 비활성화")

            st2.clear()
            time.sleep(1)

            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st3.click()
            st3.send_keys("kjjung@suprema.")

            # 초대하기 버튼 클릭 - 비활성화 확인
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            is_enabled = inviteBtn.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "초대하기 버튼 비활성화")

            st3.clear()
            time.sleep(1)

            st4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st4.click()
            st4.send_keys("kjjung@suprema.co.kr.")

            # 초대하기 버튼 클릭 - 비활성화 확인
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            is_enabled = inviteBtn.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "초대하기 버튼 비활성화")

            st4.clear()
            time.sleep(1)

            st5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st5.click()
            st5.send_keys("kjjung@suprema.co.kr")

            # 초대하기 버튼 클릭 - 비활성화 확인
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            is_enabled = inviteBtn.get_attribute("enabled")
            self.assertEqual(is_enabled, "true", "초대하기 버튼 비활성화")

            st5.clear()
            time.sleep(1)

            pass
            print("DQS_T888888_6 이메일 로그인 환경에서 관리자 초대에 이메일 입력 Validation 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T888888_6 이메일 로그인 환경에서 관리자 초대에 이메일 입력 Validation 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T888888_7(self):
        try:
            print("DQS_T888888_7 이메일 로그인 환경에서 이메일로 관리자 초대 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일")
            manualInput.click()

            #관리자 초대
            emailInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            emailInput1.click()
            emailInput1.send_keys("kjjung+p2@suprema.co.kr")
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            #최초 회원가입 시 '회원가입 전'으로 출력 되지만 회원가입 후 확인하는 케이스를 진행할 수 없어 이미 가입된 관리자로 테스트 진행함
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 관리자 2번").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kj*******@suprema.co.kr").is_displayed()

            #테스트한 관리자 삭제
            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            adminDelete1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]") #테스트한 등록된 관리자 삭제
            adminDelete1.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(3)

            pass
            print("DQS_T888888_7 이메일 로그인 환경에서 이메일로 관리자 초대 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T888888_7 이메일 로그인 환경에서 이메일로 관리자 초대 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T888888_8(self):
        try:
            print("DQS_T888888_8 이메일 로그인 환경에서 이메일 입력으로 다수의 관리자 초대 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일")
            manualInput.click()

            #관리자 초대 - 1번째
            emailInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            emailInput1.click()
            emailInput1.send_keys("kjjung+p2@suprema.co.kr")
            time.sleep(1)

            #관리자 초대 - 2번째
            addBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn.click()

            emailInput2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[1]/android.widget.EditText[2]")
            emailInput2.click()
            emailInput2.send_keys("kjjung+t100@suprema.co.kr")
            time.sleep(1)

            deleteAdmin = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[1]/android.widget.ImageView[1]")
            deleteAdmin.click()
            time.sleep(1)

            addBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn.click()

            emailInput3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[1]/android.widget.EditText[2]")
            emailInput3.click()
            emailInput3.send_keys("kjjung+t100@suprema.co.kr")
            time.sleep(1)

            addBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn.click()

            emailInput4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[3]")
            emailInput4.click()
            emailInput4.send_keys("kjjung+t101@suprema.co.kr")
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            #최초 회원가입 시 '회원가입 전'으로 출력 되지만 회원가입 후 확인하는 케이스를 진행할 수 없어 이미 가입된 관리자로 테스트 진행함
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 관리자 2번").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kj*******@suprema.co.kr").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='회원가입 전'])[1]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='회원가입 전'])[2]").is_displayed()

            #회원가입 전 관리자 삭제
            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            adminDelete1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[4]") #4번째 등록된 관리자 삭제
            adminDelete1.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(1)

            adminDelete2 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[3]") #3번째 등록된 관리자 삭제
            adminDelete2.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(1)

            adminDelete3 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]") #2번째 등록된 관리자 삭제
            adminDelete3.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(1)

            pass
            print("DQS_T888888_8 이메일 로그인 환경에서 이메일 입력으로 다수의 관리자 초대 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T888888_8 이메일 로그인 환경에서 이메일 입력으로 다수의 관리자 초대 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T888888_9(self):
        try:
            print("DQS_T888888_9 이메일 로그인 환경에서 이미 초대된 회원가입 완료된 이메일 주소로 관리자 초대 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일")
            manualInput.click()

            #관리자 초대 - 이미 초대된 계정
            emailInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            emailInput1.click()
            emailInput1.send_keys("kjjung+p1@suprema.co.kr")
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            #관리자 초대 오류 팝업 발생
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대 오류").is_displayed()
            adminInvite_Error1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='이미 해당 관리자가 등록되어 있습니다. \np1003']")
            errorDesc1 = adminInvite_Error1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {errorDesc1}")
            self.assertEqual(errorDesc1, "이미 해당 관리자가 등록되어 있습니다. \np1003")
            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            pass
            print("DQS_T888888_9 이메일 로그인 환경에서 이미 초대된 회원가입 완료된 이메일 주소로 관리자 초대 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T888888_9 이메일 로그인 환경에서 이미 초대된 회원가입 완료된 이메일 주소로 관리자 초대 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T888888_10(self):
        try:
            print("DQS_T888888_10 이메일 로그인 환경에서 이미 초대된 회원가입 전 이메일 주소로 관리자 초대 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일")
            manualInput.click()

            #관리자 초대 - 회원가입 안된 이메일 초대
            emailInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            emailInput1.click()
            emailInput1.send_keys("kjjung+t100@suprema.co.kr")
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일")
            manualInput.click()

            #관리자 초대 - 초대된 계정과 동일하게 이메일 입력
            emailInput2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            emailInput2.click()
            emailInput2.send_keys("kjjung+t100@suprema.co.kr")
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            # 지원하지 않음 오류 팝업 발생
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "지원하지 않음").is_displayed()
            adminInvite_Error1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='지원 하지 않음\ne1002']")
            errorDesc = adminInvite_Error1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {errorDesc}")
            self.assertEqual(errorDesc, "지원 하지 않음\ne1002")
            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            #테스트한 관리자 삭제
            for _ in range(2):
                self.driver.back()
                time.sleep(1)

            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            adminDelete1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]") #2번째 등록된 관리자 삭제
            adminDelete1.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(3)

            pass
            print("DQS_T888888_10 이메일 로그인 환경에서 이미 초대된 회원가입 전 이메일 주소로 관리자 초대 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T888888_10 이메일 로그인 환경에서 이미 초대된 회원가입 전 이메일 주소로 관리자 초대 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T888888_11(self):
        try:
            print("DQS_T888888_11 이메일 로그인 환경에서 다수의 이메일 관리자 초대 시 이미 초대된 이메일로 관리자 초대 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일")
            manualInput.click()

            #관리자 초대 - 이미 초대된 계정
            emailInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            emailInput1.click()
            emailInput1.send_keys("kjjung+t100@suprema.co.kr")
            time.sleep(1)

            addBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn.click()

            emailInput2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[1]/android.widget.EditText[2]")
            emailInput2.click()
            emailInput2.send_keys("kjjung+p1@suprema.co.kr")
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            #관리자 초대 오류 팝업 발생
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대 오류").is_displayed()
            adminInvite_Error1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='이미 해당 관리자가 등록되어 있습니다. \np1003']")
            errorDesc1 = adminInvite_Error1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {errorDesc1}")
            self.assertEqual(errorDesc1, "이미 해당 관리자가 등록되어 있습니다. \np1003")
            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            for _ in range(2):
                self.driver.back()
                time.sleep(1)

            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            adminDelete1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]") #2번째 등록된 관리자 삭제
            adminDelete1.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(1)

            pass
            print("DQS_T888888_11 이메일 로그인 환경에서 다수의 이메일 관리자 초대 시 이미 초대된 이메일로 관리자 초대 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T888888_11 이메일 로그인 환경에서 다수의 이메일 관리자 초대 시 이미 초대된 이메일로 관리자 초대 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T888888_12(self):
        try:
            print("DQS_T888888_12 이메일 로그인 환경에서 다수의 이메일 관리자 초대 시 동일한 이메일로 관리자 초대 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일")
            manualInput.click()

            #관리자 초대 - 회원가입 안된 이메일 초대
            emailInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            emailInput1.click()
            emailInput1.send_keys("kjjung+t100@suprema.co.kr")
            time.sleep(1)

            addBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn.click()

            emailInput2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[1]/android.widget.EditText[2]")
            emailInput2.click()
            emailInput2.send_keys("kjjung+t101@suprema.co.kr")
            time.sleep(1)

            addBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn.click()

            emailInput3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[3]")
            emailInput3.click()
            emailInput3.send_keys("kjjung+t100@suprema.co.kr")
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            #오류 팝업 발생
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "에러").is_displayed()
            adminInvite_Error = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='중복된 항목이 있습니다.']")
            errorDesc = adminInvite_Error.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {errorDesc}")
            self.assertEqual(errorDesc, "중복된 항목이 있습니다.")
            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            pass
            print("DQS_T888888_12 이메일 로그인 환경에서 다수의 이메일 관리자 초대 시 동일한 이메일로 관리자 초대 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T888888_12 이메일 로그인 환경에서 다수의 이메일 관리자 초대 시 동일한 이메일로 관리자 초대 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T888888_13(self):
        try:
            print("DQS_T888888_13 이메일 로그인 환경에서 브랜치, 대리점, 공간 그룹 계정으로 관리자 초대 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            #관리자 초대 - 브랜치 관리자
            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일")
            manualInput.click()

            emailInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            emailInput1.click()
            emailInput1.send_keys("kjjung+ba@suprema.co.kr")
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "브랜치 관리자").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='kj*******@suprema.co.kr'])[2]").is_displayed()

            #관리자 초대 - 대리점 관리자
            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일")
            manualInput.click()

            emailInput2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            emailInput2.click()
            emailInput2.send_keys("kjjung+dist1@suprema.co.kr")
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "대리점 관리자1").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kj**********@suprema.co.kr").is_displayed()

            #관리자 초대 - 공간 그룹 관리자
            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일")
            manualInput.click()

            emailInput2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            emailInput2.click()
            emailInput2.send_keys("kjjung+pga@suprema.co.kr")
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "PGA").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kj********@suprema.co.kr").is_displayed()

            #테스트 한 관리자 삭제
            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            deleteAdmin1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[4]") #공간 그룹 계정 삭제
            deleteAdmin1.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(1)

            deleteAdmin2 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[3]") #대리점 계정 삭제
            deleteAdmin2.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(1)

            deleteAdmin3 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]") #브랜치 계정 삭제
            deleteAdmin3.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(1)

            pass
            print("DQS_T888888_13 이메일 로그인 환경에서 브랜치, 대리점, 공간 그룹 계정으로 관리자 초대 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T888888_13 이메일 로그인 환경에서 브랜치, 대리점, 공간 그룹 계정으로 관리자 초대 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T16932(self):
        try:
            print("DQS_T16932 공간에 메인 관리자 1명 있을 경우 나가기 동작 확인")

            utils.placeInviteEmail(self, "37", "kjjung+p2@suprema.co.kr", "MASTER")
            time.sleep(2)

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            logout_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃")
            logout_button.click()

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            utils.email_login(self, "kjjung+p2@suprema.co.kr", "Kjstar36!!") #해당 계정 2개의 공간 존재
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "메인관리자 1명_서브관리자 1명 공간").is_displayed()

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            # 메인 관리자 나가기 동작
            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            outBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "나가기") #메인 관리자 나가기
            outBtn.click()

            #나가기 팝업 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "나가기").is_displayed()
            adminInvite_Out = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='해당 공간에서 나가시겠습니까?']")
            contentDesc = adminInvite_Out.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "해당 공간에서 나가시겠습니까?")
            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(2)

            # 다른 공간 이동 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간").is_displayed()

            pass
            print("DQS_T16932 공간에 메인 관리자 1명 있을 경우 나가기 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T16932 공간에 메인 관리자 1명 있을 경우 나가기 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T16933(self):
        try:
            print("DQS_T16933 공간에 서브 관리자 1명 있을 경우 나가기 동작 확인")

            utils.placeInviteEmail(self, "37", "kjjung+p3@suprema.co.kr", "MANAGER")
            time.sleep(2)

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            logout_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃")
            logout_button.click()

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            utils.email_login(self, "kjjung+p3@suprema.co.kr", "Kjstar36!!") #해당 계정 1개의 공간 존재
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "메인관리자 1명_서브관리자 1명 공간").is_displayed()

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            # 서브 관리자 나가기 동작
            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            outBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "나가기") #서브 관리자 나가기
            outBtn.click()

            #나가기 팝업 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "나가기").is_displayed()
            adminInvite_Out = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='해당 공간에서 나가시겠습니까?']")
            contentDesc = adminInvite_Out.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "해당 공간에서 나가시겠습니까?")
            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(2)

            # 할당된 공간 없음 - UI 출력 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "할당된 공간이 없습니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대된 공간이 없습니다\n관리자에게 연락하여 초대 여부를 확인하세요.").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[1]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대 후에 자동으로 이동합니다.").is_displayed()

            pass
            print("DQS_T16933 공간에 서브 관리자 1명 있을 경우 나가기 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T16933 공간에 서브 관리자 1명 있을 경우 나가기 동작 확인 | Failed")
            print(str(e))
            self.fail()


if __name__ == '__main__':
    unittest.main()

