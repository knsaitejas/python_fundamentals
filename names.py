# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def output (input):
# 	for index in input:
# 		print index['first_name'] + ' ' + index['last_name']


# output(students)


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def output (input):
 	for key in input:
 		print key
 		for i in range (len(input[key])):
 			num = i+1
 			first_name = input[key][i]['first_name']
 			last_name = input[key][i]['last_name']
 			length = len(first_name)+len(last_name)
 			print "{} - {} {} - {}".format(num,first_name,last_name,length)         

output(users)
