temp = [[0,0],[0,0]] 
def sum(m,n): 
    for i in range(2): 
        for j in range(2): 
            temp[i][j] = m[i][j] + n[i][j] 
    return temp


mat1 = [[1,2],[3,4]] 
mat2 = [[6,7],[8,9]] 

sum(mat1,mat2);

#Code: 
count = 0
for i in range(0, len(temp)):
    temp = len(temp[i])
    for j in range(0, temp):
        count = count + 1
        print(count, " Item of array is: ", temp[i][j])










