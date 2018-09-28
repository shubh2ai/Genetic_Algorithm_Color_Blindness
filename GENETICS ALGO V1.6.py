from random import *
#L1=population

n1=0
n2=0
global L1,L2,L3,L4,L5,L6,L66
global percent,p,p1,p2
global L1,L2,L3,list1,list2,L9,L10,L11,L8,L7,newpop,Mallele1,Mallele2,Fallele1,Fallele2,mergeallele1,mergeallele2
L1=[]
L2=[]
L3=[]
L4=[]
L5=[]
L6=[]
L66=[]
mergeallele1=[]
mergeallele2=[]
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
    global n1
    for i in range(n1):
        r1=str(randint(0,1))
    #    print('r1[',i,']=',r1)
        L1.append(r1)
def random2():
    global n2
    for i in range(n1):
        r2=str(randint(0,1))
        L2.append(r2)
#______________________________________________________________________________population__________________________________________________________________#
def population():
    global L1,L2,L3,list1,list2,L9,L10,L11,L8,L7,newpop
    print('_________________________________________________________________population vector_________________________________________________')
    random1()
    for j in range(len(L1)):
        if(L1[j]=='0'):
          Male.append(L1[j])
          #print('L1[',j,']=',L1[j],',represents male')
        elif(L1[j]=='1'):
            Female.append(L1[j])
           # print('L1[',j,']=',L1[j],',represents female')     
        
#_________________________________________________________________________________first allele__________________________________________________________________#
def firstallele():
    print('___________________________________________________________________first alleles_____________________________________________________')
    random2()
    Dominantallele_1st=[]
    Recessiveallele_1st=[]
    for k in range(len(L1)):
       # global k
        if(L2[k]=='0'):
          Recessiveallele_1st.append(L2[k])
         # print('L2[',k,']=',L2[k],',means recessive allele(20% prob)')  
        elif(L2[k]=='1'):
            Dominantallele_1st.append(L2[k])
          #  print('L2[',k,']=',L2[k],',means dominant allele(80 % prob)')
    
#_________________________________________________________________________________second allele___________________________________________________________________#
def secondallele():
    print('__________________________________________________________________second allele___________________________________________________')
    global L1,L2,L3,list1,list2,L9,L10,L11,L8,L7,newpop,L6,L66
    for i in range(n1):
        r3=str(randint(0,1))
        L3.append(r3)
    L3=L3[0:len(L1)]
    Dominantallele_2nd=[]
    Recessiveallele_2nd=[]
    for m in range(len(L1)):
        #global m,j
        if(L3[m]=='0'):
              Recessiveallele_2nd.append(L3[m])
              #print('L3[',m,']=',L3[m],',means recessive allele(20% prob)')
        elif(L3[m]=='1'):
                Dominantallele_2nd.append(L3[m])
               # print('L3[',m,']=',L3[m],',means dominant allele(80 % prob)')
       
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
#_______________________________________________________________find percents__________________________________________________________________________

global decivect
def decivect():
        global count1,count2,p,p1,p2
        global L1,L2,L3,list1,list2,L9,L10,L11,L8,L7,newpop,L6,L5,L4,L66,n2,decivect
        for j in range(len(L1)):
            if(L3[j]=='N'):
                      L3[j]='0'
            L5=int(L3[j])+int(L2[j])
            L66.append(str(L5))   
