
def primo(num):
	for n in range(2,num):
		if num%n==0:
			print(num," não é primo")
			break
	else:
		print(num," é primo")

for x in range(1,10):
	print(primo(x))			
