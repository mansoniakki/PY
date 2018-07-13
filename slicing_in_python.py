print("###################Learn slicing in python#############")
print("Slicing means accessing one or more element of a immutable sequence like tuple, string and bytes")
print("Slicing means accessing one or more element of a mutable sequence like lists and bytearrays")

a_tuple=('a','b',1,2,(3,4))
print("a_tuple: ",a_tuple)
a_string='immutable'
a_bytes=b'sequence'
a_list=[5,6,7,(4,5)]
print("a_list: ",a_list)
a_byte_array=bytearray(b'mutable')
print("Selecting data from sequences")
print("a_byte_array: ",a_byte_array)
print("a_tuple[0] -> ",a_tuple[0])
print("a_string[1] -> ",a_string[1])
print("a_bytes[3] ", a_bytes[3])
print("a_list[4] -> ",a_list[2])
print("a_byte_array[2] -> ",a_byte_array[2])
print("##############Print Negative Indexes##############")

print("a_tuple[-1] -> ",a_tuple[-1])
print("a_string[-2] -> ",a_string[-2])
print("a_bytes[-3] ", a_bytes[-3])
print("a_list[-2] -> ",a_list[-2])
print("a_byte_array[-3] -> ",a_byte_array[-3])

print("###############Sub Slicing##################")

print("a_list[0:2] -> ",a_list[0:2])
print("a_list[0:] -> ",a_list[0:])
print("a_list[:2] -> ",a_list[:2])
print("a_list[2:5] -> ",a_list[2:5])

print("######### - Referencing a list - #############")
list_ref=a_list
print("list_ref: ",list_ref)
print("######### - Change in main list will change referenced list as well - #############")
a_list.append(6)
print("a_list ",a_list)
print("list_ref: ",list_ref)

print("######### - Copying a list - #############")
list_copy=a_list[:]
print("list_copy: ",list_copy)
print("######### - Change in main list will not change copied list - #############")
a_list.append(8)
print("a_list: ", a_list)
print("list_copy after change: ",list_copy)

print("############Using third paramater in slicing############")
print("a_list[::2] ->", a_list[::2])


print("a_list[1:4:2] ->", a_list[1:4:2])
print("a_list[::-1]) -> ", a_list[::-1])
print("a_string: -> ",a_string)
print("a_string[::-1] -> ",a_string[::-1])

print("################Creating Slice Object ans using it#############")
a_slice = slice(3)
print("a_slice -> ",a_slice)
print("a_list[a_slice] ",a_list[a_slice])

a_slice = slice(1,5)
print("a_list -> ", a_list)
print("a_slice -> ",a_slice)
print("a_list[a_slice]) -> ",a_list[a_slice])

a_slice=slice(1,5,2)
print("a_slice -> ",a_slice)
print("a_list[a_slice]) -> ",a_list[a_slice])