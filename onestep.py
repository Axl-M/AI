# функции единичного скачка ( функции Хевисайда)
# на выходе 1 если результат превосходит установленное пороговое значение

import numpy as np


# ф-ция активации
def onestep(x):
    b = 5
    if x >= b:
        return 1
    else:
        return 0


class Neuron:
    def __init__(self, w):
        self.w = w

    def y(self, x):             # сумматор
        s = np.dot(self.w, x)   # суммируем входы
        return onestep(s)       # ф-ция активации


Xi = np.array([1, 0, 0, 1])     # значения входов
Wi = np.array([5, 4, 3, 1])     # веса входных сенсоров
n = Neuron(Wi)                  # создание НЕЙРОНА (объекта класса)
print('Y =', n.y(Xi))           # обращение к нейрону
