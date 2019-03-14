num1 = float(input('Please input first number (must be between 0 and 10000): '))

while num1 <=0 or num1 >= 10000:
    num1 = float(input('Error, first number must be between 0 and 10000, try again: '))

num2 = float(input('Please input second number (must be between 0 and 10000): '))

while num2 <=0 or num2 >= 10000:
    num2 = float(input('Error, first number must be between 0 and 10000, try again: '))

num3 = float(input('Please input third number (must be between 0 and 10000): '))

while num3 <=0 or num3 >= 10000:
    num3 = float(input('Error, first number must be between 0 and 10000, try again: '))

num4 = float(input('Please input fourth number (must be between 0 and 10000): '))

while num4 <=0 or num4 >= 10000:
    num4 = float(input('Error, first number must be between 0 and 10000, try again: '))

num5 = float(input('Please input fifth number (must be between 0 and 10000): '))

while num5 <=0 or num5 >= 10000:
    num5 = float(input('Error, first number must be between 0 and 10000, try again: '))

if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
    print('your first number', num1, 'is the largest')
elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
    print('your second number', num2, 'is the largest')
elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
    print('your third number', num3, 'is the largest')
elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
    print('your fourth number', num4, 'is the largest')
else:
    print('Your fifth number',  num5, 'is the largest')

if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
    print('your first number', num1, 'is the smallest')
elif num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:
    print('your second number', num2, 'is the smallest')
elif num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5:
    print('your third number', num3, 'is the smallest')
elif num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5:
    print('your fourth number', num4, 'is the smallest')
else:
    print('Your fifth number',  num5, 'is the smallest')


