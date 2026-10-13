m=[[1,2,3],
        [4,5,6],
        [7,8,9]
]
row=len(m)
col=len(m[0])

t=[[m[j][i]%2==0 for j in range(row) ]for i in range(col)] 
print(t)