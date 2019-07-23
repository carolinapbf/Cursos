#Projeto 1 Jogo da Velha
#regras Jogador 1 é X e jogador 2 é O
velha=[[1,2,3],[4,5,6],[7,8,9]]
import sys
import os
ct=0
print('Jogador 1 é X e Jogador 2 é O')
def tabuleiro(jogo):
	
	print(' |',jogo[0][0],'|',jogo[0][1],'|',jogo[0][2],'|','\n','|', jogo[1][0],'|',jogo[1][1],'|',jogo[1][2],'|','\n','|',jogo[2][0],'|',jogo[2][1],'|',jogo[2][2],'|')

tabuleiro(velha)

def marcarX(jogo,jogada):
	posicao=0
	while posicao not in range(1,10):
		if jogada in range(1,10):
			for linha in range(0,3):
				for coluna in range(0,3):
					if jogada==jogo[linha][coluna]:
						jogo[linha][coluna]='X'
		return tabuleiro(jogo)
		
def marcarO(jogo,jogada):
	for linha in range(0,3):		
		for coluna in range(0,3):
			if jogada==jogo[linha][coluna]:
				jogo[linha][coluna]='O'
	return tabuleiro(jogo)

def vencerH(jogo):
	for linha in range(0,3):
		if jogo[linha][0]==jogo[linha][1]==jogo[linha][2]:
			return True

def vencerV(jogo):
	for coluna in range(0,3):
		if jogo[0][coluna]==jogo[1][coluna]==jogo[2][coluna]:
			return True
			
def vencerD(jogo):
	if jogo[0][0]==jogo[1][1]==jogo[2][2] or jogo[0][2]==jogo[1][1]==jogo[2][0] :
		return True

def vencer(velha):
	saida=0
	parada1=vencerH(velha)
	parada2=vencerV(velha)
	parada3=vencerD(velha)
	if parada1==True or parada2==True or parada3==True:
		saida=10
	return saida
def reiniciarJogo():
	parada=''
	parada = input('Quer jogar novamente? "S" ou "N" ').upper()
	if parada=='S':
		return True
	elif parada =='N':
		return False	
while True:
	JogoVelhaON=True
	
	while True:
		jogada1=int(input('Escolha a posição :'))
		marcarX(velha,jogada1)
		fimJogo=vencer(velha)
		if fimJogo==10:
			print ('Parabens Jogador 1 você venceu')
			break
		if jogada1 in range(1,10):
			ct+=1
		if ct==9:
			print('Ninguem venceu o jogo')
			break
		jogada2=int(input('Escolha a posição :'))
		marcarO(velha,jogada2)
		fimJogo=vencer(velha)
		if fimJogo==10:
			print ('Parabens Jogador 2 você venceu')
			break
		if jogada2 in range(1,10):
			ct+=1
	if reiniciarJogo()==False:
		break
	elif reiniciarJogo()==True:
		velha=[[1,2,3],[4,5,6],[7,8,9]]
		ct=0
		tabuleiro(velha)


