'progran to calculate a fractorial og given number'

def fact_rec(num):
    if num == 1:
        return 1
    else :
        factorial = num * fact_rec(num - 1)
        return factorial

num = int (input ("enter a number"))
print(f"A factorial of {num} is {fact_rec(num)}.")
