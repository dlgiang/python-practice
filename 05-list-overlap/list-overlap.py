import random
a = random.sample(range(1,100), random.randint(10, 30))
b = random.sample(range(1,100), random.randint(10, 30))
print(a)
print(b)
result = []
for element in a:
    if element in b and element not in result:
        result.append(element)
print(result)