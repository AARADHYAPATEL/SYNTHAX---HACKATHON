from googletrans import Translator


def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text


def to_binary(input_data):
    if isinstance(input_data, (int, float)):
        binary_representation = bin(int(input_data))[2:]
    elif isinstance(input_data, str):
        binary_representation = ' '.join(format(ord(char), '08b') for char in input_data)
    else:
        binary_representation = ' '.join(format(ord(char), '08b') for char in str(input_data))
    return binary_representation


def to_octal(input_data):
    if isinstance(input_data, (int, float)):
        octal_representation = oct(int(input_data))[2:]
    elif isinstance(input_data, str):
        octal_representation = ' '.join(format(ord(char), 'o') for char in input_data)
    else:
        octal_representation = ' '.join(format(ord(char), 'o') for char in str(input_data))
    return octal_representation


def to_hexadecimal(input_data):
    if isinstance(input_data, (int, float)):
        hexadecimal_representation = hex(int(input_data))[2:]
    elif isinstance(input_data, str):
        hexadecimal_representation = ' '.join(format(ord(char), 'x') for char in input_data)
    else:
        hexadecimal_representation = ' '.join(format(ord(char), 'x') for char in str(input_data))
    return hexadecimal_representation


def to_decimal(input_data):
    if isinstance(input_data, (int, float)):
        decimal_representation = int(input_data)
    elif isinstance(input_data, str):
        decimal_representation = ' '.join(format(ord(char)) for char in input_data)
    else:
        decimal_representation = ' '.join(format(ord(char)) for char in str(input_data))
    return decimal_representation


def from_binary(binary_input, target_representation):
    decimal_res = int(binary_input, 2)

    if target_representation == 'decimal':
        return decimal_res
    elif target_representation == 'hexadecimal':
        return hex(decimal_res)[2:]  # This is to remove the Ox prefix
    elif target_representation == 'octal':
        return oct(decimal_res)[2:]  # This is done to remove the Oo prefix
    elif target_representation == 'text':
        text_res = ''.join(chr(int(binary_input[i:i + 8], 2)) for i in range(0, len(binary_input), 8))
        return text_res


def from_hexadecimal(hex_number, target_representation):
    decimal_res = int(hex_number, 16)

    if target_representation == 'decimal':
        return decimal_res
    elif target_representation == 'octal':
        return oct(decimal_res)[2:]
    elif target_representation == 'binary':
        return bin(decimal_res)[2:]
    elif target_representation == 'text':
        text_res = ''.join(chr(int(hex_number[i:i + 2], 16)) for i in range(0, len(hex_number), 2))
        return text_res
    else:
        return f"No valid conversion available from hexadecimal to {target_representation}"


def from_octal(oct_number, target_representation):
    decimal_res = int(oct_number, 8)

    if target_representation == 'decimal':
        return decimal_res
    elif target_representation == 'binary':
        return bin(decimal_res)[2:]
    elif target_representation == 'text':
        text_res = ''.join(chr(int(oct_number[i:i + 2], 8)) for i in range(0, len(oct_number), 2))
        return text_res
    elif target_representation == 'hexadecimal':
        return hex(decimal_res)[2:]  # This is to remove the Ox prefix


def binary_addition(bin_num1, bin_num2):
    max_length = max(len(bin_num1), len(bin_num2))
    bin_num1 = bin_num1.zfill(max_length)
    bin_num2 = bin_num2.zfill(max_length)

    carry_over = 0
    res = ""

    for bit1, bit2 in zip(reversed(bin_num1), reversed(bin_num2)):
        sum_bits = int(bit1) + int(bit2) + carry_over

        res = str(sum_bits % 2) + res
        carry_over = sum_bits // 2

    if carry_over:
        res = str(carry_over) + res

    return res


binary_number1 = input("Enter the first binary number.")
binary_number2 = input("Enter the second binary number.")

sum_res = binary_addition(binary_number1, binary_number2)
print(f"The sum of {binary_number1} and {binary_number2} is equal to: {sum_res}")


def binary_subtraction(bin_num1, bin_num2):
    max_length = max(len(bin_num1), len(bin_num2))
    bin_num1 = bin_num1.zfill(max_length)
    bin_num2 = bin_num2.zfill(max_length)

    res = ""
    borrow = 0

    for bit1, bit2 in zip(reversed(bin_num1), reversed(bin_num2)):
        sub_bits = int(bit1) - int(bit2) - borrow

        if sub_bits < 0:
            sub_bits += 2
            borrow = 1
        else:
            borrow = 0

        res = str(sub_bits) + res

        return res


