import plotly.graph_objects as go

def gera_grafico(dados_semProvincia ,dados_comProvincia):
    try:
        x_dados = []
        y_dados = []
        fig = go.Figure()
        if dados_comProvincia:
            dados = {}
            for chave in dados_comProvincia:
                if chave['provincia'] not in dados:
                    dados[chave['provincia']] = int(chave['total_confirmados'].replace('.', '').replace('k', ''))
                else:
                    dados[chave['provincia']] += int(chave['total_confirmados'].replace('.', '').replace('k', ''))
            dados = sorted(dados.items(), key = lambda x:-x[1])

            for chave, valor in dados:
                x_dados.append(chave)
                y_dados.append(valor)
            fig.add_trace(go.Bar(x=x_dados ,y=y_dados))
        else:
            for chave in dados_semProvincia:
                x_dados.append(chave['data'])
                y_dados.append(chave['total_confirmados'].replace('.', '').replace('k', ''))
            fig.add_trace(go.Scatter(x=x_dados ,y=y_dados))
        
        fig.update_layout(autosize=False, width=1100, height=600, modebar={'activecolor': 'black'},
        margin={ 'l':0, 'r':0, 'b':80, 't':20, 'pad':1 })

        return fig.to_html()
    except:
        return "Falha em gerar gráfico dos dados"