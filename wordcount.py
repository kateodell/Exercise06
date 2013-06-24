# Word Count (Exercise 06)
import operator
from sys import argv
import string

# open, read, and put file into list where each element is delineated by a 'space'
# or period

script, filename = argv

file_text = open(filename)
file_content = file_text.read()

# initialize a dictionary
word_count = {}
words_in_text = file_content.split()


for word in words_in_text:
	word = word.strip(string.punctuation)
	# word = word.strip('\r\n\t ')
	if word != '':
		word = word.lower()
		word_count[word] = word_count.get(word,0) + 1

# display words with sorting by value and alphabetically
word_count_sorted = sorted(word_count.iteritems(), key= lambda word: (word[1], word[0]), reverse = True)


for word, count in word_count_sorted:
	print "The word %s occurs %d times." % (word, count)


