import pytest
from fixture.application import Application

fixture = None


@pytest.fixture(scope="session")
def app(request):
    global fixture
    fixture = Application()
    fixture.request = request

    return fixture
