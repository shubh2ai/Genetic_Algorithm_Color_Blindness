from random import*
L2=[]
L3=[]
r2=''
def random1():
    for i in range(5):
        r1=str(randint(0,1))
        L2.append(r1)
    print("L2=",L2)
def random2():
    for j in range(5):
        r2=str(randint(0,1))
        L3.append(r2)
        L2=L3
    print("L2=",L2)
random1()
random2()
print("L2=",L2)
