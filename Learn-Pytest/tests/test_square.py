import pytest
from src.shapes import Square


@pytest.mark.parametrize("side_length, expected_area", [(2, 4), (3, 9), (9, 81)])
def test_multiple_square_areas(side_length, expected_area):
    assert Square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_perimter", [(1, 4), (4, 16), (16, 64)])
def test_multiple_square_perimeter(side_length, expected_perimter):
    assert Square(side_length=side_length).perimeter() == expected_perimter
