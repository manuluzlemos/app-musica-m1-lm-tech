## Projeto Final do Módulo 1 - LM Tech Data Talents

Turma: 970
Módulo: Lógica de Programação II


### Descrição do projeto

Uma das formas mais populares de se escutar música atualmente possivelmente é através de aplicativos de streaming.

Estes aplicativos se comunicam com bancos de dados contendo bibliotecas muito vastas de álbuns dos mais diversos artistas e gêneros.

Um diferencial desses aplicativos costuma ser a possibilidade do usuário criar playlists: o usuário pode buscar por músicas de diferentes artistas, salvá-las em uma ordem específica e ouvi-las sempre que quiser.

Desse modo, o presente projeto é um programa simulando um aplicativo de streaming. Ele terá um arquivo json com uma base de dados de músicas, artistas, álbuns e playlists. Um administrador poderá salvar novos artistas, músicas e álbuns, enquanto um usuário comum poderá pesquisar e criar playlists.


### Descrição da base de dados

A base de dados do projeto consiste em um arquivo json, denominado "banco-de-dados.json", onde tem-se a seguinte estrutura:
{
    "artistas": [],
    "albuns": [],
    "playlists": [],
    "musicas": []
}

Para cada um dessas entidades, tem-se a seguinte estrutura:

1) Artista 
{
    "codigo": int(),
    "nome_artista": "",
    "albuns": []
}

2) Álbum
{
    "codigo": int(),
    "nome": "",
    "musicas": []
}

3) Música
    {
        "codigo": int(),
        "nome": "",
        "duracao": "",
        "genero": ""
    }

4) Playlist
{
    "codigo": int(),
    "nome": "",
    "musicas": []
}


### Observações 

Nesse projeto, foram considerados os seguintes pontos durante o projeto e desenvolvimento do programa:

* Um artista pode ter vários álbuns, mas um álbum pertence somente a um artista. Desse modo, o campo "albuns" no Artista é uma lista com todos os códigos de álbuns do artista.

* Um álbum pode ter várias músicas, mas uma música pertence somente a um álbum. Desse modo, o campo "musicas" no Álbum é uma lista com todos os códigos de músicas do álbum.

* Uma playlist pode ter várias músicas e uma música pode fazer parte de várias playslists. Desse modo, o campo "musicas" na Playlist é uma lista com todos os códigos de músicas da playlist.


### Autora

Emanuelle da Luz Lemos

