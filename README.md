# Language Model

### University Stuttgart

### Programming Project, Winter 2021/22

## Author Information

* [Kuan-Yu Lin](https://github.com/kuan-yu-lin)

## Project Information

### Description

This is a n-gram Language Model that is designed and implemented in python. The language model learns from the provided training text, and then generates new text that is statistically similar to training text.

## Run

1. Run

    ```bash
        python3 main.py
    ```

2. Answer two questions:

    1. Define n for n-gram. Most common n-gram language model are 1-gram, 2-gram, and 3-gram. Number 1 to 3 are recommended.

        > Which n-gram language model you want to build? Please enter a number as n in n-gram.

    2. Define the length of text you want to generate.

        > What is the length of text you want to generate? Please enter an integer greater than 0.

3. The next question is to provide the file name of the data for training the language model. This data needs to be put in the same directory as main.py.

    > Which data you want to use to train the language model? Please enter the full file name.

4. The language model will start training. The following sentence will be printed to the screen if the language model is ready.

    > The _-gram language model is ready. (underlined space will be filled according to the n that you provided)

5. The language model finish generating all text. The first text will be printed with the following sentence.

    > This is the first text generate from the language model: _______. (underlined part will be fill according to the text that language model generated)

6. Then, the full text will be printed with the following sentence.

    > This are all the text generated from the language model: _______.(underlined part will be fill according to the text that language model generated)

7. The result is saved in the file, named “lm_generation.txt”. The following sentence
will be printed out.

    > The result is also saved in “lm_generation.txt”. Go check it out!

8. The program ends. It will automatically exit.
