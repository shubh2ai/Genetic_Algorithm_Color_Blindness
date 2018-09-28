from random import *
L1=[]
j=0
for i in range(10):
    r1=str(randint(0,1))
#    print('r1[',i,']=',r1)
    L1.append(r1)
Dominantallele=[]
Recessiveallele=[]
for j in range(len(L1)):
    if(L1[j]=='0'):
      Recessiveallele.append(L1[j])
      print('L1[',j,']=',L1[j],',means recessive allele(20% prob)')
    elif(L1[j]=='1'):
        Dominantallele.append(L1[j])
        print('L1[',j,']=',L1[j],',means dominant allele(80 % prob)')
        
print('l1[',i,']=',L1)
print(fal)
print(mal)


