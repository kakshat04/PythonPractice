import pytest
import source.shapes as shapes


@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)

