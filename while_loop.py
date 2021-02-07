print("This will teach us about while loop in python")
ctr=3
while ctr > 0:
    print("Counting Down: ", ctr)
    ctr -= 1

names=['Tom', 'Mangal','Kamal', 'Shinaa','Rojana']
while names:
    print("first person to go: ", names.pop())

results = [1,1,0,1,1,0]
processed = 0
passed = 0
while results:
    processed +=1
    result=results.pop()
    if result:
       passed+=1
else:
    print('Processed', processed, 'Passed', passed)

