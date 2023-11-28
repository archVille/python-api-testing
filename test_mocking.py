from unittest.mock import patch
import requests
import pytest

def mock_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse({"key": "value"}, 200)

def test_mocked_api():
    with patch('requests.get', mock_get):
        response = requests.get('https://google.co.uk')
        assert response.json()['key'] == 'value'