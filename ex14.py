from sys import argv
script, username = argv
prompt='>>>>	'
print("Hi %s, I am the %s script " %(username, script))
print("I'd like to as a few questions.")

print("Do you like me %s?"% username)
likes=input(prompt)


print("Where do you live %s?"% username)
lives=input(prompt)

print ("What kind of computer do you have?")
computer = input(prompt)

print ("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))