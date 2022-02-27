#!/usr/bin/env python
# -*- coding: utf-8 -*-
from matrix import *

if __name__ == "__main__":
  matr = [
    [0.9384, 0.0000, -0.2451, 0.1724, 0.2873],
      [-0.0575, 0.6128, 0.0000, -0.1168, 0.0383],
      [0.0192, -0.1724, 1.1107, 0.0211, 0.0670],
      [0.0575, 0.0000, -0.1398, 1.1107, 0.0000],
      [0.0383, -0.0575, 0.2777, -0.0230, 0.8043]
  ]
  a1, x1 = Matrix.danMethod(matr)
  print('Собственное значение a1(единственное): ' + str(a1))
  print('Собственный вектор x1:')
  print(x1)
  print('A * x1:')
  print(Matrix.mulVector(matr, x1))
  print('a1 * x1:')
  x1 = [a1 * i for i in x1]
  print(x1)