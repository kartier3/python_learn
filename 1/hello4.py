data = input("Enter a string: ")


file = open('text.txt', 'w')

file.write(data)

file.close()

file1 = open('text.txt', 'r' )

print(file1.read())

file1.close()