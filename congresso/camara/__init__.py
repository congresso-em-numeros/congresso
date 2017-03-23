from .deputados import DeputadosClient
from .orgaos import OrgaosClient
from .proposicoes import ProposicoesClient
from .sessoesreunioes import SessoesClient

class Camara(object):
    """
    Camara dos Deputados Federal of Brazil low-level client. Provides a mapping from Python to REST endpoints.

    The instance has attributes ``deputados``, ``orgaos``, ``proposicoes``, ``sessoesreunioes``,
    that provide access to instances of
    :class:`~congresso.camara.DeputadosClient`,
    :class:`~congresso.camara.OrgaosClient`,
    :class:`~congresso.camara.ProposicoesClient` and
    :class:`~congresso.camara.SessoesClient` respectively. This is the
    preferred (and only supported) way to get access to those classes and their
    methods.

    You can initialize your connection class by:

        camara = congresso.Camara()

    and you'll be ready to use the API on your Python projetct.
    """

    def __init__(self):

        self.deputados   = DeputadosClient()
        self.orgaos      = OrgaosClient()
        self.proposicoes = ProposicoesClient()
        self.sessoes     = SessoesClient()
