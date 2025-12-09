#import datetime
import os
import time
import unittest
from faulthandler import is_enabled

#from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
#from appium.options.android import UiAutomator2Options
from selenium.common import NoSuchElementException
#from selenium.webdriver.common.action_chains import ActionChains
#from configuration.utill import capture_screenshotTestCase 작성완료
from configuration.webDriver import AppiumConfig
#from configuration.utill import swipe_until_element_found, swipe_up, capture_screenshot, extract_verification_code
from configuration.utill import capture_screenshot
import sys
sys.path.append('../Android')
from Android import utils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


'Xpath'
NameInputBox = "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.widget.EditText[1]"
phoneInputBox = "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.widget.EditText[2]"
confirm = "확인"
cancel = "취소"
modify = "수정"
invite = "초대"
delete = "삭제"
allAgree = "약관 전체 동의"
nextBtn = "다음"
authenticationBtn = "인증요청"
" ClassName "
signUpPhoneNumber = "android.widget.EditText"


class UserMenu(unittest.TestCase):

    def setUp(self):
        self.driver = AppiumConfig.get_driver()
        self.driver.implicitly_wait(10)

        utils.mobile_login(self, "01011111111", "Kjstar36!!")

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_DQS_T7196(self):
     try:
        print("DQS_T7196 사용자 목록 UI 구조 확인")

        self.driver.tap([(967, 2060)])
        #사용자 초대 버튼 클릭
        time.sleep(1)

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 목록")
        assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='초대하기']")
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 리스트")
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "등록순")
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "정국진\n출입기간")
        # 크리덴셜 아이콘 확인
        assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='정국진\n출입기간']/android.widget.ImageView[1]")
        assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='정국진\n출입기간']/android.widget.ImageView[2]")
        assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='정국진\n출입기간']/android.widget.ImageView[3]")
        assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='정국진\n출입기간']/android.widget.ImageView[4]")

        pass
        print("DQS_T7196 사용자 목록 UI 구조 확인 | Pass")

     except Exception as e:
        capture_screenshot(self.driver, self._testMethodName)
        print("DQS_T7196 사용자 목록 UI 구조 확인 | Failed")
        print(str(e))
        self.fail()

    def test_DQS_T7649(self):
        try:
            print("DQS_T7649 사용자 출입문 권한 설정 기능 동작 확인")

            self.driver.tap([(967, 2060)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            utils.user_invite_phone(self, "e2e_Test1", "01012345678")

            user_selete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_Test1\n출입기간")
            user_selete.click()
            time.sleep(1)

            #1번째 리스트에 있는 출입문 x버튼 클릭
            door1_delete = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='출입문\nBS3_538200888\nBS3_54780678\nBS3_547838616\nXS2_543478219\nN2_800000900\nN2_538761744\nXS2_543309324\n모든 출입문은 해당 공간에 추가 혹은 삭제되는 모든 출입문 권한을 자동 반영 합니다.']/android.widget.ImageView[2]")
            door1_delete.click()
            time.sleep(1)

            # 모든 출입문이 ID로 출력되어 2번째 출입문 선택 후 출입문 삭제 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문\nBS3_54780678\nBS3_547838616\nXS2_543478219\nN2_800000900\nN2_538761744\nXS2_543309324")

            modify_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, modify)
            modify_Btn.click()
            time.sleep(1)

            user_selete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_Test1\n출입기간")
            user_selete.click()
            time.sleep(1)

            # 모든 출입문이 ID로 출력되어 2번째 출입문 선택 후 출입문 삭제 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문\nBS3_54780678\nBS3_547838616\nXS2_543478219\nN2_800000900\nN2_538761744\nXS2_543309324")

            # 테스트 복구 - 사용자 삭제
            utils.backBtn(self)

            utils.user_delete(self)

            pass
            print("DQS_T7649 사용자 출입문 권한 설정 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T7649 사용자 출입문 권한 설정 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T12217(self):
        try:
            print("DQS_T12217 사용자 출입 기간 요일별 설정 시 기능 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            utils.user_invite_phone(self, "e2e_Test1", "01012345678")

            userSelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_Test1\n출입기간")
            userSelete.click()
            time.sleep(1)

            #요일별 클릭
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\n제한없음").is_displayed()
            daySetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\n제한없음")
            daySetting.click()

            #Schedule 설정
            scheduleSelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "E2E_Schedule")
            scheduleSelete.click()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirm_Btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\nE2E_Schedule").is_displayed()

            #수정 버튼 클릭
            modify_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, modify)
            modify_Btn.click()
            time.sleep(2)

            #뒤로가기 후 사용자 상세 재 진입
            self.driver.tap([(54, 152)])
            time.sleep(1)

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            userSelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_Test1\n출입기간")
            userSelete.click()
            time.sleep(1)

            #요일별 클릭
            daySetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\nE2E_Schedule")
            daySetting.click()
            time.sleep(1)

            #Schedule 설정
            scheduleSelete1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "근무시간1")
            scheduleSelete1.click()

            # 기존 설정된 Schdeuld 재 선택
            scheduleSelete2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "E2E_Schedule")
            scheduleSelete2.click()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirm_Btn.click()

            # 수정 버튼 클릭 - 비활성화 확인
            modify_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, modify)
            is_enabled = modify_Btn.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "수정 버튼 비활성화")

            # 테스트 복구 - 사용자 삭제
            utils.backBtn(self)

            utils.user_delete(self)

            pass
            print("DQS_T12217 사용자 출입 기간 요일별 설정 시 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T12217 사용자 출입 기간 요일별 설정 시 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T12218(self):
        try:
            print("DQS_T12218 사용자 출입문 전체 삭제 시 기능 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            utils.user_invite_phone(self, "e2e_Test1", "01012345678")

            userSelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_Test1\n출입기간")
            userSelete.click()
            time.sleep(1)

            #1번째 리스트에 있는 출입문 x버튼 클릭
            door1_delete = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='출입문\nBS3_538200888\nBS3_54780678\nBS3_547838616\nXS2_543478219\nN2_800000900\nN2_538761744\nXS2_543309324\n모든 출입문은 해당 공간에 추가 혹은 삭제되는 모든 출입문 권한을 자동 반영 합니다.']/android.widget.ImageView[2]")
            door1_delete.click()
            time.sleep(0.5)

            #2번째 리스트에 있는 출입문 x버튼 클릭
            door2_delete = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='출입문\nBS3_54780678\nBS3_547838616\nXS2_543478219\nN2_800000900\nN2_538761744\nXS2_543309324']/android.widget.ImageView[2]")
            door2_delete.click()
            time.sleep(0.5)

            #3번째 리스트에 있는 출입문 x버튼 클릭
            door3_delete = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='출입문\nBS3_547838616\nXS2_543478219\nN2_800000900\nN2_538761744\nXS2_543309324']/android.widget.ImageView[2]")
            door3_delete.click()
            time.sleep(0.5)

            #4번째 리스트에 있는 출입문 x버튼 클릭
            door4_delete = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='출입문\nXS2_543478219\nN2_800000900\nN2_538761744\nXS2_543309324']/android.widget.ImageView[2]")
            door4_delete.click()
            time.sleep(0.5)

            #5번째 리스트에 있는 출입문 x버튼 클릭
            door5_delete = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='출입문\nN2_800000900\nN2_538761744\nXS2_543309324']/android.widget.ImageView[2]")
            door5_delete.click()
            time.sleep(0.5)

            #6번째 리스트에 있는 출입문 x버튼 클릭
            door6_delete = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='출입문\nN2_538761744\nXS2_543309324']/android.widget.ImageView[2]")
            door6_delete.click()
            time.sleep(0.5)

            #7번째 리스트에 있는 출입문 x버튼 클릭
            door7_delete = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='출입문\nXS2_543309324']/android.widget.ImageView[2]")
            door7_delete.click()
            time.sleep(0.5)

            # 수정 버튼 클릭 - 비활성화 확인
            modify_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, modify)
            is_enabled = modify_Btn.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "수정 버튼 비활성화")

            # 테스트 복구 - 사용자 삭제
            utils.backBtn(self)

            utils.user_delete(self)

            pass
            print("DQS_T12218 사용자 출입문 전체 삭제 시 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T12218 사용자 출입문 전체 삭제 시 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T12231(self):
        try:
            print("DQS_T12231 동일한 이름 및 휴대폰번호로 사용자 초대 시 실패 케이스 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            utils.user_invite_phone(self, "e2e_Test1", "01012345678")

            #사용자 초대화면 진입
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 휴대폰 번호(QR)로 사용자 초대
            qrSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호")
            qrSetting.click()

            add_user = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_user.click()

            # 기등록된 사용자의 동일한 이름 입력
            st1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.widget.EditText[1]")
            st1.click()
            st1.send_keys("e2e_Test1")

            # 기등록된 사용자의 폰번호 입력
            st2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.widget.EditText[2]")
            st2.click()
            st2.send_keys("01012345678")

            # 다음 버튼 클릭
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()

            #초대 버튼
            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, invite)
            st3.click()
            time.sleep(1)

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirm_Btn.click()

            try:
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='e2e_Test1\n출입기간'])[2]")

            except NoSuchElementException:
                pass

            utils.user_delete(self)

            pass
            print("DQS_T12231 동일한 이름 및 휴대폰번호로 사용자 초대 시 실패 케이스 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T12231 동일한 이름 및 휴대폰번호로 사용자 초대 시 실패 케이스 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T12236(self):
        try:
            print("DQS_T12236 사용자 요일별 스케줄 추가 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            #utils.user_invite_phone(self, "e2e_Test1", "01012345678")

            userSelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_Test1\n출입기간")
            userSelete.click()
            time.sleep(1)

            #스케줄 추가
            daySchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\n제한없음")
            daySchedule.click()

            addSchedule_add = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가하기")
            addSchedule_add.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "시간 구역 추가")

            scheduleName1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            scheduleName1.click()
            scheduleName1.send_keys("Test_Schedule1")

            self.driver.back()

            monSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[15]")
            monSchedule.click()
            time.sleep(1)

            mon_start_hour = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='09'])[1]")
            mon_start_hour.click()

            max_swipes = 10
            start_x = 260
            start_y = 1960
            end_x = 260
            end_y = 1460
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "08")
                    if element.is_displayed():
                        element.click()
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            mon_end_hour = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "09")
            mon_end_hour.click()

            max_swipes = 10
            start_x1 = 255
            start_y1 = 2060
            end_x1 = 255
            end_y1 = 1460
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "17")
                    if element.is_displayed():
                        element.click()
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x1, start_y1, end_x1, end_y1, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[18]") # -버튼 출력 확인
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[21]") # +버튼 출력 확인

            # 아래방향으로 스크롤 이동
            start_x2 = 779
            start_y2 = 1920
            end_x2 = 779
            end_y2 = 390
            self.driver.swipe(start_x2, start_y2, end_x2, end_y2)
            time.sleep(1)

            # 수요일 + 버튼 선택
            wedSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[2]")
            wedSchedule.click()
            time.sleep(1)

            wed_end_hour = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='09'])[2]")
            wed_end_hour.click()

            max_swipes = 10
            start_x3 = 260
            start_y3 = 1320
            end_x3 = 260
            end_y3 = 720
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "18")
                    if element.is_displayed():
                        element.click()
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x3, start_y3, end_x3, end_y3, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[5]") # -버튼 출력 확인
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[8]") # +버튼 출력 확인

            wedSchedule_add1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[8]") # +버튼 선택
            wedSchedule_add1.click()
            time.sleep(0.5)

            # 아래방향으로 스크롤 이동
            start_x2 = 779
            start_y2 = 1920
            end_x2 = 779
            end_y2 = 390
            self.driver.swipe(start_x2, start_y2, end_x2, end_y2)
            time.sleep(1)

            wed_start_hour2 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='09'])[1]")
            wed_start_hour2.click()

            max_swipes = 10
            start_x4 = 250
            start_y4 = 1070
            end_x4 = 250
            end_y4 = 500
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "18")
                    if element.is_displayed():
                        element.click()
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x4, start_y4, end_x4, end_y4, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            time.sleep(1)

            wed_end_hour2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "09")
            wed_end_hour2.click()

            max_swipes = 10
            start_x5 = 260
            start_y5 = 1180
            end_x5 = 260
            end_y5 = 620
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "21")
                    if element.is_displayed():
                        element.click()
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x5, start_y5, end_x5, end_y5, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[3]") # -버튼 출력 확인
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[6]") # +버튼 출력 확인

            # 토요일 + 버튼 선택
            satSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[12]")
            satSchedule.click()
            time.sleep(1)

            sat_start_hour = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='09'])[1]")
            sat_start_hour.click()

            max_swipes = 10
            start_x6 = 246
            start_y6 = 2130
            end_x6 = 246
            end_y6 = 1630
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "10")
                    if element.is_displayed():
                        element.click()
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x6, start_y6, end_x6, end_y6, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            sat_end_hour = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='09']")
            sat_end_hour.click()

            max_swipes = 10
            start_x7 = 250
            start_y7 = 1430
            end_x7 = 250
            end_y7 = 830
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "15")
                    if element.is_displayed():
                        element.click()
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x7, start_y7, end_x7, end_y7, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[15]") # -버튼 출력 확인
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[18]") # +버튼 출력 확인

            satSchedule2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[18]")
            satSchedule2.click()
            time.sleep(1)

            # 아래방향으로 스크롤 이동
            start_x2 = 779
            start_y2 = 1920
            end_x2 = 779
            end_y2 = 390
            self.driver.swipe(start_x2, start_y2, end_x2, end_y2)
            time.sleep(1)

            sat_start_hour2 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='09'])[1]")
            sat_start_hour2.click()

            max_swipes = 10
            start_x9 = 250
            start_y9 = 2050
            end_x9 = 250
            end_y9 = 1480
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='15'])[2]")
                    if element.is_displayed():
                        element.click()
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x9, start_y9, end_x9, end_y9, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            sat_end_hour2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "09")
            sat_end_hour2.click()

            max_swipes = 10
            start_x10 = 250
            start_y10 = 2150
            end_x10 = 255
            end_y10 = 1590
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "18")
                    if element.is_displayed():
                        element.click()
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x10, start_y10, end_x10, end_y10, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            sat_end_min2 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='00'])[4]")
            sat_end_min2.click()

            max_swipe = 40
            start_x11 = 700
            start_y11 = 2140
            end_x11 = 700
            end_y11 = 1590
            duration = 200

            for _ in range(max_swipe):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "30")
                    if element.is_displayed():
                        element.click()
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x11, start_y11, end_x11, end_y11, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[15]") # -버튼 출력 확인
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[18]") # +버튼 출력 확인

            satSchedule3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[18]")
            satSchedule3.click()
            time.sleep(1)

            # 아래방향으로 스크롤 이동
            start_x2 = 779
            start_y2 = 1920
            end_x2 = 779
            end_y2 = 390
            self.driver.swipe(start_x2, start_y2, end_x2, end_y2)
            time.sleep(1)

            sat_start_hour3 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='09'])[1]")
            sat_start_hour3.click()

            max_swipes = 10
            start_x13 = 250
            start_y13 = 2020
            end_x13 = 250
            end_y13 = 1540
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "19")
                    if element.is_displayed():
                        element.click()
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x13, start_y13, end_x13, end_y13, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            sat_end_hour3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "09")
            sat_end_hour3.click()

            max_swipes = 10
            start_x14 = 250
            start_y14 = 2140
            end_x14 = 250
            end_y14 = 1560
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "22")
                    if element.is_displayed():
                        element.click()
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x14, start_y14, end_x14, end_y14, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            sat_end_min3 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='00'])[5]")
            sat_end_min3.click()

            max_swipe = 40
            start_x15 = 700
            start_y15 = 2130
            end_x15 = 700
            end_y15 = 1570
            duration = 200

            for _ in range(max_swipe):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "50")
                    if element.is_displayed():
                        element.click()
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x15, start_y15, end_x15, end_y15, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[19]") # -버튼 출력 확인

            save_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "저장")
            save_btn.click()
            time.sleep(1)

            #테스트한 스케줄 삭제
            delete_Schedule1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Test_Schedule1']/android.widget.ImageView[2]")
            delete_Schedule1.click()

            delete_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "삭제")
            delete_btn.click()

            pass
            print("DQS_T12236 DQS_T12236 사용자 요일별 스케줄 추가 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T12236 DQS_T12236 사용자 요일별 스케줄 추가 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T666666_1(self):
        try:
            print("DQS_T666666_1 사용자 요일별 스케줄 삭제 기능 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            utils.user_invite_phone(self, "e2e_Test1", "01012345678")

            userSelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_Test1\n출입기간")
            userSelete.click()
            time.sleep(1)

            #스케줄 추가
            daySchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\n제한없음")
            daySchedule.click()

            addSchedule_add = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가하기")
            addSchedule_add.click()

            scheduleName1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            scheduleName1.click()
            scheduleName1.send_keys("Test_Schedule1")

            self.driver.back()
            time.sleep(1)

            monSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[15]")
            monSchedule.click()
            time.sleep(1)

            mon_end_hour = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='09'])[2]")
            mon_end_hour.click()

            max_swipes = 24
            start_x1 = 255
            start_y1 = 2000
            end_x1 = 255
            end_y1 = 1500
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "17")
                    if element.is_displayed():
                        element.click()
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x1, start_y1, end_x1, end_y1, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            save_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "저장")
            save_btn.click()
            time.sleep(1)

            #테스트한 스케줄 삭제
            delete_Schedule1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Test_Schedule1']/android.widget.ImageView[2]")
            delete_Schedule1.click()

            delete_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "삭제")
            delete_btn.click()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_Schedule1")

            except NoSuchElementException:
                pass

            for _ in range(2):
                self.driver.back()

            utils.user_delete(self)


            pass
            print("DQS_T666666_1 사용자 요일별 스케줄 삭제 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T666666_1 사용자 요일별 스케줄 삭제 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T12238(self):
        try:
            print("DQS_T12238 사용자 요일별 스케줄 설정 회면에서 뒤로가기 및 취소 버튼 선택 시 기능 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            utils.user_invite_phone(self, "e2e_Test1", "01012345678")

            userSelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_Test1\n출입기간")
            userSelete.click()
            time.sleep(1)

            #스케줄 추가
            daySchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\n제한없음")
            daySchedule.click()

            addSchedule_add = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가하기")
            addSchedule_add.click()

            #뒤로가기 버튼 클릭
            self.driver.tap([(54, 148)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가하기")

            #뒤로가기 버튼 클릭
            self.driver.tap([(54, 148)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가하기").is_displayed()

            #취소 버튼 클릭
            cancel_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            cancel_Btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 상세").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_Test1\n#01012345678\n출입기간\n모든 출입문")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\n제한없음")

            self.driver.back()

            utils.user_delete(self)

            pass
            print("DQS_T12238 사용자 요일별 스케줄 설정 회면에서 뒤로가기 및 취소 버튼 선택 시 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T12238 사용자 요일별 스케줄 설정 회면에서 뒤로가기 및 취소 버튼 선택 시 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T12239_T12617(self):
        try:
            print("DQS_T12239 사용자 요일별 스케줄 일정 변경 시 기능 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            utils.user_invite_phone(self, "e2e_Test1", "01012345678")

            userSelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_Test1\n출입기간")
            userSelete.click()
            time.sleep(1)

            #스케줄 추가
            daySchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\n제한없음")
            daySchedule.click()

            addSchedule_add = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가하기")
            addSchedule_add.click()

            scheduleName1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            scheduleName1.click()
            scheduleName1.send_keys("Test_Schedule1")

            self.driver.back()
            time.sleep(1)

            monSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[15]")
            monSchedule.click()
            time.sleep(1)

            mon_end_hour = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='09'])[2]")
            mon_end_hour.click()

            max_swipes = 24
            start_x1 = 255
            start_y1 = 2000
            end_x1 = 255
            end_y1 = 1500
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "17")
                    if element.is_displayed():
                        element.click()
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x1, start_y1, end_x1, end_y1, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            save_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "저장")
            save_btn.click()
            time.sleep(1)

            schedule_selete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_Schedule1")
            schedule_selete.click()

            confirm_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_btn.click()
            time.sleep(1)

            #스케줄 수정
            modifySchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\nTest_Schedule1")
            modifySchedule.click()

            schedule_selete2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Test_Schedule1']/android.widget.ImageView[2]")
            schedule_selete2.click()

            scheduleName2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            scheduleName2.click()
            scheduleName2.send_keys("Test_Schedule2")

            self.driver.back()

            mon_start_hour = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "09")
            mon_start_hour.click()

            max_swipes = 24
            start_x2 = 255
            start_y2 = 2000
            end_x2 = 255
            end_y2 = 1500
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "05")
                    if element.is_displayed():
                        element.click()
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x2, start_y2, end_x2, end_y2, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            mon_end_hour1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "17")
            mon_end_hour1.click()

            max_swipes = 24
            start_x3 = 255
            start_y3 = 2000
            end_x3 = 255
            end_y3 = 1500
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "21")
                    if element.is_displayed():
                        element.click()
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x3, start_y3, end_x3, end_y3, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            # DQS_T12617 복사 동작 확인
            copy_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "복사")
            copy_btn.click()

            tueday = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "화요일")
            tueday.click()

            wedday = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수요일")
            wedday.click()

            confirm_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_btn.click()
            time.sleep(1)

            self.driver.back()

            start_x4 = 770
            start_y4 = 1928
            end_x4 = 770
            end_y4 = 309
            self.driver.swipe(start_x4, start_y4, end_x4, end_y4)
            time.sleep(1)

            thuSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[10]")
            thuSchedule.click()
            time.sleep(1)

            thu_end_hour = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='09'])[2]")
            thu_end_hour.click()

            max_swipes = 24
            start_x5 = 277
            start_y5 = 1570
            end_x5 = 277
            end_y5 = 1090
            duration = 200

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "17")
                    if element.is_displayed():
                        element.click()
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x5, start_y5, end_x5, end_y5, duration)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            copy_btn2 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='복사'])[2]")
            copy_btn2.click()

            friday = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "금요일")
            friday.click()

            satday = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "토요일")
            satday.click()

            sunday = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일요일")
            sunday.click()

            confirm_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_btn.click()
            time.sleep(1)

            save_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "저장")
            save_btn.click()
            time.sleep(1)

            modifySchedule2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Test_Schedule2']/android.widget.ImageView[2]")
            modifySchedule2.click()

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='05'])[1]")
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='21'])[1]")
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='05'])[2]")
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='21'])[2]")

            start_x6 = 770
            start_y6 = 1928
            end_x6 = 770
            end_y6 = 309
            self.driver.swipe(start_x6, start_y6, end_x6, end_y6)
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='09'])[1]")
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='17'])[1]")
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='09'])[2]")
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='17'])[2]")

            #테스트한 스케줄 삭제
            delete_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "삭제")
            delete_btn.click()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_Schedule2")

            except NoSuchElementException:
                pass

            for _ in range(2):
                self.driver.back()

            utils.user_delete(self)

            pass
            print("DQS_T12239 사용자 요일별 스케줄 일정 변경 시 기능 동작 확인 || DQS-T12617 사용자 요일별 스케줄 설정 시 시간 복사 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T12239 사용자 요일별 스케줄 일정 변경 시 기능 동작 확인 || DQS-T12617 사용자 요일별 스케줄 설정 시 시간 복사 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    # def test_DQS_T12618(self):  #수정 필요
    #     try:
    #         print("DQS_T12618 사용자 요일별 스케줄 설정 시 익일 기능 동작 확인")
    #         self.driver.tap([(967, 2084)])
    #         #사용자 초대 버튼 클릭
    #         time.sleep(1)
    #
    #         utils.user_invite_phone(self, "e2e_Test1", "01012345678")
    #
    #         userSelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_Test1\n출입기간")
    #         userSelete.click()
    #         time.sleep(1)
    #
    #         #스케줄 추가
    #         daySchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\n제한없음")
    #         daySchedule.click()
    #
    #         addSchedule_add = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가하기")
    #         addSchedule_add.click()
    #
    #         scheduleName1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
    #         scheduleName1.click()
    #         scheduleName1.send_keys("Test_Schedule1")
    #
    #         self.driver.back()
    #         time.sleep(1)
    #
    #         monSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[15]")
    #         monSchedule.click()
    #         time.sleep(1)
    #
    #         mon_start_hour = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='09'])[1]")
    #         mon_start_hour.click()
    #
    #         max_swipes = 24
    #         start_x1 = 280
    #         start_y1 = 1866
    #         end_x1 = 280
    #         end_y1 = 1400
    #         duration = 100
    #
    #         for _ in range(max_swipes):
    #             try:
    #                 element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "23")
    #                 if element.is_displayed():
    #                     element.click()
    #                     break
    #             except NoSuchElementException:
    #                 self.driver.swipe(start_x1, start_y1, end_x1, end_y1, duration)
    #         else:
    #             raise NoSuchElementException("찾을 수 없습니다.")
    #
    #         time.sleep(1)
    #
    #         # mon_end_hour = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "09")
    #         # mon_end_hour.click()
    #         self.driver.tap([(228, 1347)])
    #         time.sleep(0.5)
    #
    #         max_swipes = 24
    #         start_x2 = 250
    #         start_y2 =1980
    #         end_x2 = 250
    #         end_y2 = 1540
    #         duration = 100
    #
    #         for _ in range(max_swipes):
    #             try:
    #                 element1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "23")
    #                 if element1.is_displayed():
    #                     element1.click()
    #                     break
    #             except NoSuchElementException:
    #                 self.driver.swipe(start_x2, start_y2, end_x2, end_y2, duration)
    #         else:
    #             raise NoSuchElementException("찾을 수 없습니다.")
    #
    #         time.sleep(1)
    #
    #         mon_end_min = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='00'])[3]")
    #         mon_end_min.click()
    #
    #         max_swipes = 60
    #         start_x3 = 711
    #         start_y3 =2010
    #         end_x3 = 711
    #         end_y3 = 1517
    #         duration = 100
    #
    #         for _ in range(max_swipes):
    #             try:
    #                 element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "59")
    #                 if element.is_displayed():
    #                     element.click()
    #                     break
    #             except NoSuchElementException:
    #                 self.driver.swipe(start_x3, start_y3, end_x3, end_y3, duration)
    #         else:
    #             raise NoSuchElementException("찾을 수 없습니다.")
    #
    #         time.sleep(1)
    #
    #         tueSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[23]")
    #         tueSchedule.click()
    #         time.sleep(1)
    #
    #         tue_start_hour = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='09'])[1]")
    #         tue_start_hour.click()
    #
    #         max_swipes = 24
    #         start_x4 = 255
    #         start_y4 = 1450
    #         end_x4 = 255
    #         end_y4 = 980
    #         duration = 100
    #
    #         for _ in range(max_swipes):
    #             try:
    #                 element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "00")
    #                 if element.is_displayed():
    #                     element.click()
    #                     break
    #             except NoSuchElementException:
    #                 self.driver.swipe(start_x4, start_y4, end_x4, end_y4, duration)
    #         else:
    #             raise NoSuchElementException("찾을 수 없습니다.")
    #
    #         tue_end_hour = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='09']")
    #         tue_end_hour.click()
    #
    #         max_swipes = 24
    #         start_x5 = 277
    #         start_y5 =1550
    #         end_x5 = 277
    #         end_y5 = 1100
    #         duration = 100
    #
    #         for _ in range(max_swipes):
    #             try:
    #                 element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "05")
    #                 if element.is_displayed():
    #                     element.click()
    #                     break
    #             except NoSuchElementException:
    #                 self.driver.swipe(start_x5, start_y5, end_x5, end_y5, duration)
    #         else:
    #             raise NoSuchElementException("찾을 수 없습니다.")
    #
    #         save_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "저장")
    #         save_btn.click()
    #         time.sleep(1)
    #
    #         schedule_selete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_Schedule1")
    #         schedule_selete.click()
    #
    #         confirm_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
    #         confirm_btn.click()
    #         time.sleep(1)
    #
    #         daySchedule2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\nTest_Schedule1")
    #         daySchedule2.click()
    #
    #         schedule_selete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_Schedule1")
    #         schedule_selete.click()
    #
    #         #테스트한 스케줄 삭제
    #         delete_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "삭제")
    #         delete_btn.click()
    #
    #         for _ in range(2):
    #             self.driver.back()
    #
    #         utils.user_delete(self)
    #
    #         pass
    #         print("DQS_T12618 사용자 요일별 스케줄 설정 시 익일 기능 동작 확인 | Pass")
    #
    #     except Exception as e:
    #         capture_screenshot(self.driver, self._testMethodName)
    #         print("DQS_T12618 사용자 요일별 스케줄 설정 시 익일 기능 동작 확인 | Failed")
    #         print(str(e))
    #         self.fail()

    def test_DQS_T12619(self):
        try:
            print("DQS_T12619 사용자 요일별 스케줄 설정 시 시간 설정 오류 케이스 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            utils.user_invite_phone(self, "e2e_Test1", "01012345678")

            userSelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_Test1\n출입기간")
            userSelete.click()
            time.sleep(1)

            #스케줄 추가
            daySchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\n제한없음")
            daySchedule.click()

            addSchedule_add = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가하기")
            addSchedule_add.click()

            scheduleName1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            scheduleName1.click()
            scheduleName1.send_keys("Test_Schedule1")

            self.driver.back()
            time.sleep(1)

            monSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[15]")
            monSchedule.click()
            time.sleep(1)

            mon_start_hour = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='09'])[1]")
            mon_start_hour.click()

            start_hour1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "02")
            start_hour1.click()

            mon_end_hour = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='09']")
            mon_end_hour.click()

            end_hour1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "01")
            end_hour1.click()
            time.sleep(1)

            time_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='시작 시간이 종료 시간보다 늦습니다.']")
            contentDesc1 = time_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "시작 시간이 종료 시간보다 늦습니다.")
            time.sleep(0.5)

            mon_end_hour2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='01']")
            mon_end_hour2.click()

            end_hour2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "04")
            end_hour2.click()
            time.sleep(1)

            addSchedule_add = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[21]")
            addSchedule_add.click()

            mon_start_hour2 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='09'])[1]")
            mon_start_hour2.click()

            start_hour2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "03")
            start_hour2.click()

            mon_end_hour3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='09']")
            mon_end_hour3.click()

            end_hour2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "05")
            end_hour2.click()
            time.sleep(1)

            save_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "저장")
            save_btn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 저장")
            time_pop = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='스케줄 저장에 실패하였습니다.\n[CODE: 400]']")
            contentDesc2 = time_pop.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "스케줄 저장에 실패하였습니다.\n[CODE: 400]")
            time.sleep(0.5)

            confirm_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_btn.click()

            self.driver.back()

            for _ in range(3):
                self.driver.back()

            utils.user_delete(self)

            pass
            print("DQS_T12619 사용자 요일별 스케줄 설정 시 시간 설정 오류 케이스 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T12619 사용자 요일별 스케줄 설정 시 시간 설정 오류 케이스 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15911(self):
        try:
            print("DQS_T15911 고객사  관리, 무인매장, 멤버쉽 관리 공간별 사용자 편집 아이콘 출력 및 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            logout_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃")
            logout_button.click()

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            utils.mobile_login(self, "01020905304", "Kjstar36!!")
            time.sleep(2)

            # 고객사 확인 공간에 사용자 초대 버튼 출력 확인
            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            #사용자 목록 화면 출력 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 목록")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 리스트")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")

            self.driver.back()

            place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1")
            place.click()
            time.sleep(2)

            placeInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            placeInput.click()
            placeInput.send_keys("비디오 공간")
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간\nID : 22")

            self.driver.tap([(260, 644)])
            time.sleep(2)

            #멤버쉽 공간에 사용자 초대 버튼 출력 확인
            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            #사용자 목록 화면 출력 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 목록")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 리스트")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")

            self.driver.back()

            place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간")
            place.click()
            time.sleep(2)

            placeInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            placeInput.click()
            placeInput.send_keys("QA 무인매장")
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "QA 무인매장\nID : 23")

            #무인 매장 공간에 사용자 초대 버튼 출력 확인
            self.driver.tap([(260, 644)])
            time.sleep(2)

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 좌표 클릭
            time.sleep(1)

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 목록")
                assert False, "사용자 목록 진입함"
            except NoSuchElementException:
                pass

            print("DQS_T15911 고객사  관리, 무인매장, 멤버쉽 관리 공간별 사용자 편집 아이콘 출력 및 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15911 고객사  관리, 무인매장, 멤버쉽 관리 공간별 사용자 편집 아이콘 출력 및 동작 확인 | Failed")
            print(str(e))
            self.fail()

