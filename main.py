import os

#file func
def update_file(info):
    file = open("user.txt","a")
    file.write(f'{info} \n')
    file.close()

def get_info():
    file = open("user.txt",'r')
    info = file.readlines()
    for l in info:
        l = l[:-2]
        print(l)
    print(info)


def register(name,password):
    info = name+' '+password+' '+'0'
    update_file(info)



update_file('hello')
get_file()