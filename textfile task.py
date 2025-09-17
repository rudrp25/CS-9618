# initializing arrays
hobbies = ["Reading books","Play computer games","Sport","Programming","Watching TV"]
count = [0,0,0,0,0]

file = open("hobby.txt", "w")

# task starts here
for i in range(5):
    try:
        choice = int(input('Enter a number: '))
    except:
        print('Error, input is not an integer')
        break
    try:
        count[choice-1] += 1
    except:
        print('Error, number inputted has to be between 1-5')
        break


for i in range(len(hobbies)):
    writeLine = str(count[i]) + ", " + hobbies[i] + "\n"
    file.write(writeLine)

file.close()

file = open("hobby.txt", "r")

for i in range(len(hobbies)):
    readLine = file.read()
    print(readLine)

file.close()



