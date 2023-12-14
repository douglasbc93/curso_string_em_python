# url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100";

url = " "

# sanitização da url
url = url.strip()

# validação da url
if url == "":
    raise ValueError("A URL está vazia")

# separa base e os parâmetros
indice_interrogacao = url.find('?')     # encontra o ? na url
url_base = url[:indice_interrogacao]       # separa a base da url
url_parametros = url[indice_interrogacao+1:]   # separa os parametros

# busca o valor de um parâmetro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)