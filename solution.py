import requests
from datetime import datetime, timedelta

def cotar():
    cotacoes = []
    hoje = datetime.now()

    for i in range(365):
        data = hoje - timedelta(days=i)
        data = datetime.strftime(data, "%m-%d-%Y")

        while True:
            url = fr"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data}'&$top=100&$format=json&$select=cotacaoCompra"

            res = requests.get(url)
            res = res.json()

            if res['value']:
                cotacoes.append(res['value'][0]['cotacaoCompra'])
                break
            else:
                data = datetime.strptime(data, "%m-%d-%Y") - timedelta(days=1)
                data = datetime.strftime(data, "%m-%d-%Y")

    return cotacoes
print(cotar())
