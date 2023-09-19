# from functions import get_todos,write_todos
import time
import functions

now = time.strftime("%b %d,%Y %H:%M:%S")
print(now)
while True:
    user_action = input("add or show or edit or complete or exit")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for items in todos]

        for index,item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}.{item}" #fstring
            print(row)
    elif  user_action.startswith("edit"):
        try:
            number = int(user_action[5:])-1

            todos = functions.get_todos()

            new_todo = input("enter the new todo")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("your command is not valid")
            continue


    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            index = number-1

            todos = functions.get_todos()
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)
            message = f"Todo {todo_to_remove} is removed from the list"
            print(message)
        except IndexError:
            print("no item with that no.")
            continue

    elif  user_action.startswith("exit"):
        break
    else:
        print("unknown command")




