word_list = ['hello','world','my','name','is','Anna']

def findChar (li, a):
	newList = []
	for count in range(0, len(li),1): 
		for num in range (0, len(li[count]),1):
			if (li[count][num] == a):
				newList.append(li[count])
				break
	print newList

findChar(['hello','world','my','name','is','Anna'],'n')
		

