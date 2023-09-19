FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """ read a text file and return list of todo items."""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos( todos_arg, filepath=FILEPATH):
    """ writes to the text file using todos list."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
