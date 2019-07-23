import random
#Função Criar Cartas
class Jogador(object):
	def __init__(self):
		self.nome=input('Olá Jogador , digite seu nome: ').upper()

class Baralho(object):
	def __init__(self,face,nipe):
		self.carta=(face,nipe)	

def pegarCarta():
	cartaRetirada=random.choice(baralhoJogo)
	baralhoJogo.remove(cartaRetirada)
	return cartaRetirada

#Declarando dados iniciais
face={'As':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Da':10,'Va':10,'Re':10}
nipes=('CO','PA','OU','ES')
baralhoCompleto=[]
jogador=Jogador()
player=0
maquina=0
soma=0
somaBanca=0
jogoOn=True
bancoJogador=10
continuarJogando=True
#criando o Baralho do jogo
for i in nipes:
	for j in face:
		montaCarta=Baralho(j,i)
		baralhoCompleto.append(montaCarta.carta)
baralhoJogo=baralhoCompleto*8
#Cartas para distribuir entre jogadores
while continuarJogando:
	while jogoOn:
		print('Saldo de fichas: ',bancoJogador)
		while True:
			try:
				aposta=int(input(' Digite sua aposta '))
			except:
				print('Voce digitou uma entrada invalida')
				continue
			else:
				break
		print(aposta)
		if aposta>bancoJogador:
			print('Voce não tem saldo suficiente para esta aposta')
			print('Saldo: ',bancoJogador)
			aposta=int(input('Digite sua aposta '))

		#Distribuição carta jogador1
		while player<2:
			#JOGADOR
			carta=pegarCarta()
			print(jogador.nome,' Sua carta é - ',carta)
			soma+=face.get(carta[0])
			player+=1
		while maquina<2:
			#BANCA
			carta=pegarCarta()
			#print(jogador.nome,' A carta da banca é - ',carta)
			somaBanca+=face.get(carta[0])
			maquina+=1

		print(jogador.nome,'Voce tem um total de ',soma, ' na sua mão')
		#jogo 
		while jogoOn:
			continuar=input('Você quer mais uma carta ? (s) ou (n) ').lower()

			#JOGADOR
			if continuar=='s':
				carta=pegarCarta()
				print(jogador.nome,' Sua carta é - ',carta)
				soma+=face.get(carta[0])
				print(jogador.nome,'Voce tem um total de ',soma, ' na sua mão')

				if soma>21:
					print('Sua mão tem um total de ',soma, 'sendo assim maior que 21 ')
					print ('A banca vence com um total de ', somaBanca)
					bancoJogador-=aposta
					
					jogoOn=False
				elif soma==21:
					print('Parabens você fez 21 e ganhou o jogo')
					bancoJogador+=aposta
					jogoOn=False

			#BANCA
			if continuar=='n':
				print ('A Banca tem uma mão com ',somaBanca)
				while jogoOn:
					carta=pegarCarta()
					print('A carta da banca é - ',carta)
					somaBanca+=face.get(carta[0])
					if somaBanca>soma and somaBanca<=21:
						print('A Banca ganha com  :', somaBanca)
						bancoJogador-=aposta
						jogoOn=False
						
					elif somaBanca>21:
						print(' Banca: ',somaBanca,'\n',jogador.nome,':', soma, '\n',jogador.nome,' Parabens você ganhou')
						bancoJogador+=aposta
						jogoOn=False
	print('\n''Saldo Atual :',bancoJogador, 'reais em fichas')
	if bancoJogador==0:
		print('Desculpe suas fichas acabaram e você nao pode mais jogar')
		continuarJogando=False
	else:						
		jogarNovamente=input('Deseja continuar jogando? (s) ou (n)').lower()
		if jogarNovamente=='n':
			continuarJogando=False
			print('Obrigada por Jogar, seu saldo de fichas é:', bancoJogador)
		elif jogarNovamente=='s':
			jogoOn=True
			player=0
			maquina=0
			soma=0
			somaBanca=0