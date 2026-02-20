count=int(input("Enter the number of inputs"))
numbers= []
for i in range(count):
    num=int(input(f"Enter number {i+1}:"))
    numbers.append(num)
operation=input("Choose operation(double/triple/square):").lower()
for i in numbers:
    if operation == "Double":
        print("Double", i*2)
    elif operation == "Triple":
        print("Triple",i*3)
    elif operation== "Square":
        print(" Squared",i*i)
    else: 
        print("no operation")
print("This is a new thing that i am trying Chatgpt")
    



