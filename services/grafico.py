import plotly.graph_objects as go

# Função responsável por gerar os gráficos
def gera_grafico(dados_semProvincia ,dados_comProvincia):
    try:
        x_dados = []
        y_dados = []
        fig = go.Figure()

        # Verifica se há dados na variavel 'dados_comProvincia
        if dados_comProvincia:
            dados = {}
            # Coletando dados do arary que possui provincias
            for chave in dados_comProvincia:
                if chave['provincia'] not in dados:
                    dados[chave['provincia']] = [int(chave['total_confirmados'].replace('.', ''))]
                else:
                    dados[chave['provincia']] += [int(chave['total_confirmados'].replace('.', ''))]
            
            # Pega o ultimo valor de cada provincia e substituo o dados já existente no mesmo pelo novo
            for chave in dados:
                dados[chave] = dados[chave][-1]
            
            # Organiza os dados por decrescente 
            dados_ordenados = sorted(dados.items(), key = lambda item:-item[1])
            
            # Adiciona as respectivas lista de eixos, os itens que o loop esta passando  
            for chave in dados_ordenados:
                x_dados.append(chave[0])
                y_dados.append(chave[1])

            fig.add_trace(go.Bar(x=x_dados, y=y_dados))
        
        else:
            # Quando não tem dados no array com provincia, é feito um loop no array sem provincia
            for chave in dados_semProvincia:
                x_dados.append(chave['data'])
                y_dados.append(chave['total_confirmados'].replace('.', ''))
            fig.add_trace(go.Scatter(x=x_dados ,y=y_dados))
        
        # Estilização do gráfico
        fig.update_layout(autosize=False, width=1100, height=600, modebar={'activecolor': 'black'},
        margin={ 'l':0, 'r':0, 'b':180, 't':20, 'pad':1 })

        # Retorna com todo o código HTML gerado
        return fig.to_html()
    except:
        return "Falha em gerar gráfico dos dados"