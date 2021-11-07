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
        constant = int(input())
        break
    else:
        print("Please, try again")
result = []
for i in range(columns_a):
    result.append([0]*line_a)
for i in range(len(matrix_a)):
    for j in range(len(matrix_a[0])):
        result[i][j] = matrix_a[i][j] * constant
for matrix_result in range(len(result)):
    print(*result[matrix_result])
