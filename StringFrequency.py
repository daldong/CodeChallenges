'''
This is for string frequncy program.
There is an input file with txt format.
After reading the file, the words are counted by count function.
An regular expression is used to replace special characters to a space.
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
