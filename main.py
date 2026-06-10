import os

#file func

    

def getInfo():
    file = open("user.txt",'r')
    text = file.readlines()
    info = []
    for l in text:
        l = l[:-1]
        print(l)
        l = l.split()
        print(l)
        l[2] = int(l[2])
        print(l)
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




getInfo()
