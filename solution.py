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