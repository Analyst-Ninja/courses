# Global file to store pytest fixtures
# It can useful when you have a large codebase with multiple shared objects

import pytest
from src.shapes import Rectangle


@pytest.fixture
def my_rectangle():
    return Rectangle(length=10, breadth=8)


@pytest.fixture
def weird_rectangle():
    return Rectangle(length=5, breadth=8)
