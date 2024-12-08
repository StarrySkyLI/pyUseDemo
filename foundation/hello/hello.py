# 输出
print("Hello,World!",end="\n") #输出

print("Hello,World!",end="\t") #输出

print("hello,china")

print("hello","china",sep="...")

print("hello","china"*3)

print("520"+"1314")

print(520+1314)

print('I "love" you')

print('I love you')

print("I 'love' you")

print(r"c:\abc\def")

print(3.14)

name="starry"
print(name)

print(False and True)
print(False or True)
print( not True)

a = b = c = 1
isinstance(a,int)

age=18
if age>=18:
    print("you are a younger")
else:
    print("you are a older")

list_ada =["ada","3.144","yyy-xxx-ddd","Eng"]
print(list_ada)
print(list_ada[0])
print(list_ada[1])
print(list_ada[2])

for ada in list_ada:
    print(ada)

tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')

print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')


# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)     # a 和 b 的差集

print(a | b)     # a 和 b 的并集

print(a & b)     # a 和 b 的交集

print(a ^ b)     # a 和 b 中不同时存在的元素


dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]= "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}


print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

x = b"hello"
y = x[1:3]  # 切片操作，得到 b"el"
z = x + b"world"  # 拼接操作，得到 b"helloworld"
print(x)
print(z)

a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c = a - b
print("2 - c 的值为：", c)

c = a * b
print("3 - c 的值为：", c)

c = a / b
print("4 - c 的值为：", c)

c = a % b
print("5 - c 的值为：", c)

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print("6 - c 的值为：", c)

a = 10
b = 5
c = a // b
print("7 - c 的值为：", c)

# 该实例演示了数字猜谜游戏
number = 7
guess = -1
print("数字猜谜游戏!")
# while guess != number:
#     guess = int(input("请输入你猜的数字："))
#
#     if guess == number:
#         print("恭喜，你猜对了！")
#     elif guess < number:
#         print("猜的数字小了...")
#     elif guess > number:
#         print("猜的数字大了...")

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 402 | 403:
            return "Not allowed"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

mystatus=400
print(http_error(400))

n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))

count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")


for x in range(6):
  print(x)
else:
  print("Finally finished!")


n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('循环结束。')



n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('循环结束。')

set()