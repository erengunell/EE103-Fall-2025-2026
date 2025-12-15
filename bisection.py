x = 100
epsilon = 0.01
num_guesses = 0
low = 0.0
high = x
guess = (high + low) / 2

while abs(guess**2 - x) >= epsilon:
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2
    num_guesses += 1
print("Square root of", str(x), "is approximately", str(guess))
print("Number of guesses:", num_guesses)