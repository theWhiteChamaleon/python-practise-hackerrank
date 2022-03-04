import math

inputs = input("Please enter the text separated by space")
list_of_inputs = inputs.split()
list_of_integers = []
for input in list_of_inputs:
    try:
        list_of_integers.append(int(input))
    except:
        #DO nothing
        print("input not an integer",input)
print(sum(list_of_integers))


    