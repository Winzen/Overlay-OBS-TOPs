import requests as link
import json


def clear_link(text_link):
    try:
        link_event = (text_link.split("/"))
        index = link_event.index("tournament")

        if len(link_event) > 6 or str(link_event[0]).lower() == "tournament" and len(link_event) > 3:
            link_event = "/".join(link_event[index:index + 4])
            return link_event
        else:
            raise ValueError
    except ValueError:
        return False


def query_graphiql(query):
    """Retorna um objeto JSON de uma query para o Start.gg"""

    pedido = link.post(
        "https://www.start.gg/api/-/gql",
        headers={
            "client-version": "20",
            'Content-Type': 'application/json'
        },
        json={
            "query": query
        }
    )
    query_json = json.loads(pedido.text)

    return query_json


def linhas(x):
    try:
        index = "".join(x)

        dic_lines = {"1": """<div class="linha_winner_meio1 linha_animado"></div>""",
                     "100": """
        <div class="linha_after_winner2 linha_animado"></div>
        <div class="linha_next_stage_winner1 linha_animado"></div>
        <div class="linha_division_next_stage_winner1b linha_animado"></div>
        <div class="linha_intermedio_winner1 linha_animado"></div>
        <div class="linha_after_close_winner1 linha_animado"></div>
        <div class="linha_close_top_winner1 linha_animado"></div>""",
                     "101": """ 
        <div class="linha_after_winner2 linha_animado"></div>
        <div class="linha_next_stage_winner1 linha_animado"></div>
        <div class="linha_division_next_stage_winner1b linha_animado"></div>
        <div class="linha_intermedio_winner1 linha_animado"></div>
        <div class="linha_after_close_winner2 linha_animado"></div>
        <div class="linha_close_top_winner2 linha_animado"></div>""",
                     "110": """
        <div class="linha_after_winner1 linha_animado"></div>

        <div class="linha_next_stage_winner1b linha_animado"></div>
        <div class="linha_division_next_stage_winner1 linha_animado"></div>

        <div class="linha_intermedio_winner1b linha_animado"></div>

        <div class="linha_after_close_winner1b linha_animado"></div>
        <div class="linha_close_top_winner1b linha_animado"></div>""",
                     "111": """
        <div class="linha_after_winner1 linha_animado"></div>

        <div class="linha_next_stage_winner1b linha_animado"></div>
        <div class="linha_division_next_stage_winner1 linha_animado"></div>

        <div class="linha_intermedio_winner1b linha_animado"></div>
        <div class="linha_close_top_winner2b linha_animado"></div>
        <div class="linha_after_close_winner2b linha_animado"></div>""",
                     "2": """
        <div class="linha_meio_winner2 linha_animado"></div>
        <div class="linha1_close2_winner2 linha_animado"></div>
        <div class="traço1_close2_winner2 linha_animado"></div>""",
                     "200": """
        <div class="linha1_close_winner2 linha_animado"></div>
        <div class="traço1_close_winner2 linha_animado"></div>""",
                     "201": """
        <div class="traço2_close_winner2 linha_animado"></div>
        <div class="linha2_close_winner2 linha_animado"></div>""",
                     "-30": """
        <div class="linha_meio_loser1_top8 linha_animado"></div>

        <div class="linha2_close2_loser1 linha_animado"></div>
        <div class="traço1_close2_loser1 linha_animado"></div>
        """,
                     "-300": """
        <div class="linha1_close_loser1 linha_animado"></div>
        <div class="traço2_close_loser1 linha_animado"></div>
        """,
                     "-301": """
        <div class="traço1_close_loser1 linha_animado"></div>
        <div class="linha2_close_loser1 linha_animado"></div>
        """,
                     "-31": """
        <div class="linha_meio_loser2 linha_animado"></div>

        <div class="traço2_close2_loser2 linha_animado"></div>
        <div class="linha2_close2_loser2 linha_animado"></div>
         """,
                     "-310": """
        <div class="traço1_close_loser2 linha_animado"></div>
        <div class="linha1_close_loser2 linha_animado"></div>
         """,
                     "-311": """
        <div class="traço2_close_loser2 linha_animado"></div>
        <div class="linha2_close_loser2 linha_animado"></div>
         """,
                     "-4": """
        <div class="linha_loser_meio1 linha_animado"></div>
                     """,
                     "-400": """
        <div class="linha_division_next_stage_loser1 linha_animado"></div>
        <div class="linha_next_stage_loser1 linha_animado"></div>

        <div class="linha_after_loser2 linha_animado"></div>

        <div class="linha_intermedio_loser1 linha_animado"></div>

        <div class="linha_after_close_loser1 linha_animado"></div>
        <div class="linha_close_top_loser1 linha_animado"></div>
                     """,
                     "-401": """  
        <div class="linha_division_next_stage_loser1 linha_animado"></div>
        <div class="linha_next_stage_loser1 linha_animado"></div>

        <div class="linha_after_loser2 linha_animado"></div>

        <div class="linha_intermedio_loser1 linha_animado"></div>
        <div class="linha_close_top_loser2 linha_animado"></div>
        <div class="linha_after_close_loser2 linha_animado"></div>
                     """,
                     "-410": """
        <div class="linha_division_next_stage_loser1b linha_animado"></div>
        <div class="linha_next_stage_loser1b linha_animado"></div>

        <div class="linha_after_loser1 linha_animado"></div>

        <div class="linha_intermedio_loser1b linha_animado"></div>

        <div class="linha_after_close_loser1b linha_animado"></div>
        <div class="linha_close_top_loser1b linha_animado"></div>
                     """,
                     "-411": """
        <div class="linha_division_next_stage_loser1b linha_animado"></div>
        <div class="linha_next_stage_loser1b linha_animado"></div>

        <div class="linha_after_loser1 linha_animado"></div>

        <div class="linha_intermedio_loser1b linha_animado"></div>
        <div class="linha_after_close_loser2b linha_animado"></div>
        <div class="linha_close_top_loser2b linha_animado"></div>
                     """,
                     "-5": """
        <div class="linha_meio_loser4 linha_animado"></div>
        <div class="linha2_close2_loser4 linha_animado"></div>
        <div class="traço2_close2_loser4 linha_animado"></div>
                     """,
                     "-500": """
        <div class="linha1_close_loser4 linha_animado"></div>
        <div class="traço1_close_loser4 linha_animado"></div>
                     """,
                     "-501": """
        <div class="linha2_close_loser4 linha_animado"></div>
        <div class="traço2_close_loser4 linha_animado"></div>
                     """}

        return dic_lines[index]

    except Exception as Error:

        return ""


