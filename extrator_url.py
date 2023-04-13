import re
class ExtratorURL:
    def __init__(self,url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError('A URL está vazia')

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError('A URL não é valida.')

    def get_url_bse(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[0:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametros = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametros + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)


url = 'bytebank.com/cambio?quantidade=300&moedaOrigem=dolar&moedaDestino=real'
extrator_url = ExtratorURL(url)

VALOR_DOLAR = 4.98  # 1 dólar = 4.98 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")


if moeda_origem == 'real' and moeda_destino == 'dolar':
    valor_conversao = int(quantidade) / VALOR_DOLAR
    print(f'O valor de R$ {quantidade} reais é igual a $ {valor_conversao:,.2f} dolares.')
elif moeda_origem == 'dolar' and moeda_destino == 'real':
    valor_conversao = int(quantidade) * VALOR_DOLAR
    print(f'O valor de $ {quantidade} dolares é igual a R$ {valor_conversao:,.2f} reais' .format(quantidade, valor_conversao))
else:
    print('Cambio inválido, tente novamente')