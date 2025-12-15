def is_even_odd(input_number):
    if input_number % 2 == 0:
        return "even"
    else:
        return "odd"
    
def calc_sum(input_number_1, input_number_2):
    return input_number_1 + input_number_2

def sum_message(input_number_1, input_number_2):
    total = calc_sum(input_number_1, input_number_2)
    
    sum_status = is_even_odd(total)
    
    return f"Sum of {input_number_1} and {input_number_2} is {total}, and the sum is {sum_status}."
    