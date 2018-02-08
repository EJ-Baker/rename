import random

def int_array(size):
    return list(range(0, size))

def int_array_random(size):
    array = int_array(size)
    random.shuffle(array)
    return array

def hex_array(size):
    array = int_array(size)
    return ([hex(i)[2:] for i in array])

def hex_array_random(size):
    array = int_array_random(size)
    return ([hex(i)[2:] for i in array])
