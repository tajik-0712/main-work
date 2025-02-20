import matplotlib.pyplot as plt
import numpy as np

def y_func(x):
    return 2 * x**3 - 4

x_graph = np.linspace(-2, 2, 400)
y_graph = y_func(x_graph)

plt.figure(figsize=(8, 6))
plt.plot(x_graph, y_graph, label='2x^3 -4')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.title('Graph of y = 2x^3 - 4')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()