# String Programs by Rahul Kumar

# 1. Program to input a string and print it
s = input("Enter a string: ")
print("You entered:", s)

# 2. Program to find length of a string
print("Length of the string:", len(s))

# 3. Program to print string in reverse
print("Reverse of the string:", s[::-1])

# 4. Program to check if string is palindrome
if s == s[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

# 5. Program to count vowels in a string
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Number of vowels in the string:", count)

# 6. Program to convert string into uppercase and lowercase
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())

# 7. Program to check if string contains only alphabets
if s.isalpha():
    print("The string contains only alphabets")
else:
    print("The string contains other characters also")
