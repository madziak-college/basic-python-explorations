import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 10.1, 0.1)

def fn1(x):
    return x**2 -6*x + 36

# plot using blue squares:
#fn = np.exp
fn = fn1
plt.plot(x, fn(x), 'bs')

plt.show()