def findpercents():
    print("_______________________________________________________________________find percents_____________________________________________")
    global count1,count2,p,p1,p2
    global L1,L2,L3,list1,list2,L9,L10,L11,L8,L7,newpop,L6,L5,L4,L66,n2
    global percent,p,p1,p2  
            
                 #replace outside of for loop
    print("    decision vect.=",L6)
    #L6=L6[0:len(L1)]       #L6 comes as [appended which has size L1 + newone ]so use slicing  
    for j in range(len(L1)): # if L1 then index out of range so take as L6 becoz L6 will be same as L1
        if (L6[j]=='0'):
            #print("sum of allele1st and allele2nd is 0 so",j,"person is CB")
            #print("L1=",L1[j])
            if(L1[j]=='0'):
                count1=count1+1
                print(j,"th person is male cb")    
            elif(L1[j]=='1'):
                count2=count2+1
                print(j,"th person is female cb")
    try:
        global percent,p,p1,p2
        def percent():
            global p,p1,p2
            p=((count1+count2)/len(L6))*100
            print("totalcb%=",p)
            p1=(count1/len(L6))*100
            print("malecb%=",p1)
            p2=(count2/len(L6))*100
            print("femalecb%=",p2)
    except(TypeError,ZeroDivisionError):
        print("error")

#print("    allel2 after=",L3)
#_______________________________________________________________LIST and GENES______________________________________________________________
def lists():
    print("___________________________________________________________________LIST of parent allele(MF) formation____________")
    global L1,L2,L3,list1,list2,L9,L10,L11,L8,L7,newpop,L5,L6,L4,L66
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
    #print("MaleFemale_list=[Male],[Female]")
    #print("MaleFemale_list=",MaleFemalelist)
    
    #print("male_al_list=[Mallele1],[Mallele2]")
    #print("male_al_list=",male_al)
    #print("female_al_list=[Fallele1],[Fallele2]")
    #print("female_al_list=",female_al)
    list1=[L2,L3]
    print("Genes=",list1)
#_________________________________________________________________________OFFSPRING formation___________________________________________________________________________
def offspring():
    global L1,L2,L3,list1,list2,L9,L10,L11,L8,L7,newpop,L6,L66
    newpop=[]
    L7=[]    #newpop
    L8=[]    #malechildallele 1
    L9=[]   #femalechildallele 2
    L10=[]  #childallele1
    L11=[]   #childallele2
    newpop=[]
    global totalchild
    def totalchild():
        r3=(randint(0,5))
        #print("offspring",[i],"have total child=",r3)
        for j in range(r3):
            r4=str(randint(0,1))
            if(r4=='0'):
                newpop.append(r4)
                #L8.append(Fallele1[i])#because totalchild() is called after , for i in range(len(L1)):    mergeallele1=[ Mallele1[i],Fallele1[i] ] so i is well defined.
                #L8.append(Fallele2[i])
                L8=[Fallele1[i],Fallele2[i]]
                L10.append(Fallele1[i])# for childallele 1 formation
                L11.append(Fallele2[i])# for childallele 2 formation
               #print(j,"th child is Male[",r4,"]","with assigned allele pair(parents F1F1)[",L8,"]")
            elif(r4=='1'):
                newpop.append(r4)
                #L9.append(Fallele2[i])#because totalchild() is called after , for i in range(len(L1)):    mergeallele1=[ Mallele1[i],Fallele1[i] ] so i is well defined.
                #L9.append(Mallele1[i])
                L9=[Fallele1[i],Mallele1[i]] #in male allele2 is not available so take Mallele1
                L10.append(Fallele1[i])# for childallele 1 formation
                L11.append(Mallele1[i])# for childallele 2 formation
                #print(j,"th child is Female[",r4,"]","with assigned allele pair(parents F1M1)[",L9,"]")
        #print("\n")       
    try:
            print("_________________________________________________________________OFFSPRING formation____________________________________","\n")
            
            try:
                global mergeallele1
                mergeallele1=[]
                print("offspring created by allele 1 of male and female")
                for i in range(len(L1)):
                   # mergeallele1= Mallele1[i]+'\t'+Fallele1[i] 
                    mergeallele1=[ Mallele1[i],Fallele1[i] ]
                      #print("'for'","'Male'",[i],"'Female'",[i],"having pair=",Male[i],Female[i],"offspring",[i],"'mergeallele1(MF)='",mergeallele1,"have",r3,"child")
                    #print("'for'","'Male'",[i],"'Female'",[i],"offspring",[i],"'mergeallele1(MF)='",mergeallele1)
                    totalchild()
            except:
                global mergeallele2
                mergeallele2=[]
                print("offspring created by allele 2 of male and female")
                for i in range(len(L1)):
                    #mergeallele2= Mallele2[i]+'\t'+Fallele2[i]
                    mergeallele2=[ Mallele2[i],Fallele2[i] ]
                      #print("'for'","'Male'",[i],"'Female'",[i],"having pair=",Male[i],Female[i],"offspring",[i],"'mergeallele2(MF)='",mergeallele2)
                    #print("'for'","'Male'",[i],"'Female'",[i],"offspring",[i],"'mergeallele2(MF)='",mergeallele2)
                    totalchild()
            
                    
    except:
        print("_____________________________________________________offspring created successfully for new generation ___________________","\n")
    global update
    def update():
        global L1,L2,L3,list1,list2,L9,L10,L11,L8,L7,newpop,L6,L66,decivect
        print("newpop=",newpop,"total pop=",len(newpop))
        L2=L10
        L3=L11
        L1=newpop
        L6=L66
        
        #L6=L6[len(L1):len(L6)] # this update is not working
        print("newallele1=",L10)
        print("newallele2 before=",L11)
        print("population vectn=",L1)
        secondallele()
        lists()
        global decivect
        decivect()
        findpercents()
        #offspring()
        finaloutput()
    #print("Genesn=",list1)
