import numpy as np

if __name__ == '__main__':
    print("______Numpy_______")
    # data = [1, 2, 3]
    # print("data:", type(data))
    # a = np.array(data)
    # print("np.array:", type(a))
    #
    # c = np.zeros((2, 3))
    # print("np.zeros():")
    # print(c)
    # c=np.ones((2,2))
    # print("np.ones():")
    # print(c)
    # d=np.arange(0,10,3)
    # print("np,arange():",d)
    # ------------------------
    # e = np.linspace(0, 1, 5)
    # print("np.linespace():", e)
    # ---------------------
    # f = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # g = np.reshape(f, (3, 3))
    # print("np.reshape():")
    # print(g)
    # ---------------------
    # a1 = np.array([1, 2])
    # a2 = np.array([3, 4, 5])
    # h = np.concatenate((a1, a2))
    # print("np.concatenate():", h)
    # ---------------------
    # i = np.array([1, 2, 3, 4, 5, 6])
    # j = np.split(i, 3)
    # print("np.split():", j)
    # ---------------------
    # i = np.array([1, 2, 3, 4, 5, 6])
    # j = np.split(i, 3)
    # print("np.split():", j)
    cc = np.array([1, 5, 2, 8])
    z = np.mean(cc)
    print("np.mean():", z)
    bb = np.max(cc)
    print("np.max():", bb)
    dd = np.min(cc)
    print("np.min():", dd)


