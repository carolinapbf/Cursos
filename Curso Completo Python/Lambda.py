def square(num):
	result=num*num
	return result

print (square(4))

def square2(num):
	return num*num

print (square2(4))

x=lambda num: num**2
print(x(2))

even = lambda x: x%2==0
print (even(3))

rev = lambda s: s[::-1]
print(rev('carolina'))

print (x(4))