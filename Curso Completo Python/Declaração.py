lista=[1,2,3,4,5,6,7]
for x in lista:
	print(x)
for x in lista:
	print('Numero vezes 1;' ,x)
	print('Numero vezes 2;', x*2)
	print('Numero vezes 3;', x*3)
for x in lista:
	if x % 2 ==0:
		print(x, ' é par')
	else:
		print(x,'é imppar')

sum_=0
for num in lista:
	sum_ +=num
print (sum_)

string='estou fera na programação '
for letra in string:
	print(letra)
tupla=(1,2,3,4,5,6)

for t in tupla:
	print(t)

l=[(1,2),(3,4),(5,6)]
(t1,t2)=l[0]
print (l)
for	 t1 in l:
	print (t1)
d={'k1':1,'k2':2,'k3':3}
for (key,valor) in d.items():
	print (valor)
	print (key ,':' ,valor)

	