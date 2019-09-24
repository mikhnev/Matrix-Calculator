import math
import numpy as nm

def do_mult(x, y):
    return nm.dot(x, y)

def do_sum(x, y):
    return x+y

def do_subtract(x, y):
    return x - y

def do_transpose(x):
    return nm.transpose(x)