"""
Base Page Object - Common methods for all page objects
Web CAM E2E Automation Test Framework
"""
from playwright.sync_api import Page, Locator, expect
from typing import Optional


class BasePage:
    """
    Base Page Object containing common methods for all pages.
    All page objects should inherit from this class.
    """
    
    def __init__(self, page: Page, base_url: str = ""):
        self.page = page
        self.base_url = base_url
    
    # Navigation Methods
    def navigate(self, path: str = "") -> None:
        """Navigate to a specific path"""
        url = f"{self.base_url}{path}" if self.base_url else path
        self.page.goto(url)
    
    def reload(self) -> None:
        """Reload the current page"""
        self.page.reload()
    
    def go_back(self) -> None:
        """Navigate back in browser history"""
        self.page.go_back()
    
    def go_forward(self) -> None:
        """Navigate forward in browser history"""
        self.page.go_forward()
    
    # Element Interaction Methods
    def click(self, selector: str) -> None:
        """Click an element"""
        self.page.click(selector)
    
    def double_click(self, selector: str) -> None:
        """Double click an element"""
        self.page.dblclick(selector)
    
    def right_click(self, selector: str) -> None:
        """Right click an element"""
        self.page.click(selector, button="right")
    
    def fill(self, selector: str, text: str) -> None:
        """Fill text into an input field"""
        self.page.fill(selector, text)
    
    def clear(self, selector: str) -> None:
        """Clear an input field"""
        self.page.fill(selector, "")
    
    def type_text(self, selector: str, text: str, delay: int = 50) -> None:
        """Type text character by character with delay"""
        self.page.type(selector, text, delay=delay)
    
    def select_option(self, selector: str, value: str) -> None:
        """Select option from dropdown by value"""
        self.page.select_option(selector, value)
    
    def check(self, selector: str) -> None:
        """Check a checkbox"""
        self.page.check(selector)
    
    def uncheck(self, selector: str) -> None:
        """Uncheck a checkbox"""
        self.page.uncheck(selector)
    
    def hover(self, selector: str) -> None:
        """Hover over an element"""
        self.page.hover(selector)
    
    # Wait Methods
    def wait_for_selector(self, selector: str, timeout: int = 30000) -> Locator:
        """Wait for an element to appear"""
        return self.page.wait_for_selector(selector, timeout=timeout)
    
    def wait_for_load_state(self, state: str = "networkidle") -> None:
        """Wait for page load state"""
        self.page.wait_for_load_state(state)
    
    def wait_for_url(self, url: str, timeout: int = 30000) -> None:
        """Wait for URL to match"""
        self.page.wait_for_url(url, timeout=timeout)
    
    def wait_for_timeout(self, timeout: int) -> None:
        """Wait for specified milliseconds"""
        self.page.wait_for_timeout(timeout)
    
    # Element State Methods
    def is_visible(self, selector: str) -> bool:
        """Check if element is visible"""
        return self.page.is_visible(selector)
    
    def is_enabled(self, selector: str) -> bool:
        """Check if element is enabled"""
        return self.page.is_enabled(selector)
    
    def is_checked(self, selector: str) -> bool:
        """Check if checkbox is checked"""
        return self.page.is_checked(selector)
    
    def is_hidden(self, selector: str) -> bool:
        """Check if element is hidden"""
        return self.page.is_hidden(selector)
    
    # Get Element Properties
    def get_text(self, selector: str) -> str:
        """Get text content of an element"""
        return self.page.text_content(selector) or ""
    
    def get_inner_text(self, selector: str) -> str:
        """Get inner text of an element"""
        return self.page.inner_text(selector)
    
    def get_inner_html(self, selector: str) -> str:
        """Get inner HTML of an element"""
        return self.page.inner_html(selector)
    
    def get_attribute(self, selector: str, attribute: str) -> Optional[str]:
        """Get attribute value of an element"""
        return self.page.get_attribute(selector, attribute)
    
    def get_input_value(self, selector: str) -> str:
        """Get value of an input field"""
        return self.page.input_value(selector)
    
    # Screenshot and Video
    def take_screenshot(self, path: str, full_page: bool = False) -> None:
        """Take a screenshot"""
        self.page.screenshot(path=path, full_page=full_page)
    
    # Locator Methods
    def locator(self, selector: str) -> Locator:
        """Get locator for an element"""
        return self.page.locator(selector)
    
    def get_by_role(self, role: str, **kwargs) -> Locator:
        """Get element by ARIA role"""
        return self.page.get_by_role(role, **kwargs)
    
    def get_by_text(self, text: str, exact: bool = False) -> Locator:
        """Get element by text content"""
        return self.page.get_by_text(text, exact=exact)
    
    def get_by_label(self, text: str) -> Locator:
        """Get element by label"""
        return self.page.get_by_label(text)
    
    def get_by_placeholder(self, text: str) -> Locator:
        """Get element by placeholder"""
        return self.page.get_by_placeholder(text)
    
    def get_by_test_id(self, test_id: str) -> Locator:
        """Get element by test ID (data-testid attribute)"""
        return self.page.get_by_test_id(test_id)
    
    # Assertion Methods
    def expect_visible(self, selector: str) -> None:
        """Assert element is visible"""
        expect(self.page.locator(selector)).to_be_visible()
    
    def expect_hidden(self, selector: str) -> None:
        """Assert element is hidden"""
        expect(self.page.locator(selector)).to_be_hidden()
    
    def expect_text(self, selector: str, text: str) -> None:
        """Assert element has specific text"""
        expect(self.page.locator(selector)).to_have_text(text)
    
    def expect_value(self, selector: str, value: str) -> None:
        """Assert input has specific value"""
        expect(self.page.locator(selector)).to_have_value(value)
    
    def expect_url(self, url: str) -> None:
        """Assert current URL matches"""
        expect(self.page).to_have_url(url)
    
    def expect_title(self, title: str) -> None:
        """Assert page title matches"""
        expect(self.page).to_have_title(title)
    
    # Page Properties
    @property
    def title(self) -> str:
        """Get page title"""
        return self.page.title()
    
    @property
    def url(self) -> str:
        """Get current URL"""
        return self.page.url
