from top8_dq import get_list_top8


def clear_none(slot):
    for v, n_ in enumerate(slot):
        if n_ is None:
            slot[v] = ""
    if slot[1] == "" and len(slot[2]) > 0:
        slot[1] = 0
    if slot[3] == "" and len(slot[4]) > 0:
        slot[3] = 0

    return slot


def winner(valores):
    resultados = ["", "", "div_score_jogador", "div_score_jogador", False, ""]

    try:
        if valores[0] != valores[1]:
            if valores.count("DQ"):
                resultados[valores.index("DQ")] += " loser"
                resultados[valores.index("DQ") + 2] += " loser"
                resultados[valores.index(0)] += " win_name"
                resultados[valores.index(0) + 2] += " win_name"
                resultados[-1] = valores.index(0)
                resultados[4] = True
            else:
                win = valores.index(max(valores))
                resultados[win] += " win_name"
                resultados[win + 2] += " win_name"
                loser = valores.index(min(valores))
                resultados[loser] += " loser"
                resultados[loser + 2] += " loser"
                resultados[-1] = win
                resultados[4] = True
    except TypeError:
        return resultados

    return resultados


def separar_nome(nome):
    try:

        f = nome[0]
        if f.lower() == "dq" or len(f) == 0:
            h = [nome[2], nome[4]]
        else:
            h = f.split(" - ")
            h[0] = h[0][:len(h[0]) - 1].strip()
            h[1] = h[1][:len(h[1]) - 1].strip()

        return h

    except IndexError:

        return ["", ""]


def html_partida(key, n, jogador1="", jogador2="", placar1="", placar2="", tag="", tag_score="", tag2="",
                 tag_score2=""):
    intervalo = "div_partida"
    if key < 0:
        intervalo += " loser_partida"
        if n == 1:
            intervalo += " intervalo_loser"
    partida = f"""
        <div class="{intervalo}">
            <div class="slot_partida">
                <div class="div_name_jogador {tag} text_animado" > 
                        <span class="fitname">{jogador1} </span>
                </div>
                <div class="{tag_score} text_animado">{placar1}</div>
            </div>
            <div class="slot_partida">
                <div class="div_name_jogador {tag2} text_animado"> 
                        <span class="fitname">{jogador2}</span>
                </div>
                <div class="{tag_score2} text_animado">{placar2}</div>
            </div>
        </div>
    """
    return partida


def winner_side(partida_winners):
    winners = f"""
    <div class="winner_partidas">
        {partida_winners}
    </div>
"""
    return winners


def loser_side(loser_winners):
    losers = f"""
    <div class="winner_partidas loser_side">
        {loser_winners}
    </div>
"""
    return losers


def loser_side_round2(loser_winners):
    losers = f"""
    <div class="winner_partidas loser_side loser_side_round_2">
        {loser_winners}
    </div>
"""
    return losers


def reader_html(partidas):
    reader = f"""
<link rel="stylesheet" href="../css/fundo.css">
<link rel="stylesheet" href="../css/linhas.css">
<link rel="stylesheet" href="../css/top8_div_name.css">
<link rel="stylesheet" href="../css/top_16.css">



<div class="div_fundo_video">
    <video class="fundo_video" loop autoplay muted>
        <source class="fundo_video" src="../imagens/top16.MP4" type="video/mp4">
    </video>
    {partidas}
</div>

<script src="../js/funtions.js"></script>
<script>anima2()</script>
"""
    return reader


# Linhas

def div_linhas_winner(linhas):
    winner_linhas = f"""
        <div class="winner_partidas div_linhas_winner linha_animado"> 
            {linhas}
        </div>
    """
    return winner_linhas


def div_linhas_loser(linhas):
    winner_linhas = f"""
        <div class="winner_partidas div_linhas_loser linha_animado">

            {linhas}
        </div>
    """
    return winner_linhas


def div_linhas_loser2(linhas):
    winner_linhas = f"""
<div class="winner_partidas div_linhas_loser2 linha_animado">
    {linhas}
</div>
    """
    return winner_linhas


def top8_winner(linhas):
    winner_linhas = f"""
<div class="winner_partidas pass_to_top8">
    {linhas}
</div>
    """
    return winner_linhas


def top8_losers(linhas):
    winner_linhas = f"""
<div class="winner_partidas pass_to_top8_losers">
    {linhas}
</div>
    """
    return winner_linhas


def make_lines(key, n, resultado, index_winner):
    dic_linhas = {1: ["""
    <div class="linha_resultado"></div>
    <div class="linha1_jogador"></div>
    <div class="traco1_jogador"></div>""",
                      """
            <div class="linha_resultado"></div>
            <div class="linha2_jogador"></div>
            <div class="traco2_jogador"></div>

                       """],
                  -3: ["""
            <div class="linha_meio_loser1"></div>
            <div class="traco_resultado"></div>
            <div class="linha_resultado_loser"></div>

            <div class="linha1_jogador_losers"></div>
            <div class="traco1_jogador_losers"></div>
                       """,
                       """
            <div class="linha_meio_loser1"></div>
            <div class="traco_resultado"></div>
            <div class="linha_resultado_loser"></div>

            <div class="linha2_jogador_losers"></div>
            <div class="traco2_jogador_losers"></div>
                       """], -4: ["", ""]}

    if resultado:
        win_line = dic_linhas[key][index_winner]
    else:
        win_line = ""

    intervalo = ""
    if n == 1:
        intervalo = " conjuto_linha_loser_intervalo"

    linha_slot = {1: f"""
    <div class="div_partida conjunto_linha">
           {win_line}
    </div>
    """,
                  -3: f"""
    <div class="div_partida conjunto_linha conjuto_linha_loser{intervalo}">
        {win_line}
    </div>
"""}

    return linha_slot[key]


