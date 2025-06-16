def convert_to_float(my_string):
    sign_negative = my_string[0] == '-'

    if (my_string[0] == '-') or (my_string[0] == '+'):
        my_string = my_string[1:]

    if '.' in my_string:
        int_part, fractional_part = my_string.split('.')
    else:
        int_part, fractional_part = my_string, '0'
    

    int_value = convert_int_part(int_part)
    fractional_value = convert_fractional_part(fractional_part)

    res = int_value + fractional_value

    if sign_negative:
        res = -res

    return res

def convert_int_part(int_part):
    int_value = 0

    for char in int_part:
        if char.isdigit():
            int_value = int_value * 10 + int(char)
        else:
            raise ValueError("Некорректные данные")
        
    return int_value
        
def convert_fractional_part(fractional_part):
    fractional_value = 0
    for i, char in enumerate(fractional_part):
        if char.isdigit():
            fractional_value += int(char) * (10 ** -(i + 1))
        else:
            raise ValueError("Некорректные данные")
        
    return fractional_value