inputs = input("Enter the sequence : ")
int_list = [int(i) for i in inputs.split()]


def remove_element(list, i):
    print("list before removal of ",i,list)
    list.remove(i)
    print("list after removal ",list)
    return list

unique_list = list(int_list)
print([i for i in int_list if (i not in (remove_element(unique_list, i)))])
