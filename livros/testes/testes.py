import re



def to_date(data):
    dia = re.findall(r'\d+', data)
    mes = re.findall(r'\w\w+[a-z]+', data)
    ano = re.findall(r'\d\d\d+', data)

    dia_str = dia[0]
    ano_str = ano[0]
    if (mes[0] == 'novembro'):
        mes_str = '11'
    data_pub = ano_str +'-'+ mes_str + '-' + dia_str
    return data_pub

data = " 14 de novembro de 2019, 14h11"
saida = to_date(data)
print(type(saida))