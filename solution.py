"""import math
from functools import reduce
def std(values: str) -> float:
    pass
def standard_deviation(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    variance = sum((x - mean) ** 2 for x in numbers) / n
    return round(math.sqrt(variance), 1)

numbers = list(map(int, '10 40 30 50 20'.split()))
print(standard_deviation(numbers))

import math
from functools import reduce

def standard_deviation(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    variance = sum((x - mean) ** 2 for x in numbers) / n
    return round(math.sqrt(variance), 1)

numbers = list(map(int, '10 40 30 50 20'.split()))
print(standard_deviation(numbers))"""

import math
from functools import reduce
def std(values: str) -> float:
    numbers = list(map(int, values.split()))
    mean = sum(numbers) / len(numbers)
    variance = reduce(lambda x, y: x + y, map(lambda x: (x - mean) ** 2, numbers)) / len(numbers)
    std_deviation = round(math.sqrt(variance), 1)
    return std_deviation
values = '10 40 30 50 20'
result = std(values)
print(result)

#Avila Lucho