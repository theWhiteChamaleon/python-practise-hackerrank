if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    my_tuple = hash(tuple(integer_list))
    print(my_tuple)
    