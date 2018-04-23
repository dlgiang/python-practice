word = input("Input a word: ")
backward = word[::-1]
print(backward)
if word == backward:
    print(word + " is palindrome")
else:
    print(word + " is NOT palindrome")