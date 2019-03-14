num1 = float(input('Please input first number: '))
num2 = float(input('Please input second number: '))
num3 = float(input('Please input third number: '))
num4 = float(input('Please input fourth number: '))
num5 = float(input('Please input fifth number: '))
num6 = float(input('Please input sixth number: '))
num7 = float(input('Please input seventh number: '))
num8 = float(input('Please input eigth number: '))
num9 = float(input('Please input ninth number: '))
num10 = float(input('Please input tenth number: '))
largest = 0
smallest = 0

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


