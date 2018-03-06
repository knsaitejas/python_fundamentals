# words = "It's thanksgiving day. It's my birthday,too!"

# print words.find('day')
# print words.replace('day','month',2)

# x = [2,54,-2,7,12,98]

# print max(x)
# print min(x)

# x = ["hello",2,54,-2,7,12,98,"world"]
# newArr = []
# last = len(x)-1
# newArr.append(x[0])
# newArr.append(x[last])
# print newArr

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
print len(x)

temp = x[0:5]
temp_two = x[5:len(x)-1]
print temp
print temp_two

del x[0:4]
print x

x[0] = temp

print x