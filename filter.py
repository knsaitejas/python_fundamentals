def greater_than (num):
	if num >= 100:
		print "that's a big number!"
	else:
		print "that's a small number"

greater_than(1)

def str_greater_than (str): 
	if len(str) >= 50: 
		print "Long sentence"
	else:
		print "Short sentence"

str_greater_than("Rubber baby buggy bumpers")
str_greater_than("Tell me and I forget. Teach me and I remember. Involve me and I learn.")

def list_greater_than (list):
	if len(list) >= 10:
		print "big list"
	else:
		print "small list"

list_greater_than([1,7,4,21])
list_greater_than([3,5,7,34,3,2,113,65,8,89])
list_greater_than([4,34,22,68,9,13,3,5,7,9,2,12,45,923])

