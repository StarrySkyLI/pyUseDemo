#case 1
def a1(func):
    def a2():
        print("case1 start")
        func()
        print("case1 over")
    return a2
@a1
def a3():
    print("starry")
# a3 = a1(a3)   语法糖等同于@a1
a3()

# case 2
def a1(func):
    def a2(name):
        print("case2 start")
        func(name)
        print("case2 over")
    return a2
@a1
def a3(name):
    print(f"starry{name}")

a3("starry")
# case 3
def a1(func):
    def a2(*args):
        print("case3 start")
        func(*args)
        print("case3 over")
    return a2
@a1
def a3(name,time):
    print(f"starry{name},the time is {time}")

a3("starry",18)
@a1
def a4(age):
    print(f"starry‘s age is {age}")
a4(18)

# case 4 final
def a1(func):
    def a2(*args,**kwargs):
        print("case4 start")
        func(*args,**kwargs)
        print("case4 over")
    return a2
@a1
def a3(name,time):
    print(f"starry{name},the time is {time}")

a3("starry",18)
@a1
def a4(age):
    print(f"starry‘s age is {age}")
a4(18)

@a1
def a5(name,time,**kwargs):
    print(f"starry's name is {name},the time is {time}")
    print(kwargs)

a5("starry",18,level="super",age=18,star="earth")