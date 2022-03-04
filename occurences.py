def count_substring(string, sub_string):
    sub_len = len(sub_string)
    first_sub_string_letter = sub_string[0]
    count = 0
    for letter_no in range(len(string)):
        letter = string[letter_no]
        print(type(letter_no))
        if (letter == first_sub_string_letter):
            sliced_end = letter_no+sub_len-1
            sliced = string[letter_no, sliced_end]
            if (sub_string == sliced):
                count += 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
