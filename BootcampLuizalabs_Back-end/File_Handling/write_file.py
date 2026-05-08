file = open('write.txt', 'w')

file.write('Escrevendo no arquivo\n')
file.writelines(['Escrevendo mais uma linha\n','\n', 'Escrevendo outra linha\n'])
file.close()
