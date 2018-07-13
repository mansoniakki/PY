print("Learning For Loop ")
for elem in range(5):
    print(elem, end=' ')
print()

print("using for loop with start and end parameters")
for elem in range(1, 6):
    print(elem, end=' ')
print()

print("using for loop with start, end and stepping parameter")
for elem in range(5, -1, -1):
    print('countdown: ', elem)
print()

print("using for loop in string")
for char in 'Mangal Singh':
    print(char, end=' ')
print()

print("using for loop with tuple")
for tup in (1,2,3):
    print(tup, end=' ')
print()

print("using for loop with list")
for val in ('Mangal', 'Kamal', 'Pawan'):
    print(val, end=' ')
print()

print("Using for loop with dictionary")
greek = {'alpha':1, 'beta':2, 'gamma':3}
for elem in greek:
    if elem=='beta':
        continue
    print(elem, greek[elem])

print("Using nested for loop -  finding prime number")
for outer in range(2, 10):
    for inner in range(2, outer):
        #print('outer: ', outer)
        #print('inner: ', inner)
        #print(not outer%inner)
        if not outer % inner:
            print(outer, '=', inner, '*', int(outer/ inner))
            break
    else:
        print(outer, 'is prime')

