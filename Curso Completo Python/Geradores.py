import random
def gencube(n): # não guarda na memoria, 
    for num in range(n):
        yield num**3
for x in gencube(10):
    print(x)

def gencube2(n):
    lst=[]
    for num in range(n):
        lst+=[num**3]
    return lst
print (gencube2(10))
print(gencube(10))

def genfib(n):
    a=1
    b=1
    for i in range(n):
        yield a    
        a,b=b,a+b
for fib in genfib(10):
    print (fib)
print(list(genfib(10)))
#next() acesse o proximo valor de onde meu gerador parou
g=genfib(5)
print (g)
print(next(g))
print(next(g))
print(next(g))

s='hello'
for char in s:
    print(char)
s_inter=iter(s)

print(next(s_inter))
print(next(s_inter))
print(next(s_inter))
print('\n')

def genqua(n): # não guarda na memoria, 
    for num in range(n):
        yield num**2
for x in genqua(10):
    print(x)
print('\n')
def randomCarol(menor,maior,n): # não guarda na memoria, 
    for i in range(n):
        yield random.randint(menor,maior)

for num in randomCarol(1,10,12):
    print(num)

srt='hello'
str_iter=iter(srt)

