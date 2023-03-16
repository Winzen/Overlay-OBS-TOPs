from top8_dq import get_list_top8
from funtions import linhas, clear_html_slots, separar_nome


def winner(valores):

    resultados = ["", "", "div_score_jogador text_animado", "div_score_jogador text_animado", False, ""]

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
                resultados[win+2] += " win_name"
                loser = valores.index(min(valores))
                resultados[loser] += " loser"
                resultados[loser + 2] += " loser"
                resultados[-1] = win
                resultados[4] = True
    except TypeError:
        return resultados

    return resultados


def make_top8_video(link, test=False):

    try:

        if not test:

            lugares = get_list_top8(link, top16=False)

        else:

            lugares = link

        with open("modelo/video_top8.html", "r") as hltm_modelo:
            modelo = hltm_modelo.read()

        if lugares:
            for key, slots in lugares.items():

                partida_txt = ""
                for n, slot in enumerate(slots):

                    if None in slot:
                        for v, n_ in enumerate(slot):
                            if n_ is None:
                                slot[v] = ""
                    if len(slot[2]) > 0 and slot[1] == "":
                        slot[1] = 0
                    if len(slot[4]) > 0 and slot[3] == "":
                        slot[3] = 0

                    nomes = separar_nome(slot)
                    resultado = winner([slot[1], slot[3]])

                    if resultado[4]:

                        if key == -3:

                            partida_txt += linhas([str(key), str(n)])

                        else:
                            if linhas(str(key)) not in partida_txt:
                                partida_txt = linhas(str(key))

                        partida_txt += linhas([str(key), str(n), str(resultado[-1])])

                    modelo = modelo.replace(f"!n{key}{n}0", nomes[0])
                    modelo = modelo.replace(f"!s{key}{n}0", str(slot[1]))
                    modelo = modelo.replace(f"!p{key}{n}0", resultado[0])
                    modelo = modelo.replace(f"!ps{key}{n}0", resultado[2])

                    modelo = modelo.replace(f"!n{key}{n}1", nomes[1])
                    modelo = modelo.replace(f"!s{key}{n}1", str(slot[3]))
                    modelo = modelo.replace(f"!p{key}{n}1", resultado[1])
                    modelo = modelo.replace(f"!ps{key}{n}1", resultado[3])

                modelo = modelo.replace(f"!{key}", partida_txt)
            modelo = clear_html_slots(modelo)
            with open("Top 8/Top_8.html", "w", encoding="utf-8") as hltm_modelo:
                hltm_modelo.write(modelo)

            return "Top 8 Formado com sucesso"

        else:

            return "Link Invalido\nEvento não selecionado ou talvez link fora do Start.gg"

    except Exception as Error:
        print(Error)
        return "Possivel Start.gg bug API. Tente Novamente"
