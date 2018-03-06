def type_list (start):
	rsum = 0
	string = ''
	for count in range(0,len(start),1):
		if type(start[count]) == int or type(start[count]) == float:
			rsum+=start[count]
		else:
			string+=str(start[count]) + ' '
	if rsum > 0 and len(string) > 0:
		print 'mix of numbers and strings'
	elif rsum > 0:
		print 'just numbers'
	else:
		print 'just string'
	print 'Sum: {}'.format(rsum)
	print string

type_list(['magical unicorns',19,'hello',98.98,'world'])
type_list([2,3,1,7,4,12])
type_list(['magical','unicorns'])



