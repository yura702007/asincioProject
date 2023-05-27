"""
Вычисление средних в большой матрице с помощью numpy
"""
import numpy as np
import time


data_points = 10 ** 9
rows = 50
columns = data_points // rows

matrix = np.arange(data_points).reshape(rows, columns)

start = time.time()
result = np.mean(matrix, axis=1)
print(time.time() - start)
