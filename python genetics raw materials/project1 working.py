from random import *
#L1=population
L1=[]
L2=[]
L3=[]
L4=[]
j=0
k=0
m=0
for i in range(10):
    r1=str(randint(0,1))
#    print('r1[',i,']=',r1)
    L1.append(r1)
Female=[]
Male=[]
print('__________population vector_________')
for j in range(len(L1)):
    global j
    if(L1[j]=='0'):
      Male.append(L1[j])
      print('L1[',j,']=',L1[j],',represents male')
    elif(L1[j]=='1'):
        Female.append(L1[j])
        print('L1[',j,']=',L1[j],',represents female')
        
#....................first allele...........................................#

for i in range(10):
    r2=str(randint(0,1))
    L2.append(r2)
Dominantallele_1st=[]
Recessiveallele_1st=[]
print('_________first alleles_______')
for k in range(len(L2)):
   # global k
    if(L2[k]=='0'):
      Recessiveallele_1st.append(L2[k])
      print('L2[',k,']=',L2[k],',means recessive allele(20% prob)')
    elif(L2[k]=='1'):
        Dominantallele_1st.append(L2[k])
        print('L2[',k,']=',L2[k],',means dominant allele(80 % prob)')
    
#..........................second allele....................................#
for i in range(10):
    r3=str(randint(0,1))
    L3.append(r3)
Dominantallele_2nd=[]
Recessiveallele_2nd=[]
print('_________second allele______')
for m in range(len(L3)):
   # global m,j
    if(L3[m]=='0'):
          Recessiveallele_2nd.append(L3[m])
          print('L3[',m,']=',L3[m],',means recessive allele(20% prob)')
    elif(L3[m]=='1'):
            Dominantallele_2nd.append(L3[m])
            print('L3[',m,']=',L3[m],',means dominant allele(80 % prob)')
       
#......................insert N to the second allele of male................
'''for j in range(len(L1)):
        if(L1[j]=='0'):
            print("nannn")
            L4= L3.insert(m,'N')
 '''
print('population vector=',L1)
print("    allel2 before=",L3)
L5=[]
L6=[]
MMTX = []
FMTX = []
#MMTX1 = []
#FMTX1 = []
#L1=population vector,L2=allele1,L3=allele2 before,L3=allele2 after,L6=decision vector
for j in range(len(L1)):
    global j,m
    if(L1[j]=='0'):
        print('0 represents male so no 2nd allele')
        L3[j]='N'
       #L3[L3.index(L1[j])]='N'
        #L3[L1.index(j)]='N'
        #MMTX.append(L2[j], L3[j])
        #MMTX1(L2[j],L3[j])
        #MMTX1.append(L1[k])
    if(L1[j]=='1'):
         print('1 represents female,still 2nd allele exists')
         #FMTX.append(L2[j], L3[j])
         #FMTX1(L2[j],L3[j])
         #FMTX1.append(L1[k])
    try:
        L5=int(L1[j])+int(L3[j])
        L6.append(L5)
    except:
        L6.append('N')

def decision():
    for j in range(len(L1)):
        if (L6[j]==0):
            print('sum of PV and allele2nd is 0 so CB')
        else:
            print("sum of PV and allele2nd is not 0 so no CB")    
#print("    allel2 after=",L3)


def lists():
    list1=[L1,L3]
    print("Genes=",list1)
   # male1=[Male,]
    
#.................................................................


print('         allele 1st=',L2)
#print('   Dominantallele_1st=',Dominantallele_1st)
#print(' Recesssiveallele_1st=',Recessiveallele_1st)
print('in allele2 0 represents male so no 2nd allele and 1 represents female,still 2nd allele exists')
#print('   Dominantallele_2nd=',Dominantallele_2nd)
#print(' Recesssiveallele_2nd=',Recessiveallele_2nd)
#print('population vector=',L1)
#print("    allel2 before=",L3)
print('population vector=',L1)
print('   allele 2 after=',L3)
print('  decision vector\=',L6)
decision()
lists()
#............creating 2D list
#print("FMTX=",FMTX)
#print("MMTX=",MMTX)

