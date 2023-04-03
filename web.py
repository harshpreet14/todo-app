import streamlit as st
import functions_todo

todos = functions_todo.get_todos()

def add_todo():
    todo = st.session_state['new_todo'].strip() + '\n'
    todos.append(todo)
    functions_todo.write_todos(todos)


st.set_page_config(page_title="ToDo App", page_icon="📝")
st.title("Your day's plan")
st.subheader("Let's make progress - here's what's next")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions_todo.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo", placeholder="Add a new todo...", on_change=add_todo, key='new_todo')
