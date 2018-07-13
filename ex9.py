x="There are %d type of people" % 10
binary = 'binary'
do_not = "don't"
y="Those who know %s and those who %s" % (binary, do_not)

print (x)
print (y)

print("I said %r " % x)

print (x +". "+ y)

formatter = "%r %r %r %r"
print(formatter % (1,2,3,4))
print("Jan\nFeb\nMar")

print("I am 6'2\" tall")
print('I am 6\'2" tall ')

print("\t\t I am tabbed in")

#while True:
#	for i in ["/","- ","|","\\","|"]:
#		print ("%s\r" % i,)

print('''cdnkdnfdk ch cdjbdjcbdjcndjc
ccdcdcndc dc
dc#dcd#c#dc#dcd#c#d
dcc
dcd#c#dc#dcd#c#dcd''')

print("printing one backslash \\")

#a=input("Enter your name: ")
#print("Your Name is ",a)

print("How Old Are you: "),
age = int(input())

print("How tall Are you: "),
tall = int(input())

print("So you are %d old and %d tall" % (age, tall))
