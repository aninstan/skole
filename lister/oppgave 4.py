import random

a = []
b = []
i = 0

while i < 25:
    c = random.randint(1, 100)
    a.append(c)
    i += 1

while i < 75:
    c = random.randint(1, 100)
    b.append(c)
    i += 1

def get_median(x):
    x.sort()
    if len(x) % 2 == 0:
        median = (x[len(x) // 2] + x[len(x) // 2 - 1]) / 2
    else:
        median = x[len(x) // 2]
    return median

print(get_median(a))
print(a)   

print(get_median(b))
print(b)