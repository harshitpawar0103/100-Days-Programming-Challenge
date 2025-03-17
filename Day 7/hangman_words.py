import nltk
import random as r
from nltk.corpus import words


word_list = words.words()


# for i in range(10):
# print(r.choice(word_list))

# count = 0
# for i in range(len(word_list)):
#     if len(word_list[i])>3:
#         pass
#     else :
#         count+=1

# print(count)

hn_words = [word.lower() for word in word_list if len(word)>3]
