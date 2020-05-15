from flask import Flask, render_template, url_for, request
import services.apicovid as apiCovid
import services.util as util

app = Flask(__name__)

@app.route('/')
def index():
    dados = []
    paises = []
    dados_global = {}    
    message = None
    try:
        busca = apiCovid.todas_regioes()
        if busca[1] == 200:
            pais = busca[0].json()
            dados_global['total_confirmados'] = util.custom_numero(pais['Global']['TotalConfirmed'])
            dados_global['total_mortos'] = util.custom_numero(pais['Global']['TotalDeaths'])
            dados_global['total_recuperados'] = util.custom_numero(pais['Global']['TotalRecovered'])
            
            for chave in pais['Countries']:
                json = {
                    'pais' : chave['Country'],
                    'codigo': chave['CountryCode'],
                    'total_confirmados': util.custom_numero(chave['TotalConfirmed']),
                    'total_mortos': util.custom_numero(chave['TotalDeaths']),
                    'total_recuperados': util.custom_numero(chave['TotalRecovered']),
                    'data': util.custom_data(chave['Date'])
                }
                dados.append(json)
        else:
            message = "Lista vazia por getileza atualizar a página."

    except:
        message = "Falha em realizar processamento por buscas dos dados"

    import plotly.graph_objects as go
    fig = go.Figure(data=[go.Bar(y=[2, 1, 3])], layout={'modebar': None})
    grafico = fig.write_html('templates/graficos/grafico.html')

    return render_template('index.html', dados=dados, total=dados_global, message=message)

@app.route('/regiao')
def regiao():
    dados = []
    verificador_provincia = False
    try:
        regiao = request.args['regiao']
        busca = apiCovid.por_regiao(regiao)
        if busca[1] == 200:
            pais = busca[0].json()
            verificador_data = None
            dados_segurado = None
            for chave in pais:
                if dados_segurado == None:
                    dados_segurado = chave
                
                if chave['Province'] != '':
                    verificador_provincia = True
                
                if dados_segurado != None:
                    if dados_segurado['Date'].split('T')[0] == chave['Date'].split('T')[0]:
                        if chave['Confirmed'] > dados_segurado['Confirmed']:

                            if chave['Province'] != '':
                                verificador_provincia = True
                            json = {
                            'pais': chave['Country'],
                            'provincia': chave['Province'],
                            'codigo': chave['CountryCode'],
                            'total_confirmados': util.custom_numero(chave['Confirmed']),
                            'total_mortos': util.custom_numero(chave['Deaths']),
                            'total_recuperados': util.custom_numero(chave['Recovered']),
                            'data': util.custom_data(chave['Date']),
                            }
                            dados.append(json)
                    else:
                        json = {
                            'pais': chave['Country'],
                            'provincia': chave['Province'],
                            'codigo': chave['CountryCode'],
                            'total_confirmados': util.custom_numero(chave['Confirmed']),
                            'total_mortos': util.custom_numero(chave['Deaths']),
                            'total_recuperados': util.custom_numero(chave['Recovered']),
                            'data': util.custom_data(chave['Date']),
                            }
                        dados.append(json)
                    
    
    except:
        message = "Falha em processar a busca dos dados"
    # dados.reverse()
    
    return render_template('tabela/por_regiao.html', dados=dados, provincia=verificador_provincia)


app.run('127.0.0.1', 8000)