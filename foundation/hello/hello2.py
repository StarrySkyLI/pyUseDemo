姓名="starry"
年龄=20
print(f"我的名字是{姓名}，年龄是{年龄}")
print(f"我的名字是{姓名}，年龄是{年龄+1}")
#
# name = input("plz enter your name:")
# age = int(input("plz enter your age:"))
name = "I'am starry"
age =20
print(f"your name is {name} and your age is {age}")
print(f"your name is {name} and your age is {age+1} in next year")
print(name[0])
print(name[1])
print(name[2])
print(name[5:11])
print(name[5:11:2])
print(name[-6:])


name =" i ,am ,starry"
print(name)
print(name.replace("starry","hello"))
print(name.split(",",1))

name2=['i', 'am','starry']
print(name2)
print('_'.join(name2))
print(name2.index("am"))
print(len(name2))
name2.append('aa')
name2.extend(['bb','cc'])
name2.insert(1,'qq')
print(name2)

def add_name(a,b,c=abs):
    """add two names"""
    print(f"hello a,b,c:{a}{b}{c}")
    return c(a)+c(b)

print(add_name(1,2,abs))

help(add_name)

def update_name(**kwargs):
    print(f"hello {kwargs}")

update_name(a="aa",b="bb",c="cc")

def 递归(a):
    if a==1:
        return a
    resp =a +递归(a-1)
    return resp
print(递归(5))