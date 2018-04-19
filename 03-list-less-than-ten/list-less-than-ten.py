a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
inputNum = int(input("Input a number: "))
def findLessThan(selectNum):
    result = []
    for number in a:
        if number < selectNum:
            result.append(number)
    return result

result = findLessThan(inputNum)
print(result)