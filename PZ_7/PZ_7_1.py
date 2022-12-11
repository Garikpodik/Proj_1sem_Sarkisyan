import random
import string
N = random.randrange(1,11)
s = ''.join(random.choice(string.digits) for x in range(N))
print("String:",s)
L = list(s)
print("List of char-s:",L)
L_int = list(map(int,L))
print("List of int-s:",L_int)
print("Sum of digits:",sum(L_int))
    									

