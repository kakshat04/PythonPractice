import pytest
import source.my_functions as myfunc

def test_add():
    result = myfunc.addition(10, 20)
    assert result == 30

def test_subtract():
    result = myfunc.subtraction(10, 20)
    assert result == -10

def test_divide():
    result = myfunc.division(10, 20)
    assert result == 0.5

def test_divide_divide_by_zero():
    with pytest.raises(ValueError):
        myfunc.division(20, 0)


@pytest.mark.abc
def test_subtraction():
    assert myfunc.subtraction(10, 20) == -10

@pytest.mark.skip
def test_skip():
    result = myfunc.addition(10, 20)
    assert result == 30

@pytest.mark.xfail(reason="not implemented")
def test_xfail():
    assert myfunc.subtraction(10, 0.5) == -10
