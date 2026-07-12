def test_area(my_rectangle):
    assert my_rectangle.area() == my_rectangle.length * my_rectangle.breadth


def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 2 * (my_rectangle.length + my_rectangle.breadth)


def test_rectangle_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle
