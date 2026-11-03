#Q1. Write a Python program to check if a number is even or odd.

num = int(input("enter a number:"))
if num % 2 ==0:
    print("even")
else:
    print("odd")


#Q2. Write a Python function to reverse a string.

def reverse_string(s):
    return s[::-1]

#Q3. How can you find the largest number in a list?

def find_largest (numbers):
    return max(numbers)

