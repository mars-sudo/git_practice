import word_count as wc

filenames =['descartes.txt','siddhartha.txt','alice.txt',]
for filename in filenames:
#    with open(filename, encoding='utf-8'):
        wc.count_words(filename)