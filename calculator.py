#!/usr/bin/env python3
# Created by: Minab Berhane
# Created on: Dec 8, 2021
# This program asks the user for three
# parameters: an operation and two numbers.
# It then calculates the results using a separate
# function.


# calculates the result of two numbers
def calculate(sign, first_num, second_num):

    if sign == '/':
        result = first_num / second_num
    elif sign == '*':
        result = first_num * second_num
    elif sign == '%':
        result = first_num % second_num
    elif sign == '+':
        result = first_num + second_num
    else:
        result = first_num - second_num
    return result


# checks for invalid input and calls
# function to determine result of two numbers
def main():

    # displays opening message
    print("This program will perform calculations between two numbers!")
    print("")

    # gets operation from user
    sign_user = input("Enter the operation you want to perform "
                      "(-, *, %, /, +): ")

    # checks if invalid operator is entered
    if sign_user == '-' or sign_user == '%' or sign_user == '*' \
       or sign_user == '/' or sign_user == '+':
        # gets first number from user
        first_num_string = input("Enter the first number: ")

        try:
            # converts input value to float
            first_num_float = float(first_num_string)

            # gets second number from user
            second_num_string = input("Enter the second number: ")

            try:
                # converts input values to float
                second_num_float = float(second_num_string)

                # assigns variable to function call that gives return value
                result_user = calculate(sign_user,
                                        first_num_float, second_num_float)

                # display results to user
                print("The result of {} {} {} is {}"
                      .format(first_num_float, sign_user,
                              second_num_float, result_user))

            # catches any entered strings
            except Exception:
                print("{} is not a valid number." .format(second_num_string))

        # catches any entered strings
        except Exception:
            print("{} is not a valid number." .format(first_num_string))

    else:
        print("Error. {} is not a recognized operation." .format(sign_user))


if __name__ == "__main__":
    main()