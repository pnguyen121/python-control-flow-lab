color = " "
while color != 'quit':
    color = input('Enter "green", "yellow", "red": ').lower()
    print(f'The user entered {color}')

    if color == 'green':
        print('Green means go')

    elif color == 'yellow':
        print('Yellow means slow down')

    elif color == 'red':
        print('Red means stop!')

    else:
        print('Nothing')






