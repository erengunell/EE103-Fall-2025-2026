increment = 0.01
epsilon = 0.1
x = 15
guess = 0.0

while (guess**2) < x:
    guess += increment
if abs(guess**2-x) < epsilon:
        print("Square root of", str(x), "is approximately", str(guess))
else:
    print(str(x), "is not a perfect square")








