import random

def int_array(size, offset):
    return list(range(offset, size + offset))

def int_array_random(size, offset):
    array = int_array(size, offset)
    random.shuffle(array)
    return array

def hex_array(size, offset):
    array = int_array(size, offset)
    return ([hex(i)[2:] for i in array])

def hex_array_random(size, offset):
    array = int_array_random(size, offset)
    return ([hex(i)[2:] for i in array])
