def MatrixMulticiplation(M1, M2):

    if len(M1[0]) != len(M2):
        print("error")

    res = [[0 for x in range(3)] for y in range(3)]

    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M2)):
                res[i][j] += M1[i][k] * M2[k][j]

    return res


if __name__ == "__main__":

    a = [[24,7,3],
        [4 ,8,6],
        [7 ,8,1]]

    b = [[0,8,6],
        [2,8,3],
        [1,5,9]]

    c = MatrixMulticiplation(a, b)
    for row in c:
        print(row)
