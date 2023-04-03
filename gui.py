import PySimpleGUI as sg
import functions_todo
import time

sg.theme("Black")
clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip='Enter a to-do', key='todo')
add_button = sg.Button('Add', size=10)
list_box = sg.Listbox(values=functions_todo.get_todos(), key='todos',
                      enable_events=True, size=(33, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
window = sg.Window('My To-do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 18))
while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%Y-%m-%d %H:%M:%S"))
    match event:
        case "Add":
            todos = functions_todo.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions_todo.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions_todo.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions_todo.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select a todo first.", font=('Helvetica', 15))

        case "todos":
            window['todo'].update(value=values['todos'][0])
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions_todo.get_todos()
                todos.remove(todo_to_complete)
                functions_todo.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value=" ")
            except IndexError:
                sg.popup("Please select a todo first.", font=('Helvetica', 15))
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
window.close()

