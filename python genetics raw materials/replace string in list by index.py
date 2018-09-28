L1=['1','1','0','1','0']
PV=['0','1','1','0','1']
L4=[]
L3=[]
print("L1:",L1)
for i2 in range(len(PV)):
    #global j,m
    if(PV[i2]=='0'):
        print('represents male so no 2nd allele') 
        L1[L1.index(PV[i2])]='N'
    if(L1[i2]=='1'):
         print('represents female,still 2nd allele exists')

#for i in range(len(PV)):
    try:
        L3=int(PV[i2])+int(L1[i2])
        L4.append(L3)
    except:
        L4.append('N')
    if (L4[i2]==0):
        print('RWB')
    else:
        print("no.. RWB")
print("L1 after:",L1)
print(L4)
    
