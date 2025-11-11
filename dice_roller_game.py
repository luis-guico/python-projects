import random
while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f'({dice1},{dice2})')
    elif choice == 'n':
        print('Thank you for playing!')
        break
    else:
        print('Invalid choice!')

    # Ask: roll the dice?
    # if user enters y
    #   generate 2 random numbers between 1 and 6
    #   print the numbers
    #if user enters n
    #   print thank you
    #   terminate
    #Else
    #   print invalid input
    