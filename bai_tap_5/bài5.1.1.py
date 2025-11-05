# File: mymath.py

def square(n):
    return n * n

def cube(n):
    return n * n * n

def average(values):
    nvals = len(values)
    tong = 0.0
    for v in values:
        tong += v
    return float(tong / nvals)
