#Kaikki tehtävät tässä tiedostossa

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

#teht 2

x1 = np.linspace(5, 1, 100)
x2 = np.linspace(1, 3, 100)
x3 = np.linspace(3, 10, 100)

y1 = -2 * x1 + 6
y2 = np.full_like(x2, 4)
y3 = -2 * x3 + 10

plt.plot(x1, y1, 'b')
plt.plot(x2, y2, 'b')
plt.plot(x3, y3, 'b')

plt.xlim(-5, 10)
plt.ylim(0, 5)

plt.grid(True)
plt.show()

#teht 3

#a

a = 1
b = -4
c = 3

h = -b / (2 * a)
k = c - (b**2) / (4 * a)

x = np.linspace(h - 5, h + 5, 400)
y = a * x**2 + b * x + c

plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.plot(h, k, 'ro')
plt.xlim(h - 5, h + 5)
plt.ylim(k - 10, k + 10)
plt.grid(True)
plt.show()

#b

a = -1.5
b = -3
c = 7

h = -b / (2 * a)
k = c - (b**2) / (4 * a)

x = np.linspace(h - 5, h + 5, 400)
y = a * x**2 + b * x + c

plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.plot(h, k, 'ro')
plt.xlim(h - 5, h + 5)
plt.ylim(k - 10, k + 10)
plt.grid(True)
plt.show()

#teht 4

a = -0.0063
b = 0.55
c = 0

h = -b / (2 * a)
k = c - (b**2) / (4 * a)

x = np.linspace(h -50, h + 50, 100)
y = a * x**2 + b * x + c

plt.plot(x, y)
plt.plot(h, k, 'ro')
plt.grid(True)
plt.show()
