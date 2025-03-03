"""
Integration tests for the Recent Searches functionality.

These tests verify that the recent searches feature works correctly.
They use Selenium to interact with the browser's localStorage.
"""
import json
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def setup_recent_searches(client, selenium, live_server):
    """Set up the test by clearing localStorage and loading the page."""
    # Start the live server
    live_server.start()
    
    # Navigate to the page
    selenium.get(live_server.url())
    
    # Clear localStorage before each test
    selenium.execute_script("localStorage.removeItem('recentSearches');")
    
    # Refresh to ensure clean state
    selenium.refresh()
    
    yield selenium
    
    # Clean up after the test
    selenium.execute_script("localStorage.removeItem('recentSearches');")


class TestRecentSearches:
    """Tests for the recent searches functionality."""
    
    def test_initially_empty(self, setup_recent_searches):
        """Test that recent searches is initially empty."""
        selenium = setup_recent_searches
        
        # Check that the empty message is displayed
        empty_message = selenium.find_element(By.CSS_SELECTOR, ".searches-container .empty-message")
        assert "Your recent searches will appear here" in empty_message.text
        
    def test_add_single_search(self, setup_recent_searches):
        """Test adding a single search item."""
        selenium = setup_recent_searches
        
        # Input an error message
        error_input = selenium.find_element(By.ID, "error-input")
        error_input.send_keys("SyntaxError: invalid syntax")
        
        # Select Python as the language
        selenium.find_element(By.ID, "language-select").click()
        selenium.find_element(By.CSS_SELECTOR, "option[value='python']").click()
        
        # Click the translate button
        selenium.find_element(By.ID, "translate-btn").click()
        
        # Wait for the translation to complete
        WebDriverWait(selenium, 10).until(
            EC.visibility_of_element_located((By.ID, "translation-content"))
        )
        
        # Verify that the recent searches container now has an item
        searches_container = selenium.find_element(By.ID, "searches-container")
        search_items = searches_container.find_elements(By.CSS_SELECTOR, ".search-item")
        
        assert len(search_items) == 1
        assert "SyntaxError" in search_items[0].text
        assert "Python" in search_items[0].text
        
    def test_multiple_searches_order(self, setup_recent_searches):
        """Test adding multiple searches and verify they're ordered correctly."""
        selenium = setup_recent_searches
        
        # Add first search
        error_input = selenium.find_element(By.ID, "error-input")
        error_input.send_keys("SyntaxError: invalid syntax")
        selenium.find_element(By.ID, "translate-btn").click()
        
        # Wait for the translation
        WebDriverWait(selenium, 10).until(
            EC.visibility_of_element_located((By.ID, "translation-content"))
        )
        
        # Clear input and add second search
        selenium.find_element(By.ID, "clear-btn").click()
        error_input = selenium.find_element(By.ID, "error-input")
        error_input.send_keys("TypeError: cannot concatenate str and int objects")
        selenium.find_element(By.ID, "translate-btn").click()
        
        # Wait for the second translation
        time.sleep(2)  # Additional wait to ensure UI updates
        
        # Get search items
        searches_container = selenium.find_element(By.ID, "searches-container")
        search_items = searches_container.find_elements(By.CSS_SELECTOR, ".search-item")
        
        # Verify order (most recent first)
        assert len(search_items) == 2
        assert "TypeError" in search_items[0].text
        assert "SyntaxError" in search_items[1].text
        
    def test_persistence_after_refresh(self, setup_recent_searches):
        """Test that searches persist after page refresh."""
        selenium = setup_recent_searches
        
        # Add a search
        error_input = selenium.find_element(By.ID, "error-input")
        error_input.send_keys("SyntaxError: invalid syntax")
        selenium.find_element(By.ID, "translate-btn").click()
        
        # Wait for the translation
        WebDriverWait(selenium, 10).until(
            EC.visibility_of_element_located((By.ID, "translation-content"))
        )
        
        # Verify localStorage has been updated
        local_storage = selenium.execute_script("return localStorage.getItem('recentSearches');")
        assert local_storage is not None
        
        # Refresh the page
        selenium.refresh()
        
        # Wait for page to load completely
        WebDriverWait(selenium, 10).until(
            EC.presence_of_element_located((By.ID, "searches-container"))
        )
        
        # Additional wait to ensure recent searches are loaded
        WebDriverWait(selenium, 10).until(
            lambda s: len(s.find_elements(By.CSS_SELECTOR, ".search-item")) > 0 or
                     len(s.find_elements(By.CSS_SELECTOR, ".searches-container .empty-message")) > 0
        )
        
        # Verify the search is still there
        searches_container = selenium.find_element(By.ID, "searches-container")
        search_items = searches_container.find_elements(By.CSS_SELECTOR, ".search-item")
        
        assert len(search_items) == 1
        assert "SyntaxError" in search_items[0].text
        
    def test_click_loads_translation(self, setup_recent_searches):
        """Test that clicking a search item loads its translation."""
        selenium = setup_recent_searches
        
        # Add a search
        error_input = selenium.find_element(By.ID, "error-input")
        error_input.send_keys("SyntaxError: invalid syntax")
        selenium.find_element(By.ID, "translate-btn").click()
        
        # Wait for the translation
        WebDriverWait(selenium, 10).until(
            EC.visibility_of_element_located((By.ID, "translation-content"))
        )
        
        # Clear the translation (hide it)
        selenium.execute_script("document.getElementById('translation-content').style.display = 'none';")
        selenium.execute_script("document.getElementById('result-placeholder').style.display = 'flex';")
        
        # Click the search item
        search_item = selenium.find_element(By.CSS_SELECTOR, ".search-item")
        search_item.click()
        
        # Wait for the translation to be shown again
        WebDriverWait(selenium, 10).until(
            EC.visibility_of_element_located((By.ID, "translation-content"))
        )
        
        # Verify the translation content
        translation_title = selenium.find_element(By.ID, "error-title").text
        assert "SyntaxError" in translation_title
        
    def test_clear_all_button(self, setup_recent_searches):
        """Test that the Clear All button works."""
        selenium = setup_recent_searches
        
        # Add a search
        error_input = selenium.find_element(By.ID, "error-input")
        error_input.send_keys("SyntaxError: invalid syntax")
        selenium.find_element(By.ID, "translate-btn").click()
        
        # Wait for the translation
        WebDriverWait(selenium, 10).until(
            EC.visibility_of_element_located((By.ID, "translation-content"))
        )
        
        # Verify search item exists
        searches_container = selenium.find_element(By.ID, "searches-container")
        search_items = searches_container.find_elements(By.CSS_SELECTOR, ".search-item")
        assert len(search_items) == 1
        
        # Click the Clear All button
        clear_button = selenium.find_element(By.ID, "clear-searches-btn")
        clear_button.click()
        
        # Wait for the empty message to reappear
        WebDriverWait(selenium, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".searches-container .empty-message"))
        )
        
        # Verify the search items are gone
        searches_container = selenium.find_element(By.ID, "searches-container")
        search_items = searches_container.find_elements(By.CSS_SELECTOR, ".search-item")
        assert len(search_items) == 0
        
        # Verify localStorage is cleared
        local_storage = selenium.execute_script("return localStorage.getItem('recentSearches');")
        assert local_storage is None
        
    def test_empty_error_message(self, setup_recent_searches):
        """Test that empty error messages don't get added to recent searches."""
        selenium = setup_recent_searches
        
        # Submit an empty error message
        error_input = selenium.find_element(By.ID, "error-input")
        error_input.send_keys("")
        
        # Select Python as the language
        selenium.find_element(By.ID, "language-select").click()
        selenium.find_element(By.CSS_SELECTOR, "option[value='python']").click()
        
        # Click the translate button
        selenium.find_element(By.ID, "translate-btn").click()
        
        # Wait for a moment
        time.sleep(2)
        
        # Verify that recent searches container is still empty
        searches_container = selenium.find_element(By.ID, "searches-container")
        search_items = searches_container.find_elements(By.CSS_SELECTOR, ".search-item")
        
        # Should have no searches
        assert len(search_items) == 0
        
        # Verify empty message is still shown
        empty_message = selenium.find_element(By.CSS_SELECTOR, ".searches-container .empty-message")
        assert "Your recent searches will appear here" in empty_message.text