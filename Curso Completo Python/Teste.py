s='hello'
s=s[::-1]
print (s)

lista=[0,0,0]
lista2=[]
for num in lista:
    lista2.append(0)

print (lista)
print (lista2)
lista3=[1,2,[3,4,'hello']]
lista3[2][2]='goodbye'
print (lista3)


lista4=[5,6,4,8,1,2]
print(lista4)
lista4=sorted(lista4)
print (lista4)
lista4=[5,6,4,8,1,2]
lista4.sort()
print(lista4)
l = [1,2,2,33,4,4,11,22,3,3,2]
print(l)
l=list(set(l))
print (l)
l.sort()
print(l)

d = {'simple_key':'hello'}
print (d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

