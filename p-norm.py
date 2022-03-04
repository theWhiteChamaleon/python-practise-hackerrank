

def p_norm (v, n=2):
    return pow(sum([i**n for i in v]), (1/n))

list_of_nums = [3,4,7]
print(p_norm(list_of_nums,3))