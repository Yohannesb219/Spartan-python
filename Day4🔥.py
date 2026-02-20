count=int(input("Enter the number of inputs:"))
numbers=[]
for n in range(count):
    num=int(input(f"Enter number {n+1}:"))
    numbers.append(num)
operation=input("Enter your operations (double/triple/squared/cubed/power) ")
if operation=="power":
    m= int(input("Enter value of the power:"))
else:
    print("continue")
for i in numbers:
   def double(i):
         return i*2
   def triple(i):
       return i*3
   def squared(i):
       return i*i
   def cubed(i):
       return i**3
   def power(i):
       return i**m
for i in numbers:
    if operation =="double":
        print("Double:", double(i))
    elif operation =="triple":
        print("Triple:", triple(i))
    elif operation =="squared":
         print("Squared:", square(i))
    elif operation =="cubed":
        print("Cubed:", cubed(i))
    elif operation =="power":
        print(m,"th","power:", power(i))
    else:
        print("Invalid operation")
name=input("Enter your name")
print(f"You deserve respect {name}")
