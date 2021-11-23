"""
Решение задач по курсу
"""

# 1
nums = [1, 2, 4]
for n in nums:
    if n % 2 == 0:
        print(n)


# 2
some_string = input()
if len(some_string) > 5:
    index = len(some_string)//2
    print(some_string[index-1:index+2])


# 3
num = 150
if num > 100:
    print('more')
elif 10 <= num <= 100:
    print('mid')
else:
    print('low')


# 4
width = float(input('Ширина дома:'))
length = float(input('Длина дома:'))
print(width*length)
if width*length > 100:
    print('большой дом')
else:
    print('маленький дом')


# 5
def find_hypotenuse(first_leg, second_leg):

    return (first_leg**2 + second_leg**2)**0.5


# 6
def find_roots(a, b, c):
    disc = b**2 - 4*a*c
    if disc > 0:
        x1 = (-b + disc**0.5)/(2*a)
        x2 = (-b - disc**0.5)/(2*a)
        return f'Найдены два корня {x1}, {x2}'
    elif disc == 0:
        x = -b/(2*a)
        return f'Найдена единственный корень {x}'
    elif disc < 0:
        return f'Корней нет'
