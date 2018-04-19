number = int(input("Please input a number: "))
candidateList = range(number, 1, -1)
result = []
for element in candidateList:
    if number % element == 0:
        result.append(element)
print(result)