import numpy as np

a = np.zeros((4, 3))
print(a)

b = np.ones((4, 3))
print(b)

c = np.arange(12).reshape((4, 3))
print(c)

x1 = np.arange(1, 101)
Fx1 = 2*x1**2+5
print(Fx1)

x2 = np.arange(-10, 11)
Fx2 = np.exp(-x2)
np.set_printoptions(suppress=True)
print(Fx2)
