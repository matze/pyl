# Using NumPy

Let's first import NumPy:

    import numpy as np

Now, create an array

    a = np.linspace(0.0, 2 * np.pi, 20)

The approximative integral (i.e. the sum) of the sines should be  pretty close
to zero: $\sum\sin a$ = `np.sum(np.sin(a))`.
