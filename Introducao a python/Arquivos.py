#função OPEN
#variavel=open(nome,modo)
#se eu definir o modo o program ainterprte que o arquivo e somente leitura
#modos 
#r -somente leitura; 
#w -escrita(caso o arquivo ja exisitia , ele sera apafado e um novoa arquivo vazio sera criado)
#a -leitura e escrita (adiciona o novo conteudo ao fim do arquivo)
#r+ - leitura e escrita
#w+ - escrita (o modo w+, assim como o we, tambem apafa o conteudo anterior do arquivo)
#a+ - Leitura e escrita(abre o arquivo para atualização)

# ****Lendo Arquivos****
#read() - le arquivos inteiro
#readline() le uma linha
#readlines() le arquivo e o armazena em uma lista

arquivo=open("arquivo.txt")

linhas=arquivo.readlines()
print(linhas)

for linha in linhas:
	print(linha)
texto=arquivo.read()
print (texto)

#criar arquivo

w =open("arquivo2.txt","w")#abre e cria outro arquivo

w.write("estou aprendendo python \n") #Escreve no arquivo e o \ n quebra para proxima linha

w.close()#fecha o arquivo


