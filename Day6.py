workers= { }
def employ(name,age,salary):
    workers[name]={"age":age,"salary":salary}
    print(f"{name} has been employed")
num=int(input("Enter number of employees"))
for i in range(num):
    name=input("Enter name:")
    age=int(input("Enter age:"))
    salary=int(input("Enter salary"))
    employ(name,age,salary)
operation=input("Enter purpose (check/employ):").lower()
if operation=="employ":
    employ(name,age,salary)
elif operation=="check":
    print(workers)
else :
    print("invalid")
