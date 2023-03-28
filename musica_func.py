# Estudante: Emanuelle da Luz Lemos (manuluz.lemos@gmail.com)
# Funções relacionadas com músicas

import utils, album_func
from excecoes import *

def criar_musica(nome, duracao, genero, musicas):
    if utils.verificar_existencia_dado("nome", nome, musicas):
        raise DadoExiste()
    
    codigo = utils.gerar_codigo(musicas)
    musica = {
        "codigo": codigo,
        "nome": nome,
        "duracao": duracao,
        "genero": genero
    }

    return musica

# retornar músicas com base no tipo de dado
def consultar_musicas(musicas, dado, tipo="nome"):
    selecao_musicas = []
    if tipo == "nome":
        selecao_musicas = [d for d in musicas if dado in d[tipo]]
    else:
        try:
            selecao_musicas = [d for d in musicas if d[tipo] == dado]
        except KeyError:
            print("Chave inválida!")
    
    return selecao_musicas


# retornar somente uma música com base no código
def consultar_uma_musica(codigo, musicas):
    musica = consultar_musicas(musicas, codigo, tipo="codigo")
    musica = musica[0] if len(musica) == 1 else {}
    return musica


# retornar musicas de uma lista de código
def consultar_musicas_by_codigos(codigos, musicas):
    musicas_artistas = [consultar_uma_musica(codigo, musicas) for codigo in codigos]
    return musicas_artistas

# retornar dados da música e seu respectivo artista
def retornar_musica_completa(musica, albuns, artistas):
    album = [a for a in albuns if musica["codigo"] in a["musicas"]]
    if len(album) == 0:
        raise DadoInexistente()
    
    try:
        artista = album_func.retornar_artista_album(album[0], artistas)
    except DadoInexistente:
        raise DadoInexistente()
    
    musica_completa = musica.copy()
    musica_completa["artista"] = artista["nome"]
    return musica_completa 

