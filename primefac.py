#2Prime factors

#1prime check
def prime(n):
  k=True
  if(n<2):
    k=False
  else:
    for i in range(2,(n//2+1)):
      if(n%i==0):
        k=False
  return k



fa=[]
def primefac(n):

  while n>=2:
    if prime(n):
      fa.append(n)

    else:
      for i in range(2,(n//2+1)):
        if prime(i):
          if(n%i==0):
            fa.append(i)
            break

    l=fa[len(fa)-1]
    n=n//l 
  return fa

#print("factors=",primefac(188))

#number
no=196

li=[]
k=primefac(no)
for i in k:
  if i not in li:
    print("prime:",i,"times:",k.count(i))
    li.append(i)
