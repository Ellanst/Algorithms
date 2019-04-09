# Gaussian Elimination
# 为线性方程组求解，时间复杂度O(n^3)
# 当矩阵为方阵，且秩等于方阵的行列数时，矩阵有唯一解

A = [[2,1,1],[6,2,1],[-2,2,1]]
B = [[1],[-1],[7]]
A = np.array(A)
row = A.shape[0]
col = A.shape[1]
Rank = np.linalg.matrix_rank(A)
if row == col and Rank == row:
    print("A only have one solution")
    # 设被求助阵为二维表A[0:n][0:n]
    for i in range(row - 1):
        # 用A[i][i]将A[i+1:n][i]的值都变为0

    det = 0.0
    for i in range(row):
        det += A[i][i]
else:
    print("A have no solution or too many solutions")
