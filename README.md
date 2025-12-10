# 웹 E2E 테스트 코드

이 리포지토리는 Playwright + Pytest 기반의 웹 E2E 테스트 예제입니다.

## 요구 사항
- Python 3.10+
- pip

## 설치
```bash
pip install -r requirements.txt
python -m playwright install chromium
```

## 실행
```bash
pytest
```

## 구조
- `tests/`: 테스트 케이스 및 픽스처
- `pages/`: Page Object 클래스
- `utils/`: 유틸리티 (브라우저, 대기, 스크린샷, 이미지 인식, 로거)
- `config/`: 설정과 상수
- `resources/`: 테스트 데이터와 좌표/이미지 리소스
- `reports/`: 스크린샷 및 로그 출력

## 참고
- OCR(pytesseract)와 OpenCV 사용은 선택적입니다. 환경에 Tesseract 바이너리가 없으면 OCR 관련 기능은 자동으로 건너뜁니다.