def losers_round_2(n, winner_index, txt_losers2):
    if n == 2:
        n = 0
    elif n == 3:
        n = 1

    line_center = """<div class="linha_meio_resultado_losers2"></div>"""

    if line_center not in txt_losers2:
        txt_losers2 += line_center

    partidas_key_4 = {0: """
    <div class="linha1_resultado_loser2"></div>
    <div class="traco1_resultado_loser2"></div>

    <div class="linha1_intermediario_loser2"></div>
    <div class="traco1_intermediario_loser2"></div>
    """, 1: """
     <div class="linha2_resultado_loser2"></div>
     <div class="traco2_resultado_loser2"></div>
     <div class="linha2_intermediario_loser2"></div>
     <div class="traco2_intermediario_loser2"></div>
    """}

    winner_dic = {0: ["""
    <div class="linha1_jogador_losers_partida1"></div>
    <div class="traco1_jogador_losers_partida1"></div>""",
                      """
    <div class="linha2_jogador_losers_partida1"></div>
    <div class="traco2_jogador_losers_partida1"></div>
                      """],
                  1: ["""
    <div class="linha1_jogador_losers_partida2"></div>
    <div class="traco1_jogador_losers_partida2"></div>
                  """,
                      """
    <div class="linha2_jogador_losers_partida2"></div>
    <div class="traco2_jogador_losers_partida2"></div>
                      """]}

    txt_losers2 += partidas_key_4[n] + winner_dic[n][winner_index]

    return txt_losers2


def controle_to_top8(top8_players):
    div_winner = ""
    for key in [1, -4]:
        txt_top8 = ""
        div_loser = ""

        for n, players in enumerate(top8_players[key]):

            if key == 1:
                div_winner += \
                    f"""<div class="div_partida top8_name">
                        <div class="div_name_jogador {players[1]} text_animado" style="width: 100%;">
                            <span class="fitname">{players[0]}</span>
                        </div>
                    </div>"""
            else:
                txt_top8 += \
                    f"""<div class="div_partida top8_name_losers">
                            <div class="div_name_jogador {players[1]} text_animado" style="width: 100%;">
                                <span class="fitname">{players[0]}</span>
                            </div>
                        </div>"""

                if n in [1, 3]:
                    div_loser += f"""
<div class="div_partida top8_partida_losers">
    {txt_top8}
</div>"""
                    txt_top8 = ""

    return top8_winner(div_winner) + top8_losers(div_loser)


def conjunto_partidas(partidas):
    all_matchs = ""
    all_lines = ""
    player_to_top8 = {1: [["", ""], ["", ""], ["", ""], ["", ""]], -4: [["", ""], ["", ""], ["", ""], ["", ""]]}
    position_on_html = {1: [winner_side, div_linhas_winner],
                        -3: [loser_side, div_linhas_loser],
                        -4: [loser_side_round2, div_linhas_loser2]}
    for key, matchs in partidas.items():
        partidas_txt = ""
        lines_txt = ""
        matchs_lines = ""
        for n, match in enumerate(matchs):
            match = clear_none(match)
            nomes = separar_nome(match)
            resultado = winner([match[1], match[3]])
            partidas_txt += html_partida(key, n, nomes[0], nomes[1], match[1], match[3], tag=resultado[0],
                                         tag2=resultado[1], tag_score=resultado[2], tag_score2=resultado[3])

            if resultado[-2] and key in [1, -4]:
                player_to_top8[key][n] = [nomes[resultado[-1]], resultado[resultado[-1]]]

            if key != -4:
                lines_txt += make_lines(key, n, resultado[-2], resultado[-1])
            else:
                if resultado[-2]:
                    lines_txt += losers_round_2(n, resultado[-1], lines_txt)
                if n == 1 or n == 3:
                    matchs_lines += f"""
                            <div class="div_partida conjunto_linha conjuto_linha_loser2">
                            {lines_txt}
                            </div>"""
                    lines_txt = "" if n != 3 else matchs_lines

        all_matchs += position_on_html[key][0](partidas_txt)
        all_lines += position_on_html[key][1](lines_txt)

    all_matchs += all_lines + controle_to_top8(player_to_top8)
    return all_matchs


def rodape_html(dic_partidas, test=False):

    try:
        if not test:
            top16_list = get_list_top8(dic_partidas, True)
        else:
            top16_list = dic_partidas

        if top16_list:
            txt_html = reader_html(conjunto_partidas(top16_list))
            with open("Top 16/Top_16.html", "w", encoding="utf-8") as html:
                html.write(txt_html)

            return "Top 16 Formado com sucesso"

        else:

            return "Link Invalido\nEvento não selecionado ou talvez link fora do Start.gg"
    except Exception as Error:
        print(Error)
        return "Possivel Start.gg bug API. Tente Novamente"

# if __name__ == '__main__':
#     top16_list = get_list_top8("https://www.start.gg/tournament/"
#                                "88-br-kumite-etapa-01-08/event/street-fighter-v-champion-edition", True)
#     print(top16_list)
#     rodape_html(top16_list)
