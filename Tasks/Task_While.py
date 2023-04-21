while True:
    try:
        num1 = float(input('Enter first number:'))
        num2 = float(input('Enter second number:'))
    except ValueError as e:
        print(e)
        print('You must enter numbers!')
        continue

    total = num1 / num2
    print(total)

    answer = input('Do you want continue? yes or no:')
    if answer == 'no':
        break
