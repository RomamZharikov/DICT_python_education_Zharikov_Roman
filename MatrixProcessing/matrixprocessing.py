while True:
    while True:
        line_and_columns_a = list(input("Please, input line and columns matrix A: \n"))
        columns_a = int(line_and_columns_a[0])
        line_a = int(line_and_columns_a[2])
        matrix_a = []
        line_true_a = 0
        for i in range(columns_a):
            matrix_a.append(list(map(int, input().split())))
        for height in range(len(matrix_a)):
            if len(matrix_a[height]) == line_a:
                line_true_a += 1
        if line_true_a == columns_a:
            break
        else:
            print("Please, try again")

    while True:
        line_and_columns_b = list(input("Please, input line and columns matrix B: \n"))
        columns_b = int(line_and_columns_b[0])
        line_b = int(line_and_columns_b[2])
        matrix_b = []
        line_true_b = 0
        for i in range(columns_b):
            matrix_b.append(list(map(int, input().split())))
        for height in range(len(matrix_b)):
            if len(matrix_b[height]) == line_b:
                line_true_b += 1
        if line_true_b == columns_b:
            break
        else:
            print("Please, try again")

    if columns_a == columns_b and line_a == line_b:
        result = []
        for i in range(columns_a):
            result.append([0]*line_b)
        for i in range(len(matrix_a)):
            for j in range(len(matrix_a[0])):
                result[i][j] = matrix_a[i][j] + matrix_b[i][j]
        for matrix_result in range(len(result)):
            print(*result[matrix_result])
            break
    else:
        print("ERROR")
