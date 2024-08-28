#using python
#using chat gpt
# Method 2: Using a loop
numbers = [4, 12, 7, 3, 9]

# Assume the first number is the greatest
greatest = numbers[0]

# Loop through the numbers
for number in numbers:
    if number > greatest:
        greatest = number

# Print the result
print("The greatest number is:", greatest)
#
