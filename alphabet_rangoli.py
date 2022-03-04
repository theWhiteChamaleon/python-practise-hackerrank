def print_rangoli(size):
    # start_char = chr(ord('a')+size)
    all_chars = list(reversed([chr(ord('a')+i) for i in range(0,size)]))
    for i in range(1,size+1):
        chars = "-".join(all_chars[:i])+("-"if(i>1)else"")+"-".join(reversed(all_chars[:i-1]))
        print(chars.center(((size-1)*4)+1,"-"))
    for i in range(size-1,0,-1):
        chars = "-".join(all_chars[:i])+"-"+"-".join(reversed(all_chars[:i-1]))
        print(chars.center(((size-1)*4)+1,"-"))
        
    # your code goes here

if __name__ == '__main__':
    # n = int(input())
    print_rangoli(1)