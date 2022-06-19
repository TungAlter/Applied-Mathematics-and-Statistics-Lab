
#! MSSV: 20127661
#! Họ và tên: Lê Phan Duy Tùng

def printMatrix(A):
    n = len(A)
    for i in range(n):
        print(A[i])

def unitMatrix(n):
    B = [] 
    for i in range(n):
        B.append([0])
    for i in range(n):
        for j in range(n-1):
            B[i].append(0)
    for i in range(n):
        B[i][i] = 1
    return B

def addMatrix(A):
    n = len(A)
    B = unitMatrix(n)
    for i in range(n):
        for j in range(n):
            A[i].append(B[i][j])
    return A

def splitMatrix(A):
    nRow = len(A)
    nCol = len(A[0])
    newCol = int(nCol/2)
    for i in range(nRow):
        for j in range(newCol-1,-1,-1):
            A[i].pop(j)
    
def switch_row(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def multi_row(A,i,alpha):
    m = len(A[0])
    for j in range(m):
        A[i][j] = round(alpha * A[i][j],4)

def row_plus_row(A,i,j,alpha):
    m = len(A[0])
    for k in range(m):
        A[i][k] = round(A[i][k] + alpha * A[j][k],4)

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

def row_zero(A,i):
    check = True
    n = len(A)
    for j in range(n):
        if(A[i][j] != 0):
            check = False
            break
    return check

def inverse(A):
    
    nRow = len(A)
    nCol = len(A)
    #todo B1: Kiểm tra xem ma trận vừa truyền vào có là ma trận vuông hay không
    if(nRow != nCol):
        print("Ma trận không khả nghịch")
        return
    
    #todo B2: Kiểm tra xem có dòng/cột của ma trận vừa truyền vào chứa toàn 0 hay không
    for i in range(nRow):
        if(row_zero(A,i)):
            print("Ma trận không khả nghịch")
            return
        for j in range(nCol):
            if(col_zero(A,j,0)):
                print("Ma trận không khả nghịch")
                return

    R  = addMatrix(A.copy())

    #todo B3: Dùng thuật toán Gauss để đưa ma trận bổ sung về dạng bậc thang
    row = 0
    while(row < nRow):
        #! B3.1: Xác định cột ở phía trái nhất không chứa toàn 0
        col = row
        while(col < nCol and col_zero(R,col,row)):
            col+=1
        if(col == nCol): # đã là dạng bậc thang
             break
        #! B3.2: Đổi dòng đầu với những dòng khác nhằm đưa hệ số khác 0 lên đầu cột ở B3.1 để biến thành leading
        for pivot in range(row,nRow):
            if(R[pivot][col] != 0):
                break
        switch_row(R,row,pivot)
        #! B3.3: Nhân dòng đầu với alpha để đưa leading về 1 
        #!        theo công thức drow = alpha * drow
        multi_row(R,row,1/R[row][col])
        #! B3.4: Cộng alpha lần dòng đầu với các dòng ở phía dưới để đưa các hệ số dưới leading về 0
        #!       theo công thức di = di + alpha * drow
        for i in range(row+1,nRow):
            row_plus_row(R,i,row,-R[i][col])
            if(row_zero(A,i) == True):
                print("Ma trận không khả nghịch")
                return
        #! B3.5: Bảo toàn dòng đầu và tiếp tục thuật toán với submatrix còn lại
        row += 1

    #todo B4: Cộng n lần từng dòng với các dòng ở trên nó để đưa các hệ số cùng cột ở trên leading về 0
    for row in range(nRow-1,-1,-1):
        col = row
        for i in range(row-1,-1,-1):
            row_plus_row(R,i,row,-R[i][col])

    #todo B5: Lấy ma trận nghịch đảo bên vế phải ma trận bổ sung và in lên màn hình
    splitMatrix(R)
    print("Ma trận nghịch đảo của ma trận ban đầu là: ")
    printMatrix(R)


#? ví dụ 4
A = [[-1,3,-4],[2,4,1],[-4,2,-9]]
inverse(A)



#? ví dụ 1
#A = [[1,2,1],[3,7,3],[2,3,4]]
#? ví dụ 2
#A = [[1,-1,2],[1,1,-2],[1,1,4]]
#? ví dụ 3
#A = [[1,2,3],[2,5,3],[1,0,8]]



      