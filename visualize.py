import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

fig = plt.figure()
plt.ylim(0,5)
x = np.linspace(0, 10, 100)
plt.plot(x+36, x + 0, linestyle='solid')
plt.axhline(y=1, color='r', linestyle=':')
plt.axvline(x = 38, color = 'r', label = 'B', linestyle=":")
plt.show()