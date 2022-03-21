def matrix(matrix): 
  for item in matrix:
    for num in item:
      print(num, end=" ")
    print()

mtrx = [ [1,2,3],[4,5,6],[7,8,9] ] 
matrix(mtrx)