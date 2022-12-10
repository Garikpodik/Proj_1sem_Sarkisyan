import random

N = random.randrange(2,11)
a = [random.randrange(1,10) for i in range(N)]
b = [random.randrange(1,10) for i in range(N)]

print("N:",N)
print("Array a:\n",a)
print("Array b:\n",b)

for i in range(0,N) :
    a[i], b[i] = b[i], a[i]

print()
print("Array a:\n",a)
print("Array b:\n",b)