#!/usr/bin/env python
# -*- coding: latin-1 -*-

import random
from functools import reduce

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
    
    #метод гаусса с выбором главного эл-та по столбцу
    @staticmethod
    def _gauss(matrix, vector=None):
        tMatrix = [list(i) for i in matrix]
        if (vector != None):
            tResult = list(vector)
        replaces = 0
        for i in range(len(tMatrix)-1):
            maxnumber = i
            maxvalue = tMatrix[i][i]
            # выбор максимального элемента
            for k in range(i+1,len(tMatrix)):
                if abs(tMatrix[k][i]) > abs(maxvalue):
                    maxvalue = tMatrix[k][i]
                    maxnumber = k
            #перестановка строки с макс. элементом
            if (maxnumber != i):
                tMatrix[maxnumber], tMatrix[i] = list(tMatrix[i]), list(tMatrix[maxnumber])
                if (vector != None):
                    tResult[maxnumber], tResult[i] = tResult[i], tResult[maxnumber]
                replaces+=1
            for j in range(i,len(tMatrix)-1):
            #преобразование строки
                for k in range(i,len(tMatrix)-1):
                    if (tMatrix[i][i] != 0):
                        tMatrix[j+1][k+1] -= tMatrix[i][k+1] * tMatrix[j+1][i] / tMatrix[i][i]
                    else:
                        raise Exception("Impossible to use Gauss-method: division by 0")
                if (vector != None):
                    tResult[j+1] -= tResult[i] * tMatrix[j+1][i] / tMatrix[i][i]

                for k in range(0,i+1):
                    tMatrix[j+1][k]=0
        #возвращает преобразованную матрицу, количество перестановок и вектор F
        if (vector != None):
            return (tMatrix, replaces, tResult)
        else:
            return (tMatrix, replaces)

    #решение СЛУ
    @staticmethod
    def _solveSystem(matrix,f):
        
        if Matrix.det(matrix)==0:
            raise Exception("Impossible to solve: det = 0")

        result = []
        tMatrix,replaces,tResult = Matrix._gauss(matrix,f)
        
        #обратный ход метода гаусса
        for i in reversed(range(len(tMatrix))):
            x = tResult[i]
            k=0
            for j in reversed(range(1,len(tMatrix))):
                if (tMatrix[i][j-1]==0):
                    break
                x-=result[len(result)-k-1]*tMatrix[i][j]
                k+=1
            result.insert(0,x/tMatrix[i][i])

        return result
    
    #транспонирование
    @staticmethod
    def transpose(matrix):
        return [[matrix[j][i] for j in range(len(matrix[i]))] for i in range(len(matrix))]

    #определитель
    @staticmethod
    def det(matrix):
        tMatrix, replaces = Matrix._gauss(matrix)
        return reduce(lambda x,y:x*y,[tMatrix[i][i] for i in range(len(tMatrix))]) * ((-1) ** int(replaces % 2 != 0))

    #поиск обратной матрицы 
    @staticmethod
    def inverse(matrix):
        return Matrix.transpose([Matrix._solveSystem(matrix, line) for line in 
            [[int(i==j) for j in range(len(matrix[i]))] for i in range(len(matrix))]])

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
    def __init__(self,n):
        #задание матрицы A 
        self.__matrix = [
        [0.9384, 0.0000, -0.2451, 0.1724, 0.2873],
      [-0.0575, 0.6128, 0.0000, -0.1168, 0.0383],
      [0.0192, -0.1724, 1.1107, 0.0211, 0.0670],
      [0.0575, 0.0000, -0.1398, 1.1107, 0.0000],
      [0.0383, -0.0575, 0.2777, -0.0230, 0.8043],
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
            return Matrix._solveSystem(self.__matrix,self.__result)
        else:
            return Matrix._solveSystem(self.__matrix,f)