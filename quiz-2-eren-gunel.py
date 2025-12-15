input_number = input("Enter a 5-digit integer number: ")

digit_sum = 0
for num in input_number:
    digit_sum += int(num)

print("Digit sum =", digit_sum)
if digit_sum % 2 == 0:
    print("The sum of digits is even.")
else:
    print("The sum of digits is odd.")     