def getMaxMinElementOfMatrix(matrix):
  maxMinElements = []
  max = matrix[0][0]
  min = matrix[0][0]
  for i in range(0,len(matrix)):
    for j in range(0,len(matrix[i])):
      if  matrix[i][j] > max:
        max = matrix[i][j]
      if matrix[i][j]  < min:
        min = matrix[i][j] 
  maxMinElements.append(min)
  maxMinElements.append(max)
  return maxMinElements

matrix = [[5,1234,78],[15,9800,12]
minMaxElements = getMaxMinElementOfMatrix(matrix)

print(minMaxElements)
