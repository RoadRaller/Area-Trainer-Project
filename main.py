import os

#file func
def append_file(info):
    file = open("user.txt","a")
    file.write(f'{info} \n')
    file.close()

def get_info():
    file = open("user.txt",'r')
    text = file.readlines()
    info = []
    for l in text:
        l = l[:-2]
        l = l.split()
        info.append(l)

    return info

def update_file(info):
    file = open("user.txt",'w')
    for u in info:
        line = " ".join(line)
        file.write(f'{line}\n') 

            

def search(user):
    info = get_info()
    for u in info:
        if u[0] == user:
            return u
    return None



def register(name,password):
    info = name+' '+password+' '+'0'
    if search(name) == None:
        append_file(info)
        print("register complete")
    else:
        print('name taken')



register("u1","1234")
