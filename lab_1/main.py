#!/usr/bin/env python
# -*- coding: utf-8 -*-
from matrix import *

#тестирование программы
if __name__ == "__main__": 
    try:
        
        rle = SLE(5)
        print("Система уравнений:")
        rle.print()
        print('\nРешение системы: ' + str(rle.solve()))
        print('\nОбратная матрица:')
        Matrix.print(matrix = Matrix.inverse(rle.getMatrix()), precision = 2)
        print("Произведение обратной матрицы и исходной:")
        Matrix.print(Matrix.mul(Matrix.inverse(rle.getMatrix()),rle.getMatrix()), precision=2)
        print("A*x " + str(Matrix.mulVector(rle.getMatrix(), rle.solve())))
        print("Максимум-норма невязки: " +
            str(abs(max(Vector.sub(Matrix.mulVector(rle.getMatrix(),rle.solve()),rle.getF())))))
        print("Определитель: " + str(Matrix.det(rle.getMatrix())))


    except Exception as e:
        print(repr(e))
