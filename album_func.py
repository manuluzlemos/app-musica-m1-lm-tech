# Estudante: Emanuelle da Luz Lemos (manuluz.lemos@gmail.com)
# Funções relacionadas com álbuns 

import utils
from excecoes import *

def criar_album(nome, musicas, albuns):
    codigo = utils.gerar_codigo(albuns)
    album = {
        "codigo": codigo,
        "nome": nome,
        "musicas": musicas
    }

    return album 


# retornar álbuns com base no tipo de dado
def consultar_albuns(albuns, dado, tipo="nome"):
    selecao_albuns = []
    if tipo == "nome":
        selecao_albuns = [d for d in albuns if dado in d[tipo]]
    else:
        try:
            selecao_albuns = [d for d in albuns if d[tipo] == dado]
        except KeyError:
            print("Chave inválida!")
    
    return selecao_albuns 


# retornar somente um álbum
def consultar_um_album(codigo, albuns):
    album = consultar_albuns(albuns, codigo, tipo="codigo")
    album = album[0] if len(album) == 1 else {}
    return album


# retornar albuns de uma lista de código
def consultar_albuns_by_codigos(codigos, albuns):
    albuns_artistas = [consultar_um_album(codigo, albuns) for codigo in codigos]
    return albuns_artistas

# retornar artista do álbum
def retornar_artista_album(album, artistas):
    artista = [a for a in artistas if album["codigo"] in a["albuns"]]
    if len(artista) == 0:
        raise DadoInexistente()
    return artista[0]