from text_tools import to_uppercase, to_titlecase

user_sentence = input("Enter a sentence: ")

print(f"Uppercase version: {to_uppercase(user_sentence)}")
print(f"Titlecase version: {to_titlecase(user_sentence)}")
print("Formatting completed successfully.")