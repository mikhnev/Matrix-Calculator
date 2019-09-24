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

def do_det(x):
    return nm.linalg.det(x)

def do_inv(x):
    return nm.linalg.inv(x)

def do_pow(x, n):
    return nm.linalg.matrix_power(x, n)