def test_area(my_rectangle):
    assert my_rectangle.area() == my_rectangle.width * my_rectangle.height


def test_perimited(my_rectangle):
    assert my_rectangle.perimeter()  == 2 * my_rectangle.width + my_rectangle.height