from nltk.util import ngrams
from collections import Counter
import random

class LanguageModel:
    def __init__(self, n = 3, gen_txt_len = 10):
        self.n = n
        # 'gen_txt_len' is the parameter for the user to specify the length of texts he/she wants the language model to generate. The default value is 10.
        self.gen_txt_len = gen_txt_len
        self.t_seq = list()
        self.ngram_dict = dict()

    def train(self, token_sequences):
        total_ngrams = list()
        total_fewer_ngrams = list()

        # Store the tokens for later usage. The tokens are from the text for training the language model.
        self.t_seq = token_sequences

        if self.n > 1:
            # For the calculation the probabilities of n-grams, the ngrams are store in the list named 'total_ngrams'. It can be used as numerator to count the n-gram probability.
            [total_ngrams.append(g) for g in ngrams(self.t_seq, self.n)]
            tn_counter = Counter(total_ngrams)

            # The (n-1)grams are store in the list named 'total_fewer_ngrams'. It can be used as denominator to count the n-gram probability.
            [total_fewer_ngrams.append(g) for g in ngrams(self.t_seq, self.n-1)]
            tfn_counter = Counter(total_fewer_ngrams)

            # Calculate the probabilities of n-grams. Store the ngrams and their probability in the dictionary call 'ngram_dict'. 
            for key in tn_counter:
                next_word_prob = tn_counter[key]/tfn_counter[key[:self.n-1]]
                self.ngram_dict[key] = next_word_prob
                # e.g. ('the', 'dog'): 0.25
                    
    def p_next(self, tokens):
        pre_next_dict = dict()

        # Find the prediction text and its probability with the parameter of p_next(). Store them in the dictionary called 'pre_next_dict'.
        for key, value in self.ngram_dict.items():
            if key[:len(tuple(tokens))] == tuple(tokens):
                pre_next_dict[key[-1]] = value

        return pre_next_dict
        # one of the dict: 'foolish': '0.00196'

    def sample(self, dicts):
        no_pad_dicts = dict()

        # accept the result from p_next(), and provide the next word
        for key, value in dicts.items():
            if key == '<s>':
                pass
            elif key == '</s>':
                pass
            else:
                no_pad_dicts[key] = value        

        max_val = max(no_pad_dicts.values())
        max_keys = [k for k in no_pad_dicts if no_pad_dicts[k] == max_val]
        next_word = random.choice(max_keys)

        return next_word

    def generate(self):
        ngram_list = list()
        prob_list = list()
        sent_begin = list()

        # build the ngrams and their frequencies
        ng = ngrams(self.t_seq, self.n)
        ngram_freq = Counter(ng)

        if self.n == 1:
            # generate the texts by unigram model
            for key, value in dict(ngram_freq).items():
                ngram_list.append(key[0])
                prob_list.append(value)
            result = random.choices(ngram_list, weights = prob_list, k = self.gen_txt_len)
        else:
            # generate the beginning of the sentence for ngram
            for i in range(self.n-1):
                sent_begin.append('<s>')

            # find ngrams for the beginning of the sentence and their probabilities for weighting the random.choices
            for key, value in self.ngram_dict.items():
                if key[:self.n-1] == tuple(sent_begin):
                    ngram_list.append(key)
                    prob_list.append(value)
            output = random.choices(ngram_list, weights = prob_list, k = 1)
            # e.g. output -> [('<s>', '<s>', 'well')]

            # when the user only want to generate 1 text with any n-gram(n>1) language model
            if self.gen_txt_len == 1:
                result = [next(iter(output))[-1]]
            # generate the rest of the texts
            else:
                context = list(output[0])
                p_next_token = context[-self.n+1:]
                while self.gen_txt_len > 1:
                    context.append(self.sample(self.p_next(p_next_token)))
                    # get rid of the pad(s) for beginning of the sentence
                    p_next_token = context[-self.n+1:]
                    self.gen_txt_len -= 1
                result = context[self.n-1:]

        return result
