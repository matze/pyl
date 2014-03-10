# Using NumPy

Let's first import NumPy:

    import numpy as np

Now, create an array

    a = np.linspace(0.0, 2 * np.pi, 20)

The approximative integral (i.e. the sum) of the sines should be  pretty close
to zero: $\sum\sin a$ = `np.sum(np.sin(a))`.


## Plotting

First set up our data

    x = np.linspace(0.0, np.pi, 200)
    y1 = 0.5 * np.sin(np.pi * x)
    y2 = 0.2 * np.sin(2 * np.pi * x)

Now we have to import Matplotlib

    import matplotlib.pyplot as plt

lets also define a function for saving the file and returning the filename:

    import random
    from pyl.nodes import Image

    def show():
        fname = 'plot-{0:032x}.png'.format(random.getrandbits(128))
        plt.savefig(fname)
        return Image(fname)

and plot our sines.

    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.plot(x, y1 + y2)

Here's our plot: `show()`.
