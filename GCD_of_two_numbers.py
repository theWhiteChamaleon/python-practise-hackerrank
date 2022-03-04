import math
import time
inputs = input(
    "Enter the length and breadth of the rectangle separated by space : ")

# No need to unpact args here this is called as list
num1, num2 = (inputs.split())
num1 = int(num1)
num2 = int(num2)


start = float(time.time())
# Using Math GCD method
print("Math GCD : ", math.gcd(num1, num2))
end = float(time.time())
print(end - start, " seconds for math")

start = float(time.time())
# Using loops and finding factors
# Find the greater number as greater number will have greater sq root
if (num2 > num1):
    no = num2
else:
    no = num1
# Sq root of the bigger no
x = int(math.sqrt(no))

# Find a factor that divides both num2 and num1
while x >= 1:
    if (num2 % x == 0 and num1 % x == 0):
        print("GCD is : ", x)
        break
    else:
        x -= 1
end = float(time.time())
print(end - start, " seconds for my")
