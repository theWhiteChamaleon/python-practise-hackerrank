# x = 1
# y = 1
# z = 2
# n = 2

x, y, z, n = (int(input("Enter number")) for i in range(4))

i = 0
j = 0
k = 0
mainList = []
for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            mainList.append([i, j, k])
print([sub_list for sub_list in mainList if sum(sub_list) != n])
