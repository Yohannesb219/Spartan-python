workers={
    "Miki": {"Age":19, "Salary":1500}
    }
def employ(name,age,salary):
    workers[name]={"Age":age,"Salary":salary}
    print(f"{name}has been employed!!!!!!!!!!!!!!")
def fire(name):
    del workers[name]
    print(f"{name} has been fired!!!!!!!!!!!!!!!!!")
while True:
    action=input("type 'add' to employ 'del' to fire 'stop' to stop ")
    if action=="add":
        name=input("Enter name:")
        age=int(input("Enter age:"))
        if age<= 18:
            print("go home kid!!!!!!!!!!!")
            continue
        salary=int(input("Enter salary:"))
        if salary>50000:
            print("Too much!!!!!!!!!!!!!")
            continue
        employ(name,age,salary)
    elif action=="del":
        name=input("Enter name ")
        if name in workers:
            fire(name)
        else:
            print("name not found")
    elif action=="stop":
        break
    else:
        print("invalid input")
print("\nList of currents employees:")
for name , info in workers.items():
    print(f"{name}:Age={info['Age']}, Salary={info['Salary']}")
