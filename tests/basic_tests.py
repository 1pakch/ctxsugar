# basic_tests.py - basic tests for the main mixin classes

import nose
from nose.tools import raises

from ctxsugar import ProvidesContext, ContextAware
from ctxsugar import ContextStackError


def test_simple():
    ctx = ProvidesContext()
    with ctx:
        assert(ContextAware().current_context == ctx)


@raises(ContextStackError)
def test_empty():
    ContextAware()


def test_nested():
    ctx1 = ProvidesContext()
    ctx2 = ProvidesContext()
    with ctx1:
        assert(ContextAware().current_context == ctx1)
        with ctx2:
            assert(ContextAware().current_context == ctx2)

