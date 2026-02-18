numbers=[]
for i in range(6):
   num = int(input(f"Enter number {i+1}: "))
   numbers.append(num)
print("\nCalculation for each number:")
for i in numbers:
    print(f"\nCalculation for : {i}")
    print("double:", i*2)
    print("Triple:",i*3)
    print("Squared:",i*i)
    print("Cubed",i**3)
    
total=0
for i in numbers:
    total +=i
average= total / len(numbers)
print("total:", total)
print("average:", average)
name=input("Enter your name")
print("day2 complete !!" , name)
    
    

