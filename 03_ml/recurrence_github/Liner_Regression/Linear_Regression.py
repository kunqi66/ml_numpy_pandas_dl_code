import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def first_demo():
    x = [
        [80,86],
        [82,80],
        [85,78],
        [90,90],
        [86,82],
        [82,90],
        [78,80],
        [92,94]
    ]
    y=[84.2,80.6,80.1,90,83.2,87.6,79.4,93.4]
    item = LinearRegression()
    item.fit(x,y)
    print("线性回归的系数：",item.coef_)
    print(item.predict([[78,89]]))
    
    
def load_data():
    data = pd.read_csv('./data/advertising.csv')
    # print(data)
    data.drop(data.columns[0], axis= 1, inplace=True)
    data.dropna(inplace=True)
    x = data.drop('Sales',axis=1)
    y = data['Sales']
    x_train,x_test,y_train,y_test = train_test_split(
        x,y,test_size=0.2,random_state=100
    )
    return x_train,x_test,y_train,y_test

def pretreat_data():
    x_train,x_test,y_train,y_test = load_data()
    item = StandardScaler()
    x_train = item.fit_transform(x_train)
    x_test = item.transform(x_test)
    return x_train,x_test,y_train,y_test
def advert_put_predict():
    x_train,x_test,y_train,y_test =pretreat_data()
    fun = LinearRegression()
    fun.fit(x_train,y_train)
    print("线性回归的系数：",fun.coef_)
    print(fun.predict(x_test))
    print(y_test)
    print("正规方程法均方误差:", mean_squared_error(y_test, fun.predict(x_test)))
if __name__ == "__main__":
    # first_demo()
    advert_put_predict()