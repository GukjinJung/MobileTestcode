# 자동화 플랜

## 테스트 프레임워크 개요

본 프로젝트는 **Mobile App (Appium)** 과 **Web E2E (Playwright)** 테스트를 모두 지원합니다.

| 구분 | 프레임워크 | 언어 | 대상 |
|------|-----------|------|------|
| Mobile | Appium + UiAutomator2 | Python | Android/iOS 앱 |
| Web | Playwright + Pytest | Python | Web CAM 애플리케이션 |

---

## Web E2E 테스트 환경 구성 (Playwright)

### 사전 요구사항
- Python 3.8 이상
- IntelliJ IDEA (Python Plugin 설치)

### 환경 설정

```bash
# 1. 가상환경 생성 (권장)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. 의존성 설치
pip install -r requirements.txt

# 3. Playwright 브라우저 설치
playwright install

# 4. 테스트 실행
pytest Web/tests/ -v
```

### IntelliJ 설정
1. **File > Project Structure > SDKs** 에서 Python 인터프리터 추가
2. **File > Project Structure > Modules** 에서 `Web` 폴더를 Sources로 지정
3. **Run > Edit Configurations** 에서 pytest 설정 추가

### 폴더 구조
```
Web/
├── __init__.py          # 패키지 초기화
├── conftest.py          # Pytest 설정 및 픽스처
├── pages/               # Page Object Model
│   ├── __init__.py
│   ├── base_page.py     # 기본 페이지 클래스
│   └── sample_page.py   # 샘플 페이지 객체
├── tests/               # 테스트 케이스
│   ├── __init__.py
│   ├── test_sample.py   # 샘플 테스트
│   └── test_webcam.py   # Web CAM 테스트
├── utils/               # 유틸리티 함수
│   ├── __init__.py
│   ├── web_utils.py     # 웹 유틸리티
│   └── api_utils.py     # API 유틸리티
└── fixtures/            # 테스트 데이터
    ├── __init__.py
    └── test_data.py     # 테스트 데이터 정의
```

### 설정 파일
- `configuration/web_config.json` - 웹 테스트 설정
- `pytest.ini` - Pytest 설정

---

## Mobile 테스트 프레임워크 (Appium)

###  테스트 프레임워크 선정 기준

+ Flutter 로 개발된 Application 의 경우 Flutter Integration Test 를 활용 하겠지만, (Key 작성 과 Widget 에 Key 를 넣어줘야 하는 과정이 존재하지만 Appium 에 비해 강력하고 변하지 않는 Selector 그러나 Flutter 로 개발된 Application 에서만 사용 가능함)
  
+ Application 을 검증해야 하는 과제 이므로
Mobile Automation Test 에 널리 활용되고 있으며 크로스 플랫폼 (IOS/AOS) 사용 가능하고 또한 언어 및 프레임워크의 유연성을 가진 (Java,Python,JavaScript,Ruby) 
하이브리드,네이티브 모두 활용가능한 Appium 을 활용.


### GUI로 자동화 가능한 영역

+ Video 컴포넌트 제외 모든 UI 
"CLUe" 의 모든 UI (Click,Swipe,Scrolling,SendKey 등의 UI와 상호작용이 가능한 영역)
+ 본 Test에 필요한 최소한의 함수들은 Uitl 파일에 작성 하였습니다. 자세한 사항은 파일 안의 내용 확인 부탁드립니다.

### API 자동화 가능한 영역

+ 협의 후 확정 예정
### 자동화 구현 중 발생 할 수 있는 문제점 및 해결 방안

+ 추가 된 UI 로 인한 Selector 변경
  + Xpath 등의 변경이 쉬운 Selector 로 Code 를 구성한 경우 UI 가 변경될 경우 이전 Code 를 찾아가 새로운 Xpath 로 변경해야하는 번거로움이 있음
    + 하여 개발자와의 협업을 통해 ClassName 으로 UI 를 정의 하는것이 이상적인 방향

+ 동기화 문제 (타이밍 이슈)
  + UI 간 상호작용 중 네트워크 및 테스트 디바이스 성능 이슈로 인하여 다음 코드를 실행하지 못하는 Test Fail 이 자주 발샐된다, 이를 방지하기 위하여 sleep time 을 적절히 사용해야 한다
+ Test Code 의 복잡성
  + Test code 가 과다하게 복잡해지는 경우 lagacy code 를 야기한다, 하여 항상 타 QE 들과 Review 과정을 진행하고, Test code 는 간결하고 명확하게 작성할 수 있도록 해야한다. (함수명,클래스명,폴더명 등등)  

### 테스트 리포트 구성 방안

+ Intellij Test Report 제공 (HTML 형태 간결한 UI)
+ Reporting Frameword 활용 (Allure,ReportNG)
+ Slack 을 통한 Report 자동 전송 (Test 종료 시 설정된 Email 로 전송하는 방법)
+ Jenkins/Firebase Testlab 의 TestReport 활용
