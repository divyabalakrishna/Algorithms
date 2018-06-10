
import copy

def perm(a,k=0,result=[], count=0):
   if(k==len(a)):
      if a not in result:
          result.append(copy.deepcopy(a))
   else:
      for i in range(k,len(a)):
         a[k],a[i] = a[i],a[k]
         perm(a, k+1, result)

array = [0, 1, 1]
result=[]
perm(array, 0, result, count=0)
for i in result:
    print(i)
