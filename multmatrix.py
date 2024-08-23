a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3,3],[4,5,6,6],[7,8,9,9]]

x=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            x[i][j]+=a[i][k]*b[k][j]

for i in x:
    print(i)