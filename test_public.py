import dataclasses

import pytest

from main import find_str

@dataclasses.dataclass
class Case:
    text: str
    s: str
    expected: bool


TEST_CASES = [
    Case(
        text='',
        s='',
        expected=False
    ),
    Case(
        text='',
        s='hello',
        expected=False
    ),
    Case(
        text='hello',
        s='',
        expected=False
    ),
    Case(
        text='hello',
        s='hello',
        expected=True
    ),
    Case(
        text='Hello',
        s='hello',
        expected=False
    ),
    Case(
        text='h ello',
        s='hello',
        expected=False
    ),
    Case(
        text='lililil',
        s='lil',
        expected=True
    ),
    Case(
        text='lililil',
        s='lill',
        expected=False
    ),
    Case(
        text='lallilil',
        s='lill',
        expected=False
    ),
    Case(
        text='lililil',
        s='lillil',
        expected=False
    ),
    Case(
        text='lililil',
        s='lilililil',
        expected=False
    ),
    Case(
        text='lilililill',
        s='lilililil',
        expected=True
    ),
    Case(
        text='llilililill',
        s='lilililil',
        expected=True
    )
]


@pytest.mark.parametrize('t', TEST_CASES)
def test_find_str(t: Case) -> None:
    assert find_str(t.text, t.s) == t.expected
