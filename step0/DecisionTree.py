import graphviz
import pandas
import pandas as pd
from graphviz import Digraph
from sklearn import datasets, tree
from sklearn.model_selection import train_test_split


class DecisionTree:
    def __init__(self):
        pass

    def onStart(self):
        print("决策树开始")
        # self.onTitanic()
        self.onRedWine()

    def onRedWine(self):
        print("=======")
        wine = datasets.load_wine()
        print(wine)
        print("--------------------------------------------p")

        print(wine.data.shape)
        print(wine.target)
        print("--------------------------------------------0")
        result = pandas.concat([pandas.DataFrame(wine.data), pandas.DataFrame(wine.target)], axis=1)
        print(result)
        print("--------------------------------------------1")

        print(wine.feature_names)
        print("--------------------------------------------2")

        print(wine.target_names)
        print("--------------------------------------------3")

        # 百分之30是测试集，百分之70是训练集
        xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data, wine.target, test_size=0.3, )
        print(xtrain.shape)
        print("--------------------------------------------4")

        print(Xtest.shape)
        print("--------------------------------------------5")

        # 实例化，criterion精密系数
        clf = tree.DecisionTreeClassifier(criterion="entropy")
        # 训练模型
        clf = clf.fit(xtrain, Ytrain)
        # 使用接口并测试集打分
        score = clf.score(Xtest, Ytest)
        print(score)
        feature_names = ['酒精', '苹果酸', '灰', '灰的酸度', '镁', '总酚', '类黄酮', '非黄烷类酚类', '花青素', '颜色强度', '色调', '0d280/0d315稀释葡萄酒',
                         '脯氨酸', ]
        dot_data = tree.export_graphviz(clf, feature_names=feature_names, class_names=["琴酒", "雪莉", "贝尔摩德"], filled=True,
                                        rounded=True)
        graph = graphviz.Source(dot_data).render(view=True)


def onTitanic(self):
    pass
    # 泰坦尼克数据
    # https://mp.weixin.qq.com/s/xumIM0i7er0r0fEGtzE4uw
    '''1 获取数据'''
    path = "/Users/huhuijie/Documents/GitHub/OKAi/res/csv/titanic.csv"
    titanic = pd.read_csv(path)
    print(titanic)
    # display(titanic.tail(3))
