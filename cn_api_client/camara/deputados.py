"""
ObterDeputados: Retorna os deputados em exercício na Câmara dos Deputados
ObterDetalhesDeputado: Retorna detalhes dos deputados com histórico de participação em comissões, períodos de exercício, filiações partidárias e lideranças.
ObterLideresBancadas: Retorna os deputados líderes e vice-líderes em exercício das bancadas dos partidos
ObterPartidosCD: Retorna os partidos com representação na Câmara dos Deputados
ObterPartidosBlocoCD: Retorna os blocos parlamentares na Câmara dos Deputados.
"""
class DeputadosClient:

    def obter_deputados(self):
        """
        Retorna os deputados em exercício na Câmara dos Deputados

        API ENDPOINT:
        `<http://www.camara.leg.br/SitCamaraWS/Deputados.asmx/ObterDeputados>`

        API DOC:
        'http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/deputados/obterdeputados'

        This method does not have input parameters
        """

        print('obter_deputados')

    def obter_detalhes_deputado(self):

        print('obter_detalhes_deputado')

    def obter_lideres_bancadas(self):

        print('lideres_bancadas')

    def obter_partidos(self):

        print('partids')

    def obter_partidos_bloco(self):

        print('bloco')


