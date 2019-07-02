# Enter your code here. Read input from STDIN. Print output to STDOUT

n,m=input().split()
someth=input().split()
A = set(input().split())
B = set(input().split())
c=[]
d=[]
for i in someth:
    if i in A:
        c.append(i)

for i in someth:
    if i in B:
        d.append(i)
print (len(c)-len(d))
