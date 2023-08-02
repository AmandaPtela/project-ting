import sys


def txt_importer(path_file):
    path_name = str(path_file)  # String
    arquivo = None  # arquivo/string separada vem p cá p ser retornada no fim

    if not path_name.endswith('.txt'):  # se final não for .txt
        print('Formato inválido', file=sys.stderr)
    try:
        with open(path_file, 'r') as Arquivo:  # abrir arquivo p leitura nomean
            data = Arquivo.read().split('\n')  # Dividindo a stringona/arquivo
            arquivo = data  # define a stringona na var arquivo pra retornar
            print(data)
    except FileNotFoundError:  # Caso arquivo não encontrado lança a exceção
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        print(arquivo)

    return arquivo  # arquivo criado e com valor associado no TRY
