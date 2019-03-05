import random

n = int(input())
z = []
for i in range(n):
    k = int(input())
    if k % 2 == 0:
        z.append(k)
for i in range(5):
    z.append(random.randint(0,100))
print(z)
    
