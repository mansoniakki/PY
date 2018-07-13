import math
x = math.pi
print(x)

print(round(x , 4))
pos_inf = float(8)
print(pos_inf)

print ('######Using Bool Function######')
f = 1
print(bool(x))
y = 0
print(bool(y))
m= 'None'
print(bool(m))

if not None:
    print ('None is False')

print('True or False Returns: ', True or False)
print('1 or 0 returns: ', 0 or 0 or 0.00)
print ('1 or 0 returns', 0  or 1)

print('True AND False returns: ', True and False)
print('True and False returns ', 0 and 1)
print('None and 0 returns: ', None and 0)

str1 = 'It\'s Me'
print(str1)
str2 = 'col1\tcol2\tcol3'
print(str2)
str3 = 'col1\ncol2\ncol3'
print(str3)
str4="it's me"
print(str4)
str5 = 'He is "abc"'
print (str5)

compstr='Hii am not in India'
subtext = 'India'
print(subtext in compstr)
print(compstr.count('I'))
print(compstr.index('I',4,18))

csv = 'a,b,c,d'
str8='fjskfskfjsk fjskdfs'
csvsplit = csv.split(",")
print(str8.isalpha())

bytes_l = b'Copyright \xc2\xa9'
print (bytes_l)
print(bytes_l.decode())
print(bytes_l.decode("utf-8"))
print(bytes_l.decode("utf-16"))
b_from_hex = bytes.fromhex('54 72')
print (b_from_hex)