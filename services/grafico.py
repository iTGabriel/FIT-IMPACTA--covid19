import plotly.graph_objects as go


def gera_grafico(dados):
    try:
        fig = go.Figure(data=[go.Bar(y=[2, 1, 3])], layout={'modebar': None})
        fig.write_html('templates/graficos/grafico.html')
        return "Sucesso em gerar gráfico dos dados"
    except:
        return "Falha em gerar gráfico dos dados"

