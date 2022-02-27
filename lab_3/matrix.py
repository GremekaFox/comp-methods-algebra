#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from functools import reduce
from math import pow, log

class Vector:
  @staticmethod
  def sub(a,b):
    if (len(a)!=len(b)):
      raise Exception("Vector sub error: wrong sizes")
    return [i-j for i,j in zip(a,b)]

  @staticmethod
  def sum(a,b):
    if (len(a)!=len(b)):
      raise Exception("Vector sub error: wrong sizes")
    return [i+j for i,j in zip(a,b)]

  @staticmethod
  def compare(a, eps):
    for elem in a:
      if(abs(elem) > eps):
        return 1
    return 0

  @staticmethod
  def norm(a):
    return max([abs(i) for i in a])

class Matrix:

  @staticmethod
  def _gauss(matrix, f):
    eps = pow(10, -5)
    x = list(f)
    n = 0
    tmp = [0 for _ in range(len(x))]

    while(Vector.compare(Vector.sub(x, tmp), eps) > 0):
      tmp = list(x)
      for i in range(len(x)):
        sum = 0
        for j in range(len(x)):
          if j != i:
            sum += matrix[i][j] * x[j] / matrix[i][i]
        x[i] = f[i] / matrix[i][i] - sum
      n = n + 1

    return x, n

  @staticmethod
  def _jacobi(matrix, f):
    tMatrix = list(list(i) for i in matrix)
    tF = list(f)
    eps = pow(10, -5)
    n = 0
    tmp = [0 for _ in range(len(f))]
    for i in range(len(matrix)):
      for j in range(len(matrix[i])):
        if(i != j):
          tMatrix[i][j] /= tMatrix[i][i]
      tF[i] /= tMatrix[i][i]
      tMatrix[i][i] = 0

    x = list(tF)

    normB = Matrix.norm(tMatrix)
    normF = Vector.norm(tF)
    print("Норма B: " + str(normB))
    print("Норма x0: " + str(normF))
    print("Оценка количества итераций: n <= " + str(log(eps * (1 - normB) / normF) / log(normB) + 1))

    while (Vector.compare(Vector.sub(x, tmp), eps) > 0):
      tmp = list(x)
      for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix)):
            sum += tMatrix[i][j] * tmp[j]
        x[i] = tF[i] - sum
      n = n + 1

    return tMatrix, x, n

  #транспонирование
  @staticmethod
  def transpose(matrix):
      return [[matrix[j][i] for j in range(len(matrix[i]))] for i in range(len(matrix))]

  @staticmethod
  def norm(matrix):
    return max([sum([abs(i) for i in line]) for line in matrix])

  #умножение матриц
  @staticmethod
  def mul(a,b):
    if (len(a[0])!=len(b)):
      raise Exception("Matrix mul error: wrong sizes")
    return [[(sum(a[i][k]*b[k][j] for k in range(len(a)))) for j in range(len(a[i]))] for i in range(len(a))]

  #умножение матрицы на столбец
  @staticmethod
  def mulVector(matrix,vector):
    if (len(matrix[0])!=len(vector)):
      raise Exception("Matrix mulVector error: wrong sizes")
    return [(sum([matrix[i][j]*vector[j] for j in range(len(vector))])) for i in range(len(matrix))]               

  #сумма матриц
  @staticmethod
  def sum(a,b):
    if (len(a)!= len(b) or len(a[0]) != len(b[0])): 
      raise Exception("Matrix sub error: wrond size")   
    return [[a[i][j]+b[i][j] for j in range(len(a[i]))]for i in range(len(a))]

  #разность матриц
  @staticmethod
  def sub(a,b):
    if (len(a)!= len(b) or len(a[0]) != len(b[0])): 
      raise Exception("Matrix sub error: wrond size")   
    return [[a[i][j]-b[i][j] for j in range(len(a[i]))]for i in range(len(a))]

  @staticmethod
  def devide(a,con):
    return [[a[i][j] / con for j in range(len[a[i]])] for i in range(len(a))]

  #печать матрицы
  @staticmethod
  def print(matrix,precision = 16): 
    for line in matrix:
      for item in line:
        print(str(round(item,precision)), end='\t')
      print('\n')


class SLE:
  #инициализация СЛУ
  def __init__(self):
    #задание матрицы A 
    self.__matrix = [
      [0.9384, 0.0000, -0.2451, 0.1724, 0.2873],
      [-0.0575, 0.6128, 0.0000, -0.1168, 0.0383],
      [0.0192, -0.1724, 1.1107, 0.0211, 0.0670],
      [0.0575, 0.0000, -0.1398, 1.1107, 0.0000],
      [0.0383, -0.0575, 0.2777, -0.0230, 0.8043]
    ]
    #задание f
    self.__result = [2.9951, -3.3187, 2.6676, 3.3398, -3.9181]

  #A
  def getMatrix(self):
    return [(list(i)) for i in self.__matrix]
  
  #f
  def getF(self):
    return list(self.__result)

  #печать условия
  def print(self):
    for i in range(len(self.__matrix)):
      for j in range(len(self.__matrix[i])):
        print(str(self.__matrix[i][j]), end='\t')
      print(" | "+ str(self.__result[i]))
      print('\n')

  #решение системы
  def solve(self,f = None):
    if (f == None):
      return Matrix._gauss(self.__matrix,self.__result), Matrix._jacobi(self.__matrix, self.__result)
    else:
      return Matrix._gauss(self.__matrix,f), Matrix._jacobi(self.__matrix, f)