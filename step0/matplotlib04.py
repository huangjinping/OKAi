import matplotlib
import random
matplotlib.use('macosx')
import matplotlib.pyplot as plt

x=range(120)
y=[random.randint(20,35) for i in range(120)]
plt.plot(x, y)
plt.show()
