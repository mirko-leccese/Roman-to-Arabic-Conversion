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

test_roman = 'CMIV'

#value = dict_roman[test_roman[-1]]
#print(value)

#arabic = value
#for i in reversed(test_roman[:-1]):
#    value_next = dict_roman[i]
#    if value_next < value:
#        arabic -= value_next
#    else:
#        arabic += value_next
#    
#    value = value_next

#print(arabic)


values = [ dict_roman[roman_char] if i == 0 or dict_roman[test_roman[i-1]] <= dict_roman[roman_char]  
    else -dict_roman[roman_char] for i, roman_char in enumerate(reversed(test_roman))]

print(values)