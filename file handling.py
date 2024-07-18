#writin in file
with open('example.txt' , 'w') as file:
    file.write('Hello, World\n')
    file.write('This is a file handling example.\n')

#appending the file
with open('example.txt', 'a') as file:
    file.write('appending a new line\n')

#reading from the file
with open('example.txt', 'r') as file:
    content = file.read()
    print('file content:\n', content)

#reading the file line by line
with open ('example.txt','r') as file:
    print('reading the file line by line:')
    for line in file:
        print(line.strip())