import requests, pytest

def test_requirements_page_opens():
    value = requests.get('http://127.0.0.1:5000/requirements/')
    assert value.status_code == 200

@pytest.mark.xfail()
def test_generate_users_page_opens():
    value = requests.get('http://127.0.0.1:5000/generate-users/')
    print(f'Page URL is {value.url}')
    assert value.status_code == 200

def test_space_page_and_api_opens():
    source_code = requests.get('http://api.open-notify.org/astros.json').status_code
    value_code = requests.get('http://127.0.0.1:5000/space/').status_code
    assert source_code == value_code == 200

@pytest.mark.skipif(requests.get('http://api.open-notify.org/astros.json').status_code == 200, reason='API is reachable, cannot reproduce')
def test_space_page_and_api_dont_open():
    #source_code = requests.get('http://api.open-notify.org/astros.json').status_code
    value_code = requests.get('http://127.0.0.1:5000/space/').status_code
    assert value_code != 200
