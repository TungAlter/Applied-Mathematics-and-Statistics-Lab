import math

#! MSSV: 20127661
#! Họ và Tên: Lê Phan Duy Tùng
#! Lớp 20CLC01

#! Vì để thuận tiện cho việc làm tròn có số xấp xỉ 0,tính căn bậc hai,làm tròn kết quả đến chữ số thập phân thứ 4 nên
#! em có sử dụng hàm "sqrt" và "isclose" của thự math và hàm "round" của lớp float  

#! Hàm có nhiệm vụ làm tròn các số có giá trị gần bằng 0 
#! và làm tròn các kết quả khác tới số thập phân thứ 4
def round_num(value):
    if(math.isclose(value,0) == True):
        value = 0
    else:
        value = round(value,4) 
    return value

#! Hàm thực hiện nhân 2 vector
def Nhan2Vector(a,b):
    n = len(a)
    sum = 0
    for i in range(n):
        sum += a[i]*b[i]
    sum = round_num(sum)
    return sum

#! Hàm thực hiện nhân 2 vector với nhau
def NhanVector(a,alpha):
    n = len(a)
    for i in range(n):
        value = a[i] * alpha
        a[i] = round_num(value) 
    return a

#! Hàm tính độ dài của vector
def DoDaiVector(a):
    n = len(a)
    sum = 0
    for i in range(n):
        sum += a[i]**2
    res = math.sqrt(sum)
    res = round_num(res)
    return res

#! Hàm thực hiện cộng 2 vector
def Cong2Vector(a,b):
    n = len(a)
    for i in range(n):
        a[i] += b[i]
        a[i] = round_num(a[i])
    return a

#! Hàm thực hiện trừ 2 vector
def Tru2Vector(a,b):
    n = len(a)
    for i in range(n):
        a[i] -= b[i]
        a[i] = round_num(a[i])
    return a

#! Hàm lấy các vector u từ ma trận A và lưu vào 1 list trả về
def get_u_list(a,row,col):
    u_list = []
    for i in range(col):
        temp = []
        for j in range(row):
            temp += [a[j][i]]
        u_list.append(temp)
    return u_list

#! Hàm kiểm tra xem vector v có bằng 0 hay không
def isVectorZero(v):
    n = len(v)
    check = True
    for i in range(n):
        if(v[i] != 0):
            check = False
            break
    return check

#! Hàm thực hiện in ma trận
def printMatrix(a):
    n = len(a)
    for i in range(n):
        print(a[i])
    print("\n",end="")

#! Hàm thực hiện giải thuật Gramschmit để phân rã QR ma trận A
def Gramschmit(a):
    u_list = []
    q_list = []
    v_list = []
    row = len(a)
    col = len(a[0])
    #! Lấy u
    u_list = get_u_list(a,row,col)
    #! Tính v
    for i in range(len(u_list)):
        #! v1 = u1
        if(i == 0):
            if(isVectorZero(u_list[i]) == True):
                print("Vì có v = 0 nên giải thuật kết thúc")
                return
            v_list.append(u_list[i])
            continue
        #! v from 2 -> n
        #! tính proj
        sum_list = []
        for j in range(i-1,-1,-1):
            alpha = Nhan2Vector(u_list[i],v_list[j])/(DoDaiVector(v_list[j])**2)
            alpha = round_num(alpha)
            sum_list.append(NhanVector(v_list[j].copy(),alpha))
        sum = [0] * row
        for k in range(len(sum_list)):
            sum = Cong2Vector(sum,sum_list[k])
        #! vi = ui - proj
        temp = Tru2Vector(u_list[i].copy(),sum)
        if(isVectorZero(temp) == True):
                print("Vì có v = 0 nên giải thuật kết thúc")
                return
        v_list.append(temp)

    #! Tính q
    for i in range(len(v_list)):
        alpha = 1/DoDaiVector(v_list[i])
        temp = NhanVector(v_list[i].copy(),alpha)
        q_list.append(temp)
    
    #! Tạo ma trận Q
    q = []
    for i in range(len(q_list)):
        temp = [0]*len(q_list)
        q.append(temp)
    for i in range(len(q_list)):
        for j in range(col):
            q[i][j] = q_list[j][i]
    print("Ma trận Q:")
    printMatrix(q)

    #! Tạo ma trận R
    r = []
    for i in range(len(q_list)):
        temp = []
        for j in range(len(q_list)):
            if(j<i):
               temp += [0]
            else:
                value = Nhan2Vector(q_list[i],u_list[j])
                temp += [value]
        r.append(temp)
    print("Ma trận R:")
    printMatrix(r)

#! Chạy thử thuật toán,vì limit của phần in kết quả của jupiter notebook 
#! nên khi chạy cell code thì sẽ xảy tình trạng kết quả bị mất và thay thế bằng dấy "...."
#! chứ không phải là code lỗi

# print("Câu a:")
# A = [[1,1,2],[2,-1,1],[-2,4,1]]
# Gramschmit(A)

# print("Câu b:")
# A = [[1,1,1],[2,-2,2],[1,1,-1]]
# Gramschmit(A)

print("Câu c:")
A = [[1,1,-1],[0,1,2],[1,1,1]]
Gramschmit(A)

print("Câu d:")
A = [[-1,-1,1],[1,3,3],[-1,-1,5],[1,3,7]]
Gramschmit(A)

# print("Câu e:")
# A = [[1,1,1],[2,2,0],[3,0,0],[0,0,1]]
# Gramschmit(A)

# print("Câu f:")
# A = [[-2,1,3],[1,0,0],[0,1,0],[0,0,1]]
# Gramschmit(A)

# print("Câu g:")
# A = [[1,-1,2],[1,0,-1],[-1,1,2],[0,1,1]]
# Gramschmit(A)


