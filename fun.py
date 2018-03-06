def odd_even ():
	for i in range (2001):
		if i%2 == 0:
			print '{} is an even number.'.format(i)
		else:
			print '{} is an odd number'.format(i)

odd_even()

def multiply (a):
	for i in range (len(a)):
		a[i] = a[i]*5
	print a
	return a

multiply([2,4,10,16])
