#!/usr/bin/python
# -*- coding: latin-1 -*-

from ..connection import Connection
from ..utils import _make_url, _must_contain

class SessoesClient(Connection):

    def listar_discursos_plenario(self,
                                dataIni=None,
                                dataFim=None,
                                codigoSessao=None,
                                parteNomeParlamentar=None,
                                siglaPartido=None,
                                siglaUF=None):
        """
        Retorna a lista dos deputados que proferiam discurso no Plenário da Câmara dos Deputados em um determinado período.



        API ENDPOINT:
        http://www.camara.gov.br/sitcamaraws/SessoesReunioes.asmx/ListarDiscursosPlenario?dataIni=23/11/2012&
                                                                                          dataFim=23/11/2012&
                                                                                          codigoSessao=&
                                                                                          parteNomeParlamentar=&
                                                                                          siglaPartido=&
                                                                                          siglaUF=

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/sessoesreunioes-2/listardiscursosplenario

        dataIni: 	            Date (Obrigatorio) ::   Data início do período desejado (formato: DD/MM/AAAA)
        dataFim: 	            Date (Obrigatorio) :: 	Data de fim do período desejado (formato (DD/MM/AAAA)
        codigoSessao: 	        String (Opcional)  ::	Código da sessão a ser pesquisada
        parteNomeParlamentar: 	String (Opcional)  ::	Parte do nome do Deputado a ser pesquisada
        siglaPartido: 	        String (Opcional)  ::	Sigla do Partido do Deputado
        siglaUF: 	            String (Opcional)  ::	Sigla da UF do Deputado
        """
        base_url = 'http://www.camara.gov.br/sitcamaraws/SessoesReunioes.asmx/ListarDiscursosPlenario?'
        params = dict([('dataIni', dataIni),
                        ('dataFim', dataFim),
                        ('codigoSessao', codigoSessao),
                        ('parteNomeParlamentar', parteNomeParlamentar),
                        ('siglaPartido', siglaPartido),
                        ('siglaUF', siglaUF)])

        _must_contain(params, ['dataIni', 'dataFim'])

        return self.perform_request(_make_url(api_house='camara',
                                              base_url=base_url,
                                              params=params))

    def listar_presencas_dia(self,
                             data=None,
                             numMatriculaParlamentar=None,
                             siglaPartido=None,
                             siglaUF=None):
        """
        Retorna a quantidade de sessões ocorridas no dia especificado e a presença dos parlamentares em cada sessão.

        API ENDPOINT:
        http://www.camara.gov.br/SitCamaraWS/sessoesreunioes.asmx/ListarPresencasDia?
                                                                                    data=10/04/2012&
                                                                                    numLegislatura=54&
                                                                                    numMatriculaParlamentar=1&
                                                                                    siglaPartido=&
                                                                                    siglaUF=

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/sessoesreunioes-2/listarpresencasdia

        Args:
            data: 	                  Date(Obrigatorio) :: Data da Sessão (formato: DD/MM/AAAA)
            numMatriculaParlamentar:   Int(Opcional) 	:: Numero da matrícula do Parlamentar obtido pelo método ObterDeputados
            siglaPartido: 	          String(Opcional) 	:: Sigla do Partido
            siglaUF:	              String(Opcional) 	:: Sigla da UF a ser pesquisada
        """
        base_url = 'http://www.camara.gov.br/SitCamaraWS/sessoesreunioes.asmx/ListarPresencasDia?'
        params = dict([('data', data),
                        ('numMatriculaParlamentar', numMatriculaParlamentar),
                        ('siglaPartido', siglaPartido),
                        ('siglaUF', siglaUF),])



        _must_contain(params, ['data'])

        return self.perform_request(_make_url(api_house='camara',
                                              base_url=base_url,
                                              params=params))

    def listar_presencas_parlamentar(self,
                                     dataIni=None,
                                     dataFim=None,
                                     numMatriculaParlamentar=None,
                                     ):
        """
        Retorna a quantidade de sessões ocorridas no Plenário em um período especificado e a presença dos parlamentares em cada sessão.

        API ENDPOINT:
        http://www.camara.gov.br/SitCamaraWS/sessoesreunioes.asmx/ListarPresencasParlamentar?
                                                                                dataIni=20/11/2012&
                                                                                dataFim=23/11/2012&
                                                                                numMatriculaParlamentar=1

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/sessoesreunioes-2/listarpresencasparlamentar

        Args:
            dataIni 	                Date(Obrigatorio) ::	Data inicial
            dataFim 	                Date(Obrigatorio) ::	Data Final
            numMatriculaParlamentar 	Int(Obrigatorio)  ::	Numero da matrícula do Parlamentar obtido pelo método ObterDeputados
        """
        base_url = 'http://www.camara.gov.br/SitCamaraWS/sessoesreunioes.asmx/ListarPresencasParlamentar?'
        params = dict([('dataIni', dataIni),
                        ('dataFim', dataFim),
                        ('numMatriculaParlamentar', numMatriculaParlamentar)])


        _must_contain(params, ['dataIni', 'dataFim', 'numMatriculaParlamentar'])

        return self.perform_request(_make_url(api_house='camara',
                                              base_url=base_url,
                                              params=params))

    def listar_situacoes_reuniao_sessao(self):
        """
        Retorna a lista de situações para as reuniões de comissão e sessões plenárias da Câmara dos Deputados

        API ENDPOINT:
        http://www.camara.gov.br/SitCamaraWS/SessoesReunioes.asmx/ListarSituacoesReuniaoSessao

        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/sessoesreunioes-2/listarsituacoesreuniaosessao

        This method does not have input parameters
        """

        return self.perform_request('http://www.camara.gov.br/SitCamaraWS/SessoesReunioes.asmx/ListarSituacoesReuniaoSessao')


    def obter_inteiro_teor_discursos_plenario(self,
                                            codSessao=None,
                                            numOrador=None,
                                            numQuarto=None,
                                            numInsercao=None):
        """
        Retorna o inteiro teor de um discurso proferido no Plenário.

        Modo de utilização: primeiro deve-se chamar o método ListarDiscursosPlenario para obtenção dos parâmetros
        necessários para a identificação única do discurso desejado. São eles o código da sessão, o número do orador,
        e mais 2 parâmetros numéricos, numQuarto e numInsercao.

        API ENDPOINT:
        http://www.camara.gov.br/SitCamaraWS/SessoesReunioes.asmx/obterInteiroTeorDiscursosPlenario?
                                                                                            codSessao=022.3.54.O&
                                                                                            numOrador=1&
                                                                                            numQuarto=11&
                                                                                            numInsercao=0
        API DOC:
        http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/sessoesreunioes-2/obterinteiroteordiscursosplenario

        Args:
            codSessao: 	    String (Obrigatorio) 	:: codigo que identifica uma sessão do Plenário
            numOrador: 	    Inteiro (Obrigatorio) 	:: Identificador do orador na sessão
            numQuarto: 	    Inteiro (Obrigatorio) 	:: Número da fração taquigráfica que identifica o início do discurso
            numInsercao: 	Inteiro (Obrigatorio) 	:: Número da inserção taquigráfica que identifica o início do discurso
        """
        base_url = 'http://www.camara.gov.br/SitCamaraWS/SessoesReunioes.asmx/obterInteiroTeorDiscursosPlenario?'
        params = dict([ ('codSessao', codSessao),
                        ('numOrador', numOrador),
                        ('numQuarto', numQuarto),
                        ('numInsercao', numInsercao)])

        _must_contain(params, ['codSessao','numOrador','numQuarto','numInsercao'])

        return self.perform_request(_make_url(api_house='camara',
                                              base_url=base_url,
                                              params=params))
