x=input()
while type(x)!=float():
	try:
		x=float(x)
		break
	except ValueError:
		print('неправильно ввели')
		x=input()    
N=input()
while type(N)!=int():
	try:
		N=int(N)
		break
	except ValueError:
		print('неправильно ввели')
		N=input()
i = 1
while i in range(N):		    
	s=((-1)**N)*x**(2*N+1)/(2*N+1)
	print(s)
	break