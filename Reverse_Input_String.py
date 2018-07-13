print("##################This script with reverse the string input by user###########")
name=input("Please enter first and last name to reverse: ")
print("name: ", name)

words=name.split()
print("words: ", words)

for word in words:
    lastindex = len(word) -1
    print("lastindex ", lastindex)
    for index in range(lastindex, -1, -1):
        print(word[index], end='')
    print(end= ' ')
print(end='\n')
