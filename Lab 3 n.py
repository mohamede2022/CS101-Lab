#printing the welcome to the user
print('Welcome to the Flarsheim Guesser!')
print()
#assigns the user choice to Y and N
user_choice = 'Y' or 'N'
#creating a while loop that runs the itteration if the user choice is Y (to continue)
while user_choice =='Y':
    #asks the user to think of a number between and including 1-100
    print('please think of a number between and including 1 and 100.')
    print()
    #asks the user for the remainder of the number if divided by 3 and assigns it to a variable
    three_remainder= int(input('What is the remainder when your number is divided by 3?'))
    #checks if the remainder divided by 3 is a negative number
    if three_remainder < 0:
        print('The value entered must be 0 or greater')
        #asks the user again for the remainder divided by 3 since it was divided by 3
        three_remainder= int(input('What is the remainder when your number is divided by 3?'))
    #checks if the remainder divided by 3 is greater than or equal to 3
    elif three_remainder >= 3:
        print('The value entered must be less than 3')
        #asks the user again for the remainder divided by 3 since it was greater than 3
        three_remainder= int(input('What is the remainder when your number is divided by 3?'))
        #asks the user for the remainder of the number if divided by 5 and assigns it to a variable
    five_remainder = int(input('What is the remainder when your number is divided by 5?'))
    #checks if the remainder divided by 5 is a negative number
    if five_remainder < 0:
        print('The value entered must be 0 or greater')
        #asks the user again for the remainder divided by 5 since it was negative number
        five_remainder= int(input('What is the remainder when your number is divided by 5?'))
    #checks if the remainder divided by 5 is greater than or equal to 5
    elif five_remainder >= 5:
        print('The value entered must be less than 5')
        #asks the user again for the remainder divided by 5 since it was greater than 5
        five_remainder= int(input('What is the remainder when your number is divided by 5?'))
        #asks  the user for the remainder of the number if divided by 7 and assigns it to a variable
    seven_remainder = int(input('What is the remainder when your number is divided by 7?'))
    #checks if the remainder divided by 7 is a negative number
    if seven_remainder < 0:
        print('The value entered must be 0 or greater')
        #asks the user again for the remainder divided by 7 since it was a negative number
        seven_remainder= int(input('What is the remainder when your number is divided by 7?'))
    #checks if the remainder divided by 7 is greater than or equal to 7
    elif seven_remainder >= 7:
        print('The value entered must be less than 7')
        #asks the user again for the remainder divided by 7 since it was greater than 7
        seven_remainder= int(input('What is the remainder when your number is divided by 7?'))
        #creats a for loop for the numbers range 1-100 and checks what number in that range is divisible by 3,5 and 7 and then print it 
    for i in range (1,101):
        if (i%3 == three_remainder and i%5 == five_remainder and i%7 == seven_remainder):
                         print('Your number was', i)
    print('How amazing is that?')
    #asks the user if he/she wants to play again or not and assigns the two Letters Y(Continue) and N(Quit)
    user_choice = input('Do you want to play again? Y to continue, N to quit')
    #creates an if statement to quit the loop if the user enters N
    if user_choice == 'N':
        break
