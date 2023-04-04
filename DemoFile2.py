# open the file in write mode
with open(r'c:\work\demo2.txt', 'w') as file:
    # write some text to the file
    file.write('This is a demo text.')

# open the file in read mode
with open(r'c:\work\demo2.txt', 'r') as file:
    # read the contents of the file
    contents = file.read()
    # print the contents of the file
    print(contents)
