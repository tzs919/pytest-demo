import pytest
import requests
import tests.app as app


class MockResponse:
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


# monkeypatch操作移到fixture中
@pytest.fixture
def mock_response(monkeypatch):
    """Requests.get() mock返回json值： {'mock_key':'mock_response'}."""

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)


# 注意我们的测试函数传入的是fixture方法，而不是直接传入monkeypatch
def test_get_json(mock_response):
    result = app.get_json("https://fakeurl")
    assert result["mock_key"] == "mock_response"
