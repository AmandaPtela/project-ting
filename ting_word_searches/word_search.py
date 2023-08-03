def exists_word(word, instance):
    """Aqui irá sua implementação"""
    palavra = word.lower()
    dict = []
    ocorrencias = []

    for i in instance.queue:
        linhas = i["linhas_do_arquivo"]
        nome = i["nome_do_arquivo"]

        for index, texto in enumerate(linhas):
            if palavra in texto.lower():
                ocorrencias.append({"linha": index + 1})
        dict.append(
            {
                "palavra": palavra,
                "arquivo": nome,
                "ocorrencias": ocorrencias,
            }
        )
    if ocorrencias == []:
        return []

    return dict


""" dict_found = {
            "palavra": word,
            "arquivo": lista["nome_do_arquivo"],
            "ocorrencias"
        }
        print("palavra":) """


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
