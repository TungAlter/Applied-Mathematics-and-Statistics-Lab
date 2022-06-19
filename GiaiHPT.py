import math

def round_num(value):
    if(math.isclose(value,0) == True):
        value = 0
    else:
        value = round(value,4) 
    return value

def col_zero(A,col,row):
    check = True
    n = len(A)
    i = row
    while(i<n):
        if(A[i][col] != 0):
            check = False
            break
        i+=1
    return check

def printMatrix(a):
    row = len(a)
    for i in range(row):
        print(a[i])

def switch_row(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def multi_row(A,i,alpha):
    m = len(A[0])
    for j in range(m):
        A[i][j] = alpha * A[i][j]
        #A[i][j] = round_num(A[i][j])

def row_plus_row(A,i,j,alpha):
    m = len(A[0])
    for k in range(m):
        A[i][k] = A[i][k] + alpha * A[j][k]
        A[i][k] = round_num(A[i][k])

def addMatrix(A,B):
    for i in range(len(A)):
        A[i].append(B[i])
    return A

def Gauss(A,B):
    R = addMatrix(A.copy(),B.copy())
    nRow = len(R)
    nCol = len(R[0])
    row = 0
    while(row < nCol):
        #! Xác định cột không chứa toàn 0
        col = row 
        while(col <nCol and col_zero(R,col,row)):
            col +=1
        if(col == nCol): 
            break #! Đã là bậc thang
        #! swap row
        for pivot in range(row,nRow):
            if(R[pivot][col] != 0):
                break
        switch_row(R,row,pivot)
        #! drow = alpha * drow
        multi_row(R,row,1/R[row][col])
        #! di = di + alpha * drow
        for i in range(row+1,nRow):
            row_plus_row(R,i,row,-R[i][col])
        row += 1
    return R

def back_substitution(A):
    n = len(A[0]) - 1
    #! kiểm tra có vô nghiệm
    for i in range(n):
        no_solution = True
        if(A[i][n] != 0):
            for j in range(n):
                if(A[i][j] != 0):
                    no_solution = False
                    break
            if(no_solution == True):
                print("Hệ vô nghiệm")
                return 
    #! Trường hợp có vô số nghiệm
    count = 0
    for i in range(n):
        if(A[i][i] == 0):
            count += 1
    if(count != 0):
        print("Hệ có vô số nghiệm với " + str(count)+ " ẩn tự do")
        return
    #! Trường hợp có nghiệm duy nhất   
    # tạo list rỗng chứa n nghiệm
    result = []
    for i in range(n):
        result.append(0)
    # bắt đầu back_substitution
    result[n-1] = (A[n-1][n]/A[n-1][n-1])
    for i in range(n-2,-1,-1):
        sum = 0
        for j in range(i+1,n):
            sum += A[i][j]*result[j]
        result[i] = (A[i][n] - sum)/A[i][i] 
    print("Hệ có nghiệm duy nhất là")
    print(result)

# A =[[1,2,-1],
#     [2,2,1],
#     [3,5,-2]]
# B = [-1,1,-1]

# A =[[1,-2,-1],
#     [2,-3,1],
#     [3,-5,0],
#     [1,0,5]]
# B = [1,6,7,9]

# A = [[1,2,0,2],
#     [3,5,-1,6],
#     [2,4,1,2],
#     [2,0,-7,11]]
# B = [6,17,12,7]

# A = [[2,-4,-1],[1,-3,1],[3,-5,-3]]
# B = [1,1,2]

# A = [[1,2,-2],[3,-1,1],[-1,5,-5]]
# B = [3,1,5]

# A = [[1,-2,3],[2,2,0],[0,-3,4],[1,0,1]]
# B = [-3,0,1,-1]

A = [[1,-1,1,-3],[2,-1,4,-2]]
B = [0,0]
R = Gauss(A,B)
printMatrix(R)
back_substitution(R)

#print(R)

