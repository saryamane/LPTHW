from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^c)."
print "If you do want that, hit ENTER"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w+')

print "Truncating the file. Goodbye!"

target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I am now going to write these to the file."

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

final_string = line1 + "\n" + line2 + "\n" + line3 + "\n"
target.write(final_string)

print "And finally, we close."

target.close()
