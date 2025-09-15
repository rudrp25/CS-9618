
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