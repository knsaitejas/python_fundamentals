import random

def random_score ():
	for i in range(10):
		grade = int(round(60 + (random.random()*40),0))
		if(grade>=90):
			print 'Score: {}; Your grade is A'.format(grade)
		elif(grade>=80):
			print 'Score: {}; Your grade is B'.format(grade)
		elif(grade>=70):
			print 'Score: {}; Your grade is C'.format(grade)
		else:
			print 'Score: {}; Your grade is D'.format(grade)

random_score()