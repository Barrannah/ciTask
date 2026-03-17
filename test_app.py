from app import add, greet


def test_greet_default():
    assert greet() == "Hello, CI!"


def test_greet_name():
    assert greet("Student") == "Hello, Student!"


def test_add_positive():
    assert add(2, 3) == 5
