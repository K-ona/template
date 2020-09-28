import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = x ** 2
y2 = x * 2 + 1

plt.figure(num=160, figsize=(8, 5))
plt.plot(x, y1)

plt.figure(num=150)
plt.plot(x, y2)
plt.plot(x, y1, color = 'red', linewidth = 1.0, linestyle = '--')

plt.show()