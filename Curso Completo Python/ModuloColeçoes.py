from collections import Counter
l=[2,3,5,4,1,3,2,1,2,3,5,1,2,4]
print(Counter(l))
print(type(Counter(l)))

print(Counter('aabsbsbsbhshhbbsbs'))
s = 'How many times does each word show up in this sentence word times each each word'
palavra=s.split()
print(Counter(palavra))
c=Counter(palavra)
print(c.most_common(2))
print(c.values())

from collections import defaultdict
d={}
d['one']=1
d2=defaultdict(object)
d2['one']=1
print(d2['two'])
d3=defaultdict(lambda : 'Carol')
print(d3['one'])

t=(12,13,14)
print(t[0])
from collections import namedtuple #
dog=namedtuple('dog', 'age breed name ')