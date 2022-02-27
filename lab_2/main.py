#!/usr/bin/env python
# -*- coding: utf-8 -*-
from matrix import *

#тестирование программы
if __name__ == "__main__":
  try:
    rle = SLE()
    print("Система уравнений:")
    rle.print()

    sMatrix, x, y, tMatrix, tResult, detA = rle.solve()

    print("\nAт * A:")
    Matrix.print(tMatrix, 4)

    print("\nAт * b: " + str(tResult))

    print("\ns: ")
    Matrix.print(sMatrix, 4)

    print("\ny: " + str(y))

    print("\nx: " + str(x))

    print("\nA*x: " + str(Matrix.mulVector(rle.getMatrix(), x)))

    print("\nМаксимум-норма невязки: " +
      str(abs(max(Vector.sub(Matrix.mulVector(rle.getMatrix(),x),rle.getF())))))

    print("\nОпределитель: " + str(detA))

  except Exception as e:
    print(repr(e))