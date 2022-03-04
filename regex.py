import re
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
lines = int(input())
list_of_lines = []
for i in range(lines):
    line = input()
    # found = re.findall("\A#[a-fA-F0-9{3}|a-fA-F0-9{6}]*.$", line)
    found = re.findall("(?<!^)#[a-fA-F0-9]*", line,)
    if (found):
        for i in found:
            print(i)