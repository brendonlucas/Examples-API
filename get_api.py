def main():
    print()
    # fortnite_info()
    # random_cat()
    # letras_de_musicas()


def random_cat():
    # Api que exiibe imagens aleatorias de gatos
    # https://aws.random.cat/meow
    import requests
    while True:
        print("1- Gerar uma imagem de gato aleatoria: \n"
              "0- sair")
        op = int(input("-> "))
        if op == 1:
            r_cats = requests.get('https://aws.random.cat/meow')
            print("Link: ", r_cats.json()['file'])
        if op == 0:
            break


def letras_de_musicas():
    # faz a busca de uma musica passada e retorna a letra dessa musica
    # https://lyricsovh.docs.apiary.io/#reference/0/lyrics-of-a-song/search
    import requests
    artista = input("Digite o nome do artista / Banda -> ")
    musica = input("Digite o nome da musica -> ")
    url = 'https://api.lyrics.ovh/v1/' + artista + '/' + musica
    r_rank = requests.get(url)
    print()
    if r_rank.json()['lyrics'] == '':
        print("Não foi possivel encontrar:")
    else:
        print("Letra da musica:")
        print(r_rank.json()['lyrics'])


def fortnite_info():
    # Api de informções sobre o game Fortnite incluindo dados de jogadores e informações da loja e desafios
    # https://fortnitetracker.com/site-api
    import requests
    headers = {"TRN-Api-Key": "9c31c8a9-af19-42e6-9b79-7065901f24a2"}
    plataforma = 'pc'

    while True:
        print("1- Ver status de um Jogador: \n"
              "2- Ver itens da loja: \n"
              "3- Ver os desafios da semana: \n"
              "0- sair")
        op1 = int(input("opção -> "))
        if op1 == 0:
            break

        if op1 == 1:
            nick = input("Digite o nome do jogador: ")
            link = 'https://api.fortnitetracker.com/v1/profile/'
            url = link + plataforma + '/' + nick
            r_player = requests.get(url, headers=headers)
            json_player = r_player.json()

            # informações do jogador
            print("Nome/Nick do jogador: " + json_player['epicUserHandle'])
            print()

            print("------ Dados das partidas Solo -----")
            print("Total de Partidas Solo: " + json_player['stats']['p2']['matches']['displayValue'])
            print("Total de Vitorias Solo: " + json_player['stats']['p2']['top1']['displayValue'])
            print("Total de Eliminações Solo: " + json_player['stats']['p2']['kills']['displayValue'])
            print()
            print("------ Dados das partidas Dupla -----")
            print("Total de Partidas Dupla: " + json_player['stats']['p10']['matches']['displayValue'])
            print("Total de Vitorias em Dupla: " + json_player['stats']['p10']['top1']['displayValue'])
            print("Total de Eliminações em Dupla: " + json_player['stats']['p10']['kills']['displayValue'])
            print()
            print("------ Dados das partidas Equipe -----")
            print("Total de Partidas em Equipe: " + json_player['stats']['p9']['matches']['displayValue'])
            print("Total de Vitorias em Equipe: " + json_player['stats']['p9']['top1']['displayValue'])
            print("Total de Eliminações em Equipe: " + json_player['stats']['p9']['kills']['displayValue'])
            print()

            # todos os dados resumo
            print("Datos totais do Jogador:")
            print("Total de Partidas Jogadas: " + json_player['lifeTimeStats'][7]['value'])
            print("Total de Vitorias: " + json_player['lifeTimeStats'][8]['value'])
            print("Total de Eliminações: " + json_player['lifeTimeStats'][10]['value'])
            print()

        if op1 == 2:
            url_loja = "https://api.fortnitetracker.com/v1/store"
            r_loja = requests.get(url_loja, headers=headers)
            json_loja = r_loja.json()
            print(" = = = =  lOJA DE ITENS DE HOJE = = = = ")
            for k in range(len(json_loja)):
                print("Item " + str(k + 1) + ':')
                print("Nome: " + json_loja[k]['name'])
                print("Preço vBucks: " + str(json_loja[k]['vBucks']) + " vBucks")
                print("Link da imagem: " + json_loja[k]['imageUrl'])
                print()

        if op1 == 3:
            url = "https://api.fortnitetracker.com/v1/challenges"
            r2 = requests.get(url, headers=headers)
            json = r2.json()
            items = json['items']
            for i in range(len(items)):
                print("Missão " + str(i + 1) + ' - ' + items[i]['metadata'][1]['value'])
            print()


if __name__ == '__main__':
    main()
