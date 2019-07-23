dic={'key1':'value1','key2':'value2','key3':'value9'}
print (dic["key2"])
dic2 = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
print (dic2['key3'])
print (dic2['key3'][0])
print (dic2)
d={}
d['animal']='dog'
d['answer']=42
print (d) 
x={'key1':{'nestkey':{'subnestkey':'value'}}}
print(x)
print(x['key1'])
print(x['key1']['nestkey'])
print(x['key1']['nestkey']['subnestkey'])
print (d.keys())
print (d.values())
print (d.items())