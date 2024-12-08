class person(object):
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def func1(self):
        print(f'name is {self.name},age is {self.age}, gender is {self.gender}')


p1=person('John',23,'Male')
p1.func1()

p2=person('Johner',24,'Female')
p2.func1()

class food(object):
    def __init__(self):

        self.time = 0
        self.state='fresh'
        self.dressing=[]

    def CookTime(self,time):
        self.time +=time

        if 0<self.time<10:
            self.state= 'not good'
        elif 10<self.time<20:
            self.state= 'good'
        else:
            self.state= 'bad'
    def dress(self,dressing):
        self.dressing.extend(dressing)

    def __str__(self):
        return f'the cook time is {self.time} min,state is {self.state},dressing is {self.dressing}'

moonCookie =food()
moonCookie.CookTime(12)
moonCookie.dress(['milk','egg'])
print(moonCookie)

moonCookie.CookTime(12)
moonCookie.dress(['suger'])
print(moonCookie)

# 单继承
class 炒菜(food):
    pass

回锅肉 =炒菜()

回锅肉.CookTime(12)
回锅肉.dress(['肉','豆瓣'])
print(回锅肉)
# 多继承
class cook(person,food):
    pass

做饭=cook('a','b',2)

print(cook.__mro__)