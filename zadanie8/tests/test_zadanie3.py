import os
import time
import subprocess
import signal
import requests
import pytest

PROJECT = os.path.join(os.path.dirname(__file__), '..', '..', 'zadanie3')
JAR = os.path.join(PROJECT, 'build', 'libs', 'zadanie3-0.0.1-SNAPSHOT.jar')

@pytest.fixture(scope='session', autouse=True)
def server():
    subprocess.run(['./gradlew', 'bootJar', '--no-daemon'], cwd=PROJECT, check=True)
    proc = subprocess.Popen(['java', '-jar', JAR, '--spring.profiles.active=lazy'], cwd=PROJECT)
    for _ in range(30):
        try:
            requests.get('http://localhost:8080/api/users', timeout=1)
            break
        except Exception:
            time.sleep(1)
    yield
    proc.terminate()
    proc.wait()

BASE = 'http://localhost:8080'

valid_creds = [
    ('alice', 'password123'),
    ('bob', 'qwerty'),
    ('charlie', 'admin!')
]

invalid_creds = [
    ('alice', 'wrong'),
    ('bob', '123'),
    ('charlie', ''),
    ('baduser', 'password123'),
    ('', 'qwerty'),
    ('Alice', 'password123'),
    ('bob', 'qwerty1'),
    ('charlie', 'admin'),
    ('abc', 'def'),
    ('x', 'y')
]


def test_get_users_data():
    r = requests.get(f'{BASE}/api/users')
    assert r.status_code == 200
    assert r.headers['Content-Type'].startswith('application/json')
    data = r.json()
    assert len(data) == 3
    assert data[0]['id'] == 1
    assert data[0]['username'] == 'Jakub'
    assert data[1]['id'] == 2
    assert data[1]['username'] == 'Maciej'
    assert data[2]['id'] == 3
    assert data[2]['username'] == 'Tymoteusz'


def test_valid_logins():
    for u, p in valid_creds:
        r = requests.post(f'{BASE}/api/auth/login', json={'username': u, 'password': p})
        js = r.json()
        assert r.status_code == 200
        assert js['success'] is True
        assert js['user']['username'] == u
        assert js['token']


def test_invalid_logins():
    for u, p in invalid_creds:
        r = requests.post(f'{BASE}/api/auth/login', json={'username': u, 'password': p})
        js = r.json()
        assert r.status_code == 200
        assert js['success'] is False
        assert js['user'] is None
        assert js['token'] is None


def test_token_uniqueness():
    tokens = set()
    for _ in range(10):
        r = requests.post(f'{BASE}/api/auth/login', json={'username': 'alice', 'password': 'password123'})
        js = r.json()
        assert js['success'] is True
        assert js['token'] not in tokens
        tokens.add(js['token'])


def test_token_length():
    for _ in range(10):
        r = requests.post(f'{BASE}/api/auth/login', json={'username': 'alice', 'password': 'password123'})
        js = r.json()
        assert len(js['token']) > 20


def test_users_stable():
    for _ in range(5):
        r = requests.get(f'{BASE}/api/users')
        assert len(r.json()) == 3


def test_login_missing_fields():
    r = requests.post(f'{BASE}/api/auth/login', json={'username': 'alice'})
    assert r.status_code == 400


def test_login_malformed_json():
    r = requests.post(f'{BASE}/api/auth/login', data='{')
    assert r.status_code in (400, 415)


def test_endpoint_not_found():
    r = requests.get(f'{BASE}/nope')
    assert r.status_code == 404


def test_reject_get_to_login_endpoint():
    r = requests.get(f'{BASE}/api/auth/login')
    assert r.status_code == 405
