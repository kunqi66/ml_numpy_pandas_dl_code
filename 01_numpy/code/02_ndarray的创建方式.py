import numpy as np

'''
2.4.1 array()与asarray()
array()：将输入数据转换为ndarray，会进行copy。
asarray()：将输入数据转换为ndarray，如果输入本身是ndarray则不会进行copy。
'''


list = [1,2,3]
array1 = np.array(list)
array2 = np.array(list)

print(f"id(list)={id(list)},type(list)={type(list)}")
print(f"id(array1)={id(array1)},type(array1)={type(array1)}")
print(f"id(array2)={id(array2)},type(array2)={type(array2)}")



print()
origin_arr = np.array(list)
array3 = np.array(origin_arr)
array4 = np.asarray(origin_arr)
print(f"id(origin_arr)={id(origin_arr)},type(origin_arr)={type(origin_arr)}")
print(f"id(array3)={id(array3)},type(array3)={type(array3)}")
print(f"id(array4)={id(array4)},type(array4)={type(array4)}")

print()
origin_arr[0] = 666
print(array3)
print(array4)