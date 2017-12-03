name = input ('Enter the file name') 
readedFile = open(name, 'r')
text = readedFile.read()
words = text.split()
for word in words :
    print(word)
