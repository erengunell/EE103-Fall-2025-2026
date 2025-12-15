def create_student(name, age):
    return (name, age)

def describe_student(student_tuple):
    name = student_tuple[0]
    age = student_tuple[1]
    return f"Student {name} is {age} years old."

user_name = input("Enter student name: ")
user_age = int(input("Enter student age: "))
my_student_tuple = create_student(user_name, user_age)
result_string = describe_student(my_student_tuple)
print(result_string)