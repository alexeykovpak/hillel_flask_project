import requests, pytest, requests_mock
from test_fixtures import user_count_fixture
from homework2 import astros

def test_requirements_page_opens():
    value = requests.get('http://127.0.0.1:5000/requirements/')
    assert value.status_code == 200

def test_generate_users_page_generates_correct_quatity_of_users(user_count_fixture):
    value = requests.get(f'http://127.0.0.1:5000/generate-users/?user_count={user_count_fixture}')
    assert str(value.text).count('<li>') == user_count_fixture

def test_space_page_and_api_opens():
    source_code = requests.get('http://api.open-notify.org/astros.json').status_code
    value_code = requests.get('http://127.0.0.1:5000/space/').status_code
    assert source_code == value_code == 200

@pytest.mark.skipif(requests.get('http://api.open-notify.org/astros.json').status_code == 200, reason='API is reachable, cannot reproduce')
def test_space_page_and_api_dont_open():
    value_code = requests.get('http://127.0.0.1:5000/space/').status_code
    assert value_code != 200

def test_astros_output():
    session = requests.Session()
    adapter = requests_mock.Adapter()
    session.mount('mock://', adapter)
    adapter.register_uri('GET', 'mock://api.open-notify.org/astros.json', json={'number': 7})
    resp = session.get('mock://api.open-notify.org/astros.json')
    print()
    assert str(requests.get('http://127.0.0.1:5000/space/').text).count('<h1>There are 7 astronauts currently flying above Earth on spaceships.</h1>') == 1

