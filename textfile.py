# case1
try:
    a = print(20/0)
except:
    print('Error, cannot divide number by zero')  # exception handler is used to ensure program continuity.

print()

# case2
num = input('Enter an integer: ')  # if letter inputted, it will go straight to exception handler (line 14)
try:
    n = int(num)
    print('Your number is:', n)
except:
    print('Input is not an integer')