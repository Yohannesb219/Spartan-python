players={
    "Cristiano":{"Age":41,"Goals":926},
    "Messi":{"Age":37,"Goals":853},
    "Neymar":{"Age":33,"Goals":350},
    "Salah":{"Age":34,"Goals":450}
}
name=input("Enter Name:")
Age=int(input("Enter age:"))
Goals=int(input("Enter Goals:"))
players[name]={"Age":Age,"Goals":Goals}
print(f"{name} has been added")
