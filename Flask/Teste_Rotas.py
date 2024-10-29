import requests
import json
    
def colocar():
    url = 'http://127.0.0.1:5000/cadastrar/transacao'

    dados = {'conta': "5", 'agencia':"7" , 'texto':'dasdas', 'valor':5.6}

    a = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(dados))
    print(a.status_code)

def excluir(id):
    url = f'http://127.0.0.1:5000/excluir/{id}'
    a = requests.delete(url)
    print(a.status_code)

def duplicado(id):
    url = f'http://127.0.0.1:5000/duplicado/{id}'
    a = requests.patch(url)
    print(a.status_code)



option = int(input(''))

match option:

    case 1:
        id = input('insira o id: ')
        excluir()
    case 2:
        colocar()
    case 3:
        id = input('insira o id: ')
        duplicado(id)