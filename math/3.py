import numpy as np
import numpy.linalg as la

A = np.array([[-1, 2], [3, -5]])

B = np.array([[2, 0], [-1, 4]])

summa = 2 * A + 3 * B

erotus = A - B

print('2A + 3B: ')
print(summa)
print('A - B:')
print(erotus)

print('\n')

a_1 = np.array([[5, 3], [2, 1]])
a_2 = np.array([9, 4])

ratkaisu_a = la.solve(a_1, a_2)

print('a) ')
print(ratkaisu_a)

b_1 = np.array([[2, 1, 1], [1, 3, 1], [2, 1, 2]])
b_2 = np.array([6, 2, 9])

ratkaisu_b = la.solve(b_1, b_2)

print('b) ')
print(ratkaisu_b)

c_1 = np.array([[1, 1, 3], [3, 1, 1], [2, 1, 2]])
c_2 = np.array([-1, 5, 2])

ratkaisu_c = la.solve(c_1, c_2)

print('c) ')
print(ratkaisu_c)