class User_Credential(unittest.TestCase):

    def setUp(self):
        self.driver = AppiumConfig.get_driver()
        self.driver.implicitly_wait(10)

        utils.mobile_login(self, "01011111111", "Kjstar36!!")

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_DQS_T15912(self):
        try:
            print("DQS_T15912 휴대폰 번호 인증방식 설정 시 Validation 체크 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 휴대폰 번호(QR) 선택
            qrSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호")
            qrSetting.click()

            add_user = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_user.click()

            #이름 입력 - 한글 31자 입력 시도
            userInput1 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput1.click()
            userInput1.send_keys("가나다라마바사아자차가나다라마바사아자차가나다라마바사아자차카")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='가나다라마바사아자차가나다라마바사아자차가나다라마바사아자차']").is_displayed()
            userInput1.clear()

            #이름 입력 - 영어 31자 입력 시도
            userInput2 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput2.click()
            userInput2.send_keys("abcdefghijabcdefghijabcdefghijk")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='abcdefghijabcdefghijabcdefghij']").is_displayed()
            userInput2.clear()

            #이름 입력 - 일어 31자 입력 시도
            userInput3 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput3.click()
            userInput3.send_keys("ユーザー名入力テストユーザー名入力テストユーザー名入力テストです")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='ユーザー名入力テストユーザー名入力テストユーザー名入力テスト']").is_displayed()
            userInput3.clear()

            #이름 입력 - 숫자 31자 입력 시도
            userInput4 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput4.click()
            userInput4.send_keys("1234567890123456789012345678901")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123456789012345678901234567890']").is_displayed()
            userInput4.clear()

            #이름 입력 - 특수문자 입력 시도
            userInput5 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput5.click()
            userInput5.send_keys("~!@#$%^&")
            time.sleep(1)

            phoneInput1 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            phoneInput1.click()
            phoneInput1.send_keys("01099990099")
            time.sleep(1)

            # 다음 버튼 클릭 - 비활성화 확인
            next_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            is_enabled = next_Btn.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "다음 버튼 비활성화")

            userInput5 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput5.click()
            userInput5.clear()
            time.sleep(1)

            userInput6 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput6.click()
            userInput6.send_keys("Test_QR1")

            phoneInput1 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            phoneInput1.click()
            phoneInput1.clear()
            time.sleep(1)

            phoneInput2 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            phoneInput2.click()
            text_to_input = "ABCDEFG"
            er1 = phoneInput2.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er1)
            phoneInput2.clear()

            phoneInput3 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            phoneInput3.click()
            text_to_input = "abcdefg"
            er2 = phoneInput3.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er2)
            phoneInput3.clear()

            phoneInput4 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            phoneInput4.click()
            text_to_input = "가나다라마바사"
            er3 = phoneInput4.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er3)
            phoneInput4.clear()

            phoneInput5 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            phoneInput5.click()
            text_to_input = "!@#$%^&*()"
            er4 = phoneInput5.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er4)
            phoneInput5.clear()

            phoneInput6 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            phoneInput6.click()
            phoneInput6.send_keys("0123456789012345678901")
            time.sleep(1)

            # 다음 버튼 클릭 - 비활성화 확인
            next_Btn1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            is_enabled = next_Btn1.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "다음 버튼 비활성화")

            phoneInput6.clear()
            time.sleep(1)

            phoneInput7 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            phoneInput7.click()
            phoneInput7.send_keys("010123456")
            time.sleep(1)

            # 다음 버튼 클릭 - 비활성화 확인
            next_Btn2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            is_enabled = next_Btn2.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "다음 버튼 비활성화")

            phoneInput7.clear()
            time.sleep(1)

            phoneInput8 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            phoneInput8.click()
            phoneInput8.send_keys("01012345678")
            time.sleep(1)

            # 다음 버튼 클릭 - 활성화 확인
            next_Btn3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            is_enabled = next_Btn3.get_attribute("enabled")
            self.assertEqual(is_enabled, "true", "다음 버튼 활성화")

            pass
            print("DQS_T15912 휴대폰 번호 인증방식 설정 시 Validation 체크 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15912 휴대폰 번호 인증방식 설정 시 Validation 체크 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T7650_T7977(self):
        try:
            print("DQS_T7650 사용자 초대 성공 케이스 동작 확인(인증방식 : QR) || DQS_T7977 사용자 삭제 기능 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            logout_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃")
            logout_button.click()

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            utils.mobile_login(self, "01020905304", "Kjstar36!!")
            time.sleep(2)

            place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1")
            place.click()
            time.sleep(2)

            placeInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            placeInput.click()
            placeInput.send_keys("출입보안 공간")
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입보안 공간\nID : 27")

            self.driver.tap([(260, 644)])
            time.sleep(2)

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 휴대폰 번호(QR) 선택
            qrSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호")
            qrSetting.click()

            add_user = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_user.click()

            #이름 입력
            userInput = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput.click()
            userInput.send_keys("Add QR_Test")

            phoneInput = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            phoneInput.click()
            phoneInput.send_keys("01099990001")

            # 다음 버튼 클릭 - 출입 권한 UI 확인
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()

            #초대 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, invite)
            inviteBtn.click()
            time.sleep(1)

            confirm_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_btn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Add QR_Test\n출입기간")\

            print("DQS_T7977 사용자 삭제 기능 동작 확인")
            user_modity = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            user_modity.click()

            user_delete1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "삭제")
            user_delete1.click()

            #사용자 제외 팝업 취소 버튼 클릭
            cancle_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, cancel)
            cancle_Btn.click()
            time.sleep(1)

            user_delete2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "삭제")
            user_delete2.click()

            # 사용자 제외 팝업 확인 버튼 클릭
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 제외")
            delete_pop = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='해당 사용자를 이 공간에서 제외하시겠습니까?']")
            contentDesc = delete_pop.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "해당 사용자를 이 공간에서 제외하시겠습니까?")

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()
            time.sleep(1)


            pass
            print("DQS_T7650 사용자 초대 성공 케이스 동작 확인(인증방식 : QR) || DQS_T7977 사용자 삭제 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T7650 사용자 초대 성공 케이스 동작 확인(인증방식 : QR) || DQS_T7977 사용자 삭제 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T12237_T7198(self):
        try:
            print("DQS_T12237 사용자 다중 초대 성공 케이스 동작 확인(인증방식 : QR) || DQS_T7198 사용자 조회 화면에서의 기능 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            logout_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃")
            logout_button.click()

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            utils.mobile_login(self, "01020905304", "Kjstar36!!")
            time.sleep(2)

            place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1")
            place.click()
            time.sleep(2)

            placeInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            placeInput.click()
            placeInput.send_keys("출입보안 공간")
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입보안 공간\nID : 27")

            self.driver.tap([(260, 644)])
            time.sleep(2)

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 휴대폰 번호(QR) 선택
            qrSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호")
            qrSetting.click()

            add_user = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_user.click()

            #사용자1 정보 입력
            user1_1 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            user1_1.click()
            user1_1.send_keys("Test1")

            user1_2 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            user1_2.click()
            user1_2.send_keys("01011111111")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            # 추가 버튼 클릭
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_btn.click()
            time.sleep(1)

            #사용자2 정보 입력
            user2_1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.widget.EditText[3]")
            user2_1.click()
            user2_1.send_keys("Test2")

            self.driver.back()
            time.sleep(0.5)

            user2_2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.widget.EditText[4]")
            user2_2.click()
            user2_2.send_keys("01022222222")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            # 추가 버튼 클릭
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_btn.click()
            time.sleep(1)

            #사용자3 정보 입력
            user3_1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.widget.EditText[5]")
            user3_1.click()
            user3_1.send_keys("Test3")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            user3_2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.widget.EditText[6]")
            user3_2.click()
            user3_2.send_keys("01033333333")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            # 추가 버튼 클릭
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_btn.click()
            time.sleep(1)

            #사용자4 정보 입력
            user4_1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[7]")
            user4_1.click()
            user4_1.send_keys("Test4")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            user4_2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[7]")
            user4_2.click()
            user4_2.send_keys("01044444444")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            # 추가 버튼 클릭
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_btn.click()
            time.sleep(1)

            #사용자5 정보 입력
            user5_1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[8]")
            user5_1.click()
            user5_1.send_keys("홍길동")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            user5_2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[7]")
            user5_2.click()
            user5_2.send_keys("01055555555")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            # 추가 버튼 클릭
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_btn.click()
            time.sleep(1)

            #사용자6 정보 입력
            user6_1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[8]")
            user6_1.click()
            user6_1.send_keys("아무개")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            user6_2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[7]")
            user6_2.click()
            user6_2.send_keys("01066666666")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            # 추가 버튼 클릭
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_btn.click()
            time.sleep(1)

            #사용자6 정보 입력
            user7_1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[8]")
            user7_1.click()
            user7_1.send_keys("1a-_-")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            user7_2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[7]")
            user7_2.click()
            user7_2.send_keys("01077777777")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            # 다음 버튼 클릭 - 출입 권한 UI 확인
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()

            #초대 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, invite)
            inviteBtn.click()
            time.sleep(3)

            #벌크초대 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 권한")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test1\n01011111111")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n01022222222")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n01033333333")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n01044444444")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n01055555555")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n01066666666")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n01077777777")

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()
            time.sleep(2)

            #사용자 리스트 - 초대 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test1\n출입기간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간")

            # #이름순 정렬 확인
            # name_list = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "등록순")
            # name_list.click()
            #
            # assert self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "이름순")
            #
            # #등록순 정렬 확인
            # add_list = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "이름순")
            # add_list.click()
            #
            # assert self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "등록순")

            print("DQS_T7198 사용자 조회 화면에서의 기능 동작 확인")
            search_btn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button")
            search_btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")

            user_search1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            user_search1.click()
            user_search1.send_keys("010")
            time.sleep(0.5)

            search_btn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button")
            search_btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대된 사용자가 없습니다.")
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대하기']")

            user_search1.clear()

            user_search2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            user_search2.click()
            user_search2.send_keys("01011111111")
            time.sleep(0.5)

            search_btn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button")
            search_btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test1\n출입기간")

            user_search2.clear()

            cancel_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            cancel_btn.click()
            time.sleep(1)

            print("검색된 사용자가 최상단에 출력되는 이슈가 있어 사용자 재진입 동작 수행")
            self.driver.back()

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            # name_list = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "등록순")
            # name_list.clear()
            #
            # add_list = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "이름순")
            # add_list.clear()

            #모든 사용자 리스트 출력
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test1\n출입기간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간")

            search_btn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button")
            search_btn.click()

            user_search3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            user_search3.click()
            user_search3.send_keys("Test1")
            time.sleep(0.5)

            search_btn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button")
            search_btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test1\n출입기간")

            user_search3.clear()

            user_search4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            user_search4.click()
            user_search4.send_keys("test1")
            time.sleep(0.5)

            search_btn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button")
            search_btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test1\n출입기간")

            user_search4.clear()

            user_search5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            user_search5.click()
            user_search5.send_keys("TEST1")
            time.sleep(0.5)

            search_btn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button")
            search_btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test1\n출입기간")

            user_search5.clear()

            user_search6 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            user_search6.click()
            user_search6.send_keys("Te")
            time.sleep(0.5)

            search_btn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button")
            search_btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test1\n출입기간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")

            user_search6.clear()

            user_search7 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            user_search7.click()
            user_search7.send_keys("홍길동")
            time.sleep(0.5)

            search_btn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button")
            search_btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간")

            user_search7.clear()

            user_search8 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            user_search8.click()
            user_search8.send_keys("1a-_-")
            time.sleep(0.5)

            search_btn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button")
            search_btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간")

            user_search8.clear()

            user_search9 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            user_search9.click()
            user_search9.send_keys("홍")
            time.sleep(0.5)

            search_btn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button")
            search_btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간")

            user_search9.clear()

            user_search10 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            user_search10.click()
            user_search10.send_keys("1a-_")
            time.sleep(0.5)

            search_btn = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button")
            search_btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간")

            user_search10.clear()

            cancel_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            cancel_btn.click()
            time.sleep(1)

            print("검색된 사용자가 최상단에 출력되는 이슈가 있어 사용자 재진입 동작 수행")
            self.driver.back()

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            #모든 사용자 삭제
            user_modity = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            user_modity.click()

            for _ in range(6):
                user_delete = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[1]")
                user_delete.click()

                confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
                confirm_Btn.click()
                time.sleep(1)

            user_delete2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "삭제")
            user_delete2.click()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()
            time.sleep(1)

            pass
            print("DQS_T12237 사용자 다중 초대 성공 케이스 동작 확인(인증방식 : QR) || DQS_T7198 사용자 조회 화면에서의 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T12237 사용자 다중 초대 성공 케이스 동작 확인(인증방식 : QR) || DQS_T7198 사용자 조회 화면에서의 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15938(self):
        try:
            print("DQS_T15938 사용자 다중 초대시 중복 사용자 실패 케이스 동작 확인(인증방식 : QR)")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            logout_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃")
            logout_button.click()

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            utils.mobile_login(self, "01020905304", "Kjstar36!!")
            time.sleep(2)

            place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Visitor Place1")
            place.click()
            time.sleep(2)

            placeInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            placeInput.click()
            placeInput.send_keys("출입보안 공간")
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입보안 공간\nID : 27")

            self.driver.tap([(260, 644)])
            time.sleep(2)

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 휴대폰 번호(QR) 선택
            qrSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호")
            qrSetting.click()

            add_user = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_user.click()

            #사용자1 정보 입력
            user1_1 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            user1_1.click()
            user1_1.send_keys("Test1")

            user1_2 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            user1_2.click()
            user1_2.send_keys("01011111111")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            # 추가 버튼 클릭
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_btn.click()
            time.sleep(1)

            #사용자2 정보 입력
            user2_1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.widget.EditText[3]")
            user2_1.click()
            user2_1.send_keys("Test2")

            self.driver.back()
            time.sleep(0.5)

            user2_2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.widget.EditText[4]")
            user2_2.click()
            user2_2.send_keys("01022222222")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            # 추가 버튼 클릭
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_btn.click()
            time.sleep(1)

            #사용자3 정보 입력
            user3_1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.widget.EditText[5]")
            user3_1.click()
            user3_1.send_keys("Test3")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            user3_2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.widget.EditText[6]")
            user3_2.click()
            user3_2.send_keys("01033333333")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            # 추가 버튼 클릭
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_btn.click()
            time.sleep(1)

            #사용자4 정보 입력
            user4_1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[7]")
            user4_1.click()
            user4_1.send_keys("Test4")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            user4_2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[7]")
            user4_2.click()
            user4_2.send_keys("01044444444")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            # 다음 버튼 클릭 - 출입 권한 UI 확인
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()

            #초대 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, invite)
            inviteBtn.click()
            time.sleep(3)

            #벌크초대 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 권한")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test1\n01011111111")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n01022222222")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n01033333333")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n01044444444")

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()
            time.sleep(2)

            #사용자 리스트 - 초대 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test1\n출입기간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 휴대폰 번호(QR) 선택
            qrSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호")
            qrSetting.click()

            add_user = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_user.click()

            #사용자1 정보 입력
            user1_3 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            user1_3.click()
            user1_3.send_keys("Test1")

            user1_4 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            user1_4.click()
            user1_4.send_keys("01011111111")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            # 추가 버튼 클릭
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_btn.click()
            time.sleep(1)

            #사용자2 정보 입력
            user2_3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.widget.EditText[3]")
            user2_3.click()
            user2_3.send_keys("Test2")

            self.driver.back()
            time.sleep(0.5)

            user2_4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.widget.EditText[4]")
            user2_4.click()
            user2_4.send_keys("01022222222")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            # 추가 버튼 클릭
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_btn.click()
            time.sleep(1)

            #사용자3 정보 입력
            user3_3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.widget.EditText[5]")
            user3_3.click()
            user3_3.send_keys("Test3")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            user3_4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.widget.EditText[6]")
            user3_4.click()
            user3_4.send_keys("01033333333")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            # 추가 버튼 클릭
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_btn.click()
            time.sleep(1)

            #사용자4 정보 입력
            user4_3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[7]")
            user4_3.click()
            user4_3.send_keys("Test4")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            user4_4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[7]")
            user4_4.click()
            user4_4.send_keys("01044444444")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            # 추가 버튼 클릭
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_btn.click()
            time.sleep(1)

            #사용자5 정보 입력
            user5_1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[8]")
            user5_1.click()
            user5_1.send_keys("Test5")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            user5_2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[7]")
            user5_2.click()
            user5_2.send_keys("01055555555")

            #키보드 닫기
            self.driver.back()
            time.sleep(0.5)

            # 다음 버튼 클릭 - 출입 권한 UI 확인
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()

            #초대 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, invite)
            inviteBtn.click()
            time.sleep(3)

            #벌크초대 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 권한")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test1\n01011111111")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n01022222222")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n01033333333")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n01044444444")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n01055555555")

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()
            time.sleep(2)

            #사용자 리스트 - 초대 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test1\n출입기간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간")

            #모든 사용자 삭제
            user_modity = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            user_modity.click()

            for _ in range(4):
                user_delete = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[1]")
                user_delete.click()

                confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
                confirm_Btn.click()
                time.sleep(1)

            user_delete2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "삭제")
            user_delete2.click()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()
            time.sleep(1)

            pass
            print("DQS_T15938 사용자 다중 초대시 중복 사용자 실패 케이스 동작 확인(인증방식 : QR) | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15938 사용자 다중 초대시 중복 사용자 실패 케이스 동작 확인(인증방식 : QR) | Failed")
            print(str(e))
            self.fail()

    # def test_DQS_T7198(self):
    #     try:
    #         print("DQS_T7198 사용자 조회 화면에서의 기능 동작 확인") #사용자 리스트의 element가 변경될 수 있음
    #
    #         self.driver.tap([(967, 2084)])
    #         #사용자 초대 버튼 클릭
    #         time.sleep(1)
    #
    #         userSearch = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[3]")
    #         userSearch.click()
    #
    #         # 사용자 조회 UI 확인
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 조회").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "조회").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 리스트").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "등록순").is_displayed()
    #
    #         st1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
    #         st1.click()
    #         st1.send_keys("010")
    #
    #         search_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "조회")
    #         search_Btn.click()
    #         time.sleep(1)
    #
    #         try:
    #             self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간")
    #             self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[2]")
    #             # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
    #             assert False, "사용자리스트 출력 확인"
    #         except NoSuchElementException:
    #             pass
    #
    #         # X버튼 클릭 후 조회버튼 클릭
    #         inputDelete_Btn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010']/android.widget.ImageView")
    #         inputDelete_Btn.click()
    #
    #         search_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "조회")
    #         search_Btn.click()
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간").is_displayed()
    #
    #         for _ in range(2):
    #             start_x1 = 501
    #             start_y1 = 2040
    #             end_x1 = 501
    #             end_y1 = 716
    #             self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test1\n출입기간").is_displayed()
    #
    #         #Test1 입력 후 조회 동작
    #         st2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
    #         st2.click()
    #         st2.send_keys("Test1")
    #
    #         search_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "조회")
    #         search_Btn.click()
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]").is_displayed()
    #         assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[2]").is_displayed()
    #
    #         try:
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간")
    #             # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
    #             assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
    #         except NoSuchElementException:
    #             pass
    #
    #         # X버튼 클릭 후 조회버튼 클릭
    #         inputDelete_Btn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Test1']/android.widget.ImageView")
    #         inputDelete_Btn.click()
    #
    #         #test1 입력 후 조회 동작
    #         st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
    #         st3.click()
    #         st3.send_keys("test1")
    #
    #         search_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "조회")
    #         search_Btn.click()
    #         time.sleep(1)
    #
    #         try:
    #             self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간")
    #             self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[2]")
    #             # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
    #             assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
    #         except NoSuchElementException:
    #             pass
    #
    #         # X버튼 클릭 후 조회버튼 클릭
    #         inputDelete_Btn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='test1']/android.widget.ImageView")
    #         inputDelete_Btn.click()
    #
    #         #TEST1 입력 후 조회 동작
    #         st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
    #         st3.click()
    #         st3.send_keys("TEST1")
    #
    #         search_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "조회")
    #         search_Btn.click()
    #         time.sleep(1)
    #
    #         try:
    #             self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간")
    #             self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[2]")
    #             # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
    #             assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
    #         except NoSuchElementException:
    #             pass
    #
    #         # X버튼 클릭 후 조회버튼 클릭
    #         inputDelete_Btn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='TEST1']/android.widget.ImageView")
    #         inputDelete_Btn.click()
    #
    #         #Te 입력 후 조회 동작
    #         st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
    #         st3.click()
    #         st3.send_keys("Te")
    #
    #         search_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "조회")
    #         search_Btn.click()
    #         time.sleep(1)
    #
    #         try:
    #             self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간")
    #             self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[2]")
    #             # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
    #             assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
    #         except NoSuchElementException:
    #             pass
    #
    #         # X버튼 클릭 후 조회버튼 클릭
    #         inputDelete_Btn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Te']/android.widget.ImageView")
    #         inputDelete_Btn.click()
    #
    #         #홍길동 입력 후 조회 동작
    #         st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
    #         st3.click()
    #         st3.send_keys("홍길동")
    #
    #         search_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "조회")
    #         search_Btn.click()
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간").is_displayed()
    #
    #         try:
    #             self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간")
    #             self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[2]")
    #             # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
    #             assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
    #         except NoSuchElementException:
    #             pass
    #
    #         # X버튼 클릭 후 조회버튼 클릭
    #         inputDelete_Btn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='홍길동']/android.widget.ImageView")
    #         inputDelete_Btn.click()
    #
    #         #홍 입력 후 조회 동작
    #         st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
    #         st3.click()
    #         st3.send_keys("홍")
    #
    #         search_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "조회")
    #         search_Btn.click()
    #         time.sleep(1)
    #
    #         try:
    #             self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간")
    #             self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[2]")
    #             # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
    #             assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
    #         except NoSuchElementException:
    #             pass
    #
    #         # X버튼 클릭 후 조회버튼 클릭
    #         inputDelete_Btn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='홍']/android.widget.ImageView")
    #         inputDelete_Btn.click()
    #
    #         #1a-_- 입력 후 조회 동작
    #         st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
    #         st3.click()
    #         st3.send_keys("1a-_-")
    #
    #         search_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "조회")
    #         search_Btn.click()
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간").is_displayed()
    #
    #         try:
    #             self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간")
    #             self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[2]")
    #             # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
    #             assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
    #         except NoSuchElementException:
    #             pass
    #
    #         # X버튼 클릭 후 조회버튼 클릭
    #         inputDelete_Btn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='1a-_-']/android.widget.ImageView")
    #         inputDelete_Btn.click()
    #
    #         #1a-_ 입력 후 조회 동작
    #         st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
    #         st3.click()
    #         st3.send_keys("1a-_")
    #
    #         search_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "조회")
    #         search_Btn.click()
    #         time.sleep(1)
    #
    #         try:
    #             self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간")
    #             self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간")
    #             self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[2]")
    #             # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
    #             assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
    #         except NoSuchElementException:
    #             pass
    #
    #         #뒤로가기 버튼 쿨릭 후 사용자 목록 UI 확인
    #         self.driver.tap([(54, 166)])
    #         time.sleep(1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 목록").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기").is_displayed()
    #
    #         #사용자 리스트 - 초대 확인
    #         assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간").is_displayed()
    #
    #         for _ in range(2):
    #             start_x1 = 501
    #             start_y1 = 2040
    #             end_x1 = 501
    #             end_y1 = 716
    #             self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
    #
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간").is_displayed()
    #         assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test1\n출입기간").is_displayed()
    #
    #         print("다중 사용자 삭제 - e2e_Test1만 빼고 삭제되어야 함, e2e_Test1 하위에 user 삭제이며, 순서가 상이할 경우 fail 발생")
    #         #뒤로가기 클릭
    #         self.driver.tap([(54, 158)])
    #         time.sleep(1)
    #
    #         self.driver.tap([(967, 2084)])
    #         #사용자 초대 버튼 클릭
    #         time.sleep(1)
    #
    #         modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
    #         modifyBtn.click()
    #
    #         userDelete = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]")
    #
    #         for _ in range(9):
    #             userDelete = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]")
    #             userDelete.click()
    #             time.sleep(0.5)
    #
    #             confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
    #             confirmBtn.click()
    #             time.sleep(0.5)
    #         pass
    #         print("DQS_T7198 사용자 조회 화면에서의 기능 동작 확인 | Pass")
    #
    #     except Exception as e:
    #         capture_screenshot(self.driver, self._testMethodName)
    #         print("DQS_T7198 사용자 조회 화면에서의 기능 동작 확인 | Failed")
    #         print(str(e))
    #         self.fail()

    def test_DQS_T15913(self):
        try:
            print("DQS_T15913 얼굴 인증방식 설정 시 Validation 체크 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 얼굴 인식 선택
            qrSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "얼굴 인식")
            qrSetting.click()

            # 1번 얼굴 등록
            selete_face1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+얼굴 1")
            selete_face1.click()

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aos_photo1 = self.driver.find_element(AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[5]/android.view.View[1]/android.view.View[2]/android.view.View")
            aos_photo1.click()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View/android.widget.ImageView[1]")

            #이름 입력 - 한글 31자 입력 시도
            userInput1 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput1.click()
            userInput1.send_keys("가나다라마바사아자차가나다라마바사아자차가나다라마바사아자차카")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='가나다라마바사아자차가나다라마바사아자차가나다라마바사아자차']").is_displayed()

            # 다음 버튼 클릭 - 활성화 확인
            next_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            is_enabled = next_btn.get_attribute("enabled")
            self.assertEqual(is_enabled, "true", "다음 버튼 활성화")

            userInput1.clear()

            #이름 입력 - 영어 31자 입력 시도
            userInput2 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput2.click()
            userInput2.send_keys("abcdefghijabcdefghijabcdefghijk")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='abcdefghijabcdefghijabcdefghij']").is_displayed()

            # 다음 버튼 클릭 - 활성화 확인
            next_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            is_enabled = next_btn.get_attribute("enabled")
            self.assertEqual(is_enabled, "true", "다음 버튼 활성화")

            userInput2.clear()

            #이름 입력 - 일어 31자 입력 시도
            userInput3 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput3.click()
            userInput3.send_keys("ユーザー名入力テストユーザー名入力テストユーザー名入力テストです")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='ユーザー名入力テストユーザー名入力テストユーザー名入力テスト']").is_displayed()

            # 다음 버튼 클릭 - 활성화 확인
            next_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            is_enabled = next_btn.get_attribute("enabled")
            self.assertEqual(is_enabled, "true", "다음 버튼 활성화")

            userInput3.clear()

            #이름 입력 - 숫자 31자 입력 시도
            userInput4 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput4.click()
            userInput4.send_keys("1234567890123456789012345678901")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123456789012345678901234567890']").is_displayed()

            # 다음 버튼 클릭 - 활성화 확인
            next_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            is_enabled = next_btn.get_attribute("enabled")
            self.assertEqual(is_enabled, "true", "다음 버튼 활성화")

            userInput4.clear()

            #이름 입력 - 특수문자 입력 시도
            userInput5 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput5.click()
            userInput5.send_keys("~!@#$%^&")
            time.sleep(1)

            # 다음 버튼 클릭 - 비활성화 확인
            next_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            is_enabled = next_btn.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "다음 버튼 비활성화")

            userInput5.clear()

            #이름 입력
            userInput6 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput6.click()
            userInput6.send_keys("Test_Face1")
            time.sleep(1)

            face_delete = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View/android.widget.ImageView[2]")
            face_delete.click()
            time.sleep(1)

            # 다음 버튼 클릭 - 비활성화 확인
            next_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            is_enabled = next_btn.get_attribute("enabled")
            self.assertEqual(is_enabled, "false", "다음 버튼 비활성화")

            pass
            print("DQS_T15913 얼굴 인증방식 설정 시 Validation 체크 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15913 얼굴 인증방식 설정 시 Validation 체크 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15917(self):
        try:
            print("DQS_T15917 사용자 초대 성공 케이스 동작 확인[인증방식 : 얼굴 / 갤러리(이미지) 선택]")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 얼굴 인식 선택
            faceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "얼굴 인식")
            faceSetting.click()

            #이름 입력
            userInput1 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput1.click()
            userInput1.send_keys("Test_Face1")
            time.sleep(1)

            text_output = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Test_Face1']")
            text = text_output.get_attribute('text')
            print(f"추출한 text 값 : {text}")
            self.assertEqual(text, "Test_Face1")

            seleteFace2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+얼굴 2")
            seleteFace2.click()
            time.sleep(1)

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "이미지 팝업 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            seleteFace1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+얼굴 1")
            seleteFace1.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카메라").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리").is_displayed()
            image_Msg1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지를 가져올 방법을 선택해주세요.")
            contentDesc1 = image_Msg1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "이미지를 가져올 방법을 선택해주세요.")

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aosPhoto1 = self.driver.find_element(AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[5]/android.view.View[1]/android.view.View[2]/android.view.View")
            aosPhoto1.click()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View/android.widget.ImageView[1]") #이미지 출력
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View/android.widget.ImageView[2]") #이미지 삭제 버튼 출력

            seleteFace2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+얼굴 2")
            seleteFace2.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카메라").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리").is_displayed()
            image_Msg2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지를 가져올 방법을 선택해주세요.")
            contentDesc2 = image_Msg2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "이미지를 가져올 방법을 선택해주세요.")

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aosPhoto2 = self.driver.find_element(AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]/android.view.View[2]/android.view.View")
            aosPhoto2.click()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View[2]/android.widget.ImageView[1]") #이미지 출력
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View[2]/android.widget.ImageView[2]") #이미지 삭제 버튼 출력


            # 다음 버튼 클릭
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 권한")

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대")
            inviteBtn.click()
            time.sleep(3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_Face1\n출입기간")

            userClick = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_Face1\n출입기간")
            userClick.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_Face1\n출입기간\n모든 출입문")
            # 얼굴 아이콘을 특정할 수 없어 아이콘 출력 여부만 확인
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Test_Face1\n출입기간\n모든 출입문']/android.view.View[1]/android.widget.ImageView[1]")

            face_icon = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Test_Face1\n출입기간\n모든 출입문']/android.view.View[1]/android.widget.ImageView[2]")
            face_icon.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이름 및 얼굴")
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View[1]/android.widget.ImageView[1]")
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View[1]/android.widget.ImageView[2]")
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View[2]/android.widget.ImageView[1]")
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View[2]/android.widget.ImageView[2]")


            # Test_Face1 사용자 삭제
            for _ in range(2):
                self.driver.back()

            utils.user_delete(self)

            pass
            print("DQS_T15917 사용자 초대 성공 케이스 동작 확인[인증방식 : 얼굴 / 갤러리(이미지) 선택] | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15917 사용자 초대 성공 케이스 동작 확인[인증방식 : 얼굴 / 갤러리(이미지) 선택] | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T16914(self):
        try:
            print("DQS_T16914 사용자 초대 실패 케이스 동작 확인[인증방식 : 얼굴]")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 얼굴 인식 선택
            faceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "얼굴 인식")
            faceSetting.click()

            #이름 입력
            userInput1 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput1.click()
            userInput1.send_keys("Test_Face2")
            time.sleep(1)

            seleteFace1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+얼굴 1")
            seleteFace1.click()

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            #비슴한 얼굴 이미지
            aosPhoto1 = self.driver.find_element(AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[5]/android.view.View[7]/android.view.View[2]/android.view.View")
            aosPhoto1.click()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View/android.widget.ImageView[1]")

            next_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_Btn.click()

            invite_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대")
            invite_Btn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "얼굴 등록 실패")
            faceFail_Msg1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='얼굴의 회전 각도가 기준치를 초과하였습니다.\nf1000']")
            contentDesc1 = faceFail_Msg1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "얼굴의 회전 각도가 기준치를 초과하였습니다.\nf1000")

            confirm_btn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirm_btn.click()

            seleteFace2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+얼굴 2")
            seleteFace2.click()

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            #정상 얼굴 이미지
            aos_photo2 = self.driver.find_element(AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[5]/android.view.View[1]/android.view.View[2]/android.view.View")
            aos_photo2.click()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View/android.widget.ImageView[1]")

            next_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_Btn.click()

            invite_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대")
            invite_Btn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "얼굴 등록 실패")
            faceFail_Msg2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='얼굴의 회전 각도가 기준치를 초과하였습니다.\nf1000']")
            contentDesc2 = faceFail_Msg2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "얼굴의 회전 각도가 기준치를 초과하였습니다.\nf1000")

            confirm_btn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirm_btn.click()

            #얼굴이 아닌 이미지
            seleteFace3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View[1]/android.widget.ImageView[1]")
            seleteFace3.click()

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aos_photo3 = self.driver.find_element(AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[5]/android.view.View[4]/android.view.View[2]/android.view.View")
            aos_photo3.click()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View/android.widget.ImageView[1]")

            next_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_Btn.click()

            invite_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대")
            invite_Btn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "얼굴 등록 오류")
            faceFail_Msg3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='사진에서 얼굴을 찾을 수 없습니다.\nf1002']")
            contentDesc3 = faceFail_Msg3.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc3}")
            self.assertEqual(contentDesc3, "사진에서 얼굴을 찾을 수 없습니다.\nf1002")

            confirm_btn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirm_btn.click()

            # 정상 얼굴 이미지
            seleteFace4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View[1]/android.widget.ImageView[1]")
            seleteFace4.click()

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aos_photo4 = self.driver.find_element(AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]/android.view.View[2]/android.view.View")
            aos_photo4.click()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View/android.widget.ImageView[1]")

            next_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_Btn.click()

            invite_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대")
            invite_Btn.click()
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_Face2\n출입기간")

            utils.user_delete(self)

            pass
            print("DQS_T16914 사용자 초대 실패 케이스 동작 확인[인증방식 : 얼굴] | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T16914 사용자 초대 실패 케이스 동작 확인[인증방식 : 얼굴] | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15918(self):
        try:
            print("DQS_T15918 얼굴 인증 방식 수정 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 얼굴 인식 선택
            faceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "얼굴 인식")
            faceSetting.click()

            #이름 입력
            userInput1 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput1.click()
            userInput1.send_keys("Test_Face3")
            time.sleep(1)

            seleteFace1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+얼굴 1")
            seleteFace1.click()

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aosPhoto1 = self.driver.find_element(AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[5]/android.view.View[1]/android.view.View[2]/android.view.View")
            aosPhoto1.click()

            # 다음 버튼 클릭
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 권한")

            #초대 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대")
            inviteBtn.click()
            time.sleep(3)

            userClick = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_Face3\n출입기간")
            userClick.click()
            time.sleep(2)

            face_icon = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Test_Face3\n출입기간\n모든 출입문']/android.view.View[1]/android.widget.ImageView[2]")
            face_icon.click()
            time.sleep(1)

            modify_name = self.driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.EditText')
            modify_name.click()
            modify_name.clear()
            modify_name.send_keys("얼굴 수정 테스트")
            time.sleep(1)

            photo1_modity = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View/android.widget.ImageView[1]")
            photo1_modity.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카메라").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리").is_displayed()
            image_Msg1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지를 가져올 방법을 선택해주세요.")
            contentDesc1 = image_Msg1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "이미지를 가져올 방법을 선택해주세요.")

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aosPhoto2 = self.driver.find_element(AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[5]/android.view.View[3]/android.view.View[2]/android.view.View")
            aosPhoto2.click()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View/android.widget.ImageView[1]")

            photo2_modity = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View/android.widget.ImageView[1]")
            photo2_modity.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카메라").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리").is_displayed()
            image_Msg2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지를 가져올 방법을 선택해주세요.")
            contentDesc2 = image_Msg2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "이미지를 가져올 방법을 선택해주세요.")

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aosPhoto3 = self.driver.find_element(AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[5]/android.view.View[3]/android.view.View[2]/android.view.View")
            aosPhoto3.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사진 등록 실패")
            photo_Msg = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "동일한 사진은 등록할 수 없습니다.")
            contentDesc3 = photo_Msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc3}")
            self.assertEqual(contentDesc3, "동일한 사진은 등록할 수 없습니다.")

            confirm_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_btn.click()
            time.sleep(2)

            seleteFace2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+얼굴 2")
            seleteFace2.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카메라").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리").is_displayed()
            image_Msg2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지를 가져올 방법을 선택해주세요.")
            contentDesc2 = image_Msg2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "이미지를 가져올 방법을 선택해주세요.")

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aosPhoto4 = self.driver.find_element(AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[5]/android.view.View[3]/android.view.View[2]/android.view.View")
            aosPhoto4.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사진 등록 실패")
            photo_Msg = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "동일한 사진은 등록할 수 없습니다.")
            contentDesc3 = photo_Msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc3}")
            self.assertEqual(contentDesc3, "동일한 사진은 등록할 수 없습니다.")

            confirm_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_btn.click()
            time.sleep(1)

            seleteFace2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+얼굴 2")
            seleteFace2.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카메라").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리").is_displayed()
            image_Msg2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지를 가져올 방법을 선택해주세요.")
            contentDesc2 = image_Msg2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "이미지를 가져올 방법을 선택해주세요.")

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aosPhoto5 = self.driver.find_element(AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[5]/android.view.View[5]/android.view.View[2]/android.view.View")
            aosPhoto5.click()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View[2]/android.widget.ImageView[1]") #이미지 출력
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View[2]/android.widget.ImageView[2]") #이미지 삭제 버튼 출력

            # 1번 이미지 삭제
            photo1_delete = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View[1]/android.widget.ImageView[2]")
            photo1_delete.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View/android.widget.ImageView[1]")
            assert not self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+얼굴 2")

            seleteFace2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+얼굴 2")
            seleteFace2.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카메라").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리").is_displayed()
            image_Msg2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지를 가져올 방법을 선택해주세요.")
            contentDesc2 = image_Msg2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "이미지를 가져올 방법을 선택해주세요.")

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aosPhoto6 = self.driver.find_element(AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[5]/android.view.View[8]/android.view.View[2]/android.view.View")
            aosPhoto6.click()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View[2]/android.widget.ImageView[1]") #이미지 출력
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[2]/android.view.View[2]/android.widget.ImageView[2]") #이미지 삭제 버튼 출력

            modify_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modify_btn.click()
            time.sleep(3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "얼굴 수정 테스트\n출입기간\n모든 출입문")

            self.driver.back()
            time.sleep(1)

            utils.user_delete(self)

            pass
            print("DQS_T15918 얼굴 인증 방식 수정 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15918 얼굴 인증 방식 수정 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15915(self):
        try:
            print("DQS_T15915 카드 인증방식 설정 시 Validation 체크 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 지문 인식 선택
            qrSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "RF 카드")
            qrSetting.click()

            #이름 입력 - 한글 31자 입력 시도
            userInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput1.click()
            userInput1.send_keys("가나다라마바사아자차가나다라마바사아자차가나다라마바사아자차카")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='가나다라마바사아자차가나다라마바사아자차가나다라마바사아자차']").is_displayed()
            userInput1.clear()

            #이름 입력 - 영어 31자 입력 시도
            userInput2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput2.click()
            userInput2.send_keys("abcdefghijabcdefghijabcdefghijk")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='abcdefghijabcdefghijabcdefghij']").is_displayed()
            userInput2.clear()

            #이름 입력 - 일어 31자 입력 시도
            userInput3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput3.click()
            userInput3.send_keys("ユーザー名入力テストユーザー名入力テストユーザー名入力テストです")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='ユーザー名入力テストユーザー名入力テストユーザー名入力テスト']").is_displayed()
            userInput3.clear()

            #이름 입력 - 숫자 31자 입력 시도
            userInput4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput4.click()
            userInput4.send_keys("1234567890123456789012345678901")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123456789012345678901234567890']").is_displayed()
            userInput4.clear()

            #이름 입력 - 특수문자 입력 시도
            userInput5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput5.click()
            userInput5.send_keys("~!@#$%^&")
            time.sleep(1)

            # 다음 버튼 클릭 - 비활성화 확인(출입권한 화면으로 이동하지 않고 현재 화면 출력 확인)
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이름 및 카드").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='~!@#$%^&']").is_displayed()

            pass
            print("DQS_T15915 카드 인증방식 설정 시 Validation 체크 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15915 카드 인증방식 설정 시 Validation 체크 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15932(self):
        try:
            print("DQS_T15932 사용자 초대에서 카드 스캔 시 등록 가능한 장치가 없는 경우 동작 확인")

            # 카드 스캔 장치가 없는 공간으로 이동
            place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간")
            place.click()
            time.sleep(5)

            self.driver.tap([(787, 626)])
            time.sleep(3)

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 지문 인식 선택
            cardSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "RF 카드")
            cardSetting.click()

            # +카드 1 클릭
            card1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+ 카드 1")
            card1.click()
            time.sleep(1)

            # 등록가능 장치 없음 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카드 스캔").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "등록 가능한 장치가 없습니다.").is_displayed()

            pass
            print("사용자 초대에서 카드 스캔 시 등록 가능한 장치가 없는 경우 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("사용자 초대에서 카드 스캔 시 등록 가능한 장치가 없는 경우 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15933(self):
        try:
            print("DQS_T15933 사용자 초대에서 카드 스캔 타임아웃이 지난 경우 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 지문 인식 선택
            cardSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "RF 카드")
            cardSetting.click()

            #이름 입력
            userInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput.click()
            userInput.send_keys("Test_Card1_e2e")
            time.sleep(1)

            # +카드 1 클릭
            finger1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+ 카드 1")
            finger1.click()
            time.sleep(1)

            # 지문 등록장치 선택
            deviceFinger = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "XS2_ODPB-543478219")
            deviceFinger.click()
            time.sleep(22)

            # 스캔 타임 아웃 동작 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "첫번째 카드 입력\n스캔 가능 시간을 초과하였습니다.\n다시 시도해 주세요.\n카드 스캔 남은시간\n00:00")

            pass
            print("DQS_T15933 사용자 초대에서 카드 스캔 타임아웃이 지난 경우 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15933 사용자 초대에서 카드 스캔 타임아웃이 지난 경우 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15914(self):
        try:
            print("DQS_T15914 지문 인증방식 설정 시 Validation 체크 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 지문 인식 선택
            qrSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "지문 인식")
            qrSetting.click()

            #이름 입력 - 한글 31자 입력 시도
            userInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput1.click()
            userInput1.send_keys("가나다라마바사아자차가나다라마바사아자차가나다라마바사아자차카")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='가나다라마바사아자차가나다라마바사아자차가나다라마바사아자차']").is_displayed()
            userInput1.clear()

            #이름 입력 - 영어 31자 입력 시도
            userInput2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput2.click()
            userInput2.send_keys("abcdefghijabcdefghijabcdefghijk")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='abcdefghijabcdefghijabcdefghij']").is_displayed()
            userInput2.clear()

            #이름 입력 - 일어 31자 입력 시도
            userInput3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput3.click()
            userInput3.send_keys("ユーザー名入力テストユーザー名入力テストユーザー名入力テストです")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='ユーザー名入力テストユーザー名入力テストユーザー名入力テスト']").is_displayed()
            userInput3.clear()

            #이름 입력 - 숫자 31자 입력 시도
            userInput4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput4.click()
            userInput4.send_keys("1234567890123456789012345678901")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123456789012345678901234567890']").is_displayed()
            userInput4.clear()

            #이름 입력 - 특수문자 입력 시도
            userInput5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput5.click()
            userInput5.send_keys("~!@#$%^&")
            time.sleep(1)

            # 다음 버튼 클릭 - 비활성화 확인(출입권한 화면으로 이동하지 않고 현재 화면 출력 확인)
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이름 및 지문").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='~!@#$%^&']").is_displayed()

            pass
            print("DQS_T15914 지문 인증방식 설정 시 Validation 체크 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15914 지문 인증방식 설정 시 Validation 체크 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15922(self):
        try:
            print("DQS_T15922 사용자 초대에서 지문 스캔 시 등록 가능한 장치가 없는 경우 동작 확인")

            #지문 스캔 장치가 없는 공간으로 이동
            place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간")
            place.click()
            time.sleep(5)

            self.driver.tap([(787, 626)])
            time.sleep(3)

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 지문 인식 선택
            qrSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "지문 인식")
            qrSetting.click()

            # +지문 1 클릭
            finger1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+ 지문 1")
            finger1.click()
            time.sleep(1)

            # 등록가능 장치 없음 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "지문 스캔").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "등록 가능한 장치가 없습니다.").is_displayed()

            pass
            print("사용자 초대에서 지문 스캔 시 등록 가능한 장치가 없는 경우 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("사용자 초대에서 지문 스캔 시 등록 가능한 장치가 없는 경우 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15924(self):
        try:
            print("DQS_T15924 사용자 초대에서 지문 스캔 타임아웃이 지난 경우 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 지문 인식 선택
            qrSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "지문 인식")
            qrSetting.click()

            #이름 입력
            userInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput.click()
            userInput.send_keys("Test_Finger1_e2e")
            time.sleep(1)

            # +지문 1 클릭
            finger1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+ 지문 1")
            finger1.click()
            time.sleep(1)

            # 지문 등록장치 선택
            deviceFinger = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BLN2_OA_538761744")
            deviceFinger.click()
            time.sleep(22)

            # 스캔 타임 아웃 동작 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "첫번째 지문 입력\n스캔 가능 시간을 초과하였습니다.\n다시 시도해 주세요.\n지문 스캔 남은시간\n00:00")

            pass
            print("DQS_T15924 사용자 초대에서 지문 스캔 타임아웃이 지난 경우 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15924 사용자 초대에서 지문 스캔 타임아웃이 지난 경우 동작 확인 | Failed")
            print(str(e))
            self.fail()

if __name__ == '__main__':
    unittest.main()
