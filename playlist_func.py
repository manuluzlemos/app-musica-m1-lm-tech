# Estudante: Emanuelle da Luz Lemos (manuluz.lemos@gmail.com)
# Funções relacionadas com playlist

import utils, musica_func
from excecoes import *
from functools import reduce

def criar_playlist(nome, musicas, playlists):
    codigo = utils.gerar_codigo(playlists)
    playlist = {
        "codigo": codigo,
        "nome": nome,
        "musicas": musicas
    }

    return playlist

# retornar playlist com base no tipo de dado
def consultar_playlists(playlists, dado, tipo="nome"):
    selecao_playlists = []
    if tipo == "nome":
        selecao_playlists = [d for d in playlists if dado in d[tipo]]
    else:
        try:
            selecao_playlists = [d for d in playlists if d[tipo] == dado]
        except KeyError:
            print("Chave inválida!")
    
    return selecao_playlists 


# retornar somente uma playlist
def consultar_uma_playlist(codigo, playlists):
    playlist = consultar_playlists(playlists, codigo, tipo="codigo")
    playlist = playlist[0] if len(playlist) == 1 else {}
    return playlist


# retornar playlists que contenham uma música específica
def consultar_playlists_by_musica(musica, playlists):
    playlists_musica = [playlist for playlist in playlists if musica["codigo"] in playlist["musicas"]]
    return playlists_musica


# retornar playlists que contenham músicas de um artista específico
def consultar_playlists_by_artista(artista, playlists, albuns):
    musicas_artista = [musica for album in albuns for musica in album["musicas"] if album["codigo"] in artista["albuns"]]
    playlists_artista_duplicado = [playlist for playlist in playlists for musica in playlist["musicas"] if musica in musicas_artista] #dados duplicados
    codigos_playlists = list(set(utils.retornar_codigos(playlists_artista_duplicado)))
    playlists_artista = [playlist for playlist in playlists if playlist["codigo"] in codigos_playlists]

    return playlists_artista


# com base na playlist, retornar dados de músicas 
def retornar_playlist_completa(playlist, musicas, albuns, artistas):
    try:
        musicas_playlist = [musica_func.retornar_musica_completa(musica, albuns, artistas) for musica in musicas if musica["codigo"] in playlist["musicas"]]
    except DadoInexistente:
        raise DadoInexistente()
    
    playlist_completa = playlist.copy()
    playlist_completa["musicas"] = musicas_playlist
    duracao_playlist = reduce(lambda acc, musica: utils.somar_duracao(acc, musica["duracao"]), musicas_playlist, '00:00:00')
    playlist_completa["duracao"] = duracao_playlist
    
    return playlist_completa