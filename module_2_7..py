def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if first != 0 and len(str(number)) >= 2:
        return first * get_multiplied_digits(int(str_number[1:]))
    elif first == 0 and len(str(number)) >= 2:
        third = int(str_number[2])
        return third * get_multiplied_digits(int(str_number[3:]))
    else:
        return first
result = get_multiplied_digits(0.31352)
print(result)
