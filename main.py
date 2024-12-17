import json
import os

# Файл для збереження даних
DATA_FILE = "tasks.json"

# Завантаження завдань
def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Збереження завдань
def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Додати завдання
def add_task(tasks):
    task_name = input("Введіть назву завдання: ")
    tasks.append({"name": task_name, "completed": False})
    print(f"Завдання '{task_name}' додано.")

# Показати завдання
def list_tasks(tasks):
    if not tasks:
        print("Список завдань порожній.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{i}. {task['name']} [{status}]")

# Видалити завдання
def delete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Введіть номер завдання для видалення: ")) - 1
        removed_task = tasks.pop(index)
        print(f"Завдання '{removed_task['name']}' видалено.")
    except (IndexError, ValueError):
        print("Некоректний номер завдання.")

# Позначити завдання як виконане
def complete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Введіть номер завдання для позначення виконаним: ")) - 1
        tasks[index]["completed"] = True
        print(f"Завдання '{tasks[index]['name']}' позначено виконаним.")
    except (IndexError, ValueError):
        print("Некоректний номер завдання.")

# Головне меню
def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List ---")
        print("1. Переглянути завдання")
        print("2. Додати завдання")
        print("3. Видалити завдання")
        print("4. Позначити завдання виконаним")
        print("5. Вийти")
        choice = input("Виберіть дію: ")
        
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("До побачення!")
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
