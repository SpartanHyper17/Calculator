print('Welcome to Calculator Program')

while True:
        print('Press A to Add two numbers')
        print('Press S to Subtract two numbers')
        print('Press M to Multiply two numbers')
        print('Press D to Divide two numbers')
        print('Press X to exit the program')
        option = input()

        if(option == 'A'):
                print('Welcome to addition')
                print('Enter first number to add: ')
                x=int(input())
                print('Enter second number: ')
                y= int(input())
                z = x+y
                print('Sum of two numbers: %d and %d : %d' % (x, y, z))

        elif(option == 'D'):
                print('Welcome to Division')
                print('Enter the numerator number: ')
                x = int(input())
                print('Enter the denominator number: ')
                y= int(input())
                z= x/y
                print('Division value of : %d / %d = %d ' % (x, y, z))

        elif(option == 'S'):
                print('Welcome to Subtraction')
                print('Enter the first number: ')
                x = int(input())
                print('Enter the second number: ')
                y= int(input())
                z= x-y
                print('Subtraction value of : %d - %d = %d ' % (x, y, z))

        elif(option == 'M'):
                print('Welcome to Multiplication')
                print('Enter the first number: ')
                x = int(input())
                print('Enter the second number: ')
                y= int(input())
                z= x*y
                print('Multiplication value of : %d * %d = %d ' % (x, y, z))

        elif(option == 'X'):
                break