PV=['0','0','1','0']
L2=['0','1','n','0']
L3=[]
L4=[]
for i in range(len(PV)):
    try:
        L3=int(PV[i])+int(L2[i])
        L4.append(L3)
    except:
        L4.append('N')
    if (L4[i]==0):
        print('RWB')
    else:
        print("no.. RWB")
print(L4)
    
