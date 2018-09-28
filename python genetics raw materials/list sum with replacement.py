L1=['1','0','1','0']
L2=['1','1','0','0']
L3=['1','0','1','1']
L4=[]
L5=[]
L6=[]
for j in range(4):
    if(L1[j]=='0'):
        print('0 represents male so no 2nd allele')
        L3[j]='N'
        L4.append(L3)
       #L3[L3.index(L1[j])]='N'
        #L3[L1.index(j)]='N'
        #MMTX.append(L2[j], L3[j])
        #MMTX1(L2[j],L3[j])
        #MMTX1.append(L1[k])
        
    
    print(L4)
    if(L1[j]=='1'):
         print('1 represents female,still 2nd allele exists')
         #FMTX.append(L2[j], L3[j])
         #FMTX1(L2[j],L3[j])
         #FMTX1.append(L1[k])
    try:
        L5=int(L1[j])+int(L4[j]+int(L2[j]))
        L6.append(L5)
    except:
        L3[j]=0;
        L5=int(L1[j])+int(L4[j]+int(L2[j]))
        L6.append(L5)
print(L6)
