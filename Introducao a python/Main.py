import aleatorio as a #Criei um apelido com a função as
import media as m
lista = a.geraListaInteiro(50) #preciso indicar o local exemplo. variavel=local.função(tamanho)
print(lista)
media = m.media(lista)
mediana = m.mediana(lista)
moda = m.moda(lista)
print("a média da minha lista é "+str(media))
print("a média da minha lista é "+str(mediana))
print("a média da minha lista é "+str(moda))