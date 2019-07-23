x=1
while x<10:
	print ('o valor de x e :', x)
	x +=1
else:
	print ('o valor de x e :', x)
x=1
y=1
while x<10 and y<20:
	print ('o valor de x*y e :', x*y)
	x+=1
	y+=2
else:
	print ('o valor de x*y e :', x*y)

x=1
lista=[]
while True:
	lista+=[x]
	x+=1
	if x>10:
		break
print (lista)

ate=50
x=0
while x<ate:
	x+=1
	if x%2==1:
		continue
	if x%2==0:
		print('é par : ',x)