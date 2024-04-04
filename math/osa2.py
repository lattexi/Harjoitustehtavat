#teht 1

import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt

x = np. linspace (-10, 10, 100)

y = -2 * x + 6

plt.plot(x, y, label='y = -2x + 6')

plt.grid(True)
plt. legend()
plt.show()

