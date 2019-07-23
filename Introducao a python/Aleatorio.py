#randint () é uma função inerente do módulo aleatório no Python3. O módulo aleatório dá acesso a várias funções úteis e uma delas é capaz de gerar números aleatórios, que é randint ().

import random #,odulo que seleciona numeros alaeatorios

def geraListaInteiro(tam): #tam para definir o tamanho
	Lista=[]
	for i in range(tam): # retorna uma lista conforme o tamnho indincado por tam variavel
		Lista.append(random.randint(0, tam))
		 #randint retorna um inteiro aleatório dentro do intervalo dado como parâmetros.
	return Lista
