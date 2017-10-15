import numpy as np

my_list = [1, 2, 3, 4]

array_np = np.array(my_list)

print(type(array_np))

arr = np.arange(0, 1000)
print(arr * 8)
print(arr.mean())
filtro = arr > 500
print(arr[filtro])

arr_lin = np.linspace(0, 15, 10)
print(arr_lin)
print(arr_lin.mean())
print(arr_lin.max())