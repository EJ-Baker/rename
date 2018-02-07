import random

def int_array(size):
    return list(range(0, size))
def int_array_random(size):
    array = int_array(size)
    random.shuffle(array)
    return array
