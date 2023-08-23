def reverse_words(sentence):
    return ' '.join(word[::-1] for word in sentence.split())

input_sentence = "Hello World"
output_sentence = reverse_words(input_sentence)
print(output_sentence)
