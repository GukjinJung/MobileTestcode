"""
Sample Page Object - Example implementation
Web CAM E2E Automation Test Framework
"""
from playwright.sync_api import Page
from .base_page import BasePage


class SamplePage(BasePage):
    """
    Sample Page Object demonstrating Page Object Model pattern.
    Replace this with actual page objects for your application.
    """
    
    # Selectors (CSS, XPath, or Playwright selectors)
    SELECTORS = {
        "header": "header",
        "main_content": "main",
        "footer": "footer",
        "nav_menu": "nav",
        "login_button": "[data-testid='login-btn']",
        "username_input": "#username",
        "password_input": "#password",
        "submit_button": "button[type='submit']",
        "error_message": ".error-message",
        "success_message": ".success-message",
    }
    
    def __init__(self, page: Page, base_url: str = ""):
        super().__init__(page, base_url)
    
    # Page-specific Actions
    def login(self, username: str, password: str) -> None:
        """Perform login action"""
        self.fill(self.SELECTORS["username_input"], username)
        self.fill(self.SELECTORS["password_input"], password)
        self.click(self.SELECTORS["submit_button"])
    
    def get_error_message(self) -> str:
        """Get error message text"""
        return self.get_text(self.SELECTORS["error_message"])
    
    def get_success_message(self) -> str:
        """Get success message text"""
        return self.get_text(self.SELECTORS["success_message"])
    
    def is_logged_in(self) -> bool:
        """Check if user is logged in"""
        return self.is_visible(self.SELECTORS["success_message"])
    
    def click_login_button(self) -> None:
        """Click the login button in navigation"""
        self.click(self.SELECTORS["login_button"])
    
    # Validation Methods
    def verify_page_loaded(self) -> bool:
        """Verify the page has loaded correctly"""
        return (
            self.is_visible(self.SELECTORS["header"]) and
            self.is_visible(self.SELECTORS["main_content"]) and
            self.is_visible(self.SELECTORS["footer"])
        )
    
    def verify_navigation_visible(self) -> bool:
        """Verify navigation menu is visible"""
        return self.is_visible(self.SELECTORS["nav_menu"])
