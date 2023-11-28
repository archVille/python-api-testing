import pytest
import requests

@pytest.mark.benchmark
def test_api_perf(benchmark):
    @benchmark
    def make_request():
        response = requests.get('https://google.co.uk')
        assert response.status_code == 200