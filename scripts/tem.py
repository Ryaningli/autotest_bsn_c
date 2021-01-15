import random

a = [1,2,3,4,5,6,7,8,9]

b = random.sample(a, random.randint(1, len(a)))

print(b)