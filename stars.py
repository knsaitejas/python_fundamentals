# def draw_stars (arr):
# 	for i in range (len(arr)):
# 		print "*"*arr[i]

# draw_stars([4, 6, 1, 3, 5, 7, 25])

def draw_stars (arr):
	for i in range (len(arr)):
		if (type(arr[i]) == int):
			print "*"*arr[i]
		else:
			print (arr[i][0]*len(arr[i])).lower()

draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])

