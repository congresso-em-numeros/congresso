#!/usr/bin/python
# -*- coding: latin-1 -*-

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

    def obter_emendas_substitutivo_redacao_final(self,
                                                 tipo=None,
                                                 ano=None,
                                                 numero=None):
        """
        Retorna as emendas, substitutivos e redações finais de uma determinada proposição

        API ENDPOINT:
        http://www.camara.gov.br/SitCamaraWS/Orgaos.asmx/ObterEmendasSubstitutivoRedacaoFinal?tipo=PL&numero=3962&ano=2008

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/orgaos/obteremendassubstitutivoredacaofinal

        Args:
            tipo:   String (Obrigatorio) :: Sigla do tipo de proposição
            ano:    Int (Obrigatorio) 	 :: Numero da proposição
            numero: Int (Obrigatorio) 	 :: Ano da proposição
        """

        base_url = 'http://www.camara.gov.br/SitCamaraWS/Orgaos.asmx/ObterEmendasSubstitutivoRedacaoFinal?'
        params = dict([('tipo', tipo),
                       ('numero', numero),
                       ('ano', ano)])

        _must_contain(this=params, keys=['ano', 'numero', 'tipo'])

        return self.perform_request(_make_url(api_house='camara',
                                              base_url=base_url,
                                              params=params))

    def obter_integra_comissoes_relator(self,
                                        tipo=None,
                                        ano=None,
                                        numero=None):
        """
        Retorna os dados de relatores e pareces, e o link para a íntegra de uma determinada proposição

        API ENDPOINT:
        http://www.camara.gov.br/SitCamaraWS/Orgaos.asmx/ObterIntegraComissoesRelator?tipo=PL&numero=3962&ano=2008

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/orgaos/obterintegracomissoesrelator

        Args:
            tipo:   String (Obrigatorio) :: Sigla do tipo de proposição
            ano:    Int (Obrigatorio) 	 :: Numero da proposição
            numero: Int (Obrigatorio) 	 :: Ano da proposição
        """

        base_url = 'http://www.camara.gov.br/SitCamaraWS/Orgaos.asmx/ObterIntegraComissoesRelator?'
        params = dict([('tipo', tipo),
                       ('numero', numero),
                       ('ano', ano)])

        _must_contain(this=params, keys=['ano', 'numero', 'tipo'])

        return self.perform_request(_make_url(api_house='camara',
                                              base_url=base_url,
                                              params=params))



    def obter_membros_orgaos(self, idOrgao=None):
        """
        Retorna os parlamentares membros de uma determinada comissão

        API ENDPOINT:
        http://www.camara.gov.br/SitCamaraWS/Orgaos.asmx/ObterMembrosOrgao?IDOrgao=2004

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/orgaos/obtermembrosorgao

        Args:
            idOrgao: Int (Obrigatorio)
        """

        base_url = 'http://www.camara.gov.br/SitCamaraWS/Orgaos.asmx/ObterMembrosOrgao?'
        params = dict([('idOrgao', idOrgao)])

        _must_contain(this=params, keys=['idOrgao'])

        return self.perform_request(_make_url(api_house='camara',
                                              base_url=base_url,
                                              params=params))
    def obter_orgaos(self):
        """
        Retorna a lista de órgãos legislativos da Câmara dos Deputados (comissões, Mesa Diretora, conselhos, etc.)

        API ENDPOINT:
        http://www.camara.gov.br/SitCamaraWS/Orgaos.asmx/ObterOrgaos

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/orgaos/obterorgaos

        This method does not have input parameters
        """

        return self.perform_request('http://www.camara.gov.br/SitCamaraWS/Orgaos.asmx/ObterOrgaos')

    def obter_pauta(self,
                    idOrgao=None,
                    dataIni=None,
                    dataFim=None):
        """
        Retorna as pautas das reuniões de comissões e das sessões plenárias realizadas em um determinado período

        API ENDPOINT:
        http://www.camara.gov.br/SitCamaraWS/Orgaos.asmx/ObterPauta?IDOrgao=2004&datIni=01/01/2012&datFim=30/04/2012

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/orgaos/obterpauta

        Args:
            idOrgao: Int(Obrigatorio) 	ID do órgão (comissão) da Câmara dos Deputados
            dataIni: String(Opcional) 	O métoto retorna a pauta das reuniões que foram realizadas em uma data maior ou igual a datIni
            dataFim: String(Opcional) 	O métoto retorna a pauta das reuniões que foram realizadas em uma data menor ou igual a datFim
        """

        base_url = 'http://www.camara.gov.br/SitCamaraWS/Orgaos.asmx/ObterPauta?'
        params = dict([('idOrgao', idOrgao),
                       ('dataIni', dataIni),
                       ('dataFim', dataFim)])

        _must_contain(this=params, keys=['idOrgao'])

        return self.perform_request(_make_url(api_house='camara',
                                              base_url=base_url,
                                              params=params))

    def obter_regime_tramitacao_despacho(self,
                                         tipo=None,
                                         numero=None,
                                         ano=None):
        """
        Retorna os dados do último despacho da proposição

        API ENDPOINT:
        http://www.camara.gov.br/SitCamaraWS/Orgaos.asmx/ObterRegimeTramitacaoDespacho?tipo=PL&numero=8035&ano=2010

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/orgaos/obterregimetramitacaodespacho

        Args:
            tipo:   String (Obrigatorio) ::	 Sigla do tipo de proposição
            numero: Int (Obrigatorio) 	 ::  Numero da proposição
            ano:    Int (Obrigatorio)    ::	 Ano da proposição
        """

        base_url = 'http://www.camara.gov.br/SitCamaraWS/Orgaos.asmx/ObterRegimeTramitacaoDespacho?'
        params = dict([('tipo', tipo),
                       ('numero', numero),
                       ('ano', ano)])

        _must_contain(this=params, keys=['tipo', 'ano', 'numero'])

        return self.perform_request(_make_url(api_house='camara',
                                              base_url=base_url,
                                              params=params))