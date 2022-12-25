# importando classe de expressões regulares
import re

# cria classe
class ExtratorURL:
    # cria método construtor, a url será sanitizada e em seguida validada
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
        
    # método que sanitiza (limpa os espaços em branco da variável)
    def sanitiza_url(self, url):
        return url.strip()
    
    # metodo para validar a url
    def valida_url(self):
        # se for uma string vazia, devolve um erro
        if self.url == '':
            raise ValueError("A URL está vazia")
        
        # aplica expressão regular, a url deve começar com http(o S é opcional) ou www, deve obrigatoriamente
        # ter bytebank.com, o br é opcional mas o /cambio é obrigatório. Ele define o padrão que a URL deve seguir
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        # procura se a url está de cencontro com o padrão estabelecido, se devolver true é porque está no padrão
        match = padrao_url.match(self.url)
        # se não der match (não seguir o padrão) devolve um erro
        if not match:
            raise ValueError("A URL não é válida.")
    
    # pega a parte da url que se refere a base
    def get_url_base(self):
        # encontra a ? dentro da variável que contém a url
        indicie_interrogacao = self.url.find('?')
        # define a base da url pegando o que vem antes da interrogação e colocando como valor dessa variável
        url_base = self.url[:indicie_interrogacao]
        # define a variável que esse método vai retornar no final de sua execução
        return url_base
    
    # pega a parte da url que se refere aos parametros
    def get_url_parametros(self):
        # encontra a ? dentro da variável que contém a url
        indicie_interrogacao = self.url.find('?')
        # pega tudo que vem depois da interrogação e coloca dentro dessa variável
        url_parametros = self.url[indicie_interrogacao + 1:]
        # define que o método retorna essa variável após sua execução
        return url_parametros
    
    # metodo que define qual parametro será retornado de acordo com o que o usuário escolheu buscar
    def get_valor_parametros(self, parametro_busca):
        # pega a variável com os parâmetros e encontra o parâmetro de busca que o usuário escolheu
        indicie_parametro = self.get_url_parametros().find(parametro_busca)
        # recebe o parâmetro de busca encontrado e soma o seu tamanho + 1 (o 1 é o sinal de igual) de forma a
        # encontrar o número que define a posição em que se inicia o valor do parâmetro buscado
        indicie_valor = indicie_parametro + len(parametro_busca) + 1
        # procura se há um & após a posição inicial do parâmetro encontrado (descobre se tem mais parâmetros depois
        # daquele ou não)
        indicie_e_comercial = self.get_url_parametros().find('&', indicie_valor)
        # se for igual a -1 significa que é falso, não tem, portanto o valor recebe o que vem escrito daquela
        # posição em diante até o fim da string
        if indicie_e_comercial == -1:
            valor = self.get_url_parametros()[indicie_valor:]
        # do contrário, valor vai receber o que há entre a posição inicial e o & comercial
        else:
            valor = self.get_url_parametros()[indicie_valor:indicie_e_comercial]
        # retorna o valor depois de realizado todo o método
        return valor
    
    # método que retorna o tamanho da url
    def __len__(self):
        return len(self.url)

    # método pra quando der print no objeto dessa classe, ele devolver o que tem no return, e não o endereço do objeto na memória
    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    # método que define que a comparação entre dois objetos deve ser feito entre seus valores e não entre o endereço na memória
    def __eq__(self, other):
        return self.url == other.url
    
# criando a variável url e atribuindo o valor       
url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
# essa variável recebe um objeto chamado url da classe ExtratorURL
extrator_url = ExtratorURL(url)
# essa variável recebe um objeto chamado url da classe ExtratorURL
extrator_url_2 = ExtratorURL(url)

# mostra na tela o valor da string extrator_url que, por sua vez, é a url
print("O tamanho da URL é: ", len(extrator_url))
# mostra a url completa
print("URL completa: ", extrator_url)

# Verifica que duas instâncias com a mesma URL são iguais
print("extrator_url == extrator_url_2? ", extrator_url == extrator_url_2)

# Busca o valor do parâmetro quantidade
valor_quantidade = extrator_url.get_valor_parametros("quantidade")
print("Valor do parâmetro 'quantidade': ", valor_quantidade)