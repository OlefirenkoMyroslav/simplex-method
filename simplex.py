import numpy as np
from scipy.optimize import linprog

def continue_solve(mark_in):
    mark = np.copy(mark_in)
    mark = mark[1:]
    for i in mark:
        if i > 0:
            return True,
    return False


def get_mark(matrix, function, basis): #рядок цільової функції 
    c_basis = []
    for i in basis:
        c_basis.append(function[i - 1])
    mark = np.dot(c_basis, matrix) - (np.append([0], function))
    print(mark)
    print('-----------------')
    return mark


def get_basis(matrix):  
    basis = []
    for i in range(len(matrix)):
        basis.append(matrix.shape[1] - len(matrix) + i)
    return basis


def add_additional_variables(matrix, function): 
    matrix = np.concatenate((matrix, np.eye(matrix.shape[0])), axis=1)
    function = np.append(function, matrix.shape[0] * [0])
    return matrix, function


def recount(matrix_in, index_input, index_output): #робимо стовбчик базисної змінної одиничним
    matrix = matrix_in.copy()
    k = matrix[index_output][index_input]
    matrix[index_output] /= k

    for i in range(len(matrix)):
        if i != index_output:
            matrix[i] -= matrix[i][index_input] * matrix[index_output]
    print(matrix)
    print('-----------------')
    return matrix


def get_index_input(mark):
    return np.argmax(mark)

def get_index_output(index_input, matrix_in):#обираємо змінну яку виводимо з базису
    matrix = np.copy(matrix_in)
    p_0 = matrix[:, 0]
    p_i = matrix[:, index_input]

    with np.errstate(divide='ignore', invalid='ignore'):
        teta = np.where(p_i > 0, p_0 / p_i, np.inf)

    index_output = teta.argmin()

    if teta[index_output] == np.inf:
        raise Exception("No valid pivot element found — problem is unbounded.")

    return index_output



def solve(matrix, function, basis):
    print(matrix)
    print("-----------------")
    mark = get_mark(matrix, function, basis)
    flag = continue_solve(mark)

    while flag:  # main loop

        index_input = get_index_input(mark)
        index_output = get_index_output(index_input, matrix)

        matrix = recount(matrix, index_input, index_output)

        basis[index_output] = index_input

        mark = get_mark(matrix, function, basis)
        flag = continue_solve(mark)

    return matrix, function, basis


def canonization(a, b, c):
    matrix = np.copy(a)
    vector = np.copy(b)
    function = np.copy(c * -1)

    matrix = np.concatenate((vector.T, matrix), axis=1)
    matrix, function = add_additional_variables(matrix, function)
    basis = get_basis(matrix)
    print(basis)

    return matrix, function, basis


def simplex_method(matrix, function, basis):
    matrix, function, basis = solve(matrix, function, basis)
    mark = get_mark(matrix, function, basis)

    p_0 = matrix[:, 0]

    x = np.zeros(len(C))

    for i in range(len(basis)): #шукаємо значення не штучних х
        if (basis[i] - 1) < len(C):
            x[basis[i] - 1] = p_0[i]

    print("x = " + str(x))
    print("result = " + str(mark[0] * -1))

A = np.array([[1, 3],[2, 1],[0, 1],[3,0]]) #приклад з методички
B = np.array([[18, 16,5,21]])
C = np.array([2, 3])

#A = np.array([[4, 1],[-1, 1]]) 
#B = np.array([[8, 3]])
#C = np.array([3, 4])

#A = np.array([[1, 3,5,3],[2, 6,1,0],[2, 3,2,5]]) 
#B = np.array([[40,50,30]])
#C = np.array([7, 8,6,5])

#A = np.array([[-1,-1 ,-1],[2, -1,0],[-2,0, 1],[2,1,1],[-2,0,0]]) #варіант 1
#B = np.array([[-20, 8,3,50,-1]])
#C = np.array([1,2,2])



mat, fun, bas = canonization(A, B, C)
simplex_method(mat, fun, bas)

print("\nРішення через scipy.optimize.linprog:")
res = linprog(
    c=-C,  # Мінімізуємо, тому беремо -C
    A_ub=A,
    b_ub=B,
    method='highs'
)

if res.success:
    print("x =", res.x)
    print("result =", -res.fun)  # Повертаємо знак назад, бо ми мінімізували
