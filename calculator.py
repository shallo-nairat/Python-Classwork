def add(x,y):
    result=x+y
    return result
def subtract(x,y):
    result=x-y
    return result
def divide(x,y):
    result=x/y
    return result
def multiply(x,y):
    result=x*y
    return result
def remainder(x,y):
    result=x%y
    return result
def powerof(h,i):
    result=h**i
    return result
def sum(*numbers):
    total=0
    for number in numbers:
        total+=number
    return total
def multiply_many(*numbers):
    mult=1
    for number in numbers:
        mult*=number
    return mult
 