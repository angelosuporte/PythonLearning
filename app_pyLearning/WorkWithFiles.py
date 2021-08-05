# Com 'w' reescreve o arquivo, com o 'a' atualiza. Os dois parametros criam arquivos. O 'r' é read
import shutil

def escrever_arquivo(texto):
    diretorio = 'C:/workspaces/AreaDeTeste/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/workspaces/AreaDeTeste/RecebeDeTeste/')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/workspaces/AreaDeTeste/RecebeDeTeste/teste.txt')

if __name__ == '__main__':
    move_arquivo('teste.txt')
    #copia_arquivo('teste.txt')
    #escrever_arquivo('Primeira linha.\n')
    # atualizar_arquivo('Segunda linha.\n')
    # ler_arquivo('teste.txt')