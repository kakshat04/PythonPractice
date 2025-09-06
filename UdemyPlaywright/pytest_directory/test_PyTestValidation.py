import pytest

@pytest.fixture(scope="session")
def do_setup():
    print("Doing setup")

class Test_Check:
    def test_initialcheck(self, do_setup):
        print("Testing initial check")

    @pytest.mark.smoke
    def test_check(self, initial_setup):
        print("Testing check")

    @pytest.mark.skip(reason="not implemented")
    def test_check2(self, do_setup, initial_setup):
        print("Testing 2 check")
