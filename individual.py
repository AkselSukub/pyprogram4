#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    side1 = float(input("Введите длину первой стороны прямоугольника: "))
    side2 = float(input("Введите длину второй стороны прямоугольника: "))
    perimeter = 2 * (side1 + side2)
    diagonal = (side1 + side2) ** 0.5
    print("Периметр прямоугольника: {:.2f}".format(perimeter))
    print("Длина диагонали прямоугольника: {:.2f}".format(diagonal))