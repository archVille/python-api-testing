import pytest
import requests

def assert_status_code(response, expected_code):
    assert response.status_code == expected_code, f"Expected {expected_code}, but got {response.status_code}"

def assert_list_length(list_to_check, expected_length):
    assert len(list_to_check) == expected_length, f"the length was not correect for {len(list_to_check)}."

def test_api_call_with_custom_assertion():
    url = "https://example.com"
    response = requests.get(url)
    assert_status_code(response, 200)

def test_this_list():
    the_list = [1, 2, 3]
    assert_list_length(the_list, 3)

def test_another_request_response():
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/1'
    )
    assert response.status_code == 200
    assert response.json()['id'] == 1

def test_create_payload():
    payload = {'name' : 'Panos', 'email': 'test@email.com'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/users', json = payload
    )
    assert response.status_code == 201
    assert 'id' in response.json()

def test_update_payload():
    payload = {'name' : 'John'}
    response = requests.put(
        'https://jsonplaceholder.typicode.com/users/1', json = payload
    )
    assert response.status_code == 200
    assert response.json()['name'] == 'John'

def test_content_type():
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/1'
    )
    assert response.headers[
        'Content-Type'
    ] == 'application/json; charset=utf-8'

def test_delete_example():
    response = requests.delete(
        'https://jsonplaceholder.typicode.com/users/1'
    )
    assert response.status_code == 200


