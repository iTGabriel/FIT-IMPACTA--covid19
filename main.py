from flask import Flask, render_template, url_for, request
import services.apicovid as apiCovid
import services.util as util
import services.grafico as grafico

app = Flask(__name__)

# Rota base/principal 
@app.route('/')
def index():
    dados = []
    dados_global = {}
    message = None
    try:
        # Chamando a função para relizar o request de todos os países
        busca = apiCovid.todas_regioes().json()
        # Caso tenha retornado algo, então "inflamos" nossos dicionários em suas respectivas chaves, os valores fornecido pela API
        if busca:
            dados_global['total_confirmados'] = util.custom_numero(busca['Global']['TotalConfirmed'])
            dados_global['total_mortos'] = util.custom_numero(busca['Global']['TotalDeaths'])
            dados_global['total_recuperados'] = util.custom_numero(busca['Global']['TotalRecovered'])
            
            for chave in busca['Countries']:
                json = {
                    'pais' : chave['Country'],
                    'codigo': chave['CountryCode'],
                    'total_confirmados': util.custom_numero(chave['TotalConfirmed']),
                    'total_mortos': util.custom_numero(chave['TotalDeaths']),
                    'total_recuperados': util.custom_numero(chave['TotalRecovered']),
                    'data': util.custom_data(chave['Date'])
                }
                dados.append(json)
    except:
        message = "Falha em realizar processamento por buscas dos dados"

    return render_template('index.html', dados=dados, total=dados_global, message=message)

@app.route('/pais')
def pais():
    message = None
    dados_comProvincia = []
    dados_semProvincia = []
    try:
        # Variável para guardar o país requisitado pelo usuário através do link constituido no template navsbar
        pais = request.args['pais']
        
        # Chamando a função para relizar o request por país
        busca = apiCovid.por_regiao(pais).json()
        # Caso tenha retornado algo, então "inflamos" nossos dicionários em suas respectivas chaves, os valores fornecido pela API
        if busca:
            for chave in busca:
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
    except:
        message = "Falha em realizar o processamento de busca dos dados"

    # Chamando a função para gerar o gráfico e guardando o conteúdo gerado na variável
    grafico_template = grafico.gera_grafico(dados_semProvincia, dados_comProvincia)

    return render_template('tabela/por_regiao.html', dados_semProvincia=dados_semProvincia, dados_comProvincia=dados_comProvincia, message=message, grafico_template=grafico_template)


app.run('127.0.0.1', 8000)