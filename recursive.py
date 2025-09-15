
# recursive version
def Power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * Power(base, exp - 1)

print(Power(2, 3))

#normal version
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return (base**exp)
print(power(2, 3))

# recursive function 2
def Fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
print(Fibonacci(4))
