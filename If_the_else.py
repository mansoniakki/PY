print("###############using if then else################")
age=17
if age > 17:
    print("You can bye liquer")
else:
    print("You can not buy liquer")

score=85
print('The grade was: ',end=' ')
if score < 60:
    print('F')
elif 60 <= score <70:
    print('D')
elif 70 <= score < 79:
    print('C')
elif 80 <= score < 90:
    print('B')
elif 90 <= score <=100:
    print('A')
else:
    print("Impossible!")

print("using debug to debug the code")

debug = True
if debug: print("Score was: ",score)