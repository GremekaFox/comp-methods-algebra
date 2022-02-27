#!/usr/bin/env python
# -*- coding: latin-1 -*-

import random
from functools import reduce
from math import sqrt

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

class Matrix:

  #метод квадратного корня
  @staticmethod
  def _sqrRoot(matrix, vector):
    #матрица А
    tMatrix = [list(i) for i in matrix]
    #вектор b
    tResult = list(vector)
    #Ат * А
    tResult = Matrix.mulVector(Matrix.transpose(tMatrix), tResult)
    #Ат * b
    tMatrix = Matrix.mul(Matrix.transpose(tMatrix), tMatrix)
    #матрица S
    sMatrix = [[0 for _ in range(len(matrix))] for __ in range(len(matrix))]
    #S11
    sMatrix[0][0] = sqrt(tMatrix[0][0])

    for j in range(1, len(sMatrix[0])):
      #S1j
      sMatrix[0][j] = tMatrix[0][j] / sMatrix[0][0]

    for i in range(1, len(sMatrix)):
      for j in range(i, len(sMatrix[i])):
        if(i == j):
          sum = 0
          for k in range(0, i):
            sum += sMatrix[k][i] ** 2
          #Sii
          sMatrix[i][i] = sqrt(tMatrix[i][i] - sum)
        else:
          sum = 0
          for k in range(0, i):
            sum += sMatrix[k][i] * sMatrix[k][j]
          #Sij
          sMatrix[i][j] = (tMatrix[i][j] - sum) / sMatrix[i][i]
    #Sт
    stMatrix = Matrix.transpose(sMatrix)

    y = [0 for _ in range(len(vector))]
    x = list(y)
    #y1
    y[0] = tResult[0] / sMatrix[0][0]

    for i in range(1, len(y)):
      sum = 0
      for k in range(0, i):
        sum += sMatrix[k][i] * y[k]
      #yi
      y[i] = (tResult[i] - sum) / sMatrix[i][i]
    #x1
    x[len(x) - 1] = y[len(y) - 1] / sMatrix[len(sMatrix) - 1][len(sMatrix) - 1]

    for i in reversed(range(0, len(x) - 1)):
      sum = 0
      for k in range(i + 1, len(x)):
        sum += sMatrix[i][k] * x[k]
      #xi
      x[i] = (y[i] - sum) / sMatrix[i][i]

    detA = sqrt(Matrix.det(sMatrix))

    #возвращает преобразованную матрицу и вектор F
    return (sMatrix, x, y, tMatrix, tResult, detA)

  #транспонирование
  @staticmethod
  def transpose(matrix):
      return [[matrix[j][i] for j in range(len(matrix[i]))] for i in range(len(matrix))]

  #определитель
  @staticmethod
  def det(matrix):
    res = 1
    for i in range(len(matrix)):
      res *= matrix[i][i] ** 2
    return res

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
      return Matrix._sqrRoot(self.__matrix,self.__result)
    else:
      return Matrix._sqrRoot(self.__matrix,f)