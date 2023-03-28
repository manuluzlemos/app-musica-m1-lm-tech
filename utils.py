# Estudante: Emanuelle da Luz Lemos (manuluz.lemos@gmail.com)
# Funções úteis em outras partes do código
import json, re


# verificar se um dado de determinado tipo existe em uma lista
def verificar_existencia_dado(tipo, dado, lista):    
    try:
        dados = list(filter(lambda d: d[tipo] == dado, lista))
    except KeyError:
        print("Chave inválida!")
        
    return len(dados) != 0


# gera código para um dado a ser adicionado em uma coleção do tipo lista ou tupla
def gerar_codigo(colecao):
    if len(colecao) == 0:
        return 1
    
    codigo = colecao[-1]["codigo"] + 1 # pode ser algum dado da coleção tenha sido excluído
    return codigo


# validar duracao em formato de expressões regulares
def validar_duracao(duracao):
    try:
        pattern = re.compile(r'^\d{2}:\d{2}:\d{2}$') # regex
    except UnicodeDecodeError:
        return False
    return bool(pattern.match(duracao))


# somar duracao 
def somar_duracao(d1, d2):
    h1, m1, s1 = tuple(map(int, d1.split(":")))
    h2, m2, s2 = tuple(map(int, d2.split(":")))

    s = s1 + s2 
    m = m1 + m2
    h = h1 + h2

    if s > 59:
        m += (s // 60)
        s = s % 60
    
    if m > 59:
        h += (m // 60)
        m = m % 60

    horas = f'0{h}' if h < 10 else f'{h}'
    minutos = f'0{m}' if m < 10 else f'{m}'
    segundos = f'0{s}' if s < 10 else f'{s}'

    duracao = f'{horas}:{minutos}:{segundos}'
    return duracao



# retorna todos os códigos dos dicionários cadastrados em uma lista
def retornar_codigos(lista):
    try:
        codigos = [item["codigo"] for item in lista]
    except KeyError:
        print("A estrutura de dados não apresenta chave correspondente ao código!")

    return codigos

# se não tiver uma função de consulta sendo repassada como parâmetro, então a função retorna {}
def escolher_item(lista, dado, funcao_consulta = None):
    if funcao_consulta == None:
        return {}

    exibir_dados_lista(lista, dado)
    try:
        cod = int(input(f'[{dado}] Informe o código escolhido: '))
    except:
        return {}
    
    valido = verificar_existencia_dado("codigo", cod, lista)
    try:
        item_selecionado = funcao_consulta(cod, lista) if valido else {}
    except:
        item_selecionado = {}
        
    return item_selecionado


# por padrão, exibe apenas o código e o nome dos itens de na lista 
# no entanto, podem ser exibidos outros atributos
# para isso, deve-se ser passados valores do tipo: atributo = descricao_atributo
# "atributo" refere-se a chave de um item da lista 
# "descricao_atributo" refere-se ao que o atributo representa
def exibir_dados_lista(lista, descricao_lista, **atributos):
    print(f'\n- [{descricao_lista}] Lista de Itens -')
    for item in lista: 
        print("--------------------------------------------------")
        print(f'Código: {item["codigo"]} | {descricao_lista}: {item["nome"]}')
        if atributos != {}:
            for atributo, descricao_atributo in atributos.items():
                print(f'{descricao_atributo} : {item[atributo]}')
                
    print("--------------------------------------------------")


# solicitar ao usuário informação com duas opções
def questao_v_f(texto, resposta_verdadeira = "Sim", resposta_falsa = "Não"):
    resposta_valida = False
    resposta = ""
    while not resposta_valida:
        resposta = input(f'{texto} ({resposta_verdadeira} / {resposta_falsa}) ').lower()
        resposta_valida = resposta == resposta_verdadeira.lower() or resposta == resposta_falsa.lower()
        if not resposta_valida:
            print("Opção inválida. Tente novamente!")

    return resposta == resposta_verdadeira.lower()

# adiciona álbum no dicionario dado
def gerar_add_dado(tipo_condicao, tipo_novo_dado):

    def add_dado(dado_condicao, novo_dado, dicionario):
        dicionario_atualizado = dicionario.copy()
        if dicionario_atualizado[tipo_condicao] == dado_condicao:
            dicionario_atualizado[tipo_novo_dado].append(novo_dado)
        return dicionario_atualizado
    
    return add_dado

# ler arquivo do tipo json (caso não exista, deve-se criar o arquivo)
def ler_arquivo_json(nome_arquivo):
    try:
        with open(f'{nome_arquivo}.json', 'r') as arquivo:
            conteudo = arquivo.read()
            if len(conteudo) > 0:
                conteudo = json.loads(conteudo)
            else:
                conteudo = {}
    except FileNotFoundError:
        with open(f'{nome_arquivo}.json', 'w') as arquivo:
            arquivo.write('')
            conteudo = {}
    return conteudo


# sobrescrever arquivo do tipo json 
def escrever_arquivo_json(nome_arquivo, conteudo):
    with open(f'{nome_arquivo}.json', 'w') as arquivo:
        json.dump(conteudo, arquivo, indent=4)
