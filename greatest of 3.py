#using python
#using chat gpt
numbers = [4, 12, 7, 3, 9]
greatest = numbers[0]

for number in numbers:
    if number > greatest:
        greatest = number

print("The greatest number is:", greatest)

