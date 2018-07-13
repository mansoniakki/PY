print("Excercize 27\n")

people = 20
cat = 30
dogs = 15

if people < cat:
	print("There are too many cats, world is doomed")

if people > cat:
	print("There are fewer cats, world is saved")

if people < dogs:
	print("There are too many dogs, world is drooled")

if people > dogs:
	print("The world is dry")

print("Excercize 27\n")

if people < cat:
	print("There are too many cats, world is doomed")
else:
	print("There are fewer cats, world is saved")

if people < dogs:
	print("There are too many dogs, world is drooled")
else:
	print("The world is dry")

print("\nUsing Elif\n")

if people < cat:
	print("There are too many cats, world is doomed")
elif people > cat:
	print("There are fewer cats, world is saved")
else:
	print("Cant Decide")
