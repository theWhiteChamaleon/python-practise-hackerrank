sentence = input("Please enter the sentence \n")
words = sentence.lower().split()
print("No of words in the sentence are : ",len(words))
words.sort()
for word in words:
    print(word)