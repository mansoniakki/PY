#Splitting the word
def splitword (myword):#
	sword= myword.split(' ')
	return sword

def sort_word(myword):
	return sorted(myword)

	
def print_first_and_last_word (myword):
	firstword=myword.pop(0)
	lastword=myword.pop(-1)
	print("First Word: ",firstword)
	print("Last Word: ",lastword)
	
word="I am the new head teacher of this school"
splittedword = splitword(word)
print(splittedword)
sorteddword= sort_word(splittedword)
print(sorteddword)

print_first_and_last_word(splittedword)
