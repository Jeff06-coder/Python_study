file = open('txt.txt', 'r')

#print(file.read())
#print(file.readline())
#print(file.readlines())


# Uma Lip
while len(linhas := file.readline()):
    print(linhas)

file.close()