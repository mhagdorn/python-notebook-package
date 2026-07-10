# ---
# title: "Fibonacci Number"
# author: Magnus Hagdorn
# format:
#   html:
#      code-fold: true
#   pdf:
#      echo: false
#      pdf-engine: pdflatex
#      toc: false
#      number-depth: 2
#      number-sections: true
#      papersize: a4
#      documentclass: article
# jupyter: python3
# jupyter:
#   jupytext:
#     formats: py:percent,ipynb
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: pnp
#     language: python
#     name: pnp
# ---

# %%
# %load_ext autoreload
# %autoreload 2

# %%
import numpy
import pnp
from matplotlib import pyplot

# %% [markdown]
# The ratio of two adjacent numbers of Fibonacci sequence approaches the Golden Ration $\phi$,
# $$\phi = \lim_{i->\inf}\frac{f_{i+1}}{f_i}.$$
# Check out the Figure @fig-fib.

# %%
# the golden ratio
golden = (1 + 5 ** 0.5) / 2

# %%
# construct the Fibonacci sequence using our local pnp package
data = []
for f in pnp.fibonacci(10):
    data.append(f)
data = numpy.array(data)

# %%
#| label: fig-fib
#| fig-cap: "Ratio of adjacent numbers of the Fibonacci sequence together with Golden Ration (black line)"

_ = pyplot.axhline(golden, color='k')
_ = pyplot.plot(data[1:]/data[:-1])
_ = pyplot.xlabel("$i$")
_ = pyplot.ylabel("$f_{i+1}/f_i$")

# %%
