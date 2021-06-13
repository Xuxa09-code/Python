import re

def le_assinatura(): 
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos(): 
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i = 0
    somaTracosLinguisticos = 0
    while i < len(as_a):
        somaTracosLinguisticos += abs(as_a[i] - as_b[i])
        # print('\t',somaTracosLinguisticos)
        i += 1
    return somaTracosLinguisticos / 6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    listaFrase = []
    palavras = []
    listaPalavras = []

    listaSentenca = separa_sentencas(texto)

    for sentenca in listaSentenca:
        listaFrase.append(separa_frases(sentenca))
    listaRealOficialFrases = []
    for Frase in listaFrase:
        for fraseSimples in Frase:
            listaRealOficialFrases.append(fraseSimples)
            palavras.append(separa_palavras(fraseSimples))
            
    numeroPalavras = TamPalavras = 0
    for GrandeGrupo in palavras:
        numeroPalavras += len(GrandeGrupo)
        for Palavra in GrandeGrupo:
            listaPalavras.append(Palavra)
            TamPalavras += len(Palavra)

    '''Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo 
                                                    número total de palavras.'''
    wal = TamPalavras / numeroPalavras

    '''Relação Type-Token é o número de palavras diferentes dividido pelo número total
    de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total
    (o, gato, caçava, o, rato) mas somente 4 diferentes (o, gato, caçava, rato). Nessa 
                                        frase, a relação Type-Token vale 4/5 = 0.8 '''
    ttr = n_palavras_diferentes(listaPalavras) / numeroPalavras

    '''Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido
    pelo total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras
    no total (o, gato, caçava, o, rato) mas somente 3 que aparecem só uma vez (gato, caçava,
    rato). Nessa frase, a relação Hapax Legomana vale 3/5=0.6 '''
    hlr = n_palavras_unicas(listaPalavras) / numeroPalavras

    '''Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças
    dividida pelo número de sentenças (os caracteres que separam uma sentença da outra não 
    devem ser contabilizados como parte da sentença).'''
    numeroCaracterSentenca = 0
    for sentenca in listaSentenca:
        numeroCaracterSentenca += len(sentenca)

    sal = numeroCaracterSentenca / len(listaSentenca)

    '''Complexidade de sentença é o número total de frases divido pelo número de sentenças.'''
    sac = len(listaRealOficialFrases) / len(listaSentenca)

    '''Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo 
                                                              número de frases no texto'''
    numeroCaracterFrase = 0
    for frase in listaRealOficialFrases:
        numeroCaracterFrase += len(frase)
    pal = numeroCaracterFrase / len(listaRealOficialFrases)

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    # cont = cohPiah = 0
    grauSemelhanca = []
    for texto in textos:
        # cont += 1
        grauSemelhanca.append(compara_assinatura(ass_cp, (calcula_assinatura(texto))))
        # print(grauSemelhanca)
        # if grauSemelhanca < minimo:
        #     maximo = grauSemelhanca
        #     cohPiah = cont
    print('O autor do texto',grauSemelhanca.index(min(grauSemelhanca)) + 1,'está infectado com COH-PIAH')
    return grauSemelhanca.index(min(grauSemelhanca)) + 1
def main():
    # ass_cp = le_assinatura()
    # textos = le_textos()
    # avalia_textos(textos, ass_cp)
    avalia_textos(['Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso".Quero para mim o espírito [d]esta frase,transformada a forma para a casar como eu sou:Viver não é necessário; o que é necessário é criar.Não conto gozar a minha vida; nem em gozá-la penso.Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo.Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha.Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.',
    'Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.',
    'NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.'], [4.79, 0.72, 0.56, 80.5, 2.5, 31.6])
main()