import dataclasses
import pytest

from algorithm_KMP import is_found_str


@dataclasses.dataclass
class Case:
    text: str
    s: str
    expected: bool


TEST_KMP = [
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


@pytest.mark.parametrize('t', TEST_KMP)
def test_algorithm_KMP(t: Case) -> None:
    assert is_found_str(t.text, t.s) == t.expected
