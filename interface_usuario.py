# Estudante: Emanuelle da Luz Lemos (manuluz.lemos@gmail.com)
# Arquivo principal do programa - funções que "interagem" com o usuário comum

import artista_func, album_func, musica_func, playlist_func, utils
from excecoes import *

def exibir_playlist_completa(playlist):
    print("\n- Informações sobre a playlist -")
    print(f'[Código {playlist["codigo"]}]: {playlist["nome"]} \t | Duração total: {playlist["duracao"]}')
    utils.exibir_dados_lista(playlist["musicas"], "Música", artista = "Artista", duracao = "Duração", genero = "Gênero")


def buscar_playlist_by_nome(artistas, albuns, musicas, playlists):
    print("\n- Buscar playlist por nome -")

    # escolher playlist
    nome_playlist = input("Informe o nome da playlist: ")
    lista_playlists = playlist_func.consultar_playlists(playlists, nome_playlist)
    if len(lista_playlists) == 0:
        print("Não há playlists com esse nome!")
    else:
        playlist_selecionada = utils.escolher_item(lista_playlists, "Playlist", playlist_func.consultar_uma_playlist)
        if playlist_selecionada != {}:
            try:
                playlist_completa = playlist_func.retornar_playlist_completa(playlist_selecionada, musicas, albuns, artistas)
            except DadoInexistente: 
                print("Não foi possível exibir a playlist por problemas nos dados")
            else:
                exibir_playlist_completa(playlist_completa)
        else:
            print("Não existem playlists com essa música!")


def buscar_playlist_by_artista(artistas, albuns, musicas, playlists):
    print("\n- Buscar playlist por artista -")

    # escolher artista
    nome_artista = input("Informe o nome do artista: ")
    lista_artistas = artista_func.consultar_artistas(artistas, nome_artista)
    if len(lista_artistas) == 0:
        print("Não há artistas com esse nome!")
    else:
        artista_selecionado = utils.escolher_item(lista_artistas, "Artista", artista_func.consultar_um_artista)

        # escolher playlist
        if artista_selecionado != {}:
            lista_playlists = playlist_func.consultar_playlists_by_artista(artista_selecionado, playlists, albuns)
            if len(lista_playlists) != 0:
                playlist_selecionada = utils.escolher_item(lista_playlists, "Playlist", playlist_func.consultar_uma_playlist)
                try:
                    playlist_completa = playlist_func.retornar_playlist_completa(playlist_selecionada, musicas, albuns, artistas)
                except DadoInexistente: 
                    print("Não foi possível exibir a playlist por problemas nos dados")
                else:
                    exibir_playlist_completa(playlist_completa)
            else:
                print("Não existem playlists com essa música!")
        else:
            print("Erro ao escolher artista")    

    
def buscar_playlist_by_musica(artistas, albuns, musicas, playlists):
    print("\n- Buscar playlist por música -")

    # selecionar música
    nome_musica = input("Informe o nome da música: ")
    lista_musicas = musica_func.consultar_musicas(musicas, nome_musica)
    if len(lista_musicas) == 0:
        print("Não há músicas com esse nome!")
    else:
        musica_selecionada = utils.escolher_item(lista_musicas, "Música", musica_func.consultar_uma_musica)

        # selecionar playlist
        if musica_selecionada != {}:
            lista_playlists = playlist_func.consultar_playlists_by_musica(musica_selecionada, playlists)
            if len(lista_playlists) != 0:
                playlist_selecionada = utils.escolher_item(lista_playlists, "Playlist", playlist_func.consultar_uma_playlist)
                try:
                    playlist_completa = playlist_func.retornar_playlist_completa(playlist_selecionada, musicas, albuns, artistas)
                except DadoInexistente: 
                    print("Não foi possível exibir a playlist por problemas nos dados")
                else:
                    exibir_playlist_completa(playlist_completa)
            else:
                print("Não existem playlists com essa música!")
        else:
            print("Erro ao escolher música")    


# menu para escolher o tipo de busca de playlist
def menu_buscar_playlist(artistas, albuns, musicas, playlists):
    lista_albuns = list(albuns)
    lista_musicas = list(musicas)
    lista_artistas = list(artistas)
    lista_playlists = list(playlists)

    print("\n\n-- Buscar por playlist --")
    print("1) Buscar por música")
    print("2) Buscar por artista")
    print("3) Buscar por nome")

    try:
        opcao = int(input("Informe a opção desejada: "))
    except ValueError:
        print("Atenção. A opção deve ser um número. Tente novamente!")
    else:
        if opcao == 1:
            buscar_playlist_by_musica(lista_artistas, lista_albuns, lista_musicas, lista_playlists)
        elif opcao == 2:
            buscar_playlist_by_artista(lista_artistas, lista_albuns, lista_musicas, lista_playlists)
        elif opcao == 3:
            buscar_playlist_by_nome(lista_artistas, lista_albuns, lista_musicas, lista_playlists)
        else:
            print("Opção inválida!")


