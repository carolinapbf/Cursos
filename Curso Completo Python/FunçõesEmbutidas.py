from functools import reduce

def fahrebheut(T):
    return (9/5)*T+32

temp=[9,22,40,90,120]
for t in temp:
    print(fahrebheut(t))
print(list(map(fahrebheut,temp)))

print(list(map(lambda t:(9/5)*t+32 ,temp)))

lst=[47,11,42,13]
print(reduce(lambda x,y: x+y,lst))

maxFind=lambda a,b: a if (a>b) else b
print(reduce(maxFind,lst))

lista=[1,4,5,12,19,21,22,33,44]
o=list(filter(lambda x:x%2==0,lista))
print(o)

x=[1,2,3,4,5,6]
y=[4,5,6,7,8,9]
print(list(zip(x,y)))
for i in zip(x,y):
    print(max(i))
c=0
lis=['a','b','c','d']
for l in lis:
    print (c,':',l)
    c+=1  
for l in enumerate(lis):
    print(l)
for number,item  in enumerate(lis):
    print(number,':',item) 
lt=[True,True,False,True]
print(all(lt))
print(any(lt))

frase='How long are the words in this phrase'
print(list(map(len,frase.split())))

lista=[3,4,3,2,1]
print(reduce(lambda x,y: x*10 + y,lista))
def palavra(frase,letra):
    return filter(lambda palavra: palavra[0]==letra,frase)

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
g=list(palavra(l,'h'))
print(g)

x=['A','B']
y=['a','b']
con=list(zip(x,y))
print(con[0][0],'-',con[0][1])
print(con[0][0],'-',con[0][1])

def concatenate(L1, L2, sim):
    
    return [p1+sim+p2 for (p1,p2) in zip(L1,L2)]

con=concatenate(x,y,'-')
print (con)




def dicionario(lista):
    dic={}
    for chave in enumerate(lista):
        for item in enumerate(lista):
            dic={chave:item}
    return dic

liss=['a','b','c']
dic=dicionario(liss)
print (dic.values())
print(dic.items())
print (dic.keys())
def d_list(L):
    
    return {key:value for value,key in enumerate(L)}
liss=['a','b','c']

print(d_list(liss))

lista1=[0,2,2,1,5,5,6,10]
soma=0
for count,item in enumerate(lista1):

    if count == item:
        soma+=1
print(soma)
    