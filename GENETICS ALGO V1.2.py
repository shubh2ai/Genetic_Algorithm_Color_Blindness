from random import *
#L1=population
L1=[]
L2=[]
L3=[]
L4=[]
L5=[]
L6=[]
Mallele1=[]
Fallele1=[]
Mallele2=[]
Fallele2=[]
Female=[]
Male=[]
count1=0
count2=0
p=0
p1=0
p2=0
#________________________________________________________________________random___________________________________________________________________#
def random1():
    for i in range(10):
        r1=str(randint(0,1))
    #    print('r1[',i,']=',r1)
        L1.append(r1)
def random2():
    for i in range(10):
        r2=str(randint(0,1))
        L2.append(r2)
#______________________________________________________________________________population__________________________________________________________________#
def population():
    print('__________population vector_________')
    random1()
    for j in range(len(L1)):
        if(L1[j]=='0'):
          Male.append(L1[j])
          print('L1[',j,']=',L1[j],',represents male')
        elif(L1[j]=='1'):
            Female.append(L1[j])
            print('L1[',j,']=',L1[j],',represents female')     
        
#_________________________________________________________________________________first allele__________________________________________________________________#
def firstallele():
    print('_________first alleles_______')
    random2()
    Dominantallele_1st=[]
    Recessiveallele_1st=[]
    for k in range(len(L1)):
       # global k
        if(L2[k]=='0'):
          Recessiveallele_1st.append(L2[k])
          print('L2[',k,']=',L2[k],',means recessive allele(20% prob)')  
        elif(L2[k]=='1'):
            Dominantallele_1st.append(L2[k])
            print('L2[',k,']=',L2[k],',means dominant allele(80 % prob)')
    
#_________________________________________________________________________________second allele___________________________________________________________________#
def secondallele():
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
    MMTX = []
    FMTX = []
    #L1=population vector,L2=allele1,L3=allele2 before,L3=allele2 after,L6=decision vector
    for j in range(len(L1)):
        if(L1[j]=='0'):
            print('0 represents male so no 2nd allele')
            L3[j]='N'     
        if(L1[j]=='1'):
             print('1 represents female,still 2nd allele exists')
    print('population vector=',L1)
    print("     allel2 after=",L3)
#___________________________________________________________________________find percents__________________________________________________________________________
def findpercents():
    print("_______________find percents__________________")
    global count1,count2,p,p1,p2
    
    for j in range(len(L1)):
        if(L3[j]=='N'):
                  L3[j]='0'
        L5=int(L3[j])+int(L2[j])
        L6.append(str(L5))
    print("    decision vect.=",L6)
    for j in range(len(L1)):
        if (L6[j]=='0'):
            print("sum of allele1st and allele2nd is 0 so",j,"person is CB")
            print("L1=",L1[j])
            if(L1[j]=='0'):
                count1=count1+1
                print(j,"person is male cb")    
            elif(L1[j]=='1'):
                count2=count2+1
                print(j,"person is female cb")
    global percent           
    def percent():
        p=((count1+count2)/10)*100
        print("totalcb%=",p)
        p1=(count1/10)*100
        print("malecb%=",p1)
        p2=(count2/10)*100
        print("femalecb%=",p2)
    percent()              
#print("    allel2 after=",L3)
#_______________________________________________________________LIST and GENES______________________________________________________________
def lists():
    print("___________LIST of parent allele(MF) formation____________")
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
    seperate()
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
    list1=[L2,L3]
    print("Genes=",list1)
#_________________________________________________________________________OFFSPRING formation___________________________________________________________________________
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
    
#______________________________________________________________________________________final output______________________________________________________________

def  finaloutput():
    print("______________final output______________")
    #print('   Dominantallele_1st=',Dominantallele_1st)
    #print(' Recesssiveallele_1st=',Recessiveallele_1st)
    print('in allele2 0 represents male so no 2nd allele and 1 represents female,still 2nd allele exists')
    #print('   Dominantallele_2nd=',Dominantallele_2nd)
    #print(' Recesssiveallele_2nd=',Recessiveallele_2nd)
    #print('population vector=',L1)
    print('population vector=',L1)
    print('       allele 1st=',L2)
    print('   allele 2 after=',L3)
    list1=[L2,L3]
    print("            Genes=",list1)
    print('  decision vect=',L6)
    percent()
#________________________________________________________________________________main___________________________________________________________________________________    
def main():
    
    population()
    firstallele()
    secondallele()
    lists()
    findpercents()
    offspring()
    finaloutput()
main()
    

