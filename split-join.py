from os import sep
import re
# i = input()
# # print(i.split(" "))
# if (re.fullmatch("(\+?|\-?)[0-9]*\.[0-9]+","-1.0054")):
#     print("True")
# else :
#     print("False")

after = re.split("[',.]","Let's try, Mike")
print(*after,sep="")
