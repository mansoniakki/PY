print("Here are the ten things:")
ten_things="Ball Apple Cat Car House Lamb"
print("Ten Things are - ", ten_things)

print("Wait there are no ten things listed, Let's fix it")
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
while len(stuff) != 10:
	next_item = more_stuff.pop()
	print("Adding: ", next_item)
	stuff.append(next_item)
	print("There's %d items now" % len(stuff))
print("There we go: ", stuff)

print(stuff[0])
print(stuff[1])
print(stuff[-1])
print(stuff.pop())

print("There we go: ", stuff)

print(' '.join(stuff))

print('#'.join(stuff[3:6]))