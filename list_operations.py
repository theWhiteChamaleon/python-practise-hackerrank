N = int(input())
list = []
for i in range(N):
    command_and_input = input().split()
    command = command_and_input[0]
    if ("insert"==command.lower()):
        No_to_insert = int(command_and_input[2])
        index = int(command_and_input[1])
        list.insert(index,No_to_insert)
        print(list)
    elif ("print"==command.lower()):
        print(list)
    elif ("remove"==command.lower()):
        No_to_remove = int(command_and_input[1])
        list.remove(No_to_remove)
    elif ("append"==command.lower()):
        No_to_append = int(command_and_input[1])
        list.remove(No_to_append)
    elif ("sort"==command.lower()):
        list.sort()
    elif ("pop"==command.lower()):
        list.pop()
    elif ("reverse"==command.lower()):
        reversed(list)