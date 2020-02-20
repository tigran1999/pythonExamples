def multiplyMutrix(a,b):

  if(len(a[0]) != len(b)):
    print("There is't any solution")
    return

  c= []
  for i in range(len(a)): 
    tmp = []
    for j in range(len(b[0])): 
      element=0
      for k in range(len(b)): 
        element += a[i][k] * b[k][j]
      tmp.append(element)
    c.append(tmp)  

  return c

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,2],[3,4],[5,6]]
c = multiplyMutrix(a,b)
print(c)
