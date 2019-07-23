#media, mediana, moda
#Pythin tem funções matematicas prontas
#Jeito facil
#from statistics import* #chamando todas as funções que o python oferece

#mean(lista) # media
def media(lista):
	media=sum(lista)/float(len(lista))
	return media

#median(lista) #mediana
def mediana(lista):
	lista_ordenada=sorted(lista)
	t=len(lista_ordenada) #tamanho da lista
	if t%2==0:  #verificando se p tamanho da lista é par
		mediana=(lista_ordenada[int(t/2)]+lista_ordenada[int((t/2)-1)])/2 #soma os dois valores do meio da lista
	elif t%2==1:
		mediana=lista_ordenada[int(t/2)] #pega o numero do meio
	return mediana

#mode(lista) #moda

def moda(lista): #numero que mais repete na lista
	lista_dic={} #dicionario um obejeto que recebe uma chave com valor
	for l in lista: #percorrer a lista
		#verificar se o elemento está no dicionario
		#este if mostra quantas vezes cada valor se repete
		if l not in lista_dic:
			lista_dic[l]=1 #inserir elemento
		else: 
			lista_dic[l] +=1 #inserir mais um elemento
	#aqui eu ja pego o maior valor q repetiu e descubro qual numero q quepete usando o for
	maior_repeticao=max(lista_dic.values()) #função max maior elemento .... Values metodo retorna todos os valores da minha lista
	for i in lista_dic:
		if lista_dic[i]==maior_repeticao:
				moda=i

	return moda 
# o que acontece com moda, crio um dicionario , 
#depois eu verifico quantas vezes cada valor aparece depois verifica dos que mais aparece o valor dele e imprimi



