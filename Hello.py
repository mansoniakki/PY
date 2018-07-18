########################################
# Test Script Modified ini Future Branch
########################################
str="Hello World! Future"
print("String is: %s" %str)
##
print("String Length is: %d" %len(str))
x=2
print("X is: %s" %(x==2))
##
if (x==3):
    print("X is equal to 2")
else:
    print("X is not equal to 2")
##
mlist=[1,2,3]
print("list 1st item: %s" %mlist[0])
print("list 1st item: %s" %mlist[1])
print("list 1st item: %s" %mlist[2])
print("Length of list: %d" %len(mlist))
if mlist:
    print(mlist)
##
number = 16
second_number = False
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")

#Loops
primes = [2,3,5,7]
for prime in primes:
    print(prime) 
##Printing Range using Range
# Prints out the numbers 0,1,2,3,4
print("--------")
for x in range(5):
    print(x)
# Prints out the numbers between 3 to 6
print("--------")
for x in range(3,6):
    print(x)
	
# Prints out the numbers between 3, 5, 7
print("--------")	
for x in range(3,10,2):
    print(x)
#While Loops
print("While Loops--------")	
count=0
while count < 5:
    print("Count is %d" %count)
    count += 1
	
	
#Using Breaks
cnt=0
while True:
    print(cnt)
    cnt += 1
    if cnt >= 5:
	    break

#Using continue , Print Odd numbers
for x in range(10):
    if x % 2 == 0:
	    continue
    print("X is %d" %x)	
	
#Using Else clause in loops
ctr=0
while (ctr <= 5):
    print("ctr is: %d" %ctr)
    ctr+=1
else:
    print("count value reached %d" %(ctr))
	
#Excercise, Print only Even number and dont print any number after 237
numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527]	
for n in numbers:
    if n % 2 == 0:
	    print ("Printing Even Number %d" %n)
    if n == 237:
	    print ("Printing Even Number %d" %n)
	    break
