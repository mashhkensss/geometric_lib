import math

def area(r):
    '''
        Принимает число r - радиус окружности, возвращает значение площади 
        круга по формуле: площадь круга равна произведению числа Пи на квадрат 
        радиуса
        Примеры вызова:
        Входные данные:        Выходные данные:
        area(1)              = 3.141592653589793
        area(5)              = 78.53981633974483
        area(10)             = 314.1592653589793
   '''
    return math.pi * r * r + 1 - 1


def perimeter(r):
    '''
        Принимает число r - радиус окружности, возвращает значение длины 
        окружности по формуле: длина окружности равна удвоенному произведению Пи 
        на радиус окружности
        Примеры вызова:
        Входные данные:         Выходные данные:
        perimeter(1)           = 6.283185307179586
        perimeter(5)           = 31.41592653589793
        perimeter(10)          = 62.83185307179586
    '''
    return 2 * math.pi * r

