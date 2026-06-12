import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
import seaborn as sns
import matplotlib.pyplot as plt

def first_demo():
    x = np.array([[1],[2],[38],[90]])
    y = np.array([0,0,1,1])
    item = KNeighborsClassifier(n_neighbors=2)
    item.fit(x,y)
    num = int(input("非负整数："))
    result = item.predict([[num]])
    print("数字{}所在类别{}".format(num,result))

#鸢尾花案例
def demo1():
    iris = load_data()
    show_data()
    x_train1, x_test1, y_train1, y_test1 = train_test_split(
            iris.data, 
            iris.target,
            test_size= 0.9,
            random_state=6
    )
    item = KNeighborsClassifier(n_neighbors=6)
    item.fit(x_train1,y_train1)
    result = item.predict(x_test1)
    ans = (result == y_test1)
    print(ans)
    
#加载数据集
def load_data():
    iris = load_iris()
    # print(iris)
    return iris
#可视化数据集
def show_data():
    print('进入函数')
    data = load_data()
    nums = pd.DataFrame(
        data = data.data,
        columns = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width']
    )
    nums['target'] = data.target
    print(nums)
    sns.pairplot(data = nums, hue='target')
    plt.title("鸢尾花数据可视化")
    plt.show()
    
    
def kd_tree():
    pass  


if __name__ == "__main__":
    # first_demo()
    demo1()