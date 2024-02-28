# 1. 导入所需的库
from graphviz import Digraph
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


# https://mp.weixin.qq.com/s/F6wRjHjb6OJ458Lx5v2BDQ
class SkLearnT1:
    def __init__(self):
        print("__init__")

    def getResult(self):
        a = 12
        b = 15
        return a, b




    def gaussianNB1(self):
        print("onStart")

        # 2. 加载示例数据集
        X, y = datasets.load_iris(return_X_y=True)

        # print(X)
        # print(y)

        iris = datasets.load_iris()
        print("=-----------------------------------------------0--->")
        # print(iris)
        print(iris.feature_names)
        print("=-----------------------------------------------1--->")

        # 3. 划分训练集和测试集
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # 4. 构建朴素贝叶斯分类模型
        nb = GaussianNB()

        # 5. 在训练集上拟合模型
        nb.fit(X_train, y_train)

        # 6. 在测试集上进行预测
        y_pred = nb.predict(X_test)

        # 7. 计算准确率
        accuracy = accuracy_score(y_test, y_pred)
        print("准确率:", accuracy)

    def onStart(self):
        # a, b = self.getResult()
        # print(str(a) + "======" + str(b))
        self.gaussianNB1()
        # self.onGraphviz()

    def onGraphviz(self):
        dot = Digraph('测试')
        dot.node("1", "Life's too short")
        dot.node("2", "I learn Python")
        dot.edge('1', '2')
        dot.view()
