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

        # 将A[i][i] = 0 的调整到下一行，方便消元
        if A[i][i] == 0:
            temp = A[i,:].copy() #防止数组改变切片改变，开辟一块新的内存空间，把被拷贝对象中的值复制过去
            x = 1
            while A[i + x][i] == 0:
                x += 1
            A[i][:] = A[i + x][:]
            A[i + x][:] = temp
        else:
            True

        # 用A[i][i]将A[i+1:n][i]的值都变为0
        for j in range(i+1,row):
            n =  A[j][i] / A[i][i]
            B[j] = B[j] - n * B[i]
            A[j] = A[j] - n * A[i]

    # 回代
    for i in range(row):
        j = row - 1
        while j > row-1-i:
            B[row - 1 - i] = B[row - 1 - i] - det[j]*A[row- 1 - i][j]
            j -= 1
        det[row - 1 - i] = B[row - 1 - i] / A[row- 1 - i][row- 1 - i]

    print(det)
    
else:
    print("A have no solution or too many solutions")