# função responsável por criar playlist 
def criar_playlist(artistas, albuns, musicas, playlists):
    print("\n--- Criar playlist ---")

    nova_lista_playlists = list(playlists)

    nome_playlist = input("Informe o nome do playlist: ")
    musicas_playlist = loop_selecao_musicas(artistas, albuns, musicas)
    
    nova_playlist = playlist_func.criar_playlist(nome_playlist, utils.retornar_codigos(musicas_playlist), nova_lista_playlists)
    nova_lista_playlists.append(nova_playlist)
    return tuple(nova_lista_playlists)


# função recursiva para adicionar musicas a uma lista
def loop_selecao_musicas(artistas, albuns, musicas, qtde_musicas = 0, musicas_selecionadas = [], selecionar = True):
    if selecionar == False:
        return musicas_selecionadas
    
    musica_selecionada = {}

    print(f'\nEscolha a {qtde_musicas + 1}ª música da playlist')

    # selecionar artista
    nome_artista = input("Informe o nome do artista: ")
    lista_artistas = artista_func.consultar_artistas(artistas, nome_artista)
    if len(lista_artistas) == 0:
        print("Não há artistas com esse nome.")
    else:
        artista_selecionado = utils.escolher_item(lista_artistas, "Artista", artista_func.consultar_um_artista)

        # selecionar álbum
        if artista_selecionado != {}:
            if len(artista_selecionado["albuns"]) == 0:
                print("O artistas não possui álbuns.")
            else:
                albuns_artista = album_func.consultar_albuns_by_codigos(artista_selecionado["albuns"], albuns)
                album_selecionado = utils.escolher_item(albuns_artista, "Álbum", album_func.consultar_um_album)

                # selecionar música
                if album_selecionado != {}:
                    if len(album_selecionado["musicas"]) == 0:
                        print("O álbum não possui músicas.")
                    else:
                        musicas_album = musica_func.consultar_musicas_by_codigos(album_selecionado["musicas"], musicas)
                        musica_selecionada = utils.escolher_item(musicas_album, "Música", musica_func.consultar_uma_musica)

        if musica_selecionada == {}:
            print("A operação não foi bem sucedida. Tente novamente inserir os dados!")
        else:
            if not utils.verificar_existencia_dado("codigo", musica_selecionada["codigo"], musicas_selecionadas):
                qtde_musicas += 1
                musicas_selecionadas.append(musica_selecionada)
                selecionar = not utils.questao_v_f("Deseja finalizar a seleção de músicas?")
            else:
                print("Música já existe na playlist!")

    return loop_selecao_musicas(artistas, albuns, musicas, qtde_musicas, musicas_selecionadas, selecionar)
        

# menu do usuário comum
def menu_user():
    banco_dados = utils.ler_arquivo_json("banco-de-dados")
    artistas = tuple(banco_dados["artistas"]) if "artistas" in banco_dados else ()
    albuns = tuple(banco_dados["albuns"]) if "albuns" in banco_dados else ()
    musicas = tuple(banco_dados["musicas"]) if "musicas" in banco_dados else ()
    playlists = tuple(banco_dados["playlists"]) if "playlists" in banco_dados else ()

    continuar = True
    while continuar:
        print("\n\n--- MENU DO USUÁRIO ---")
        print("1) Buscar playlist")
        print("2) Criar playlist")
        print("0) Logout\n")

        try:
            opcao = int(input("Informe a opção desejada: "))
        except ValueError:
            print("Atenção. A opção deve ser um número. Tente novamente!")
        else:
            if opcao == 0:
                print("** Sessão encerrada **")
                continuar = False
            elif opcao == 1:
                menu_buscar_playlist(artistas, albuns, musicas, playlists)
            elif opcao == 2:
                playlists = criar_playlist(artistas, albuns, musicas, playlists)
            else:
                print("Opção inválida. Tente novamente!")

    novo_banco_dados = {
        "artistas": artistas,
        "albuns": albuns,
        "playlists": playlists,
        "musicas": musicas
    }

    utils.escrever_arquivo_json("banco-de-dados", novo_banco_dados)
