"""
Integration tests for the Theme Toggle functionality.

These tests verify that the theme toggle feature works correctly.
"""
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def setup_theme_test(client, selenium, live_server):
    """Set up the test by clearing localStorage and loading the page."""
    # Start the live server
    live_server.start()
    
    # Navigate to the page
    selenium.get(live_server.url())
    
    # Clear localStorage before each test
    selenium.execute_script("localStorage.removeItem('theme');")
    
    # Refresh to ensure clean state
    selenium.refresh()
    
    # Wait for page to fully load
    WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.ID, "theme-toggle"))
    )
    
    yield selenium
    
    # Clean up after the test
    selenium.execute_script("localStorage.removeItem('theme');")


class TestThemeToggle:
    """Tests for the theme toggle functionality."""
    
    def test_default_theme(self, setup_theme_test):
        """Test that the default theme is light."""
        selenium = setup_theme_test
        
        # Wait for theme to be fully applied
        WebDriverWait(selenium, 10).until(
            lambda s: "light-theme" in s.find_element(By.TAG_NAME, "body").get_attribute("class") or
                    "dark-theme" in s.find_element(By.TAG_NAME, "body").get_attribute("class")
        )
        
        # Check that body has 'light-theme' class
        body = selenium.find_element(By.TAG_NAME, "body")
        assert "light-theme" in body.get_attribute("class")
        
        # Verify local storage
        theme = selenium.execute_script("return localStorage.getItem('theme');")
        assert theme == "light" or theme is None  # None is acceptable for default behavior
        
    def test_toggle_to_dark_theme(self, setup_theme_test):
        """Test toggling from light to dark theme."""
        selenium = setup_theme_test
        
        # Check initial state
        body = selenium.find_element(By.TAG_NAME, "body")
        assert "light-theme" in body.get_attribute("class")
        
        # Find and click the theme toggle button
        toggle_button = selenium.find_element(By.ID, "theme-toggle")
        toggle_button.click()
        
        # Wait for theme to change
        WebDriverWait(selenium, 10).until(
            lambda s: "dark-theme" in s.find_element(By.TAG_NAME, "body").get_attribute("class")
        )
        
        # Check that body now has 'dark-theme' class
        body = selenium.find_element(By.TAG_NAME, "body")
        assert "dark-theme" in body.get_attribute("class")
        
        # Verify local storage
        theme = selenium.execute_script("return localStorage.getItem('theme');")
        assert theme == "dark"
        
    def test_theme_persistence(self, setup_theme_test):
        """Test that theme preference persists after page reload."""
        selenium = setup_theme_test
        
        # Toggle to dark theme
        toggle_button = selenium.find_element(By.ID, "theme-toggle")
        toggle_button.click()
        
        # Wait for theme to change
        WebDriverWait(selenium, 10).until(
            lambda s: "dark-theme" in s.find_element(By.TAG_NAME, "body").get_attribute("class")
        )
        
        # Verify dark theme is active
        body = selenium.find_element(By.TAG_NAME, "body")
        assert "dark-theme" in body.get_attribute("class")
        
        # Verify localStorage has been updated
        dark_theme = selenium.execute_script("return localStorage.getItem('theme');")
        assert dark_theme == "dark"
        
        # Refresh the page
        selenium.refresh()
        
        # Wait for page to load
        WebDriverWait(selenium, 10).until(
            EC.presence_of_element_located((By.ID, "theme-toggle"))
        )
        
        # Wait for theme to be applied
        WebDriverWait(selenium, 10).until(
            lambda s: "dark-theme" in s.find_element(By.TAG_NAME, "body").get_attribute("class")
        )
        
        # Check that body still has 'dark-theme' class
        body = selenium.find_element(By.TAG_NAME, "body")
        assert "dark-theme" in body.get_attribute("class")
        
        # Verify local storage
        theme = selenium.execute_script("return localStorage.getItem('theme');")
        assert theme == "dark"
        
    def test_toggle_back_to_light(self, setup_theme_test):
        """Test toggling from dark back to light theme."""
        selenium = setup_theme_test
        
        # Toggle to dark theme first
        toggle_button = selenium.find_element(By.ID, "theme-toggle")
        toggle_button.click()
        
        # Wait for theme to change
        WebDriverWait(selenium, 10).until(
            lambda s: "dark-theme" in s.find_element(By.TAG_NAME, "body").get_attribute("class")
        )
        
        # Verify dark theme is active
        body = selenium.find_element(By.TAG_NAME, "body")
        assert "dark-theme" in body.get_attribute("class")
        
        # Toggle back to light theme
        toggle_button = selenium.find_element(By.ID, "theme-toggle")
        toggle_button.click()
        
        # Wait for theme to change back
        WebDriverWait(selenium, 10).until(
            lambda s: "light-theme" in s.find_element(By.TAG_NAME, "body").get_attribute("class")
        )
        
        # Check that body now has 'light-theme' class
        body = selenium.find_element(By.TAG_NAME, "body")
        assert "light-theme" in body.get_attribute("class")
        
        # Verify local storage
        theme = selenium.execute_script("return localStorage.getItem('theme');")
        assert theme == "light"
        
    def test_toggle_button_icon(self, setup_theme_test):
        """Test that the toggle button icon changes with the theme."""
        selenium = setup_theme_test
        
        # Wait for icon to be present
        WebDriverWait(selenium, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#theme-toggle i"))
        )
        
        # Get initial icon class
        toggle_button = selenium.find_element(By.ID, "theme-toggle")
        initial_icon = toggle_button.find_element(By.TAG_NAME, "i").get_attribute("class")
        
        # Toggle theme
        toggle_button.click()
        
        # Wait for theme to change
        WebDriverWait(selenium, 10).until(
            lambda s: "dark-theme" in s.find_element(By.TAG_NAME, "body").get_attribute("class")
        )
        
        # Get new icon class
        toggle_button = selenium.find_element(By.ID, "theme-toggle")
        new_icon = toggle_button.find_element(By.TAG_NAME, "i").get_attribute("class")
        
        # Verify icon changed
        assert initial_icon != new_icon 