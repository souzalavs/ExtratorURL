import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
       
    def sanitiza_url(self, url):
        return url.strip()
   
    def valida_url(self):
        if self.url == '':
            raise ValueError("A URL está vazia")
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')      
        match = padrao_url.match(self.url)        
        if not match:
            raise ValueError("A URL não é válida.")
      
    def get_url_base(self):
        indicie_interrogacao = self.url.find('?')
        url_base = self.url[:indicie_interrogacao]
        return url_base
    
    def get_url_parametros(self):
        indicie_interrogacao = self.url.find('?')
        url_parametros = self.url[indicie_interrogacao + 1:]
        return url_parametros
  
    def get_valor_parametros(self, parametro_busca):
        indicie_parametro = self.get_url_parametros().find(parametro_busca)
        indicie_valor = indicie_parametro + len(parametro_busca) + 1
        indicie_e_comercial = self.get_url_parametros().find('&', indicie_valor)
        if indicie_e_comercial == -1:
            valor = self.get_url_parametros()[indicie_valor:]
        else:
            valor = self.get_url_parametros()[indicie_valor:indicie_e_comercial]
        return valor
   
    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url
   
url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)

print("O tamanho da URL é: ", len(extrator_url))
print("URL completa: ", extrator_url)
print("extrator_url == extrator_url_2? ", extrator_url == extrator_url_2)

valor_quantidade = extrator_url.get_valor_parametros("quantidade")
print("Valor do parâmetro 'quantidade': ", valor_quantidade)
