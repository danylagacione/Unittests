
from app.api_cep import ApiCep


def consulta_api_viacep():
    nova_consulta_api_cep = ApiCep()
    json_cep = nova_consulta_api_cep.execute(input('Informe o cep para consulta: '))
    print(json_cep)
    return 'Cep consultado com sucesso!'

