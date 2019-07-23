#Escreva uma função que calcula o volume de uma esfera dado seu raio.
def volume(raio):
	vol=(4*3.14*(raio**3))/3
	return vol
for raio in range(1,5):
	print('o volume da esfera de raio',raio , 'é ',volume(raio))

#Escreva uma função que verifica se um número está em um determinado intervalo (inclusive o máximo e mínimo)

def checa(num,min,max):
	if min<num<max:
		return print('Está dentro do limite')
	else:
		return print('esta fora')
checa(1,5,10)
checa(9,8,10)

def checa2(num,min,max):
	if num in range(min,max+1):
		return True
	else:
		return False

print(checa2(1,5,10))
print(checa2(4,2,10))
print(checa2(3,1,10))

#** Escreva uma função Python que aceita uma string e calcule o número de maiúsculas e minúsculas. **
string='O'
print(string.isupper())

def up_low(s):
	up=0
	low=0
	for i in s:
		if i.isupper():
			up+=1
		elif i.islower():
			low+=1
		else:
			continue
	print('Número de maiúsculas é :', up)
	print('Número de minusculas é :', low)

up_low('Meu Mundo Azul?????')

#** Escreva uma função Python que recebe uma lista e retorna uma nova lista com elementos exclusivos da primeira lista. **
def lu(l):
	return list(set(l))

print(lu([1,1,11,5,5,83,4,4,1,5,6,6]))

#** Escreva uma função Python para multiplicar todos os números em uma lista. **

def mult(l):
	mul=1
	for i in l:
		mul*=i
	return mul
print (mult([1,2,3]))

#** Escreva uma função Python que verifica se uma string passada é palindrome ou não. **
def palin(s):
	s=s.replace(' ','')
	if s==s[::-1]:
		return True
	else:
		return False
print(palin('helen'))

print(palin('Carolina'))
print(palin(' ana'))
print('---------------------------------------------------------------')
import string 
def pan(stri,alfabeto = string.ascii_lowercase):
	num=len(alfabeto)
	count=0
	for i in alfabeto:
		if i in stri:
			count+=1
	return count==num

print(pan('abcdefghijklmnopqrstuvxwyz'))
print(pan('aaaaaaaaaaaaaaaaaaaaaaaaaa'))
print(pan("The quick brown fox jumps over the lazy dog"))