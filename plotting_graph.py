import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5, 0.1)
print(x)
y = np.sin(x)
print(y)
# plt.plot(x, y)
# print(plt.subplot())
# fig, ax = plt.subplots()
plt.plot(x, y,marker = '3')
plt.show()
# plt.plot(xpoints, ypoints)
# plt.show()