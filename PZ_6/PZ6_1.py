

import random
import statistics as stat
N = random.randint(10,20)
L = random.randrange(1,N)
K = random.randint(1,L)
#N = 10
print("N = ", N)
print("L = ", L)
print("K = ", K)
A = [random.randrange(1,20) for i in range(N)]
print("Initial:")
print(A)
s = 0
c = 0
for i in range(0,N):
  if i not in range(K,L+1):
    c += 1
    s += A[i]
print(i,":",A[i])
print("Sum = ",s)
print("Count = ",c)
print("Average = ", s/c)
A1 = [j for i, j in enumerate(A) if i not in range(K,L+1)]
print()
print(A1)
print("Sum = ",sum(A1))
print("Count = ",len(A1))
print("Average = ", stat.mean(A1))
    									

