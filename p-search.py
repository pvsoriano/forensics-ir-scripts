import sys

searchWords = set()

# open file with word list
try:
	fileWords = open('wordlist.txt')
	for line in fileWords:
		searchWords.add(line.strip())
except:
	print("File handling error.")
	sys.exit()

print(searchWords)

if('kryptonie' in searchWords):
	print("Found word)"
else:
	print ("Not found")
