
roman_numerals = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M',
}

def arabic_to_roman(number):
    """
    Function to convert Arabic numeral to Roman numeral using the dictionary.
    """
    result = ""
    for value in sorted(roman_numerals.keys(), reverse=True):
        while number >= value:
            result += roman_numerals[value]
            number -= value
    return result

# Take user input
user_input = input("Enter a number to translate to Roman numeral: ")

# Convert user input to integer
try:
    number = int(user_input)

    # If the number is not in the dictionary, convert it to Roman numeral
    if number in roman_numerals:
        result_roman = roman_numerals[number]
    else:
        result_roman = arabic_to_roman(number)

    print(f"The Roman numeral for {number} is: {result_roman}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
