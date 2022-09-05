#!/bin/python3

#import the code in string1.py

from stringlib import *
from worker import *
import sys

#Function to test the functions in the stringlib module
def testStringLib(inputStr):
    #Add code to call each of the functions and print the results
    print("Input string is", inputStr)
    reverse = reverseStr(inputStr)
    print("Reverse of string is", reverse)
    containApple = containsWord(inputStr, "apple")
    containBanana = containsWord(inputStr, "banana")
    print("Does string contain apple?", containApple)
    print("Does string contain banana?", containBanana)
    isP = isPalindrome(inputStr)
    print("Is string a palindrome?", isP)
    upCase = upperCaseStr(inputStr)
    print("Uppercase of string is", upCase)
    return

#Function to test the methods in the Worker class in the worker module
def testWorkerClass(inputStr):
    #Add code to create a Worker object
    print("Input string is", inputStr)
    w1 = Worker(inputStr) 
    #Use the object to call each of the methods in the Worker class
    #Print the result of each call
    print("Reverse of string is", w1.reverse())
    print("Does string contain apple?", w1.containsW("apple"))
    print("Does string contain banana?", w1.containsW("banana"))
    print("Is string a palindrome?", w1.palindrome())
    print("Uppercase of string is", w1.upperCase())
    return

#check to make sure there is a string command line argument
if (len(sys.argv) < 2):
    print("usage: driver1.py <string>")
else:
    #call the functions that test the library and the Worker class
    print("\nTest stringlib:")
    testStringLib(sys.argv[1])
    print("\nTest Worker class:")
    testWorkerClass(sys.argv[1])




