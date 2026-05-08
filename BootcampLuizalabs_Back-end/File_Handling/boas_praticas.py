from pathlib import Path

# Falando para ele entender que o caminho é o que ele esta atualmente
ROOT_PATH = Path(__file__).parent

try:
    # Fazendo o arquivo fechar sozinho
    with open(ROOT_PATH / 'write1.txt', 'w') as file:
        file.write('Escrevendo no arquivo\n')
        file.writelines(['Escrevendo mais uma linha\n','\n', 'Escrevendo outra linha\n'])
except IOError as e:
    print(f'Ocorreu um erro ao escrever no arquivo: {e}')

try:
    # Fazendo o arquivo fechar sozinho     # Colocando o encoding para evitar erros de leitura ou escrita
    with open(ROOT_PATH / 'write.txt', 'r', encoding='utf-8') as file:
        print(file.read())
except IOError as e:
    print(f'Ocorreu um erro ao ler o arquivo: {e}')