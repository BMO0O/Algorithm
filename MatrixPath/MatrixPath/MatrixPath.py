# Python3 program to show matrix path

m = [[6, 7, 12, 5],
     [5, 3, 11, 18],
     [7, 17, 3, 3],
     [8, 10, 14, 9]]

m_len_col = int(len(m[0]))

def Matrix_path(M,n):
    C = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = M[i][j] + max(C[i-1][j], C[i][j-1])

    for i in range(n):
        print(C[i])

    return C[n-1][n-1]

result = Matrix_path(m, m_len_col)

print(result)





