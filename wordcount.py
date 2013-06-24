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
words_in_text = file_content.split(' ')

# count words line by line in the filetext
# for line in file_text:
# 	words_in_line = line.split(' ')
for word in words_in_text:
	word = word.strip(string.punctuation)
	word = word.strip(string.whitespace)
	if word != '':
		word = word.lower()
		if word_count.has_key(word):
			word_count[word] += 1
		else:
			word_count[word] = 1

# display words with sorting by value and alphabetically
word_count_sorted = sorted(word_count.iteritems(), key= lambda word: (word[1], word[0]))


for word, count in word_count_sorted:
	print "The word %s occurs %d times." % (word, count)


