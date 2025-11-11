import random
while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        dice_number = int(input('Enter number of dice to roll (1 - 5): '))
        for _ in range(dice_number):
            roll = random.randint(1, 6)
            print(f'You rolled a {roll}')
    elif choice == 'n':
        print('Thank you for playing!')
        break
    else:
        print('Invalid choice!')

