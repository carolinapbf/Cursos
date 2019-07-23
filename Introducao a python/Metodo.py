a= "Ana"
b= "Carolina"

Nome= a+" " +b
print(Nome.lower())#AS letras da string ficam todoas em minusculo
print(Nome.upper())#AS letras da string ficam todoas em maiusculo
print(Nome)

#\n da uma quebra de linha ja para retirar o caracter especial usa-se o metodo .strip()
# usando o metodo string=string.metodo()

#converção de string, vai fazer uma quebra na string
minha_string="o rato roeu a roupa do rei de Roma"

minha_lista= minha_string.split("r")
print(minha_lista)

#busca de substring

minha_string="o rato roeu a roupa do rei de Roma"

busca= minha_string.find("rei")
print(busca)
print(minha_string[busca:])# imprime a parte da busca no casao ate o fim da frase:

#substitui partes de uma string .replace
minha_string="o rato roeu a roupa do rei de Roma"

minha_string=minha_string.replace("o rei","a rainha")
print(minha_string)