##    print("Male=",Male)
##    print("Female=",Female)
##    print("Mallele1=",Mallele1)
##    print("Fallele1=",Fallele1)
##    print("Mallele2=",Mallele2)
##    print("Fallele2=",Fallele2)

 

#______________________________________________________________________________________final output______________________________________________________________

def  finaloutput():
    global L1,L2,L3,list1,list2,L9,L10,L11,L8,L7,newpop,L6,L66
    
    print("____******************************************FINAL OUTPUT***********************************************************____")
    #print('   Dominantallele_1st=',Dominantallele_1st)
    #print(' Recesssiveallele_1st=',Recessiveallele_1st)
    print('in allele2 0 represents male so no 2nd allele and 1 represents female,still 2nd allele exists')
    #print('   Dominantallele_2nd=',Dominantallele_2nd)
    #print(' Recesssiveallele_2nd=',Recessiveallele_2nd)
    #print('population vector=',L1)
    print('population vector=',L1)
    print('       allele 1st=',L2)
    print('   allele 2 after=',L3)
    global list1
    list1=[L2,L3]
    print("            Genes=",list1)
    print('  decision vect=',L6)
    percent()
#________________________________________________________________________________main___________________________________________________________________________________    
def main():
    print("_____________________________________________________________genetics algorithm__________________________________________")
    #__________Input functions___________________________
    
    global L1,L2,L3,list1,list2,L9,L10,L11,L8,L7,newpop,L6,L66,n2
    global percent,p,p1,p2
    def pop_s():
        global n1
        n1=int(input('       enter population size='))
    def n_gen():
        global n2
        n2=int(input('enter number. of generations='))
    #_____________________________________Output functions____________________
    def total_percent():
        print("percentage of the ​total​ population with R-G colorblindness=",p)
    def female_percent():
        print("percentage of the ​female​ population with R-G colorblindness=",p2)
    def male_percent():
        print("percentage of the ​male​ population with R-G colorblindness =",p1)
    def pop_final():
        print("final population ​size​=",len(L6))
    def gen():
        global n2
        print(n2)
        population()
        firstallele()
        secondallele()
        lists()
        for i in range(n2):
            print("______________________________________________this is generation:",i,"___________________________________________")
            offspring()
            update()
#______________________________________________
            total_percent()
            female_percent()
            male_percent()
            pop_final()
            


    pop_s()
    n_gen()
    gen()
    
    
main()
    

