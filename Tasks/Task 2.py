def title_case(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

input_sentence = "hello world"
output_sentence = title_case(input_sentence)
print(output_sentence)
