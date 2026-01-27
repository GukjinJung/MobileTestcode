"""
API Utility Functions for Web Server Verification
Web CAM E2E Automation Test Framework
"""
import json
import requests
from typing import Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class APIResponse:
    """Data class for API response"""
    status_code: int
    headers: Dict[str, str]
    body: Any
    elapsed_time: float
    
    @property
    def json(self) -> Dict:
        """Return body as JSON if applicable"""
        if isinstance(self.body, dict):
            return self.body
        return {}
    
    @property
    def is_success(self) -> bool:
        """Check if response is successful (2xx status)"""
        return 200 <= self.status_code < 300


class APIUtils:
    """
    Utility class for API testing and Web Server verification.
    Use this for backend API validation alongside E2E tests.
    """
    
    def __init__(self, base_url: str, default_headers: Optional[Dict[str, str]] = None):
        """
        Initialize API Utils.
        
        Args:
            base_url: Base URL for API requests
            default_headers: Default headers to include in all requests
        """
        self.base_url = base_url.rstrip("/")
        self.default_headers = default_headers or {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        self.session = requests.Session()
        self.session.headers.update(self.default_headers)
    
    def _build_url(self, endpoint: str) -> str:
        """Build full URL from endpoint"""
        return f"{self.base_url}/{endpoint.lstrip('/')}"
    
    def _make_response(self, response: requests.Response) -> APIResponse:
        """Convert requests response to APIResponse"""
        try:
            body = response.json()
        except json.JSONDecodeError:
            body = response.text
        
        return APIResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            body=body,
            elapsed_time=response.elapsed.total_seconds()
        )
    
    def get(self, endpoint: str, params: Optional[Dict] = None, 
            headers: Optional[Dict] = None) -> APIResponse:
        """
        Make GET request.
        
        Args:
            endpoint: API endpoint
            params: Query parameters
            headers: Additional headers
            
        Returns:
            APIResponse object
        """
        url = self._build_url(endpoint)
        response = self.session.get(url, params=params, headers=headers)
        return self._make_response(response)
    
    def post(self, endpoint: str, data: Optional[Dict] = None,
             json_data: Optional[Dict] = None, headers: Optional[Dict] = None) -> APIResponse:
        """
        Make POST request.
        
        Args:
            endpoint: API endpoint
            data: Form data
            json_data: JSON data
            headers: Additional headers
            
        Returns:
            APIResponse object
        """
        url = self._build_url(endpoint)
        response = self.session.post(url, data=data, json=json_data, headers=headers)
        return self._make_response(response)
    
    def put(self, endpoint: str, data: Optional[Dict] = None,
            json_data: Optional[Dict] = None, headers: Optional[Dict] = None) -> APIResponse:
        """
        Make PUT request.
        
        Args:
            endpoint: API endpoint
            data: Form data
            json_data: JSON data
            headers: Additional headers
            
        Returns:
            APIResponse object
        """
        url = self._build_url(endpoint)
        response = self.session.put(url, data=data, json=json_data, headers=headers)
        return self._make_response(response)
    
    def patch(self, endpoint: str, data: Optional[Dict] = None,
              json_data: Optional[Dict] = None, headers: Optional[Dict] = None) -> APIResponse:
        """
        Make PATCH request.
        
        Args:
            endpoint: API endpoint
            data: Form data
            json_data: JSON data
            headers: Additional headers
            
        Returns:
            APIResponse object
        """
        url = self._build_url(endpoint)
        response = self.session.patch(url, data=data, json=json_data, headers=headers)
        return self._make_response(response)
    
    def delete(self, endpoint: str, headers: Optional[Dict] = None) -> APIResponse:
        """
        Make DELETE request.
        
        Args:
            endpoint: API endpoint
            headers: Additional headers
            
        Returns:
            APIResponse object
        """
        url = self._build_url(endpoint)
        response = self.session.delete(url, headers=headers)
        return self._make_response(response)
    
    def set_auth_token(self, token: str, token_type: str = "Bearer") -> None:
        """
        Set authentication token for subsequent requests.
        
        Args:
            token: Authentication token
            token_type: Token type (default: Bearer)
        """
        self.session.headers["Authorization"] = f"{token_type} {token}"
    
    def clear_auth_token(self) -> None:
        """Remove authentication token"""
        self.session.headers.pop("Authorization", None)
    
    def health_check(self, endpoint: str = "/health") -> bool:
        """
        Check if the server is healthy.
        
        Args:
            endpoint: Health check endpoint
            
        Returns:
            True if server responds with 2xx status
        """
        try:
            response = self.get(endpoint)
            return response.is_success
        except requests.RequestException:
            return False
    
    # Assertion Methods
    def assert_status_code(self, response: APIResponse, expected: int) -> None:
        """Assert response status code"""
        assert response.status_code == expected, \
            f"Expected status {expected}, got {response.status_code}"
    
    def assert_json_key_exists(self, response: APIResponse, key: str) -> None:
        """Assert JSON response contains key"""
        assert key in response.json, f"Key '{key}' not found in response"
    
    def assert_json_value(self, response: APIResponse, key: str, expected: Any) -> None:
        """Assert JSON response key has expected value"""
        actual = response.json.get(key)
        assert actual == expected, f"Expected {key}={expected}, got {actual}"
    
    def assert_response_time(self, response: APIResponse, max_seconds: float) -> None:
        """Assert response time is within limit"""
        assert response.elapsed_time <= max_seconds, \
            f"Response time {response.elapsed_time}s exceeds limit {max_seconds}s"
