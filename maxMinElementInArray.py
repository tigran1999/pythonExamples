def getMaxMinElementOfArray(array):
  maxMinElements = []
  max = array[0]
  min = array[0]
  for i in range(1,len(array)):
    if  array[i] > max:
      max = array[i]
    if array[i] < min:
      min = array[i]  
  maxMinElements.append(min)
  maxMinElements.append(max)
  return maxMinElements

array = [5,1234,78,15,98,12]

minMaxElements = getMaxMinElementOfArray(array)  
print(minMaxElements)
