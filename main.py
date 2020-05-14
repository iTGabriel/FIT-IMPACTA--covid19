from flask import Flask, render_template, url_for
import services.apicovid as apiCovid


app = Flask(__name__)


@app.route('/')
def index():
    dados = []
    paises = []
    dados_global = {}    
    try:
        busca = apiCovid.todas_regioes()
        if busca[1] == 200:
            
            pais = busca[0].json()
            dados_global['total_confirmados'] = pais['Global']['TotalConfirmed']
            dados_global['total_mortos'] = pais['Global']['TotalDeaths']
            dados_global['total_recuperados'] = pais['Global']['TotalRecovered']
            
            for chave in pais['Countries']:
                data_original = chave['Date'].split("T")[0].split('-')
                data_br = f"{data_original[2]}/{data_original[1]}/{data_original[0]}"
                json = {
                    'pais' : chave['Country'],
                    'codigo': chave['CountryCode'],
                    'total_confirmados': chave['TotalConfirmed'],
                    'total_mortos': chave['TotalDeaths'],
                    'total_recuperados': chave['TotalRecovered'],
                    'data': data_br
                }
                dados.append(json)
            
            


    except:
        message = "Falha em processar a busca dos dados"

    return render_template('index.html', dados=dados, total=dados_global)

app.run('127.0.0.1', 8000)

#  "Global": {
#     "NewConfirmed": 100282,
#     "TotalConfirmed": 1162857,
#     "NewDeaths": 5658,
#     "TotalDeaths": 63263,
#     "NewRecovered": 15405,
#     "TotalRecovered": 230845
#   },