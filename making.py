my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def tuples (input):
	list1 = [];
	list2 = [];
	for keys in input:
		list1.append(keys)
		list2.append(input[keys])
	output = zip(list1,list2)
	print output

tuples(my_dict)