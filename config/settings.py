# 환경 설정
import os
from pathlib import Path

# 프로젝트 루트 기준 상대 경로
BASE_URL = "https://stage.moon.supremainc.com"
BROWSER_TYPE = "chromium"
HEADLESS = False
TIMEOUT = 30000
SCREENSHOT_DIR = "reports/screenshots"
LOG_DIR = "reports/logs"
VIEWPORT = {"width": 1920, "height": 1080}

# 디렉토리 보장
os.makedirs(SCREENSHOT_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)
