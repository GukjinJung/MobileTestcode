"""
Web Utility Functions
Web CAM E2E Automation Test Framework
"""
import json
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional
from playwright.sync_api import Page, BrowserContext


class WebUtils:
    """Utility class for common web testing operations"""
    
    @staticmethod
    def take_timestamped_screenshot(page: Page, name: str, directory: str = "screenshots") -> str:
        """
        Take a screenshot with timestamp in filename.
        
        Args:
            page: Playwright page object
            name: Base name for the screenshot
            directory: Directory to save screenshots
            
        Returns:
            Path to the saved screenshot
        """
        Path(directory).mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        filepath = os.path.join(directory, filename)
        page.screenshot(path=filepath)
        return filepath
    
    @staticmethod
    def save_page_content(page: Page, name: str, directory: str = "html_dumps") -> str:
        """
        Save page HTML content for debugging.
        
        Args:
            page: Playwright page object
            name: Base name for the file
            directory: Directory to save HTML files
            
        Returns:
            Path to the saved file
        """
        Path(directory).mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.html"
        filepath = os.path.join(directory, filename)
        
        content = page.content()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        
        return filepath
    
    @staticmethod
    def get_browser_logs(page: Page) -> list:
        """
        Get browser console logs (for debugging).
        Note: Requires setting up console listener before page operations.
        
        Args:
            page: Playwright page object
            
        Returns:
            List of console messages
        """
        logs = []
        page.on("console", lambda msg: logs.append({
            "type": msg.type,
            "text": msg.text,
            "location": msg.location
        }))
        return logs
    
    @staticmethod
    def set_local_storage(page: Page, items: Dict[str, str]) -> None:
        """
        Set items in local storage.
        
        Args:
            page: Playwright page object
            items: Dictionary of key-value pairs to set
        """
        for key, value in items.items():
            page.evaluate(f"localStorage.setItem('{key}', '{value}')")
    
    @staticmethod
    def get_local_storage(page: Page, key: str) -> Optional[str]:
        """
        Get item from local storage.
        
        Args:
            page: Playwright page object
            key: Key to retrieve
            
        Returns:
            Value from local storage or None
        """
        return page.evaluate(f"localStorage.getItem('{key}')")
    
    @staticmethod
    def clear_local_storage(page: Page) -> None:
        """Clear all local storage"""
        page.evaluate("localStorage.clear()")
    
    @staticmethod
    def set_session_storage(page: Page, items: Dict[str, str]) -> None:
        """
        Set items in session storage.
        
        Args:
            page: Playwright page object
            items: Dictionary of key-value pairs to set
        """
        for key, value in items.items():
            page.evaluate(f"sessionStorage.setItem('{key}', '{value}')")
    
    @staticmethod
    def get_session_storage(page: Page, key: str) -> Optional[str]:
        """
        Get item from session storage.
        
        Args:
            page: Playwright page object
            key: Key to retrieve
            
        Returns:
            Value from session storage or None
        """
        return page.evaluate(f"sessionStorage.getItem('{key}')")
    
    @staticmethod
    def clear_session_storage(page: Page) -> None:
        """Clear all session storage"""
        page.evaluate("sessionStorage.clear()")
    
    @staticmethod
    def wait_for_network_idle(page: Page, timeout: int = 30000) -> None:
        """
        Wait for network to be idle.
        
        Args:
            page: Playwright page object
            timeout: Timeout in milliseconds
        """
        page.wait_for_load_state("networkidle", timeout=timeout)
    
    @staticmethod
    def execute_javascript(page: Page, script: str) -> Any:
        """
        Execute JavaScript in the page context.
        
        Args:
            page: Playwright page object
            script: JavaScript code to execute
            
        Returns:
            Result of the script execution
        """
        return page.evaluate(script)
    
    @staticmethod
    def get_cookies(context: BrowserContext) -> list:
        """
        Get all cookies from the browser context.
        
        Args:
            context: Playwright browser context
            
        Returns:
            List of cookies
        """
        return context.cookies()
    
    @staticmethod
    def add_cookies(context: BrowserContext, cookies: list) -> None:
        """
        Add cookies to the browser context.
        
        Args:
            context: Playwright browser context
            cookies: List of cookie dictionaries
        """
        context.add_cookies(cookies)
    
    @staticmethod
    def clear_cookies(context: BrowserContext) -> None:
        """Clear all cookies from the browser context"""
        context.clear_cookies()
    
    @staticmethod
    def generate_test_data(template: str, **kwargs) -> str:
        """
        Generate test data from template.
        
        Args:
            template: Template string with placeholders
            **kwargs: Values to substitute
            
        Returns:
            Formatted string
        """
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        kwargs.setdefault("timestamp", timestamp)
        return template.format(**kwargs)
