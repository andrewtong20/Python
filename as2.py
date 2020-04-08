
# Andrew Tong
# Mr. Tomczak
# January 31, 2020
# AS2
#
# This program gives the user a menu of options (1-5) which repeats until the user quits (option 5).
# Option 1 will print an investment table compounded daily given an initial investment, number of years, and range of integer interest rates.
# Option 2 will print a multiplication table given a range of starting and ending values.
# Option 3 will print all prime numbers to an inputted integer.
# Option 4 will convert an input seconds into days, hours, minutes, and seconds.

import interest
import multiplicationTable
import sys
import primeGenerator
import timeConverter

def main():
    print("Hi, this is a program that will give you a menu of options.")
    print("First, it will print a table of investments compounded daily given an initial investment, number of years, and range of integer interest rates.")
    print("Second, it will ask for a range of starting and ending values and print a multiplication table.")
    print("Third, it will prompt for an integer and print out all prime numbers up to that integer.")
    print("Fourth, it will convert inputted seconds into days, hours, minutes, and seconds.")
    print()
    name=input("Alright, let's begin! What is your name?")
    #to address user
    print(name+", you are now entering the menu. The menu will repeat until you input option 5 to quit.")

    menu(name)

#creates menu, passing in the user's name
def menu(name):
    choice=0

    #the while loop is used to repeate the menu
    while (choice!="5"):
        print("Option 1: Investment table.")
        print("Option 2: Multiplication table.")
        print("Option 3: Prime number generator.")
        print("Option 4: Time conversion.")
        print("Option 5: Quit.")
        print("The table will repeat itself until you quit.")

        #all inputs are strings
        choice=input("Which option (1,2,3,4,5) do you want to choose? Please only enter these acceptable integer values.")
        #inputs are all strings so that all strings can be entered without breaking program, increases ELSE bounds check to check for any value
        if (choice=="1"):
            print(name+ ", you chose option 1, where you input an initial investment, lowest and highest \n integer interest rates, and the number of years invested to make a daily compound interest table.\nFormatting of the table will be off for large investments.")
            print("Please enter your initial investment.")
            initial=isFloat()

            #while to be an indefinite bounds check
            while (initial<=0):
                print("Your investment can only be a positive amount! Please enter again.")
                initial=isFloat()

            #no range bounds check for interest rates because user can enter any (even negative)
            print("Enter lowest integer interest rate (ex: 3% would be 3 not .03)")
            low=isInteger()
            print("Enter highest integer interest rate (ex: 9% would be 9 not .09)")
            high=isInteger()

            #upper bound cannot be lower than lower bound; while is indefinite loop
            while (high<=low):
                print("Your input was the same or lower than the lowest integer interest rate. \nPlease enter a higher integer interest rate.")
                high=isInteger()

            print("How many whole years will you invest?")
            MAXyear=isInteger()

            #realistic bounds restriction for time
            while (MAXyear<0):
                print("Time cannot be negative. Please enter the whole amount of years you will invest.")
                MAXyear=isInteger()

            #formatting of table will be off for large initial investments or large amount of years
            interest.interest(initial, low, high, MAXyear);


        elif (choice=="2"):
            print(name+", you chose Option 2, where you input a starting \n and ending integer values to construct a multiplication table.\n Formatting of the table will be off for large factors.")
            #instructions say integers only
            print("If you enter a higher starting value than ending value, they will be flipped automatically.")
            #because of this feature, starting does not have to be less than end and so I don't have that bounds check
            print("Enter your integer starting value.")
            start=isInteger()
            print("Enter your integer ending value.")
            end=isInteger()

            #formatting of table will be off for large factors
            multiplicationTable.multiplicationTable(start,end);


        elif (choice=="3"):
            print(name+", you chose Option 3, where you enter an integer to create a list of all prime numbers up to that integer.")

            print("Please enter your integer.")
            primeTarget=isInteger()

            #prime bounds check
            while (primeTarget<2):
                print("2 is the first prime number, so you have to enter an integer greater than 2. Please enter again")
                primeTarget=isInteger()

            #if the primeTarget is a prime number, will include that value
            sys.stdout.write("The prime numbers up to "+str(primeTarget)+" are ")

            primeGenerator.primeList(primeTarget)

        elif (choice=="4"):
            print(name+", you chose Option 4, where a time in seconds to convert to days, hours, minutes, and seconds.")
            print("Please enter a time in seconds (decimals allowed)")
            seconds=isFloat()

            #time can't be negative bounds check
            while (seconds<0):
                print("Time cannot be negative. Please enter your time as a positive value in seconds.")
                seconds=isFloat()

            timeConverter.time(seconds)

        elif(choice=="5"):
            print(name+", thank you for using this program!")

        else: #any input not from 1-5 (as strings) will be allowed
            print(name+", you did not enter an allowed value (1,2,3,4,5)! Please try again.")

#isInteger method for bounds check that the user entered an integer
def isInteger():#https://pynative.com/python-check-user-input-is-number-or-string/
  while True:
    num = input("Input:")
    try:
        val = int(num)
        return val
    except ValueError:
        print ("This is not an integer number. Please enter a valid number")

#for bounds check that user entered a float number
def isFloat():#https://pynative.com/python-check-user-input-is-number-or-string/
  while True:
    num = input("Input:")
    try:
        val = float(num)
        return val
    except ValueError:
        print ("This is not a number. Please enter a valid number")

#run
main()
