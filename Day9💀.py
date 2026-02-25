import json

filename = "task.json"

def load():
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save(tasks):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def add(tasks):
    name = input("Enter task name: ")
    tasks.append({"title": name, "completed": False})
    save(tasks)
    print("Task added successfully!")

def show(tasks):
    if not tasks:
        print("No task available")
        return

    for i, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Pending"
        print(f"{i+1}. {task['title']} - {status}")

def main():
    tasks = load()

    while True:
        print("\n1. Add task")
        print("2. Show tasks")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add(tasks)
        elif choice == "2":
            show(tasks)
        elif choice == "3":
            break
        else:
            print("Invalid input")

main()