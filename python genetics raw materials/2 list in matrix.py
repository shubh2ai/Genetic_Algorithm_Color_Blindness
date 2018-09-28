L1=['0','1','1','0','0']
L2=['1','1','0','0','1']
L3=['1','0','1','0','1']
matrix = []
for i in range(len(L1)):
     matrix.append(L1[i])
matrix.append(\n)     #matrix.append([L1[i],L2[i]])
for i in range(len(L1)):
     matrix.append(L2[i])
for i in range(len(L1)):
     matrix.append(L3[i])
        
       
#matrix2 = [[L1[i], L2[i]] for i in range(len(L1))]
##for i in range(len(L1)):
##    matrix2 = [L1[i], L2[i]]
##    print(matrix2)
    
print(matrix)

l=[L1 L2 L3]
