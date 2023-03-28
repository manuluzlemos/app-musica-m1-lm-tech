# Estudante: Emanuelle da Luz Lemos (manuluz.lemos@gmail.com)
# Arquivo principal do programa - funções que "interagem" com o usuário comum

import artista_func, album_func, musica_func, utils
from excecoes import *

def registrar_album(albuns, musicas, artistas):
    print("\n--- Registrar album ---")

    nova_lista_albuns = list(albuns)
    nova_lista_musicas = list(musicas)
    nova_lista_artistas = list(artistas)

    nome_artista = input("Informe o nome do artista: ")

    lista_artistas = artista_func.consultar_artistas(nova_lista_artistas, nome_artista)
    if len(lista_artistas) == 0:
        print("Não há artistas com esse nome!")
    else:
        artista_selecionado = utils.escolher_item(lista_artistas, "Artista", artista_func.consultar_um_artista)

        # adicionar álbum
        if artista_selecionado != {}:
            nome_album = input(f'Informe o nome do álbum do artista {artista_selecionado["nome"]}: ')

            try:
                qtde_musicas = int(input("Informe a quantidade de músicas: ")) 
                while qtde_musicas <= 0:
                    print("Lembre-se que a quantidade de músicas deve ser maior que 0. Tente novamente...")
                    qtde_musicas = int(input("Informe a quantidade de músicas: ")) 

            except TypeError:
                print("Atenção. A quantidade de músicas deve ser um número. Tente novamente!")

            except:
                print("Ocorreu um erro desconhecido!")

            else:
                novas_musicas, nova_lista_musicas = registrar_musicas(qtde_musicas, nova_lista_musicas)
                novo_album = album_func.criar_album(
                    nome_album, utils.retornar_codigos(novas_musicas), nova_lista_albuns
                )
                nova_lista_albuns.append(novo_album)
                nova_lista_artistas = artista_func.adicionar_album_artista(novo_album["codigo"], artista_selecionado["codigo"], nova_lista_artistas)
        else: 
            print("Erro ao selecionar artista!")

    return tuple(nova_lista_albuns), tuple(nova_lista_musicas), tuple(nova_lista_artistas)


def registrar_musicas(qtde_musicas, musicas):
    novas_musicas = []
    nova_lista_musicas = musicas.copy()
    for i in range(qtde_musicas):
        nome = input(f'\nInforme a {i+1}ª música do álbum: ')
        duracao = input(f'Informe a duração da música no formato HH:mm:ss: ')
        while not utils.validar_duracao(duracao):
            print("Formato de duração inválido. Tente novamente!")
            duracao = input(f'Informe a duração da música no formato HH:mm:ss: ')
        genero = input("Informe o gênero da música: ")

        nova_musica = musica_func.criar_musica(nome, duracao, genero, nova_lista_musicas)
        novas_musicas.append(nova_musica) # somente músicas do álbum
        nova_lista_musicas.append(nova_musica) # todas as músicas
    
    return novas_musicas, nova_lista_musicas


def registrar_artista(artistas):
    print("\n--- Registrar artista ---")

    nova_lista_artistas = list(artistas)
    nome_artista = input("Informe o nome do artista: ") 
    try:
        novo_artista = artista_func.criar_artista(nome_artista, artistas)
    except DadoExiste:
        print("Não foi possível cadastrar, pois o artista já existia na base de dados!")
    else:
        nova_lista_artistas.append(novo_artista)
        print("Artista cadastrado com sucesso!")

    return tuple(nova_lista_artistas)


# menu do usuário administrador
def menu_admin():
    banco_dados = utils.ler_arquivo_json("banco-de-dados")
    artistas = tuple(banco_dados["artistas"]) if "artistas" in banco_dados else ()
    albuns = tuple(banco_dados["albuns"]) if "albuns" in banco_dados else ()
    musicas = tuple(banco_dados["musicas"]) if "musicas" in banco_dados else ()
    playlists = tuple(banco_dados["playlists"]) if "playlists" in banco_dados else ()
    
    continuar = True 
    while continuar:
        print("\n\n--- MENU ADMIN ---")
        print("1) Registrar artista")
        print("2) Registrar álbum")
        print("0) Logout \n")

        try:
            opcao = int(input("Informe a opção desejada: "))
        except ValueError:
            print("Atenção. A opção deve ser um número. Tente novamente!")
        else:
            if opcao == 0:
                print("** Sessão encerrada **")
                continuar = False
            elif opcao == 1:
                artistas = registrar_artista(artistas)
            elif opcao == 2:
                albuns, musicas, artistas = registrar_album(albuns, musicas, artistas)
            else:
                print("Opção inválida. Tente novamente!")
    
    novo_banco_dados = {
        "artistas": artistas,
        "albuns": albuns,
        "playlists": playlists,
        "musicas": musicas
    }

    utils.escrever_arquivo_json("banco-de-dados", novo_banco_dados)