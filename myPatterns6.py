# This program allows the user to choose various
# patterns from a menu. This program
# imports the patterns module.
import patterns

# Constants for the menu choices
PATTERN1_CHOICE = 1
PATTERN2_CHOICE = 2
PATTERN3_CHOICE = 3
PATTERN4_CHOICE = 4
PATTERN5_CHOICE = 5
PATTERN6_CHOICE = 6
ALL_PATTERNS_CHOICE = 7
DIGIT_CHOICE = 8

QUIT_CHOICE = 0

# The main function.
def main():
    # The choice variable controls the loop
    # and holds the user's menu choice.
    choice = -1
    digit = 6

    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()

        # Get the user's choice.
        choice = int(input('\n\nEnter your choice: '))

        # Perform the selected action.
        if choice == 8:
            digit = int(input("Enter a single digit: "))

        elif choice == PATTERN1_CHOICE:
            patterns.pattern1(digit)
        elif choice == PATTERN2_CHOICE:
            patterns.pattern2(digit)
        elif choice == PATTERN3_CHOICE:
            patterns.pattern3(digit)
        elif choice == PATTERN4_CHOICE:
            patterns.pattern4(digit)
        elif choice == PATTERN5_CHOICE:
            patterns.pattern5(digit)
        elif choice == PATTERN6_CHOICE:
            patterns.pattern6(digit)
        elif choice == ALL_PATTERNS_CHOICE:
            patterns.pattern1(digit)
            patterns.pattern2(digit)
            patterns.pattern3(digit)
            patterns.pattern4(digit)
            patterns.pattern5(digit)
            patterns.pattern6(digit)
           
        elif choice == QUIT_CHOICE:
            print('Exiting the program...')
        else:
            print('Error: invalid selection.')
    
# The display_menu function displays a menu.
def display_menu():
    print('\n\n\n        MENU')
    print('1) Pattern I')
    print('2) Pattern II')
    print('3) Pattern III')
    print('4) Pattern IV')
    print('5) Pattern V')
    print('6) Pattern VI')
    print('7) All Patterns')
    print('8) Enter a Single Digit')
    print('0) Quit')

#End of display_menu function.
main()
