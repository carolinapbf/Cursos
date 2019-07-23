
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print(word)
lista=[]
for i in range(0,11,2):
	lista.append(i)
print(lista)
print('------------------------------------------------')

lista3=[]
for i in range(0,51):
	if i%3==0:
		lista3.append(i)
	else:
		continue
print (lista3)
print('------------------------------------------------')

st2 = 'Print every word in this sentence that has an even number of letters'
for i in st2.split():
	tamanho=len(i)
	if tamanho%2==0:
		print(i,tamanho)
print('------------------------------------------------')

l4=[]
for i in range(1,100):
	if i%3==0 and i%5==0 :
		x='FizzBuzz'
		l4.append(x)
	elif i%3==0:
		x='Fizz'
		l4.append(x)
	elif i%5==0:
		x='Buzz'
		l4.append(x)
	else:
		l4.append(i)
print(l4)
print('------------------------------------------------')

st3 = 'Create a list of the first letters of every word in this string'	
Ls=[]

for word in st3.split():
        Ls.append(word[0])
print(st3)
print (Ls)