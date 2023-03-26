def get_todos():
    with open('todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todo_list_local):
    with open('todos.txt', 'w') as file:
        file.writelines(todo_list_local)
