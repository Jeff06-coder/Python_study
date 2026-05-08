import os, shutil
from pathlib import Path

# Falando para ele entender que o caminho é o que ele esta atualmente
ROOT_PATH = Path(__file__).parent

# Passando o caminho para criar a pasta nova dentro do caminho atual
# os.mkdir('pasta_nova')

# Criando o documento
arquivo = open('gerenciado.txt', 'w')
arquivo.close()

# Movendo para a pasta nova
shutil.move(ROOT_PATH / 'gerenciado.txt', ROOT_PATH / 'pasta_nova' / 'renovado.txt')