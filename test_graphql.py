import requests
import pytest

# def test_graphql_query():
#     url = 'https://api.example.com/graphql'
#     query = '''
#     {
#         user(id:666){
#             id
#             name
#         }
#     }
#     '''

#     response = requests.post(url, json={'query': query})
#     assert response.status_code == 200
#     assert response.json()['data']['user']['id'] == 666