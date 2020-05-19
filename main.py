from flask import Flask, render_template, url_for, request
import services.apicovid as apiCovid
import services.util as util
import services.grafico as grafico

app = Flask(__name__)

@app.route('/')
def index():
    dados = []
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

    
    return render_template('index.html', dados=dados, total=dados_global, message=message)

@app.route('/regiao')
def regiao():
    message = None
    dados_comProvincia = []
    dados_semProvincia = []
    try:
        regiao = request.args['regiao']
        busca = apiCovid.por_regiao(regiao)
        if busca[1] == 200:
            pais = busca[0].json()
            # dados_segurado = None
            for chave in pais:
                json = {
                    'pais': chave['Country'],
                    'provincia': chave['Province'],
                    'codigo': chave['CountryCode'],
                    'total_confirmados': util.custom_numero(chave['Confirmed']),
                    'total_mortos': util.custom_numero(chave['Deaths']),
                    'total_recuperados': util.custom_numero(chave['Recovered']),
                    'data': util.custom_data(chave['Date']),
                    }
                if chave['Province']:
                    dados_comProvincia.append(json)
                else:
                    dados_semProvincia.append(json)
        grafico.gera_grafico(dados_semProvincia, dados_comProvincia)
    except:
        message = "Falha em processar a busca dos dados"
    # dados.reverse()
    return render_template('tabela/por_regiao.html', dados_semProvincia=dados_semProvincia, dados_comProvincia=dados_comProvincia, message=message)


app.run('127.0.0.1', 8000)