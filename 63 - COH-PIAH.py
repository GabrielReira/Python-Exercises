import re


def le_assinatura():
    '''
    A função lê os valores dos traços linguísticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos.
        Returns:
            (list): Retorna uma lista com todos os dados digitados pelo usuário.
    '''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado: ")

    wal = float(input("Entre o tamanho médio da palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio da sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho médio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''
    A função lê todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento.
        Returns:
            textos (list): Retorna uma lista contendo todos os textos.
    '''
    i = 1
    textos = []
    texto = input(f"Digite o texto {i} (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input(f"Digite o texto {i} (aperte enter para sair): ")

    return textos


def separa_sentencas(texto):
    '''
    A função recebe um texto e devolve uma lista das sentenças dentro do texto.
        Parameters:
            texto (str): Texto digitado pelo usuário.
        Returns:
            sentenças (list): Retorna uma lista onde cada elemento é uma sentença.
    '''
    sentenças = re.split(r'[.!?]+', texto)
    if sentenças[-1] == '':
        del sentenças[-1]

    return sentenças


def separa_frases(sentença):
    '''
    A função recebe uma sentença e devolve uma lista das frases dentro da sentença.
        Parameters:
            sentença (str): Senteça do texto.
        Returns:
            (list): Retorna uma lista contendo cada frase da sentença.
    '''
    return re.split(r'[,:;]+', sentença)


def separa_palavras(frase):
    '''
    A função recebe uma frase e devolve uma lista das palavras dentro da frase.
        Parameters:
            frase (str): Frase da sentença.
        Returns:
            (list): Retorna uma lista contendo cada palavra da frase.
    '''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''
    Essa função recebe uma lista de palavras e devolve o número de palavras que aparecem uma única vez.
        Parameters:
            lista_palavras (list): Lista contendo cada palavra de uma frase.
        Returns:
            únicas (int): Retorna o total de palavras únicas da frase.
    '''
    freq = dict()
    únicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                únicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            únicas += 1

    return únicas


def n_palavras_diferentes(lista_palavras):
    '''
    Essa função recebe uma lista de palavras e devolve o número de palavras diferentes utilizadas.
        Parameters:
            lista_palavras (list): Lista contendo cada palavra de uma frase.
        Returns:
            (int): Retorna o total de palavras diferentes da frase.

    '''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''
    Essa função recebe duas assinaturas de texto e devolve o grau de similaridade nas assinaturas.
        Parameters:
            as_a (float): Assinatura do texto A.
            as_b (float): Assinatura do texto B.
    '''
    pass


def calcula_assinatura(texto):
    '''
    Essa função recebe um texto e calcula a assinatura dele.
        Parameters:
            texto (str): Texto.
    '''
    pass


def avalia_textos(textos, ass_cp):
    '''
    Essa função recebe uma lista de textos e uma assinatura ass_cp e deve devolve o número do texto com a maior probabilidade de ter sido infectado por COH-PIAH.
        Parameters:
            textos (list): Lista contendo vários textos.
            ass_cp (float): Assinatura da cópia.
    '''
    pass