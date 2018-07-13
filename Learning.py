#If Elif
print("############learning if elif################")
name="mal"
if name is "mangal":
    print("hey mangal")
elif name is "kamal":
    print ("hey kamal")
else:
    print("hey None")

print("############for loop################")
foods=['bacon','tuna', 'ham', 'beef']
print(foods)
for f in foods[0:2]:
    print(f)
    print("length is:", len(f))

print("##########Range with one number - 0 to n ################")
for x in range(10):
    print("Range index is:", x)
print("################Range with two numbers - n1 to n2############")
for y in range(5, 10):
    print("Range2 index is:",y)
print("################Range with three numbers - n1 to n2 with n3 increments#########")#
for z in range(10,40,5):
    print("Range3 index is:",z)
print("#####While Loop####")
level=1
while level < 10:
    print ("level is:",level)
    level+=1
print("########Using Breaks#########")
magicNumber=26
for i in range(101):
    if i is magicNumber:
        print("Found MagicNumber which is:",i)
        break
    else:
        print("still finding")

print("########Multiple of 4#############")
for i in range(41):
    if i%4 is 0:
        print(i, "is multiple of 4")
    else:
         print(i)
print("###############using continue##############")
numbersTaken=[2,5,22,33,44,7]
print("here are the numbers that still available")
for i in range(1, 45):
    if i in numbersTaken:
        continue
    print(i, "is available")

print("#########using functions#############")
def myfun():
    print("This is m first function")
#Calling function
myfun()

def bitcoin_to_usd(btc, usd):
    amount=btc * 527
    usdamount=usd*100
    print ("amount in USD is ",amount)
    print ("USD amount is ",usdamount)
#Call function now
bitcoin_to_usd(4.5,7.6)

print("###########using function with return value###############")
def allowed_dating_age(my_age):
    girls_age = (my_age /2) + 7
    return girls_age

MyLimit=allowed_dating_age(27)
print("I can date girls with age ",MyLimit," or older")


print("################default values for arguments#################")
def get_gender(sex='Unknown'):
    if sex is 'm':
        print ("Male")
    elif sex is 'f':
        print ("Female")
    else:
        print(sex)

get_gender('m')
get_gender()

print("##########Calling function argument by name###########")
def print_arg(name='Mangal',action='played',item='Cricket'):
    print(name,action,item)

print_arg()
print_arg(name='Kamal')
print_arg(item='football',name='Peter',action='love')

print("#################Function with flexible number of arguments##############")

def flex_num(*args):
    total=0
    for i in args:
        total += i

    print("total is: ",total)

flex_num(4)
flex_num(5,6,7,8)
flex_num(10,20,30)

print("################Unpacking Arguments###################")
def check_my_bmi(name,age,weight,height):
    bmi=(weight/height)/height
    print ("BMI of ",name, " is ",bmi)


my_list=['Mangal',36,74,1.7]
check_my_bmi(my_list[0],my_list[1],my_list[2],my_list[3])
print("#############Now calling function by unpacking variable#########")
check_my_bmi(*my_list)

print("################Sets################")
groceries = {'milk','fruits','beer','chocolate','duct tape','milk'}
print(groceries)

if 'milk' in groceries:
    print("you already have milk")
else:
    print("You need milk hon!")

print("#############Using Dictionary#######################")
print("Dictionaries are pre-defined keys and their values")
mydict = {'Ellie':' Very Naughty','Yuvi':' Amazing Boy','Soni':' Lovely'}
print(mydict)
print(mydict['Ellie'])

for k,v in mydict.items():
    print(k + v)

print("###########Using Modules##############")
print("######Create one function in another py file :MyModules, and import the module in this file like given below")
import MyModules
MyModules.leftover()
import random
x = random.randrange(1, 10)
print(x)



