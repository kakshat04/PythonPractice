import pytest

@pytest.fixture(scope="session")
def initial_setup():
    print("Doing Initial setup")
    yield
    print("Closing Initial setup")