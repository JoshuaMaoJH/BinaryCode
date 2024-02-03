# Version: 1.0
# Date: 2024/02/3
# Author: Joshua Mao
# Description: This program is used to convert string to binary code and binary code to string.


def convertString2binaryCode(string): # convert string to binary code
    binaryCode = '' # store the binary code
    for char in string: # loop through each character in the string
        binaryCode += format(ord(char), '08b') + ' ' # 08b means 8 bits binary code

    return binaryCode # return the binary code

def convertBinaryCode2string(binaryCode): # convert binary code to string
    string = '' # store the string
    binaryCode = binaryCode.split(' ') # split the binary code by space
    for code in binaryCode: # loop through each binary code
        if code != '': # if the binary code is not empty
            string += chr(int(code, 2)) # convert the binary code to integer and then to character

    return string # return the string

def main(): # main function
    convertType = input('1. To convert string to binary code.\n'
                         '2. To convert binary code to string.\n'
                         '3. Quit.\n'
                         'Please enter a number: ') # ask the user to enter a number
    if convertType == '1': # if the user wants to convert string to binary code
        string = input('Enter a string: ') # ask the user to enter a stringsd
        binaryCode = convertString2binaryCode(string) # convert the string to binary code
        print('Binary code:', binaryCode) # print the binary code
        print() # print a new line (for better readability)
    elif convertType == '2': # if the user wants to convert binary code to string
        binaryCode = input('Enter a binary code: ') # ask the user to enter a binary code
        string = convertBinaryCode2string(binaryCode) # convert the binary code to string
        print('String:', string) # print the string
        print() # print a new line (for better readability)
    elif convertType == '3': # if the user wants to quit
        print('Goodbye!') # print goodbye
        while True: pass # keep the console open
    else: # if the user enters an invalid number
        print('Invalid input, please enter a number.') # print invalid input
        print() # print a new line (for better readability)

if __name__ == '__main__': # if the script is being run
    while True: # loop forever
        main() # run the main function