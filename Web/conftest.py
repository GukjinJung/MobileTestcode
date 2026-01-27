"""
Pytest Configuration for Web E2E Tests with Playwright
Web CAM E2E Automation Test Framework
"""
import json
import os
import pytest
from pathlib import Path
from playwright.sync_api import Playwright, Browser, BrowserContext, Page


def load_config():
    """Load web configuration from JSON file"""
    config_path = Path(__file__).parent.parent / "configuration" / "web_config.json"
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def config():
    """Provide configuration to tests"""
    return load_config()


@pytest.fixture(scope="session")
def browser_type_launch_args(config):
    """Browser launch arguments"""
    return {
        "headless": config.get("headless", False),
        "slow_mo": config.get("slow_mo", 0),
    }


@pytest.fixture(scope="session")
def browser(playwright: Playwright, config, browser_type_launch_args) -> Browser:
    """Create browser instance based on configuration"""
    browser_name = config.get("browser", "chromium")
    
    if browser_name == "chromium":
        browser = playwright.chromium.launch(**browser_type_launch_args)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(**browser_type_launch_args)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(**browser_type_launch_args)
    else:
        browser = playwright.chromium.launch(**browser_type_launch_args)
    
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser: Browser, config) -> BrowserContext:
    """Create browser context with viewport settings"""
    viewport = config.get("viewport", {"width": 1920, "height": 1080})
    
    context_options = {
        "viewport": viewport,
        "record_video_dir": "videos/" if config.get("video_recording", False) else None,
    }
    
    # Remove None values
    context_options = {k: v for k, v in context_options.items() if v is not None}
    
    context = browser.new_context(**context_options)
    
    # Set default timeout
    context.set_default_timeout(config.get("timeout", 30000))
    
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext, config) -> Page:
    """Create new page for each test"""
    page = context.new_page()
    
    # Navigate to base URL if configured
    base_url = config.get("base_url")
    if base_url:
        page.goto(base_url)
    
    yield page
    page.close()


@pytest.fixture(scope="function")
def base_url(config) -> str:
    """Provide base URL to tests"""
    return config.get("base_url", "http://localhost:8080")


# Hooks for screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Take screenshot on test failure"""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            screenshot_path = screenshot_dir / f"{item.name}.png"
            page.screenshot(path=str(screenshot_path))
            print(f"\nScreenshot saved: {screenshot_path}")
