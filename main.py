from random import randint

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


# 7
def find_euclid_dist(a, b):

    return print(((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5)


# 9
rand_nums = [randint(10, 40) for i in range(50)]
filtered_nums = [n for n in rand_nums if n % 2 == 0 and n % 5 ==0]



# 10
rand_dict = {k: [randint(0, 100) for i in range(10)] for k in [x for x in range(5)]}
sums = [sum(v) for v in list(rand_dict.values())]


#11
given_list_of_nums = [4, 78, 99, 872]
try_count = 0
while len(given_list_of_nums):
    rng_num = randint(0, 10000)
    if rng_num in given_list_of_nums:
        given_list_of_nums.remove(rng_num)
    try_count += 1
print(try_count)
