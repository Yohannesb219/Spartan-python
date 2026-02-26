numbers=[]
while True:
    operation=input("Enter purpose (Add/Stop)").lower()
    if operation=="add":
        num=int(input("Enter number:"))
        numbers.append(num)
    elif operation=="stop":
        break
    else:
        print("Invalid input")
    

def analyze(numbers):
    if not numbers:
        return None,None,None
    large=numbers[0]
    small=numbers[0]
    total=0
    for num in numbers:
        if num >large:
            large=num
        if num<small:
            small=num
        total +=num
    average= total/ len(numbers)
    return large,small,average
large,small,average=analyze(numbers)
print("max",large)
print("min",small)
print("average",average)
