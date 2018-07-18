print("Working with While Loop")
def call_loop(ulimit,incr):
	i = 0
	num = []
	while i < ulimit:
		print("At the top I is %d " %i)
		num.append(i)
		i = i + incr
		print("Number now", num)
		print("At the bottom I is %d " %i)
		print ("Numbers are:")
	for i in num:
		print(i)
print("Calling Function")
call_loop(20, 2)
		
