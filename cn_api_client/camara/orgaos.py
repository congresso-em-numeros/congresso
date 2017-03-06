"""
ListarTiposOrgaos 	Retorna a lista dos tipos de órgãos que participam do processo legislativo na Câmara dos Deputados
ObterAndamento 	Retorna o andamento de uma proposição pelos órgãos internos da Câmara a partir de uma data específica
ObterEmendasSubstitutivoRedacaoFinal 	Retorna as emendas, substitutivos e redações finais de uma determinada proposição
ObterIntegraComissoesRelator 	Retorna os dados de relatores e pareces, e o link para a íntegra de uma determinada proposição
ObterMembrosOrgao 	Retorna os parlamentares membros de uma determinada comissão
ObterOrgaos 	Retorna a lista de órgãos legislativos da Câmara dos Deputados (comissões, Mesa Diretora, conselhos, etc.)
ObterPauta 	Retorna as pautas das reuniões de comissões e das sessões plenárias realizadas em um determinado período
ObterRegimeTramitacaoDespacho 	Retorna os dados do último despacho da proposição"""
from ..connection import Connection
from ..utils import _make_url, _must_contain

class OrgaosClient(Connection):

    def listar_cargos_orgaos_legislativo(self):
        """
        Retorna a lista dos tipos de cargo para os órgãos legislativos da Câmara dos Deputados (ex: presidente, primeiro-secretário, etc)

        API ENDPOINT:
        http://www.camara.gov.br/SitCamaraWS/Orgaos.asmx/ListarCargosOrgaosLegislativosCD

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/orgaos/listarcargosorgaoslegislativoscd

        This method does not have input parameters
        """

        return self.perform_request('http://www.camara.gov.br/SitCamaraWS/Orgaos.asmx/ListarCargosOrgaosLegislativosCD')

    def listar_tipos_orgaos(self):
        """
        Retorna a lista dos tipos de órgãos que participam do processo legislativo na Câmara dos Deputados

        API ENDPOINT:
        http://www.camara.gov.br/SitCamaraWS/Orgaos.asmx/ListarTiposOrgaos

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/orgaos/listartiposorgao

        This method does not have input parameters
        """

        return self.perform_request('http://www.camara.gov.br/SitCamaraWS/Orgaos.asmx/ListarTiposOrgaos')

    def obter_andamento(self,
                        sigla=None,
                        numero=None,
                        ano=None,
                        dataIni=None,
                        codOrgao=None):
        """
        Retorna o andamento de uma proposição pelos órgãos internos da Câmara a partir de uma data específica

        API ENDPOINT:
        http://www.camara.gov.br/SitCamaraWS/Orgaos.asmx/ObterAndamento?sigla=PL&numero=3962&ano=2008&dataIni=01/01/2009&codOrgao=

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/orgaos/obterandamento

        Args:
            sigla:    String(Obrigatorio) :: Sigla do tipo de proposição
            numero:   Int(Obrigatorio)    :: Numero da proposição
            ano:      Int(Obrigatorio)    :: Ano da proposição
            dataIni:  String(Opcional)    :: Data a partir da qual as tramitações do histórico de andamento serão retornadas (dd/mm/aaaa)
            codOrgao: String(Opcional)    :: ID do órgão numerador da proposição
        """
        base_url = 'http://www.camara.gov.br/SitCamaraWS/Orgaos.asmx/ObterAndamento?'
        params = dict([('sigla', sigla),
                       ('numero', numero),
                       ('ano', ano),
                       ('dataIni', dataIni),
                       ('codOrgao', codOrgao)])

        _must_contain(this=params, keys=['ano', 'numero', 'sigla'])

        return self.perform_request(_make_url(api_house='camara',
                                              base_url=base_url,
                                              params=params))

    def obter_emendas_substitutivo_redacao_final(self):

        print('emendas')

    def obter_integra_comissoes_relator(self):

        print('integra')

    def obter_membros_orgaos(self):

        print('membros')

    def obter_orgaos(self):

        print('orgaos')

    def obter_pauta(self):

        print('pauta')

    def obter_regime_tramitacao_despacho(self):

        print('tramitacao')