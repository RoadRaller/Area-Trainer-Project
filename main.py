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
            print(u)
            return u

    
    return None



def register():
    name = input("enter name:")
    password = input("password:")
    new = [name,password,0]
    if findInfo(name) == None:
        addInfo(new)
        print("register complete")
        return name
    else:
        print('name taken,try again')
        return register()

def login():
    
    info = getInfo()
    name = input("username:")
    for user in info:
        if user[0] == name:
            password = input("password:")
            if password == user[1]:
                print("logged in")
                return user[0]
            else:
                print("try again")
                return login()
                             



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
    if   mode == "t":
        w,h,ans = qTri()
        print("find area of triangle")
        print(f"w:{w},h:{h}")
    elif mode == "r":
        w,h,ans = qRec()
        print("find area of rectangle")
        print(f"w:{w},h:{h}")

    elif mode == "c":
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




o = input("login(1) or sign up(2)")    
if o == "1":
    user = login()
elif o == "2":
    user = register()


while True:
    print("answer question(1),checkinfo(2),logout(3)")
    
    opt = input()
    if opt == "1":
        mode = input("circles(c),triangles(t),rectangle/sqaures(r)")
        askQ(user,mode)
    elif opt == "2":
        name = input("target username: ")
        findInfo(name)
    elif opt == "3":
        break
        
