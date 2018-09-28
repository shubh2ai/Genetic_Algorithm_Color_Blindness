from random import*
L1= ['1', '1', '0', '1', '1', '0', '0', '0', '1', '1', '1', '0', '0', '1', '1', '1', '1', '1', '0', '1']
L3= ['0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0']
def secondallele():
    print('__________________________________________________________________second allele___________________________________________________')
    global L1,L2,L3,list1,list2,L9,L10,L11,L8,L7,newpop
    for i in range(10):
        r3=str(randint(0,1))
        L3.append(r3)
    
#......................insert N to the second allele of male..........................
    L3=L3[0:len(L1)]
    print('population vector=',L1)
    print("    allel2 before=",L3)
    MMTX = []
    FMTX = []
    #L1=population vector,L2=allele1,L3=allele2 before,L3=allele2 after,L6=decision vector
    for j in range(len(L1)):
        if(L1[j]=='0'):
            # print('0 represents male so no 2nd allele')
            L3[j]='N'     
        if(L1[j]=='1'):
            continue
            # print('1 represents female,still 2nd allele exists')
    print('population vector=',L1)
    print("     allel2 after=",L3)
secondallele()
