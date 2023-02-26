import numpy as np

dict_roman = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

def roman_to_arabic(roman_str):
    '''
    This function converts a roman number into an arabic number.

    Args:
        roman_str (str): string defining the roman number

    Returns:
        arabic (int): the corresponding arabic (decimal) number
    '''
    reversed_roman = roman_str[::-1]
    
    values = [ dict_roman[roman_char] if i == 0 or dict_roman[reversed_roman[i-1]] <= dict_roman[roman_char]  
        else -dict_roman[roman_char] for i, roman_char in enumerate(reversed_roman)]

    arabic = sum(values)

    return arabic

assert roman_to_arabic('CMIV') == 904
assert roman_to_arabic('DCCCXLIX') == 849
assert roman_to_arabic('MMMCMXCIX') == 3999

inp_roman = input('Please insert a Roman number: ')

print(f"Roman number: {inp_roman}       Arabic number: {roman_to_arabic(inp_roman)}")


