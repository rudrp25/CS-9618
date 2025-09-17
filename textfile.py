#file creation by writing  into the file
FileHandle = open('Sample.txt', 'w')
for i in range(1,4):
    Line = input('Enter a sentence: ')
    FileHandle.write(Line)
    FileHandle.write('\n')
FileHandle.close()

# reading line 1
FileHandle = open('Sample.txt', 'r')
Line = FileHandle.read()
print(Line)
FileHandle.close()
