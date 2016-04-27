from sys import argv

script, filename = argv

txt = open(filename) # txt is the reference to the file

print "Here's your file %r:" % filename
print txt.read() # Read is a function on the reference.

txt.close()
