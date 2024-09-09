import matplotlib
# https://blog.csdn.net/qq_51763547/article/details/126918669   matplotlib bug
import numpy as np

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from pylab import mpl


# sns.set(style="darkgrid")
class SeabornT0:
    def __init__(self):
        print("开始")

    def onStart(self):
        print("---onStart---")
        # self.onDraw()
        self.onDrawIris()

    def onDraw(self):
        print("onDraw")
        sns.set_style("white")
        data = sns.load_dataset('tips')
        sns.relplot(x='total_bill', y='tip', data=data)
        plt.show(block=True)
        # df = sns.load_dataset("penguins")
        # sns.pairplot(df, hue="species")
        # plt.show(block=True)

    def onDrawIris(self):
        print("onDrawIris")
        iris = load_iris()  # 小数据集获取
        # 数据可视化，将数据转换成dataframe的格式存储
        iris_data = pd.DataFrame(data=iris.data, columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])
        iris_data['target'] = iris.target  # 新增target目标值一列
        print(iris_data)
        mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 设置显示中文字体
        mpl.rcParams["axes.unicode_minus"] = False  # 设置正常显示符号
        self.plot_iris(iris_data, col1='Sepal_Width', col2="Petal_Length")

    def plot_iris(self, iris_data, col1, col2):
        print("---------start0------")
        print(iris_data)
        print("---------start1------")
        sns.lmplot(x=col1, y=col2, data=iris_data, hue="target", fit_reg=False)  # fit_reg为是否进行线性拟合
        plt.xlabel(col1)
        plt.ylabel(col2)
        plt.title('test')
        plt.show()
