import requests
import pytest

APACHE_PORT = 8080
SNAKE_ROUTES = ["food_finder", "random"]


@pytest.mark.parametrize("snake", SNAKE_ROUTES)
def test_start(snake):
    """Check snake responds to /start request"""
    url = "http://localhost:%d/snakes/%s/start" % (APACHE_PORT, snake)
    resp = requests.post(url)

    assert resp.status_code != 404


@pytest.mark.parametrize("snake", SNAKE_ROUTES)
def test_move(snake):
    """Check snake responds to /move request"""
    url = "http://localhost:%d/snakes/%s/move" % (APACHE_PORT, snake)
    resp = requests.post(url)

    assert resp.status_code != 404
