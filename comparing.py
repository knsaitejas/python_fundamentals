def compareLists (l1, l2):
	rsum = 0;
	for count in range(0,len(l1),1):
		if l1[count] != l2[count]:
			print 'lists are not equal at index {}'.format(count)
			break
		else:
			rsum+=1
	if rsum>=len(l1):
		print 'lists are equal'
	

compareLists(['celery','carrots','bread','milk'],['celery','carrots','bread','cream'])