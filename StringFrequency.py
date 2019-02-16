'''
This is for string frequncy program.
There is a input data and count the word in the input file.
Some special characters are replaced by a space with regular expression in this code.
'''
import re
def replaceText(text):
    # regular expression is used. Special characters are replaced by a space.
    finalText = re.sub('[\,\.\(\)\[\]\#\?\'\"\:\;\^]', ' ', text).split()
    return finalText

def wordCount(inputFile):
    with open(inputFile, 'r') as file:
        text = file.read()
    wordAll = replaceText(text)
    wordDic = list(set(wordAll))
    wordCount = []
    for word in wordDic:
        wordCount.append((wordAll.count(word), word))
    for result in sorted(wordCount, reverse=True):
        print(result[0], ": ", result[1])
        file.close()

wordCount('input.txt')
