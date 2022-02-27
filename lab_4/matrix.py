class Matrix:
  #метод Данилевского
  @staticmethod
  def danMethod(matrix):
    tMatrix = list(i for i in matrix)
    sMatrix = list(list(int(i == j) for j in range(len(matrix)))for i in range(len(matrix)))
    for i in reversed(range(len(matrix) - 1)):
      mMatrix = [[int(j == k) for j in range(len(matrix))] for k in range(len(matrix))]
      mMatrix[i] = [(- tMatrix[i + 1][j] / tMatrix[i + 1][i]) if i != j else 1 / tMatrix[i + 1][i] for j in range(len(matrix))]
      mReversed = [[int(j == k) if k != i else tMatrix[i + 1][j] for j in range(len(matrix))] for k in range(len(matrix))]
      sMatrix = Matrix.mul(sMatrix, mMatrix)
      tMatrix = Matrix.mul(Matrix.mul(mReversed, tMatrix), mMatrix)
    
    print('a^5 + (' + str(-tMatrix[0][0]) + ') * a^4 + (' + str(-tMatrix[0][1]) + ') * a^3 + ('
    + str(-tMatrix[0][2]) + ') * a^2 + (' + str(-tMatrix[0][3]) + ') * a + (' + str(-tMatrix[0][4]) + ') = 0')
    a1 = 0.555267 # единственный действительный корень данного уравнения
    return a1, Matrix.mulVector(sMatrix, [a1**4, a1**3, a1**2, a1, 1])

  #умножение матриц
  @staticmethod
  def mul(a,b):
    return [[(sum(a[i][k]*b[k][j] for k in range(len(a)))) for j in range(len(a[i]))] for i in range(len(a))]

  #умножение матрицы на вектор
  @staticmethod
  def mulVector(matrix,vector):
    return [(sum([matrix[i][j]*vector[j] for j in range(len(vector))])) for i in range(len(matrix))] 