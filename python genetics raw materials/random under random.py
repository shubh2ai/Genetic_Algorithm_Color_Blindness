from random import*
def totalchild():
    r3=(randint(0,5))
    print("total child=",r3)
    for j in range(r3):
        r4=str(randint(0,1))
        if(r4=='0'):
            print(j,"th child is Male",r4)
        elif(r4=='1'):
            print(j,"th child is Female",r4)
totalchild()     
        


