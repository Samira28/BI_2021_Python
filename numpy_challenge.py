
import numpy as np

array1 = np.arange(1, 4, 1)
array2 = np.array([1, 2, 3])
array3 = np.linspace(1, 3, 3)


def matrix_multiplication(a, b):

    result = np.matmul(a, b)


    return result


def multiplication_check(array):

    i = 0
    while i < len(array):
        if array[i].shape[0] == array[i+1].shape[1]:
            return True
        else:
            return False
        i += 1


def multiply_matrices(array):

    if multiplication_check(array):
            A = array[0]


            for i in range(1, len(array)):
                B = array[i]
                A = np.dot(A, B)
            return A
    else:
        return None


def compute_2d_distance(array1, array2):

    res = np.linalg.norm(array1-array2)
    return res


def compute_multidimensional_distance(array1, array2):

    res = np.linalg.norm(array1-array2)
    return res


def compute_pair_distances(coor):

    n_coor = len(coor)
    dist = np.zeros((n_coor, n_coor))
    row, col = np.triu_indices(n_coor, 1)


    dist = np.sqrt(((coor[:, None, :] - coor) ** 2).sum(-1))
    return dist

