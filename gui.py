import PySimpleGUI as sg
import functions_todo

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip='Enter a to-do', key='todo')
add_button = sg.Button('Add')
list_box = sg.Listbox(values=functions_todo.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")

window = sg.Window('My To-do App',
                   layout=[[label] ,[input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica',15))
while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions_todo.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions_todo.write_todos(todos)
        case sg.WIN_CLOSED:
            break
        case "Edit":
            todo = values['todos']
window.close()
