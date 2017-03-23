#!/usr/bin/python
# -*- coding: latin-1 -*-
from ..connection import Connection
from ..utils import _make_url, _must_contain


class ProposicoesClient(Connection):

    def listar_proposicoes(self,
                           sigla=None,
                           ano=None,
                           numero=None,
                           datApresentacaoIni=None,
                           datApresentacaoFim=None,
                           idTipoAutor=None,
                           parteNomeAutor=None,
                           siglaPartidoAutor=None,
                           siglaUfAutor=None,
                           generoAutor=None,
                           codEstado=None,
                           codOrgaoEstado=None,
                           emTramitacao=None
                           ):
        """
        Retorna a lista de proposições que satisfaçam os critérios estabelecidos

        API ENDPOINT:
        http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx/ListarProposicoes?sigla=PL&
(                                                                codEstado=&
                                                                                codOrgaoEstado=&
                                                                                emTramitacao=

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/proposicoes-1/listarproposicoes

        Args:
            sigla: 	                    String(Obrigatorio se ParteNomeAutor não for preenchido) ::	Sigla do tipo de proposição
            ano: 	                    Int(Obrigatorio se ParteNomeAutor não for preenchido) 	 :: Ano da proposição

            numero: 	                Int(Obrigatorio)    :: Numero da proposição
            datApresentacaoIni: 	    Date(Opcional) 	 :: Menor data desejada para a data de apresentação da proposição.
                                                            Formato: DD/MM/AAAA
            datApresentacaoFim: 	    Date(Opcional) 	 :: Maior data desejada para a data de apresentação da proposição
                                                            Formato: DD/MM/AAAA
            idTipoAutor: 	            Int(Optional) 	 :: Identificador do tipo de órgão autor da proposição,
                                                            como obtido na chamada ao ListarTiposOrgao
            parteNomeAutor: 	        String(Optional) :: Parte do nome do autor(5 ou + caracteres) da proposição.
            siglaPartidoAutor: 	        String(Optional) :: Sigla do partido do autor da proposição
            siglaUfAutor: 	            String(Optional) :: UF de representação do autor da proposição
            generoAutor: 	            String(Optional) :: Gênero do autor<BR>M - Masculino; F - Feminino;
                                                            Default - Todos
            emTramitacao: 	            int(Opcional) 	 :: Indicador da situação de tramitação da proposição
                                                            1 - Em Tramitação no Congresso;
                                                            2- Tramitação Encerrada no Congresso;
                                                            Default - Todas
        """

        base_url = 'http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx/ListarProposicoes?'
        params = dict([('sigla', sigla),
                        ('ano', ano),
                        ('numero', numero),
                        ('datApresentacaoIni', datApresentacaoIni),
                        ('datApresentacaoFim', datApresentacaoFim),
                        ('idTipoAutor', idTipoAutor),
                        ('parteNomeAutor', parteNomeAutor),
                        ('siglaPartidoAutor', siglaPartidoAutor),
                        ('siglaUfAutor', siglaUfAutor),
                        ('generoAutor', generoAutor),
                        ('codEstado', codEstado),
                        ('codOrgaoEstado', codOrgaoEstado),
                        ('emTramitacao', emTramitacao)])

        try:
            _must_contain(params, ['parteNomeAutor'])
        except AttributeError:
            _must_contain(params, ['sigla', 'ano'])

        return self.perform_request(_make_url(api_house='camara',
                                              base_url=base_url,
                                              params=params))

    def listar_siglas_tipo_proposicao(self):
        """
        Retorna a lista de siglas de proposições

        API ENDPOINT:
        http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx/ListarSiglasTipoProposicao

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/proposicoes-1/listarsiglastipoproposicao

        This method does not have input parameters
        """

        return self.perform_request('http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx/ListarSiglasTipoProposicao')

    def listar_situacoes_proposicao(self):
        """
        Retorna a lista de situações para proposições

        API ENDPOINT:
        http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx/ListarSituacoesProposicao

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/proposicoes-1/listarsituacoesproposicao

        This method does not have input parameters
        """

        return  self.perform_request('http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx/ListarSituacoesProposicao')

    def listar_tipos_autores(self):
        """
        Retorna a lista de situações para proposições

        API ENDPOINT:
        http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx/ListarTiposAutores

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/proposicoes-1/listartiposautores

        This method does not have input parameters
        """

        return self.perform_request('http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx/ListarTiposAutores')

    def obter_proposicao(self,
                         tipo=None,
                         ano=None,
                         numero=None,
                         idProp=None):
        """
        Retorna os dados de uma determinada proposição

        Grupo I
        API ENDPOINT:
        http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx/ObterProposicao?tipo=PL&numero=3962&ano=2008

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/proposicoes-1/obterproposicao

        Grupo II
        API ENDPOINT:
        http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx/ObterProposicaoPorID?IdProp=354258

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/proposicoes-1/obterproposicaoporid

        Args:
            Completar ou Grupo I ou Grupo II

            Grupo I
            tipo:   String (Obrigatorio) ::	Sigla do tipo de proposição
            ano:    Int (Obrigatorio) 	 :: Numero da proposição
            numero: Int (Obrigatorio) 	 :: Ano da proposição

            Grupo II
            idProp: Int (Obrigatorio)    ::	ID da proposição desejada
        """

        params = dict([('tipo', tipo),
                       ('ano', ano),
                       ('numero', numero),
                       ('idProp', idProp),
                       ])

        try:
            _must_contain(params, ['tipo', 'ano', 'numero'])
            base_url = 'http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx/ObterProposicao?'
            return self.perform_request(_make_url(api_house='camara',
                                                  base_url=base_url,
                                                  params=params))

        except AttributeError:
            _must_contain(params, ['idProp'])
            base_url = 'http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx/ObterProposicaoPorID?'
            return self.perform_request(_make_url(api_house='camara',
                                                  base_url=base_url,
                                                  params=params))



    def obter_proposicao_votacao(self,
                                 tipo=None,
                                 ano=None,
                                 numero=None):
        """
        Retorna os votos dos deputados a uma determinada proposição em votações ocorridas no Plenário da Câmara dos Deputados

        API ENDPOINT:
        http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx/ObterVotacaoProposicao?tipo=PL&numero=1992&ano=2007

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/proposicoes-1/obtervotacaoproposicao

        Args:
            tipo:   String (Obrigatorio) ::	  Sigla do tipo de proposição
            ano:    Int (Obrigatorio) 	 ::   Numero da proposição
            numero: Int (Obrigatorio) 	 ::   Ano da proposição
        """
        base_url = 'http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx/ListarProposicoes?'
        params = dict([('tipo', tipo),
                       ('ano', ano),
                       ('numero', numero),
                       ])

        _must_contain(params, ['tipo', 'ano', 'numero'])

        return self.perform_request(_make_url(api_house='camara',
                                              base_url=base_url,
                                              params=params))

    def listar_proposicoes_votadas_em_plenario(self,
                                               ano=None,
                                               tipo=None):
        """
        Retorna a lista de proposições que sofreram votação em plenário em determinado ano.

        API ENDPOINT:
        http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx/ListarProposicoesVotadasEmPlenario?ano=2013&tipo=

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/proposicoes-1/ProposicoesVotadasEmPlenario

        Args:
            ano:  int(Obrigatorio) ::	Ano da proposição
            tipo: String(Opcional) ::	Tipo de proposição
        """

        base_url = 'http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx/ListarProposicoesVotadasEmPlenario?'
        params = dict([('tipo', tipo),
                       ('ano', ano),
                       ])

        _must_contain(params, ['ano'])

        return self.perform_request(_make_url(api_house='camara',
                                              base_url=base_url,
                                              params=params))

    def listar_proposicoes_tramitadas_no_periodo(self,
                                                 dtInicio=None,
                                                 dtFim=None):
        """
        Retorna lista de proposições que tramitaram em determinado período. O período máximo é de 7 dias

        API ENDPOINT:
        http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx/ListarProposicoesTramitadasNoPeriodo?dtInicio=20/09/2013&dtFim=21/09/2013

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/proposicoes-1/listarProposicoesTramitadasNoPeriodo

        Args:
            dtInicio: String (Obrigatorio) ::	Data de início
            dtFim:    String (Obrigatorio) ::	Data final
        """
        base_url = 'http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx/ListarProposicoesTramitadasNoPeriodo?'
        params = dict([('dtInicio', dtInicio),
                       ('dtFim', dtFim)])

        _must_contain(params, ['dtInicio', 'dtFim'])

        return self.perform_request(_make_url(api_house='camara',
                                              base_url=base_url,
                                              params=params))