def clear_html_slots(html):
    slots = ['!n300', '!s300', '!p300', '!ps300', '!n301', '!s301', '!p301', '!ps301', '!n200', '!s200', '!p200',
             '!ps200',
             '!n201', '!s201', '!p201', '!ps201', '!n-600', '!s-600', '!p-600', '!ps-600', '!n-601', '!s-601', '!p-601',
             '!ps-601', '!n-500', '!s-500', '!p-500', '!ps-500', '!n-501', '!s-501', '!p-501', '!ps-501', '!n100',
             '!s100',
             '!p100', '!ps100', '!n101', '!s101', '!p101', '!ps101', '!n110', '!s110', '!p110', '!ps110', '!n111',
             '!s111',
             '!p111', '!ps111', '!n-400', '!s-400', '!p-400', '!ps-400', '!n-401', '!s-401', '!p-401', '!ps-401',
             '!n-410',
             '!s-410', '!p-410', '!ps-410', '!n-411', '!s-411', '!p-411', '!ps-411', '!n-300', '!s-300', '!p-300',
             '!ps-300',
             '!n-301', '!s-301', '!p-301', '!ps-301', '!n-310', '!s-310', '!p-310', '!ps-310', '!n-311', '!s-311',
             '!p-311',
             '!ps-311', "!1", "!2", "!-3", "!-4", "!-5"]
    for slot in slots:
        html = html.replace(slot, "")

    return html


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
