import functions_todo
import time

date_time_str = time.strftime("%Y-%m-%d %H:%M:%S")
print("It is", date_time_str)

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todo_list = functions_todo.get_todos()

        todo_list.append(todo.title() + "\n")

        functions_todo.write_todos(todo_list)

    elif user_action.startswith('show'):
        todo_list = functions_todo.get_todos()

        new_todo_list = [item.strip('\n') for item in todo_list]

        for index, item in enumerate(new_todo_list):
            list_item = f"{index + 1}.{item}"
            print(list_item)

    elif user_action.startswith('exit'):
        break

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            todo_list = functions_todo.get_todos()

            print("The previous to-do was " + todo_list[number-1])
            change = input("Enter the change: ").title() + "\n"
            todo_list[number-1] = change

            functions_todo.write_todos(todo_list)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todo_list = functions_todo.get_todos()

            todo_list.remove(todo_list[number - 1])

            functions_todo.write_todos(todo_list)
        except IndexError:
            print("There is no to-do with that index number")
    else:
        print("You entered an invalid command")

print("Bye")

