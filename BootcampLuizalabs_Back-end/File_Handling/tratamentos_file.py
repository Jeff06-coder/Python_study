from pathlib import Path

try:
    arquivo = open('arquivo.txt', 'r')
    print(arquivo.read())
except FileNotFoundError:
    print('Arquivo não encontrado')

PATH = Path(__file__).parent

try:
    arquivo = open(PATH / 'pasta_nova', 'r')
except IsADirectoryError:
    print('O caminho especificado é uma pasta, não um arquivo')
except Exception as e:
    print(f'Ocorreu algum erro: {e}')