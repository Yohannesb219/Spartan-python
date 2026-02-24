import json
workers={
    "Mike":{"Age":19,"Salary":1563},
    "Miranda":{"Age":21,"Salary":2456},
    "Thomas":{"Age":41,"Salary":15000}
}
with open("employees.json","w") as f:
    json.dump(workers,f)
print("Workers saved to file.")
with open("employees.json","r") as f:
    employees=json.load(f)
print("\nWorkers displayed from file")
print(employees)
print("\nDisplaying employee's data")
print(f"Miranda's Salary: {employees['Miranda']['Salary']}")
print(f"Thomas's Age:{employees['Thomas']['Age']}")
employees["Alex"]={"Age":16,"Salary":45000}
print("\nAdded worker Alex")
print(employees['Alex'])
del employees["Thomas"]
print("\nDeleted Tom :Current workers:")
print(employees)
with open("employees.json","w") as j:
    json.dump(employees,j)
print("\nUpdated workers file:")
