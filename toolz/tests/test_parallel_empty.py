"""AI-assisted regression tests for fold with an explicit identity."""

from functools import reduce
from operator import add

from toolz.sandbox.parallel import fold


def test_fold_empty_with_identity():
    assert fold(add, [], default=0) == reduce(add, [], 0)


def test_fold_nonempty_with_identity():
    assert fold(add, [1, 2, 3], default=0) == reduce(add, [1, 2, 3], 0)
