num1 = float(input('Please input first number (must be between 0 and 10000): '))
num2 = float(input('Please input second number (must be between 0 and 10000): '))
num3 = float(input('Please input third number (must be between 0 and 10000): '))
num4 = float(input('Please input fourth number (must be between 0 and 10000): '))
num5 = float(input('Please input fifth number (must be between 0 and 10000): '))
num6 = float(input('Please input sixth number (must be between 0 and 10000): '))
num7 = float(input('Please input seventh number (must be between 0 and 10000): '))
num8 = float(input('Please input eigth number (must be between 0 and 10000): '))
num9 = float(input('Please input ninth number (must be between 0 and 10000): '))
num10 = float(input('Please input tenth number (must be between 0 and 10000): '))
largest = 0
smallest = 0

while num1 <=0 or num1 >= 10000:
    num1 = float(input('Error, first number must be between 0 and 10000, try again: '))

while num2 <=0 or num2 >= 10000:
    num2 = float(input('Error, second number must be between 0 and 10000, try again: '))

while num3 <=0 or num3 >= 10000:
    num3 = float(input('Error, third number must be between 0 and 10000, try again: '))

while num4 <=0 or num4 >= 10000:
    num4 = float(input('Error, fourth number must be between 0 and 10000, try again: '))

while num5 <=0 or num5 >= 10000:
    num5 = float(input('Error, fifth number must be between 0 and 10000, try again: '))

while num6 <=0 or num6 >= 10000:
    num6 = float(input('Error, sixth number must be between 0 and 10000, try again: '))

while num7 <=0 or num7 >= 10000:
    num7 = float(input('Error, seventh number must be between 0 and 10000, try again: '))

while num8 <=0 or num8 >= 10000:
    num8 = float(input('Error, eighth number must be between 0 and 10000, try again: '))

while num9 <=0 or num9 >= 10000:
    num9 = float(input('Error, ninth number must be between 0 and 10000, try again: '))

while num10 <=0 or num10 >= 10000:
    num10 = float(input('Error, tenth number must be between 0 and 10000, try again: '))

def print_results(largest, smallest):
    print("your largest number is: ", largest,", and your smallest number is: ", smallest)
    return;
def find_biggest(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10):
    largest = num1
    if num1 >= largest:
        largest = num1
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3
    if num4 > largest:
        largest = num4
    if num5 > largest:
        largest = num5
    if num6 > largest:
        largest = num6
    if num7 > largest:
        largest = num7
    if num8 > largest:
        largest = num8
    if num9 > largest:
        largest = num9
    if num10 > largest:
        largest = num10   
        
    return largest;

def find_smallest(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10):
    smallest = num1
    if num1 <= smallest:
        smallest = num1
    if num2 < smallest:
        smallest = num2
    if num3 < smallest:
        smallest = num3
    if num4 < smallest:
        smallest = num4
    if num5 < smallest:
        smallest = num5
    if num6 < smallest:
        smallest = num6
    if num7 < smallest:
        smallest = num7
    if num8 < smallest:
        smallest = num8
    if num9 < smallest:
        smallest = num9
    if num10 < smallest:
        smallest = num10

    return smallest;

largest = find_biggest(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10)
smallest = find_smallest(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10)
print_results(largest, smallest)


