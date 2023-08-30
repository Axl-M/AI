# Сигмоидальная функция активации (зачение от 0 до 1)

import numpy as np


# функция активации: f(x) = 1 / (1 + e ^ (-х))
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class Neuron:
    def __init__(self, w):
        self.w = w

    def y(self, x):             # сумматор
        s = np.dot(self.w, x)   # суммируем входы
        return sigmoid(s)       # ф-ция активации


Xi = np.array([1, 0, 0, 1])     # значения входов
Wi = np.array([5, 4, 3, 1])     # веса входных сенсоров
n = Neuron(Wi)                  # создание НЕЙРОНА (объекта класса)
print('Y =', n.y(Xi))           # обращение к нейрону
