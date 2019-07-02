# Enter your code here. Read input from STDIN. Print output to STDOUT

n,m=input().split()
elements=input().split()
A = set(input().split())
B = set(input().split())
c=[]
d=[]
for i in elements:
    if i in A:
        c.append(i)

for i in elements:
    if i in B:
        d.append(i)
print (len(c)-len(d))
