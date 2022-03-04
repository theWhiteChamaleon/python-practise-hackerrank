#numbers = input("Enter numbers").split()
#list = [int(num) for num in numbers]


def minmax(list):
    min, max = list[0], list[1]
    for num in list:
        if num > max:
            max = num
        if num < min:
            min = num
    return min,max

print([i for i in range(8,-10,-2)])
#print(minmax(list))
