from collections import OrderedDict
n=input('Enter the number of inputs: ')
inputinlist=[]
b=[]
for i in range(1,int(n)+1):
    a=input('Enter your '+ n + ' words here: ')
    inputinlist.append(a)
#print (inputinlist)
my_dict=OrderedDict()
my_dict={i:inputinlist.count(i) for i in inputinlist}
for key, value in my_dict.items():
    b.append(str(value))
for x in b:
    print (x, end=" ")
