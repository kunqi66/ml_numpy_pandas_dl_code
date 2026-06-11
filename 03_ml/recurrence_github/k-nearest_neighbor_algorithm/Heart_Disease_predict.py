import numpy as np
import pandas as pd
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def load_data():
    file_path = os.path.join('.','data', 'heart_disease.csv')
    data = pd.read_csv(file_path)
    return data
def pretreat_data():
    data = load_data()
    data.dropna()
    X_train, X_text, Y_train, Y_text = train_test_split(
        data.drop('是否患有心脏病',axis=1),
        data['是否患有心脏病'],
        test_size=0.3,
        random_state=100
    )
    num_data = ["年龄", "静息血压", "胆固醇", "最大心率", "运动后的ST下降", "主血管数量"]
    cat_data = ["胸痛类型", "静息心电图结果", "峰值ST段的斜率", "地中海贫血"]
    bin_data = ["性别", "空腹血糖", "运动性心绞痛"]
    pretreat = ColumnTransformer([
        ('num',StandardScaler(),num_data),
        ('cat',OneHotEncoder(drop='first'),cat_data),
        ('bin',"passthrough",bin_data)
    ])
    print(X_train.head())
    pretreat.fit(X_text)
    X_train = pretreat.transform(X_train)
    X_text = pretreat.transform(X_text)
    print(X_train[:5,:])
    return X_train,Y_train,X_text,Y_text

def train(X_train,Y_train):
    item = KNeighborsClassifier(n_neighbors=4)
    item.fit(X_train,Y_train)
    return item

def predict(num):
    pass
if __name__ == "__main__":
    X_train,Y_train,X_text,Y_text = pretreat_data()
    item = train(X_train,Y_train)
    result = item.predict(X_text)
    ans = Y_text == result
    y = ans[ans == True]
    print(f'准确率为{y.size/ans.size}')
    