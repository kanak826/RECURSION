#FACTORIAL NUMBER.....................................#
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))

#......................................................#
#COUNT DOWN PROGRMME...................................#
def count_down(num):
    if num==0:
        return "Time up"
    print(num)
    return count_down(num-1)

print(count_down(10))
#.....................................................#
#SUM OF N NATURAL NUMBERS.............................#
def sum_natural_num(num1):
    if num1 == 0:
        return 0
    
    return sum_natural_num(num1-1) 
print(sum_natural_num(10))
#......................................................#