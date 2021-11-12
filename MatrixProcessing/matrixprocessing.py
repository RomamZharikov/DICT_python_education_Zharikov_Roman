import ast
import itertools
from math import floor, ceil


def matrix_input(row):
    line = row
    array = []
    for i in range(line):
        t = []
        for j in input().split():
            if j != " ":
                t.append(ast.literal_eval(j))
        array.append(t)
    return array


def matrix_print(result, row, column):
    line, columns = row, column
    for i in range(line):
        for j in range(columns):
            if result[i][j] == -0.0:
                print(0, end=" ")
            elif type(result[i][j]) == int or result[i][j] == 0:
                print(result[i][j], end=" ")
            elif type(result[i][j]) == float and result[i][j] != 0:
                if result[i][j] > 0:
                    print(floor(result[i][j] * 100) / 100.0, end=" ")
                else:
                    print(ceil(result[i][j] * 100) / 100.0, end=" ")

        print()


def matrix_sum(m1, m2, row, col):
    line, columns = row, col
    append = []
    for i in range(line):
        temp = []
        for j in range(columns):
            temp.append(m1[i][j] + m2[i][j])
        append.append(temp)
    return append


def matrix_number_multiply(m1, number_m):
    multiply = []
    for i in range(len(a)):
        temp = []
        for j in range(len(a[0])):
            temp.append(m1[i][j] * number_m)
        multiply.append(temp)
    return multiply


def matrix_element_sum(l1, l2):
    result = 0
    for i in range(len(l1)):
        result += l1[i] * l2[i]
    return result


def matrix_two_multiply(m1, m2):
    value = [[0 for row in range(len(m2[0]))] for column in range(len(m1))]
    for i in range(len(m1)):
        l1 = m1[i]
        for j in range(len(m2[0])):
            l2 = [m2[x][j] for x in range(len(m2))]
            value_range = matrix_element_sum(l1, l2)
            value[i][j] = value_range
    return value


def transpose_main_diagonal(array):
    return list(itertools.zip_longest(*array))


def transpose_side_diagonal(array):
    new_matrix = [[array[j][i] for j in range(len(array))] for i in range(len(array[0]) - 1, -1, -1)]
    result = []
    for i in range(len(new_matrix[0])):
        new_matrix[i] = new_matrix[i][::-1]
        result.append(new_matrix[i])
    return result


def transpose_vertical_line(array):
    new_matrix = [[array[j][i] for j in range(len(array))] for i in range(len(array[0]) - 1, -1, -1)]
    result = list(itertools.zip_longest(*new_matrix))
    return result


def transpose_horizontal_line(array):
    result = list(itertools.zip_longest(*array[::-1]))
    result = list(itertools.zip_longest(*result))
    return result


def minor(matrix_minor, i, j):
    return [row[:j] + row[j+1:] for row in (matrix_minor[:i] + matrix_minor[i + 1:])]


def minor_transpose(array):
    determinant = det(array)
    if len(array) == 2:
        return [[array[1][1] / determinant, -1 * array[0][1] / determinant],
                [-1 * array[1][0] / determinant, array[0][0] / determinant]]
    cofactors = []
    for r in range(len(array)):
        case = []
        for j in range(len(array)):
            minored = minor(array, r, j)
            case.append(((-1)**(r+j)) * det(minored))
        cofactors.append(case)
    cofactors = transpose_main_diagonal(cofactors)
    for i in range(len(cofactors)):
        cofactors[i] = list(cofactors[i])
    for r in range(len(cofactors)):
        for j in range(len(cofactors)):
            cofactors[r][j] = int(cofactors[r][j]) / determinant
    return cofactors


def det(matrix_det):
    if len(matrix_det) == 2:
        return matrix_det[0][0] * matrix_det[1][1] - matrix_det[0][1] * matrix_det[1][0]
    determinant = 0
    for i in range(len(matrix_det)):
        determinant += ((-1) ** i) * matrix_det[0][i] * det(minor(matrix_det, 0, i))
    return determinant


while True:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
    choice = int(input("Your choice:"))
    if choice == 1:
        matrix, n = map(int, input("Enter size of first matrix:").split())
        print("Enter first matrix:")
        a = matrix_input(matrix)
        p, q = map(int, input("Enter size of second matrix:").split())
        print("Enter second matrix:")
        b = matrix_input(p)
        if matrix != p and n != q:
            print("The operation cannot be performed.")
        else:
            c = matrix_sum(a, b, matrix, n)
            matrix_print(c, matrix, n)
    elif choice == 2:
        matrix, n = map(int, input("Enter size of matrix:").split())
        print("Enter matrix:")
        a = matrix_input(matrix)
        number = float(input("Enter constant:"))
        c = matrix_number_multiply(a, number)
        print("The result is:")
        matrix_print(c, matrix, n)
    elif choice == 3:
        matrix, n = map(int, input("Enter size of first matrix:").split())
        print("Enter first matrix:")
        a = matrix_input(matrix)
        p, q = map(int, input("Enter size of second matrix:").split())
        print("Enter second matrix:")
        b = matrix_input(p)
        c = matrix_two_multiply(a, b)
        print("The result is:")
        matrix_print(c, matrix, q)
    elif choice == 4:
        print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line.""")
        choice = int(input("Your choice:"))
        if choice == 1:
            matrix, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = matrix_input(matrix)
            c = transpose_main_diagonal(a)
            print('The result is:')
            matrix_print(c, n, matrix)
        elif choice == 2:
            matrix, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = matrix_input(matrix)
            c = transpose_side_diagonal(a)
            print('The result is:')
            matrix_print(c, n, matrix)
        elif choice == 3:
            matrix, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = matrix_input(matrix)
            c = transpose_vertical_line(a)
            print('The result is:')
            matrix_print(c, matrix, n)
        elif choice == 4:
            matrix, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = matrix_input(matrix)
            c = transpose_horizontal_line(a)
            print('The result is:')
            matrix_print(c, matrix, n)
    elif choice == 5:
        matrix, n = map(int, input("Enter size of matrix:").split())
        print('Enter matrix:')
        a = matrix_input(matrix)
        c = det(a)
        print('The result is:')
        print(c)
    elif choice == 6:
        matrix, n = map(int, input("Enter size of matrix:").split())
        print('Enter matrix:')
        a = matrix_input(matrix)
        c = det(a)
        print(c)
        if c != 0:
            d = minor_transpose(a)
            print('The result is:')
            matrix_print(d, matrix, n)
        else:
            print("This matrix doesn't have an inverse.")
    elif choice == 0:
        break
