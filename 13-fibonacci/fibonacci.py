number  = int(input("Input a number: "))

def fibo(count):

    if count == 0:
        return []
    result = [1]
    a, b = 0, 1
    while count > 1:
        result.append(a + b)
        tmp = b
        b = a + b
        a = tmp
        count = count - 1
    return result

result = fibo(number)
print(result)
    
