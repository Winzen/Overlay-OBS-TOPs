from funtions import query_graphiql


def pagina_txt(link_):
    query = """query{event(slug: \"""" + link_ + """\"){
  phaseGroups{
    id
    phase {
      name
    }}}}"""

    return query


def get_id_top8(link_event, top16=False):

    bracket = "top 16" if top16 else "top 8"

    try:
        query_json = query_graphiql(pagina_txt(link_event))

        for id_fases in query_json["data"]["event"]["phaseGroups"]:
            if str(id_fases["phase"]["name"]).lower() == bracket.lower():
                return id_fases["id"]
    except Exception as Error:

        return f"{Error}\nTop 8 não encontrado"
