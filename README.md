# ctxsugar

A tiny library that allow for creating object instances aware of the
surrounding contexts:
```python
ctx = ProvidesContext()
with ctx:
    ContextAware()
    # ContextAware() has access to the ctx
```

It came out of a desire to understand how a model specification idiom
```python
from pymc3 import Model, Normal, HalfNormal

basic_model = Model()
with basic_model:

    # Priors for unknown model parameters
    alpha = Normal('alpha', mu=0, sd=10)
    beta = Normal('beta', mu=0, sd=10, shape=2)
    sigma = HalfNormal('sigma', sd=1)

```
works in [pymc3](https://github.com/pymc-devs/pymc3) and to be able to
reuse it.
