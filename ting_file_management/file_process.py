from ting_file_management import file_management
import sys


def process(path_file, instance):
    arquivo_enfileirado = file_management.txt_importer(path_file)

    dict_arquivo = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(arquivo_enfileirado),
        "linhas_do_arquivo": arquivo_enfileirado,
    }

    for i in range(len(instance.queue)):

        if instance.search(i) == dict_arquivo:
            found = instance.search(i)
            dict_arquivo = found
            return dict_arquivo

    instance.enqueue(dict_arquivo)
    print(dict_arquivo, file=sys.stdout)


def remove(instance):
    if len(instance.queue) == 0:
        print('Não há elementos', file=sys.stdout)
    else:
        deq = instance.dequeue()["nome_do_arquivo"]
        print(f'Arquivo {deq} removido com sucesso', file=sys.stdout)


def file_metadata(instance, position):
    try:
        found = instance.search(position)
        print(found, file=sys.stdout)

    except IndexError:
        print('Posição inválida', file=sys.stderr)
