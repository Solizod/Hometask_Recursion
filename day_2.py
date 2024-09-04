# write a python programm to calculate the sum of a list of numbers using recusion



# def numbers(nums):
#     if not nums:
#         return 0
#     else:
#         return nums[0] + numbers(nums[1:])

# nums = [1, 2, 3, 4, 5]
# print(numbers(nums))

# ______________________________________________________________________________
# . Write a Python program to convert an integer to a string in any base using recursion.



# def base_input (n, base):
#     digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
#     if n < base:
#         return digits[n]
#     return base_input(n // base, base) + digits[n % base]

# n = 42
# base = 2
# print(base_input(n, base))

# ___________________________________________________________________________________

# 6. Write a Python program to get the sum of a non-negative integer using recursion.

# Test Data:

# sumDigits(345) -> 12

# sumDigits(45) -> 9


# def sumDigits(n):
#     if n == 0:
#         return 0
#     return n % 10 + sumDigits(n // 10)

# print(sumDigits(345))
# print(sumDigits(45))

# ___________________________________________________________________________________

# 7. Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0) using recursion.

# Test Data:

# sum_series(6) -> 12

# sum_series(10) -> 30


# def sum_series(n):
#     if n <= 0:
#         return 0
#     return n + sum_series(n - 2)

# print(sum_series(6))
# print(sum_series(10))


# _________________________________________________________________________________________

# 10. Write a Python program to calculate the value of 'a' to the power of 'b' using recursion.

# Test Data:

# (power(3,4) -> 81




# def power(a, b):
#     if b == 0:
#         return 1
#     return a * power(a, b - 1)

# print(power(3, 4))

# ____________________________________________________________________________________________

# . Write a Python program to find the greatest common divisor (GCD) of two integers using recursion.




# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)

# print(gcd(48, 18))



