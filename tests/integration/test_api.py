"""
Integration tests for the API endpoints.
"""
import json
import pytest


class TestHomeEndpoint:
    """Tests for the home page endpoint."""
    
    def test_home_page_loads(self, client):
        """Test that the home page loads successfully."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Error Message Translator' in response.data


class TestTranslateEndpoint:
    """Tests for the translation API endpoint."""
    
    def test_translate_valid_python_error(self, client, sample_python_error):
        """Test translating a valid Python error."""
        response = client.post(
            '/api/translate',
            data=json.dumps({
                'error_message': sample_python_error,
                'language': 'auto'
            }),
            content_type='application/json'
        )
        
        assert response.status_code == 200
        data = json.loads(response.data)
        
        assert data['language'] == 'python'
        assert 'title' in data
        assert 'explanation' in data
        assert 'solution' in data
        assert 'code_example' in data
    
    def test_translate_with_specified_language(self, client):
        """Test translating with a specified language."""
        response = client.post(
            '/api/translate',
            data=json.dumps({
                'error_message': 'This is a test error',
                'language': 'javascript'
            }),
            content_type='application/json'
        )
        
        assert response.status_code == 200
        data = json.loads(response.data)
        
        assert data['language'] == 'javascript'
    
    def test_translate_without_error_message(self, client):
        """Test the API handles missing error message."""
        response = client.post(
            '/api/translate',
            data=json.dumps({}),
            content_type='application/json'
        )
        
        assert response.status_code == 400
        data = json.loads(response.data)
        
        assert 'error' in data
        assert data['error'] == 'Missing error message'
    
    def test_translate_empty_error_message(self, client):
        """Test the API handles empty error message."""
        response = client.post(
            '/api/translate',
            data=json.dumps({
                'error_message': '',
            }),
            content_type='application/json'
        )
        
        assert response.status_code == 200
        data = json.loads(response.data)
        
        assert data['title'] == 'No error message provided'


class TestLanguagesEndpoint:
    """Tests for the languages API endpoint."""
    
    def test_get_languages(self, client):
        """Test that the languages endpoint returns languages."""
        response = client.get('/api/languages')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        
        assert isinstance(data, list)
        assert len(data) > 0
        
        # Check the structure of the language data
        for language in data:
            assert 'id' in language
            assert 'name' in language 