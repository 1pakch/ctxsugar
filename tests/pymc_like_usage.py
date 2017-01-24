# pymc3_like_tests.py - tests for model/variable idiom used by pymc2/3

import nose

from ctxsugar import *


class Model(ProvidesContext):

    "A model as a collection of variables"

    def __init__(self):
        self.variables = []

    def insert(self, part):
        self.variables.append(part)


class Variable(ContextAware):

    "A variable within a model"

    def __init__(self, name):
        super(Variable, self).__init__()
        self.current_context.insert(self)
        self.name = name


def test():
    model = Model()
    with model:
        Variable('mu')
        Variable('sigma')
    names = map(lambda p: p.name, model.variables)
    assert(names == ['mu', 'sigma'])
