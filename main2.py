import math
from random import randint, choice
from collections import Counter

"""
Решение задач по курсу
"""


# 1
def wrapper(operation: str):
    func = {
        'area': lambda r: math.pi * r ** 2,
        'circumference': lambda r: 2 * math.pi * r,
        'volume': lambda r: 4 / 3 * math.pi * r ** 3,
    }

    return func[operation]


# 2
random_nums = [randint(-50, 50) for i in range(100)]
with open("numbers.txt", "w") as file:
    file.write(' '.join([str(n) for n in random_nums if n > 0]))
with open("numbers.txt", "r") as file:
    nums = [int(n) for n in file.read().split()]
print(sum(nums)/len(nums))


# 3
words = ['hello', 'python', 'good', 'car', 'bye', 'sleep', 'python', 'car', 'python']
words2 = [choice(words) for i in range(1000)]
counted = Counter(words2)
for word in list(set(words)):
    print(f'{word}: {(counted[word]/1000)*100}')


# 4
def words_prog(mode):
    if mode == 'train':
        eng_word = input('Введите слово на английском ')
        translation = input('Введите перевод ')
        with open("words.txt", "a") as file:
            file.write(f'\n{eng_word} - {translation}')
    elif mode == 'test':
        request = input('Какое слово перевести ')
        with open("words.txt", "r") as file:
            words = [x.split(' - ') for x in file.read().split('\n')]
        dict_words = {pair[0]: pair[1] for pair in words}
        print(dict_words[request])


# 6
class Wolf:

    def __init__(self, speed, weight, color):
        self.speed = speed
        self.weight = weight
        self.color = color

    def get_power(self):
        return self.speed**2/self.weight


colors = ['white', 'black', 'gray', 'ginger', 'brown']
list_of_wolfs = [Wolf(randint(20, 200), randint(30, 70), choice(colors)) for x in range(100)]
powers_of_wolves = [wolf.get_power() for wolf in list_of_wolfs]
most_powerful = powers_of_wolves.index(max(powers_of_wolves))
print(f'Cамый сильный волк № {most_powerful}, его сила: {max(powers_of_wolves)}')

# 7
class Phone:

    def __init__(self, color, price, name):
        self.color = color
        self.price = price
        self.name = name


class Nokia(Phone):

    def __init__(self, color, price, count_buttons):
        super().__init__(color, price, name=self.__class__.__name__)
        self.count_buttons = count_buttons


class Samsung(Phone):

    def __init__(self, color, price, waterproofness):
        super().__init__(color, price, name=self.__class__.__name__)
        self.count_buttons = waterproofness


class Iphone(Phone):

    def __init__(self, color, price, speed_internet):
        super().__init__(color, price, name=self.__class__.__name__)
        self.count_buttons = speed_internet


# 8
def print_triangle(number: int):
    num_list = list(range(1, number+1))
    num_list.reverse()
    for x in range(len(num_list)):
        print(' '.join(str(x) for x in num_list))
        num_list.pop(0)


# 9
def my_sqrt(number):
    if number < 0:
        raise ValueError('impossible to got negative number')

    return number**0.5


# 10
class DistanceError(Exception):
    pass


def circumference(radius):
    if radius < 0:
        raise DistanceError('radius can`t less than 0')

    return 2*math.pi*radius
