import pytest, random

@pytest.fixture
def user_count_fixture():
    return random.randint(1, 100)
