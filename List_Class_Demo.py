print("##############Demo of Python List Class#############")
empty_list = list()
print("empty_list", empty_list)

list_str = list("hello")
print ("list_str", list_str)

my_list = ['man', 'Kam', 5, 4]
print (my_list)

print("man in my_list: ",'man' in my_list)

print("liam in my_list", 'liam' in my_list)

print("1 not in my_list", 1 not in my_list)

empty_list.append(6)
print("empty_list: ", empty_list)

empty_list.append(6)
print("empty_list: ", empty_list)


empty_list.append(8)
print("empty_list: ", empty_list)

print("###Removing Item from List#############")
last_ele = empty_list.pop()
print("Last Element Removed: ", last_ele)
print("empty_list: ", empty_list)

print("####Impact of append and extend function on list")

empty_list.append([8,9])
print("empty list after append: ",empty_list)

last_ele=empty_list.pop()
print(last_ele)
print(empty_list)

empty_list.extend([8,9])
print("empty list after extend: ",empty_list)

print("#####Removing first element#########")
first_elem=empty_list.pop(0)
print("First Element: ", first_elem)

print("empty_list: ", empty_list)

print("Insert with index position")
empty_list.insert(0, 10)
print("empty_list: ", empty_list)

empty_list.insert(3, 10)

print("empty_list: ", empty_list)

print("Remove also removes but with value")

empty_list.remove(9)

print("empty_list: ", empty_list)

char_list=list("HELLO")
print("Char_List: ", char_list)

print("Min(char_list): ", min(char_list))

print("Max(char_list): ", max(char_list))

print("Sorted (char_list): ", sorted(char_list))
print(list_str)
list_str.sort()
print(" Sorted List 1: ", list_str)

print("list length: ",len(list_str))


