import matplotlib

matplotlib.use('macosx')
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(20, 8), dpi=80)
x = range(2, 26, 2)
y = [15, 13, 14, 5, 17, 20, 25, 26, 27, 22, 18, 15]
plt.plot(x, y)

# 绘制x的刻度

# plt.xticks(range(2,25))

# 过滤数据
_xtick_labels = [i / 2 for i in range(4, 49)]

# plt.xticks(range(2,25))
# plt.xticks(_xtick_labels[::3])数据取值步长
plt.yticks(range(min(y),max(y)+1))
plt.savefig("../dist/sve.svg")
plt.show()
