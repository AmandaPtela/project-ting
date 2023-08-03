def exists_word(word, instance):
    """Aqui irá sua implementação"""
    lista = instance.queue

    if not word:
        return []

    for i in range(len(lista)):
        if word not in lista[i]["linhas_do_arquivo"]:
            return []

        return [{
            "palavra": word,
            "arquivo": lista[i]["nome_do_arquivo"],
            "ocorrencias": 2
        }]


""" dict_found = {
            "palavra": word,
            "arquivo": lista["nome_do_arquivo"],
            "ocorrencias"
        }
        print("palavra":) """


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
