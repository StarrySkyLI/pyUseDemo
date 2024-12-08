import time

# case 1
a=1
b=int(input("Enter a number:"))
try:
    print(a/b)
# except ZeroDivisionError:
#     print("Division by zero")
except Exception as e:
    print("err :{}".format(e))
else:
    print("ok")
finally:
    print("fin 一般用于关闭")

# case 2
try:
    file =open("1999.txt")

    try:
        while True:
            read = file.readline()
            if len(read) == 0:
                break
            time.sleep(2)
            print(read)
    except:
        print("发生了意外终止")
    finally:
        file.close()
        print('close')
except:
    print("cant find file")

# case 3
class MyError(Exception):
    def __init__(self,len,min_len):
        self.len =len
        self.min_len = min_len
    def __str__(self):
        return f"Your password is too short, it should be at least {self.min_len} characters long."

def  check_password():
    try:
        password = input("Enter your password:")
        if len(password) < 8:
            raise MyError(len(password),8)
    except Exception as e:
        print(e)
    else:
        print("Your password is long enough.")

check_password()