def binary_multiplication(bin_num1, bin_num2):
    prod = "0"

    for bit2 in reversed(bin_num1):
        if bit2 == '1':
            prod = binary_addition(prod, bin_num1)

        bin_num1 += "0"

    return prod


def binary_division(dividend, divisor):
    quotient = "0"
    rem = dividend

    while len(rem) >= len(divisor):
        temp_res = binary_subtraction(rem, divisor)

        if temp_res[0] != '1':
            quotient = binary_addition(quotient, '1')
            rem = temp_res
        else:
            quotient = binary_addition(quotient, '0')

        divisor += '0'

    return quotient, rem





while True:

    data_input = input(
        "Enter a number, text, or any data (Type 'binary' to skip to binary conversion type 'exit' to "
        "quit): ")

    if data_input.lower() == 'exit':
        print("Thank you for using me!")
        break

    if data_input.lower() == 'binary':
        binary_input = input("Enter a binary Number: ")
        target_representation = input("Enter the target representation(binary, octal, hexadecimal and text): ")

        conversion_res = from_binary(binary_input, target_representation)
        print(f"The conversion of '{binary_input}' to {target_representation} is : {conversion_res}")

    elif data_input.lower() == 'addition':
        binary_input1 = input("Enter the first binary number: ")
        binary_input2 = input("Enter the second binary number: ")

        # This line is to perform the binary addition
        sum_res = binary_addition(binary_number1, binary_number2)
        print(f"The binary addition of {binary_input1} and {binary_number2} = {sum_res}")

    elif data_input.lower() == 'subtraction':
        binary_input1 = input("Enter the first binary number: ")
        binary_input2 = input("Enter the second binary number: ")

        # This line performs the binary subtraction
        diff_res = binary_subtraction(binary_number1, binary_number2)
        print(f"The binary subtraction of {binary_input1} and {binary_input2} = {diff_res}")

    elif data_input.lower() == 'product':
        binary_input1 = input("Enter the first binary number: ")
        binary_input2 = input("Enter the second binary number: ")

        # This line of code performs the binary multiplication.
        prod_res = binary_multiplication(binary_number1, binary_number2)
        print(f"The binary multiplication of {binary_input1} and {binary_input2} = {prod_res}")

    elif data_input.lower() == 'divide':
        binary_input1 = input("Enter the first binary number: ")
        binary_input2 = input("Enter the second binary number: ")

        # This line of code performs the binary division
        quotient_res, rem_res = binary_division(binary_input1, binary_input2)
        print(f"The binary division of {binary_input1} and {binary_input2} = Quotient = {quotient_res} remainder = {rem_res}")

    elif data_input.lower() == 'hexadecimal':
        hex_input = input("Enter a hexadecimal value: ")
        target_representation = input("Enter the target representation(binary, octal, decimal or text):")

        conversion_res = from_hexadecimal(hex_input, target_representation)
        print(f"The conversion of {hex_input} to {target_representation} is : {conversion_res}")

    elif data_input.lower() == "octal":
        oct_input = input("Enter a Octal value: ")
        target_representation = input("Enter the target representation(binary, hexadecimal, decimal or text): ")

        conversion_res = from_octal(oct_input, target_representation)
        print(f"The conversion of {hex_input} to {target_representation} is : {conversion_res}")

    else:
        binary_result = to_binary(data_input)
        octal_result = to_octal(data_input)
        hexadecimal_result = to_hexadecimal(data_input)
        decimal_result = to_decimal(data_input)

        print(f"The binary representation of '{data_input}' is: {binary_result}")
        print(f"The octal representation of '{data_input}' is: {octal_result}")
        print(f"The hexadecimal representation of '{data_input}' is: {hexadecimal_result}")
        print(f"The decimal representation of '{data_input}' is: {decimal_result}")

    language_input = input("Enter a word to translate (or 'skip' to continue without translation): ")
    if language_input.lower() != 'skip':
        target_language = input("Enter a target language (e.g., 'es' for Spanish): ")
        translation_result = translate_text(language_input, target_language)
        print(f"The translation of '{language_input}' to '{target_language}' is: {translation_result}")
# hi, kn, ta, ta, ur, ml, ml, bn, sd, sa,	pa, or, gu, bho, as
