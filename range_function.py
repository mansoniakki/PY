print("##################Using Range Function#################")
a_range=range(5)
print("a_range ", a_range)
a_list=list(a_range)
print("a_list ",a_list)

for i in range(10):
    print(i, end=' ')
print()

a_range=range(10, 16)
print("a_list(range) ",list(a_range))
a_range=range(10, -1, -1)
print("a_list(range) ",list(a_range))
