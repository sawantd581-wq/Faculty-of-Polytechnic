#problem 1
def greet():
    name=input("Enter your name:")
    age=int(input("Enter your age:"))
    print("Hi",name+"!Next year you will be", age+1)
greet()
#problem 2
num=10
unum=int(input("gives a num between 1 to 10: "))
if num<unum:
    print("high")
elif num>unum:
    print("low")
else:
    print("correct")
