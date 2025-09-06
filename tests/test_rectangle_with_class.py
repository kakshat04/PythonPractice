import source.shapes as shapes


class TestRectangle:
    def setup_method(self, method):
        self.rect = shapes.Rectangle(10, 20)
        print(f"Inside setup method {method}")

    def teardown_method(self, method):
        print(f"Inside teardown method {method}")

    def test_area(self):
        assert self.rect.area() == self.rect.width * self.rect.height

    def test_perimited(self):
        assert self.rect.perimeter() == 2 * self.rect.width + self.rect.height
