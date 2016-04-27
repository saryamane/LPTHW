from sys import argv

script, filename = argv

txt_file = open(filename)

print txt_file.read()

txt_file.close()
