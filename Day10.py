numbers=[1,8,9,5,6,4,8,7,6,3,6,4,9,7,6]
def analyze(numbers):
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
average,large,small=analyze(numbers)
print("max",large)
print("min",small)
print("average",average)
    
