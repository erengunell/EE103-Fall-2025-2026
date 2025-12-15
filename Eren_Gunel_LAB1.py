name = input("Enter a name: ")
number = input("Enter a number: ")

even_sum = 0
for digit in number:
    if int(digit) % 2 == 0:
        even_sum += int(digit)

print("Sum of even digits:", even_sum)

last_digit = even_sum % 10
print("Last digit of the sum is:", last_digit)

for i in range(last_digit):
    print(name)

