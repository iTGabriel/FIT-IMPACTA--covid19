import plotly.graph_objects as go
import os

def gera_grafico(dados_semProvincia ,dados_comProvincia):
    try:
        x_dados = []
        y_dados = []
        if dados_comProvincia:
            for chave in dados_comProvincia:
                x_dados.append(chave['provincia'])
                y_dados.append(chave['total_confirmados']) 
        else:
            for chave in dados_semProvincia:
                x_dados.append(chave['data'])
                y_dados.append(chave['total_confirmados']) 

        print("Entrou")
        fig = go.Figure(data=[go.Bar(x=x_dados ,y=y_dados)])

        fig.update_layout(autosize=False, width=1100, height=400, modebar={'orientation': 'v', 'activecolor': 'black', 'legend': 'black'},
        margin={ 'l':0, 'r':0, 'b':80, 't':20, 'pad':1 })

        os.chdir('templates/graficos/')
        fig.write_html('grafico.html')
        print("Finalizou")
        return "Sucesso em gerar gráfico dos dados"
    except:
        return "Falha em gerar gráfico dos dados"
