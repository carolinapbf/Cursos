
minha_lista=["abacaxi","melancia","abacate"] # a lista é criada usando colchete e separados por virgula
minha_lista2=[1,2,3,4,5]
minha_lista3=["abacaxi",2,4,True]
minha_lista4=[]

print(minha_lista[1]) #imprimi o valor da minha lista no local idicado

#navegar pelos elementos usando um laço
for item in minha_lista:
	print(item)

tamanho=len(minha_lista)
print(tamanho)

#adicionando elementos usa-se append

minha_lista.append("limão")
print(minha_lista)

if 7 in minha_lista2:
	print("7 esta na lista")
if 3 in minha_lista2:
	print("3 esta na lista")

#remoção de redundancia

del minha_lista[3:] #elimina item 2 ate o final
print(minha_lista)

minha_lista4.append("limão")
print(minha_lista4)


