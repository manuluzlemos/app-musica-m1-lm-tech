# Estudante: Emanuelle da Luz Lemos (manuluz.lemos@gmail.com)
# Funções relacionadas com artista

import utils
from excecoes import *

# adicionar exceptions aqui para serem tratadas no index.py

def criar_artista(nome, artistas):
    if utils.verificar_existencia_dado("nome", nome, artistas):
        raise DadoExiste()
    
    codigo = utils.gerar_codigo(artistas)
    artista = {
        "codigo": codigo,
        "nome": nome,
        "albuns": []
    }

    return artista


# adiciona álbum em artista da lista artistas
def adicionar_album_artista(codigo_album, codigo_artista, artistas):
    nova_lista_artistas = artistas.copy()
    if utils.verificar_existencia_dado("codigo", codigo_artista, nova_lista_artistas):
        add_album_em_artista = utils.gerar_add_dado("codigo", "albuns")

        nova_lista_artistas = list(
            map(
                lambda item: add_album_em_artista(codigo_artista, codigo_album, item),
                nova_lista_artistas
            )
        )
        
    return nova_lista_artistas


# retornar artistas com de acordo com o tipo de dado
def consultar_artistas(artistas, dado, tipo="nome"):
    selecao_artistas = []
    if tipo == "nome":
        selecao_artistas = [d for d in artistas if dado in d[tipo]]
    else:
        try:
            selecao_artistas = [d for d in artistas if d[tipo] == dado]
        except KeyError:
            print("Chave inválida!")
    
    return selecao_artistas 


# retornar somente um artista com base em seu código
def consultar_um_artista(codigo, artistas):
    artista = consultar_artistas(artistas, codigo, tipo="codigo")
    artista = artista[0] if len(artista) == 1 else {}
    return artista