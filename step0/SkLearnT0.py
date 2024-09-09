import jieba
import numpy as np
import sklearn.datasets as sk_datasets
from graphviz import Digraph
from sklearn.datasets import load_iris
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Binarizer
from sklearn.preprocessing import Normalizer
import seaborn as sns;

sns.set(color_codes=True)

from sklearn import preprocessing
from pylab import mpl

import matplotlib

# https://blog.csdn.net/qq_51763547/article/details/126918669   matplotlib bug
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns

"""
https://mp.weixin.qq.com/s?__biz=MjM5NzEyMzg4MA==&mid=2649428430&idx=1&sn=e09951adad1b302880958a7705f2b851&chksm=bec1738989b6fa9f42e2c4004b723c04e0521852a43ca90fcdd0372d9b734437e96502a40503&scene=27
"""


class SkLearnT0:
    def __init__(self):
        print("SkLearnT0")

    def onStart(self):
        # print("SkLearnT0 onStart")
        # self.loadDataSource()
        # self.loadDataSourceView()
        self.mapParse()
        # self.oneHot()
        # self.oneHot1()
        # self.countvec()
        # self.countvec2()
        # self.onPCA()
        # self.onBinarizer()

    def loadDataSource(self):
        # https://mp.weixin.qq.com/s/O7de418oNvCM3z4776s3CQ
        # sklearn中的IRIS（鸢尾花）数据集[1]来对特征处理功能进行说明
        iris = sk_datasets.load_iris()
        print(type(iris))
        print(iris)
        print("----------------------")
        for keys in iris:
            print(keys)
        # 特征矩阵
        iris_X = iris.data
        print("Target names: {}".format(iris['target_names']))

        # 目标向量
        iris_Y = iris.target
        # print(iris_X)
        print(iris_Y)
        # print(dir(load_iris()))
        # print(load_iris().DESCR)

    def loadDataSourceView(self):
        # https://blog.csdn.net/qq_43874317/article/details/128185255  鸢尾花数据源可视化

        # mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 设置显示中文字体
        # mpl.rcParams["axes.unicode_minus"] = False  # 设置正常显示符号
        # 数据集获取
        iris = load_iris()  # 小数据集获取
        # 数据可视化，将数据转换成dataframe的格式存储
        iris_data = pd.DataFrame(data=iris.data, columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])
        iris_data['target'] = iris.target  # 新增target目标值一列
        print(iris_data)
        self.plot_iris(iris_data, col1='Sepal_Width', col2="Petal_Length")

    def plot_iris(self, iris_data, col1, col2):
        print("---------start0------")
        print(iris_data)
        print("---------start1------")
        # sns.lmplot(x=col1, y=col2, data=iris_data, hue="target", fit_reg=False)  # fit_reg为是否进行线性拟合
        # plt.xlabel(col1)
        # plt.ylabel(col2)
        # plt.title('test')
        # plt.show()

    def mapParse(self):
        print("sparse矩阵 节约内存，方便读取处理")
        dict = DictVectorizer(sparse=False)
        data = dict.fit_transform(
            [{'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 60}, {'city': '河南', 'temperature': 30}])
        print(dict.get_feature_names_out())
        print(data)

    def oneHot(self):
        # https://cloud.tencent.com/developer/article/1688022
        print("one Hot")
        enc = preprocessing.OneHotEncoder()
        enc.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])
        array = enc.transform([[0, 1, 3]]).toarray()
        print(array)

    def oneHot1(self):
        print("oneHot1")
        dict = DictVectorizer(sparse=False)
        data = dict.fit_transform([
            {"性别": "男", "年级": "初一", "学校": "四中"},
            {"性别": "女", "年级": "初二", "学校": "一中"},
            {"性别": "男", "年级": "初三", "学校": "二中"},
            {"性别": "女", "年级": "初一", "学校": "三中"},
        ])
        print(dict.get_feature_names_out())

        print(data)

    def countvec(self):
        """
        对文本进行特征值化
        文本特征抽取
        :return:None
        """
        transfer = CountVectorizer()
        strs1 = jieba.cut("女主播周淑怡翻车")
        c1 = " ".join(strs1)
        print()
        strs2 = jieba.cut("男主播李佳琪翻车，翻车了吗")
        c2 = " ".join(strs2)
        print()
        # data = transfer.fit_transform(["life is short,i like like python", "life is too long,i dislike python"])

        data = transfer.fit_transform([c1, c2])
        """
         中文无法实现抽取特征，需要借助jieba库 cut进行分词
        """
        # data = transfer.fit_transform(["life is short,i like like python", "life is too long,i dislike python"])

        # 1.统计所有文章中所有的词，重复的只看做一次词的列表
        print("返回特征名称：\n", transfer.get_feature_names_out())
        # 2.对每篇文章，在词的列表里面进行统计每个词出现的次数
        print("文本特征抽取的结果 sparse：\n", data)
        print("\n")
        print("文本特征抽取的结果：\n", data.toarray())

    def countvec2(self):
        """
        tf*idf:重要性程度
        Tf:term frequency:词的频率
        idf:逆文档频率inverse document frequency log(总文档数量/该词出现的文档数量)
        :return:
        """
        d1 = "petrol cars are cheaper than diesel cars"
        d2 = "diesel is cheaper than petrol"
        corpus = [d1, d2]

        ## 声明一个向量化工具vectorizer
        vectorizer = TfidfVectorizer()
        vectorizer.fit(corpus)
        print(vectorizer.get_feature_names_out())
        vector = vectorizer.transform(corpus)
        ## 文本向量化
        print(vector.toarray())

    def onPCA(self):
        print("车技")

    def onBinarizer(self):
        print("onBinarizer")
        iris = sk_datasets.load_iris()
        print(iris.data)

        # 对定量特征二值化
        # binarizer = preprocessing.Binarizer(threshold=0)  # 构建模型
        # result = binarizer.fit_transform(iris.data)
        # print(result)
        #
        normalizer = preprocessing.Normalizer(norm='l2')
        result = normalizer.fit_transform(iris.data)
        print(result)
