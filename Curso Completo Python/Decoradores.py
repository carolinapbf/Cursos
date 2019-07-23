def hello(nome='Carol'):
    print('ola ,' + nome)
    def tudoben():
        print('Tudo bem?')
    def comovcesta():
        print('como vc esta?')
    print(locals())

    if nome =='Carol':
        return tudoben
    else:
        return comovcesta
print(hello())
func=hello()
print(func())


def hello1():
    print('Hello')
def outra(func):
    print('outra funcao aqui dentro')
    func()

ou=outra(hello1)
print(ou)

def novoDecorador(func):
    def funcaoInterna():
        print('Codigo executado antes da função')
        func()
        print('codigo executado depois da função')
    return funcaoInterna

def precisaDecorar():
    print('esta funcao precisa de decorador')

print(novoDecorador(hello1)())
precisaDecorar=novoDecorador(precisaDecorar)


print(precisaDecorar())
@novoDecorador
def precisaDecorar():
    print('esta funcao precisa de decorador')
print(precisaDecorar())
   
