x=[]
y=[]
for i in range(0,30):
	x+=[i]
for i in range(0,30):
	y.append(i)
print(x)
print(y)
x2=[i for i in range(0,30,3)]
print (x2)

x3=[i*2+10 for i in range(0,10)]
print (x3)

p=[]
for i in range(0,20):
	if i %2==0:
		p.append(i)
print(p)

carta =[]
carta=[letra for letra in 'mundo']
print (carta)

celsius=[0,10,50.3,70.8,90,80,100]

fa=[(((9)/5)*temp + 32) for temp in celsius]

print (fa)