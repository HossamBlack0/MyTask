def replace_vowels_with_counts(input_string):
    vowels = "aeiouAEIOU"
    count = 1
    return ''.join(str(count) if char in vowels and (count := count + 1)
                   else char for char in input_string)

input_string = "hello world"
output_string = replace_vowels_with_counts(input_string)
print(output_string)
