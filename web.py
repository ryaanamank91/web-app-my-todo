import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state['new_todo'] + '\n'
    todos.append(todo_local)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo App")
st.write("This App is to increase your productivity")

# Implementing checkboxes
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    # Implement the feature COMPLETE
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

# Implement feature for Add the item
st.text_input(label="Enter a todo: ", placeholder="Add new todo.....", on_change=add_todo, key='new_todo')


