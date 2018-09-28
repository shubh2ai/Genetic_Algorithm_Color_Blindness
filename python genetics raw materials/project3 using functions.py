from random import*
print("_______________genetics algorithm__________________")
#__________Input functions___________________________


L1=[]
L2=[]
L3=[]
def random1():
    global n1,L1,L3
    
    str(L1)
    for i in range(int(n1)):
        r1=str(randint(0,1))
       # L1[0]=r1
       # L1 = [0] * n1
        L1.append(r1)
       # L1 = [0] * n1
    print("L1=",L1)
    #print("L3=",L3)
    
    
def random2():
    global n2
    for i in range(int(n2)):
        r2=str(randint(0,1))
        L2.append(r2)
    print("L2=",L2)
def pop_s():
    global n1
    n1=int(input('       enter population size='))
def n_gen():
    global n2
    n2=int(input('enter number. of generations='))
    
    
#__________________Output functions____________________
def total_percent():
    print("percentage of the ​total​ population with R-G colorblindness=5%")
def female_percent():
    print("percentage of the ​female​ population with R-G colorblindness=3%")
def male_percent():
    print("percentage of the ​male​ population with R-G colorblindness =2%")
def pop_final():
    print("population ​size​=100")
global zerolist
'''def zerolist():
         global n1
         L1 = [0] * n1
         #return L1
         print("L1(0)=",L1)
   '''      
         
def gen():
    global n2,n1
    print(n2)
    for i in range(n2):
        print("this is generation:",i)
       # zerolist()
        total_percent()
        female_percent()
        male_percent()
        pop_final()
        random1()
        random2()
        
        
        

        


pop_s()
n_gen()
gen()
##total_percent()
##female_percent()
##male_percent()
##pop_final()
##
