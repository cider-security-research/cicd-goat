import example


def test_add():
    assert example.add(1, 1) == 2
    assert not example.add(0, 1) == 2
