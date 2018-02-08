import random

def int_array(size, offset):
    return list(range(offset, size + offset))

def int_array_random(size, offset):
    array = int_array(size, offset)
    random.shuffle(array)
    return array

def int_array_padded(size, offset):
    array = int_array(size, offset)
    length = len(str(size + offset))
    return (['{num:0{width}}'.format(num = i , width = length) for i in array])

def int_array_random_padded(size, offset):
    array = int_array_random(size, offset)
    length = len(str(size + offset))
    return (['{num:0{width}}'.format(num = i , width = length) for i in array])

def hex_array(size, offset):
    array = int_array(size, offset)
    return ([hex(i)[2:] for i in array])

def hex_array_random(size, offset):
    array = int_array_random(size, offset)
    return ([hex(i)[2:] for i in array])

def hex_array_padded(size, offset):
    array = hex_array(size, offset)
    length = len(hex(size + offset)[2:])
    return (['{:0>{width}}'.format(i , width = length) for i in array])

def hex_array_random_padded(size, offset):
    array = hex_array_random(size, offset)
    length = len(hex(size + offset)[2:])
    return (['{:0>{width}}'.format(i , width = length) for i in array])
