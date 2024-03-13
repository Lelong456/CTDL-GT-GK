import numpy as np
import matplotlib.pyplot as plt 
import pandas as  pd
file = pd.ExcelFile('F:\Book.xlsx')
df = pd.read_excel(file, 'B14',sep = " ", nrows = 38, skiprows = [0,1,2,3,4,5,7,8,9,16,18,19,20,21,22,30,31,32,33,34,35,36])
# tổng cột dự toán
Sum = df["DỰ TOÁN"].sum(axis = 0)                                                  
class NSNN:       
    def __init__ (self, linhvuc, Dutoan):
        self.linhvuc = linhvuc
        self.Dutoan = Dutoan
#tạo mảng để nhập liệu
A = []*15
for i in range(15):
    linhvuc = df['NỘI DUNG'][i]
    Dutoan = df['DỰ TOÁN'][i]
    A.append(NSNN(linhvuc,Dutoan))
#Thực hiện yêu cầu 1
#Sắp xếp giảm dần cột dự toán bằng thuật toán sủi bọt
for i in range(14):
    for j in range(14-i):
        if A[j].Dutoan < A[j+1].Dutoan:
            A[j], A[j+1] = A[j+1], A[j]
k = int(input('Nhập số k lĩnh vực dự toán cao nhất cần lấy(k<= 15): '))
print("**",k," lĩnh vực có dự toán cao nhất cần lấy: ")
for i in range(k):
    print ("-",A[i].linhvuc,"- đạt" ,A[i].Dutoan*100//Sum,"%")
#Sắp xếp giảm dần cột dự toán bằng thuật toán sủi bọt
for i in range(14):
    for j in range(14-i):
        if A[j].Dutoan > A[j+1].Dutoan:
            A[j], A[j+1] = A[j+1], A[j]
k = int(input('Nhập số k lĩnh vực có dự toán thấp nhất cần lấy: '))
print("**",k," lĩnh vực có dự toán thấp nhất cần lấy: ")
for i in range(k):
    print ("-",A[i].linhvuc,"- đạt", A[i].Dutoan*100/Sum,"%")
 
print("---------------------------------------------------------")
 #Thực hiện yêu cầu 2
 #tổng thu từ các lĩnh vực chiếm tới 80% NSNN
input('Enter để tiếp tuc...')
print("Tổng thu dự toán từ các lĩnh vực sau chiếm 80%: ")
Sum1 = 0
i = 0
while True:
    Sum1 += A[i].Dutoan
    print(A[i].linhvuc)
    i = i+1
    if(Sum1 >= Sum*4/5 ):
        break  
print("------------------------------------------------------------")
#Thực hiện yêu cầu 3
# tổng thu từ các lĩnh vực có yếu tố nước ngoài 
Sum2 =  A[1].Dutoan+A[13].Dutoan+A[2].Dutoan
print("Tổng thu các lĩnh vực có yếu tố nước ngoài chiếm ",Sum2*100//Sum,"% tổng NSNN")   
print("----------------------------------------------------------")
#Thực hiện yêu cầu 4
#in ra linh vực và số dự toán tương ứng 
k = input('Nhập tên lĩnh vực cần lấy(ghi đầy đủ có dấu): ')
for i in range(15):
    if k.capitalize() == A[i].linhvuc:
        print(A[i].linhvuc,"có dự toán là: ", A[i].Dutoan)

input('Enter để biểu diễn đồ thị....')
#Thực hiện yêu cầu 5
# Vẽ đồ thị 
plt.barh(y = df.iloc[:,1],
    width = df.iloc[:,2],
    color= 'blue')
plt.xticks(rotation = 45)
plt.title("Du toan ngan sach nha nuoc năm 2019(đơn vị:tỷ đồng)")
plt.xlabel('Dự toán')
plt.ylabel('Nội dung')
plt.show()
