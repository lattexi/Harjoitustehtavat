import numpy as np


a1 = 2.493
b1 = 0.911

print(np.degrees(a1))
print(np.degrees(b1))
print("")

A = np.array([137.7, 62.3])

for i in A:
  print(np.radians(i))

print("")

B = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

for i in B:
  print(np.radians(i))


