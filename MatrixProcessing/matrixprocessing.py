import ast


def matrix_input(row):
    line = row
    matrix = []
    for i in range(line):
        t = []
        for j in input().split():
            if j != " ":
                t.append(ast.literal_eval(j))
        matrix.append(t)
    return matrix


def matrix_print(result, row, column):
    line, columns = row, column
    for i in range(line):
        for j in range(columns):
            print(result[i][j], end=' ')
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
            temp.append(float(m1[i][j]) * float(number_m))
        multiply.append(temp)
    return multiply


def matrix_element_sum(l1, l2):
    result = 0
    for i in range(len(l1)):
        result += l1[i] * l2[i]
    return result


def matrix_two_multiply(m1, m2):
    value = [[0 for row in range(len(m2[0]))] for column in range(len(m1))]
    print(value)
    for i in range(len(m1)):
        l1 = m1[i]
        for j in range(len(m2[0])):
            l2 = [m2[x][j] for x in range(len(m2))]
            value_range = matrix_element_sum(l1, l2)
            value[i][j] = value_range
    return value


while True:
    print('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
''', end='')
    choice = int(input('Your choice:'))
    if choice == 1:
        m, n = map(int, input('Enter size of first matrix:').split())
        print('Enter first matrix:')
        a = matrix_input(m)
        p, q = map(int, input('Enter size of second matrix:').split())
        print('Enter second matrix:')
        b = matrix_input(p)
        if m != p and n != q:
            print('The operation cannot be performed.')
        else:
            c = matrix_sum(a, b, m, n)
            matrix_print(c, m, n)
    elif choice == 2:
        m, n = map(int, input('Enter size of matrix:').split())
        print('Enter matrix:')
        a = matrix_input(m)
        number = float(input('Enter constant:'))
        c = matrix_number_multiply(a, number)
        print('The result is:')
        matrix_print(c, m, n)
    elif choice == 3:
        m, n = map(int, input('Enter size of first matrix:').split())
        print('Enter first matrix:')
        a = matrix_input(m)
        p, q = map(int, input('Enter size of second matrix:').split())
        print('Enter second matrix:')
        b = matrix_input(p)
        c = matrix_two_multiply(a, b)
        print('The result is:')
        matrix_print(c, m, q)
    elif choice == 0:
        break
