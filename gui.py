import functions
import PySimpleGUI as sg
import time

sg.theme('Black')
clock = sg.Text('',key='clock')
label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="enter todo",key = "todo")
add_button = sg.Button("add")
list_box = sg.Listbox(values = functions.get_todos(),key='todos',enable_events=True,size=[45,10])
edit_button = sg.Button("edit")
complete_button = sg.Button('complete')
exit_button = sg.Button('exit')

window = sg.Window('My To-Do App',
                   layout=[[clock],[label], [input_box,add_button], [list_box,edit_button,complete_button],
                           [exit_button]],
                   font=('Helvetica',20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d,%Y %H:%M:%S"))
    # print(1,event)
    # print(2,values)
    # print(3,values['todos'])
    match event:
        case "add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("select an item",font=('Helvetica',20))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'complete':
            try:
                todo_to_complete  = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("select an item",font=('Helvetica',20))

        case 'exit':
            break

        case sg.WINDOW_CLOSED:
            break

window.close()

