#!/usr/bin/env python
# coding: utf-8

# ## Домашнее задание по numpy
# ## Создайте 3 ваших любимых эррея разными способами

# In[75]:


import numpy as np


# In[2]:


import numpy as np
array1 = np.arange(1, 4, 1)
array2 = np.array([1, 2, 3])
array3 = np.linspace(1, 3, 3)
array1, array2, array3


# ## Создайте функцию matrix_multiplication, которая принимает 2 матрицы, перемножает их по соответствующим правилам и выдаёт получившуюся матрицу

# In[123]:


def matrix_multiplication(a,b):
    result = np.matmul(a, b)
    return result
'''
a = np.matrix('1 2; 3 4')
b = np.matrix('1 1; 1 1')
print(matrix_multiplication(a,b))
'''


# ## Создайте функцию multiplication_check, которая принимает список с матрицами, и выдаёт True, если они могут быть перемножены друг на друга в порядке, в котором они находятся в списке, и False, если их нельзя перемножить

# In[149]:


def multiplication_check(array):
    i = 0
    while i < len(array):
        
        if array[i].shape[0] == array[i+1].shape[1]:
            return True
        else:
            return False
        i +=1
'''
array = [np.matrix([[0,  1, 1], [2, 3, 1]]), np.matrix([[ 4,  5],[ 6,  7], [ 1, 0 ]]), np.matrix([[ 8,  9], [10, 11]]),np.matrix([[12, 13], [14, 15]])]
print(multiplication_check(array))
'''


# ## Создайте функцию multiply_matrices, которая принимает список с матрицами, и выдаёт результат перемножения, если его можно получить, или возвращает None, если их нельзя перемножить

# In[150]:


def multiply_matrices(array):
    if multiplication_check(array):
            A = array[0]
            for i in range(1, len(array)):
                B = array[i]
                A = np.dot(A, B)
            return A
    else:
        return None

'''array = [np.matrix([[0,  1, 1], [2, 3, 1]]),  np.matrix([[ 4,  5],[ 6,  7], [ 1, 0 ]]),
      np.matrix([[ 8,  9], [10, 11]]),np.matrix([[12, 13], [14, 15]])]
multiply_matrices(array) 
'''


# ## Создайте функцию compute_2d_distance, принимающую 2 одномерных эррея c парой значений (как координаты точки на плоскости) и вычисляющую расстояние между ними

# In[66]:


def compute_2d_distance(array1, array2):
    res = np.linalg.norm(array1-array2)
    return res

'''m = map(int, input().split()) # taking number of rows and column
array1 = np.array([input().strip().split() ], int)
array2 = np.array([input().strip().split() ], int)
compute_2d_distance(array1, array2)
'''


# ## Создайте функцию compute_multidimensional_distance, принимающую 2 одномерных эррея с любым количеством значений (но равным) и вычисляющую расстояние между ними 

# In[64]:


def compute_multidimensional_distance(array1, array2):
    res = np.linalg.norm(array1-array2)
    return res

'''n, m = map(int, input().split()) # taking number of rows and column
array1 = np.array([input().strip().split() for _ in range(n)], int)
array2 = np.array([input().strip().split() for _ in range(n)], int)
compute_multidimensional_distance(array1, array2) 
'''


# ## Создайте функцию compute_pair_distances, которая получает 2d эррей, где каждая строка это наблюдение, а каждый столбец - фича. Функция рассчитывает матрицу попарных расстояний и выдаёт её пользователю

# In[ ]:


from scipy.spatial.distance import pdist


# In[117]:



def compute_pair_distances(coor):
    n_coor = len(coor)
    dist = np.zeros((n_coor, n_coor))
    row,col = np.triu_indices(n_coor,1)
    dist = np.sqrt(((coor[:, None, :] - coor) ** 2).sum(-1))
    return dist
'''
coor = np.arange(1,5).reshape(2,2)
print(compute_pair_distances(coor))
'''

