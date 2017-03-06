"""
ObterDetalhesDeputado: Retorna detalhes dos deputados com histórico de participação em comissões, períodos de exercício, filiações partidárias e lideranças.
ObterLideresBancadas: Retorna os deputados líderes e vice-líderes em exercício das bancadas dos partidos
ObterPartidosCD: Retorna os partidos com representação na Câmara dos Deputados
ObterPartidosBlocoCD: Retorna os blocos parlamentares na Câmara dos Deputados.
"""

from ..connection import Connection
from ..utils import _make_url
class DeputadosClient(Connection):

    def obter_deputados(self):
        """
        Retorna os deputados em exercício na Câmara dos Deputados

        API ENDPOINT:
        `<http://www.camara.leg.br/SitCamaraWS/Deputados.asmx/ObterDeputados>`

        API DOC:
        'http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/deputados/obterdeputados'

        This method does not have input parameters
        """
        return self.perform_request('http://www.camara.leg.br/SitCamaraWS/Deputados.asmx/ObterDeputados')

    def obter_detalhes_deputado(self, ideCadastro=None, numLegislatura=None):
        """
        Retorna detalhes dos deputados com histórico de participação em comissões, períodos de exercício,
        filiações partidárias e liderancas.

        API ENDPOINT:
        http://www.camara.leg.br/SitCamaraWS/Deputados.asmx/ObterDetalhesDeputado?ideCadastro=141428&numLegislatura=

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/deputados/obterDetalhesDeputado

        Args:
            ideCadastro: String(Optinal):: Identificador do deputado obtido na chamada ao ObterDeputados.
            numLegislatura: Int(Opcional) 	Número da legislatura. Campo vazio, todas as legislaturas do Deputado.
        """
        base_url = 'http://www.camara.leg.br/SitCamaraWS/Deputados.asmx/ObterDetalhesDeputado?'
        params = dict([('ideCadastro',  ideCadastro),
                       ('numLegislatura', numLegislatura)])

        return self.perform_request(_make_url(api_house='camara',
                                              base_url=base_url,
                                              params=params))

    def obter_lideres_bancadas(self):

        print('lideres_bancadas')

    def obter_partidos(self):

        print('partids')

    def obter_partidos_bloco(self):

        print('bloco')


