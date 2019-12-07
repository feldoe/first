import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

print(x)

y = np.sin(x)

print(y)

plt.plot(x,y)
plt.show()