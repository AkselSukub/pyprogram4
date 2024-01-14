#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    num3 = float(input("Введите третье число: "))
    num4 = float(input("Введите четвертое число: "))
    sum1 = num1 + num2
    sum2 = num3 + num4
    result = sum1 / sum2
    print("Результат: {:.2f}".format(result))