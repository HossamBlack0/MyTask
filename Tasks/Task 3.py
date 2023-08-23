def encrypt_string(input_string):
    return ''.join(chr(ord(char) + 1) if char.isalpha()
                   else char for char in input_string)

input_string = "Hello, World!"
output_string = encrypt_string(input_string)
print(output_string)
