#!/usr/bin/env python
# -*- coding: utf-8 -*-
from matrix import *

#тестирование программы
if __name__ == "__main__":
  try:
    rle = SLE()
    print("Система уравнений:")
    rle.print()

    print("Метод Якоби")
    [x, n], [b, f, k] = rle.solve()

    print("Матрица B")
    Matrix.print(b)
    print("\nx: " + str(f))
    print("Число итераций: " + str(k))
    print("\nМаксимум-норма невязки: " +
      str(abs(max(Vector.sub(Matrix.mulVector(rle.getMatrix(),f),rle.getF())))))

    print("\nМетод Гаусса-Зейделя")
    print("\nx: " + str(x))
    print("Число итераций: " + str(n))
    print("\nМаксимум-норма невязки: " +
      str(abs(max(Vector.sub(Matrix.mulVector(rle.getMatrix(),x),rle.getF())))))

  except Exception as e:
    print(repr(e))