Tejas = {
	'name': 'Tejas',
	'age': 21,
	'country of birth': 'India',
	'favorite language': 'Python'	
}

# def personal_info (person):
# 	print 'My name is {}'.format(person['name'])
# 	print 'My age is {}'.format(person['age'])
# 	print 'My country of birth is {}'.format(person['cob'])
# 	print 'My favorite language is {}'.format(person['favorite_language'])

# personal_info(Tejas)

def personal_info (person):
	for key in person:
		print "My {} is {}".format(key,person[key])

personal_info(Tejas)