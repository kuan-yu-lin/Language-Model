from corpus import tokenize, detokenize
from lm import LanguageModel

# create a new language model with a user-specified n
n = int(input('Which n-gram language model you want to build? Please enter an integer greater than 0 as n in n-gram. 1, 2, and 3 are the recommened. '))

gen_txt_len = int(input('What is the length of text you want to generate? Please enter an integer greater than 0.'))

lm = LanguageModel(n, gen_txt_len)

# Load texts from a file
filename = input('Which file you want to use to train the language model? Please enter the full file name. ')
with open(filename, 'r') as f:
    raw_file = f.read()
    tokens = tokenize(raw_file, n)

# Train the language model on those texts
lm.train(tokens)
print('The {}-gram language model is ready.'.format(n))

# Generate a text from the language model, and print it to the screen
gen_context = lm.generate()
gen_txt_first = gen_context[0]
print('This is the first word generated from the language model: {}'.format(gen_txt_first))

# Generate a user-specified number of texts from the language model
gen_txt = detokenize(gen_context)
print('This is the whole sentence generated from the language model: {}'.format(gen_txt))
# Write the text to a file
with open('lm_generation.txt', 'w') as f:
    f.write(gen_txt)
print('The texts are  saved in "lm_generation.txt". Go check it out!')

#Exit the program
quit()