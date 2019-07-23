#language:pt
@unitarios
Funcionalidade: Alugar filme
  como um usuario
  Eu quero cadastrar alugueis de filmes para controlar 
  pre�os e datas de entrega

  Cenario: Deve alugar um filme com sucesso
    Dado um filme
      | estoque |     2 |
      | preco   |     3 |
      | tipo    | comum |
    Quando alugar
    Entao o Preco do aluguel seja R$ 3
    E a data de entrega sera em 1 dia
    E o estoque do filme sera 1 unidade

  Cenario: Nao deve alugar filme sem estoque
    Dado um filme com estoque de 0 unidades
    Quando alugar
    Entao nao sera possivel por falta de estoque
    E o estoque do filme sera 0 unidade

  #Scneario outline
  Esquema do Cenario: Deve dar consdicoes conforme tipo de aluguel
    Dado um filme com estoque de 2 unidades
    E que o preco do aluguel seja R$ <preco>
    E que o tipo do aluguel seja <tipo>
    Quando alugar
    Entao o preco do alguel sera R$ <valor>
    E a data de entrega sera em <qtdDias> dias
    E a pontuacao recebida sera em <pontuacao> pontos

    Exemplos: #exaples
      | preco | tipo      | valor | qtdDias | pontuacao |
      |     4 | extendido |     8 |       3 |         2 |
      |     4 | comum     |     4 |       1 |         1 |
      |     5 | semanal   |    15 |       7 |         3 |
