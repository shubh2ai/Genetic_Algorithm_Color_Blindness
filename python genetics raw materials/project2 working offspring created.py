from random import *
#L1=population
L1=[]
L2=[]
L3=[]
L4=[]

for i in range(10):
    r1=str(randint(0,1))
#    print('r1[',i,']=',r1)
    L1.append(r1)
Female=[]
Male=[]
def population():
    print('__________population vector_________')
    for j in range(len(L1)):
        if(L1[j]=='0'):
          Male.append(L1[j])
          print('L1[',j,']=',L1[j],',represents male')
        elif(L1[j]=='1'):
            Female.append(L1[j])
            print('L1[',j,']=',L1[j],',represents female')
population()       
        
#....................first allele...........................................#

for i in range(10):
    r2=str(randint(0,1))
    L2.append(r2)
Dominantallele_1st=[]
Recessiveallele_1st=[]
Mallele1=[]
Fallele1=[]
print('_________first alleles_______')
for k in range(len(L1)):
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
for m in range(len(L1)):
   # global m,j
    if(L3[m]=='0'):
          Recessiveallele_2nd.append(L3[m])
          print('L3[',m,']=',L3[m],',means recessive allele(20% prob)')
    elif(L3[m]=='1'):
            Dominantallele_2nd.append(L3[m])
            print('L3[',m,']=',L3[m],',means dominant allele(80 % prob)')
       
#......................insert N to the second allele of male................

print('population vector=',L1)
print("    allel2 before=",L3)
L5=[]
L6=[]
MMTX = []
FMTX = []
Mallele2=[]
Fallele2=[]
#MMTX1 = []
#FMTX1 = []
#L1=population vector,L2=allele1,L3=allele2 before,L3=allele2 after,L6=decision vector
for j in range(len(L1)):
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
        L5=int(L1[j])+int(L3[j]+int(L2[j]))
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
def seperate():
    for j in range(len(L1)):
        if(L1[j]=='0'):
             Mallele1.append(L2[j])
        elif(L1[j]=='1'):
                Fallele1.append(L2[j])
    for j in range(len(L1)):
        if(L1[j]=='0'):
             Mallele2.append(L3[j])
        elif(L1[j]=='1'):
                Fallele2.append(L3[j])    
def lists():
    print("___________LIST of parent allele(MF) formation____________")
    list1=[L1,L3]
    print("Genes=",list1)
##    Mallele1.sort()
##    Mallele2.sort()
##    Fallele1.sort()
##    Fallele2.sort()
##    Male.sort()
##    Female.sort()
    MaleFemalelist=[Male,Female]
    male_al=[Mallele1,Mallele2]
    female_al=[Fallele1,Fallele2]
    print("MaleFemale_list=[Male],[Female]")
    print("MaleFemale_list=",MaleFemalelist)
    
    print("male_al_list=[Mallele1],[Mallele2]")
    print("male_al_list=",male_al)
    print("female_al_list=[Fallele1],[Fallele2]")
    print("female_al_list=",female_al)
def offspring():
    try:
            print("___________OFFSPRING formation____________")
            
            try:
                print("offspring created by allele1 of male and female")
                for i in range(len(L1)):
                    mergeallele1=Mallele1[i]+'\t'+Fallele1[i]
                    print("'for'","'Male'",[i],"'Female'",[i],"having pair=",Male[i],Female[i],"offspring",[i],"'mergeallele1(MF)='",mergeallele1)
                    
            except:
                print("offspring created by allele2 of male and female")
                for i in range(len(L1)):
                    mergeallele2=Mallele2[i]+'\t'+Fallele2[i]
                    print("'for'","'Male'",[i],"'Female'",[i],"having pair=",Male[i],Female[i],"offspring",[i],"'mergeallele2(MF)='",mergeallele2)
        
                
    except:
        print("____offspring created successfully for new generation ____")
##    print("Male=",Male)
##    print("Female=",Female)
##    print("Mallele1=",Mallele1)
##    print("Fallele1=",Fallele1)
##    print("Mallele2=",Mallele2)
##    print("Fallele2=",Fallele2)
##    
    
#.................................................................


print('         allele 1st=',L2)
#print('   Dominantallele_1st=',Dominantallele_1st)
#print(' Recesssiveallele_1st=',Recessiveallele_1st)
print('in allele2 0 represents male so no 2nd allele and 1 represents female,still 2nd allele exists')
#print('   Dominantallele_2nd=',Dominantallele_2nd)
#print(' Recesssiveallele_2nd=',Recessiveallele_2nd)
#print('population vector=',L1)
print('population vector=',L1)
print('   allele 2 after=',L3)
print('  decision vector=',L6)
decision()
seperate()
lists()
offspring()
#............creating 2D list
#print("FMTX=",FMTX)
#print("MMTX=",MMTX)

