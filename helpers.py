FILEPATH = 'todos.txt'

def listToDos(todos):
    for index, todo in enumerate(todos):
        index += 1
        item = todo.capitalize().strip('\n')
        print(f"{index}. {item}")

def readFile(filename=FILEPATH):
    with open(filename, 'r') as file:
        todos = file.readlines()
    return todos

def writeFile(todos, filename=FILEPATH):
    # file = open(filename, 'w')
    # file.writelines(todos)
    # file.close()

    # above code is optmized with contextr manager and written as below
    with open(filename, 'w') as file:
        file.writelines(todos)
    return
