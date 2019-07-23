x = 25

def printer():
    x = 50
    return x

print(x) # aparece 25, pois não chamei a função
print(printer())#vai retorna 50 pois chamei a função e ele não pede nenhum parametro

f = lambda x:x**2 # x é local aqui:

x = 50

def func(x):
	
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)
x = 50

def func():
    global x
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)

print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)
