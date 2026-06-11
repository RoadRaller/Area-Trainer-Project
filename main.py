import os
import random


#file func

    

def getInfo():
    file = open("user.txt",'r')
    text = file.readlines()
    info = []
    for l in text:
        l = l.strip()

        if not l:
            continue
        
        l = l.split()
        l[2] = int(l[2])
        
        info.append(l)
    print(info)
    return info

def pushFile(info):
    file = open("user.txt",'w')
    for u in info:
        u[2] = str(u[2])
        line = " ".join(u)
        file.write(f'{line}\n') 
    file.close()


def addScore(user,new):
    info = getInfo()
    for u in info:
        if u[0] == user:
            u[2] += new
    print(f"{new}score added, now{u[2]}")
    pushFile(info)

def addInfo(new):
    info = getInfo()
    info.append(new)
    pushFile(info)

def findInfo(user):
    info = getInfo()
    for u in info:
        if u[0] == user:
            return u
        print(u)
    return None



def register(name,password):
    new = [name,password,0]
    if findInfo(name) == None:
        addInfo(new)
        print("register complete")
    else:
        print('name taken')

def login():
    pass
#question

def qRec():
    w = random.randint(1,100)
    h = random.randint(1,100)
    return w,h,float(w*h)

def qTri():
    w = random.randint(1,100)
    h = random.randint(1,100)
    return w,h,float(w*h/2)

def qCir():
    r = random.randint(1,100)
    return r,float(r*r)


def genOpt(ans):
    ind = random.randint(0,3)
    opt = []
    for i in range(4):
        opt.append(float(random.randint(1,100)))
    opt[ind] = ans
    return opt,ind 

def askQ(user,mode):
    if   mode == "tri":
        w,h,ans = qTri()
        print("find area of triangle")
        print(f"w:{w},h:{h}")
    elif mode == "rec":
        w,h,ans = qRec()
        print("find area of rectangle")
        print(f"w:{w},h:{h}")

    elif mode == "cir":
        r,ans = qCir()
        print("find area of circle(pi)")
        print(f"r:{r}")
    
    opt,ind = genOpt(ans)
    for i in range(4):
        print(f"option {i}:{opt[i]}")
    inp = int(input("enter chosen option"))
    if inp == ind:
        addScore(user,2)
    else:
        inp = int(input("attempt 2:"))
        if inp == ind:
            addScore(user,1)
        else:
            print(f"answer:{opt[ind]}")



    


askQ("u1","tri")
findInfo("u1")