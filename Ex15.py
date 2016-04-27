from sys import argv

script, filename = argv

txt = open(filename) # txt is the reference to the file

print "Here's your file %r:" % filename
print txt.read() # Read is a function on the reference.

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
