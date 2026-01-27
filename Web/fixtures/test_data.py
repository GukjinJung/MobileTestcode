"""
Test Data for Web E2E Tests
Web CAM E2E Automation Test Framework

Store test data separately from test logic for better maintainability.
"""

# User credentials for testing
TEST_USERS = {
    "admin": {
        "username": "admin",
        "password": "admin123",
        "email": "admin@example.com",
        "role": "administrator"
    },
    "standard_user": {
        "username": "testuser",
        "password": "TestPass123!",
        "email": "testuser@example.com",
        "role": "user"
    },
    "invalid_user": {
        "username": "invalid",
        "password": "wrongpassword",
        "email": "invalid@example.com",
        "role": None
    }
}

# Form data templates
FORM_DATA = {
    "registration": {
        "first_name": "Test",
        "last_name": "User",
        "email": "test_{timestamp}@example.com",
        "phone": "010-1234-5678",
        "address": "Seoul, Korea"
    },
    "contact": {
        "name": "Test Contact",
        "email": "contact@example.com",
        "subject": "Test Subject",
        "message": "This is a test message."
    }
}

# Expected page titles
PAGE_TITLES = {
    "home": "Home - Web CAM",
    "login": "Login - Web CAM",
    "dashboard": "Dashboard - Web CAM",
    "settings": "Settings - Web CAM",
    "webcam": "Web Camera - Web CAM"
}

# URL paths
URL_PATHS = {
    "home": "/",
    "login": "/login",
    "dashboard": "/dashboard",
    "settings": "/settings",
    "webcam": "/cam",
    "api_health": "/api/health",
    "api_users": "/api/users"
}

# Error messages
ERROR_MESSAGES = {
    "invalid_login": "Invalid username or password",
    "required_field": "This field is required",
    "invalid_email": "Please enter a valid email address",
    "permission_denied": "You don't have permission to access this resource",
    "camera_blocked": "Camera access was denied"
}

# Success messages
SUCCESS_MESSAGES = {
    "login_success": "Successfully logged in",
    "logout_success": "Successfully logged out",
    "save_success": "Changes saved successfully",
    "upload_success": "File uploaded successfully",
    "capture_success": "Image captured successfully"
}

# Viewport configurations
VIEWPORTS = {
    "desktop": {"width": 1920, "height": 1080},
    "laptop": {"width": 1366, "height": 768},
    "tablet": {"width": 768, "height": 1024},
    "mobile": {"width": 375, "height": 667}
}

# Browser configurations
BROWSERS = {
    "chromium": {
        "name": "chromium",
        "channel": None
    },
    "chrome": {
        "name": "chromium",
        "channel": "chrome"
    },
    "firefox": {
        "name": "firefox",
        "channel": None
    },
    "webkit": {
        "name": "webkit",
        "channel": None
    }
}
