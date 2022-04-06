# A test file for test_pytest_cov.py:test_contexts

import unittest

import pytest


def test_01():
    assert 1 == 1                                   # r1


def test_02():
    assert 2 == 2                                   # r2


class OldStyleTests(unittest.TestCase):
    items = []

    @classmethod
    def setUpClass(cls):
        cls.items.append("hello")                   # s3

    @classmethod
    def tearDownClass(cls):
        cls.items.pop()                             # t4

    def setUp(self):
        self.number = 1                             # r3 r4

    def tearDown(self):
        self.number = None                          # r3 r4

    def test_03(self):
        assert self.number == 1                     # r3
        assert self.items[0] == "hello"             # r3

    def test_04(self):
        assert self.number == 1                     # r4
        assert self.items[0] == "hello"             # r4


@pytest.fixture
def some_data():
    return [1, 2, 3]                                # s5 s6


def test_05(some_data):
    assert len(some_data) == 3                      # r5


@pytest.fixture
def more_data(some_data):
    return [2*x for x in some_data]                 # s6


def test_06(some_data, more_data):
    assert len(some_data) == len(more_data)         # r6


@pytest.fixture(scope='session')
def expensive_data():
    return list(range(10))                          # s7


def test_07(expensive_data):
    assert len(expensive_data) == 10                # r7


def test_08(expensive_data):
    assert len(expensive_data) == 10                # r8


@pytest.fixture(params=[1, 2, 3])
def parametrized_number(request):
    return request.param                            # s9-1 s9-2 s9-3


def test_09(parametrized_number):
    assert parametrized_number > 0                  # r9-1 r9-2 r9-3


def test_10():
    assert 1 == 1                                   # r10


@pytest.mark.parametrize("x, ans", [
    (1, 101),
    (2, 202),
])
def test_11(x, ans):
    assert 100 * x + x == ans                       # r11-1 r11-2


@pytest.mark.parametrize("x, ans", [
    (1, 101),
    (2, 202),
], ids=['one', 'two'])
def test_12(x, ans):
    assert 100 * x + x == ans                       # r12-1 r12-2


@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [3, 4])
def test_13(x, y):
    assert x + y > 0                                # r13-1 r13-2 r13-3 r13-4
