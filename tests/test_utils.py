from cn_api_client.utils import _must_contain, _make_url, _treat_inputs
from unittest import TestCase

class Test(TestCase):

    def test_must_contain(self):

        this = {'test1': None, 'test2': 2, 'test3': 'no'}

        self.assertTrue(_must_contain(this=this,
                                      keys=[]))

        self.assertTrue(_must_contain(this=this,
                                      keys=['test2']))

        with self.assertRaises(AttributeError):
            _must_contain(this=this, keys=['test1'])

    def test_treat_inpust(self):

        self.assertIsInstance(_treat_inputs(2), str)

        self.assertIsInstance(_treat_inputs(2.3), str)

        self.assertIsInstance(_treat_inputs('str'), str)

        with self.assertRaises(AttributeError):
            _treat_inputs(['a'])
            _treat_inputs({'as': 3})


    def test_make_url(self):

        with self.assertRaises(ReferenceError):
            _make_url()
            _make_url(api_house='camara')

        base_url = 'http://www.camara.gov.br/sitcamaraws/SessoesReunioes.asmx/ListarDiscursosPlenario?'
        params = dict([('dataIni', '23/03/2013'),
                       ('dataFim', '24/03/2013')])

        self.assertIsInstance(_make_url(api_house='camara',
                                        base_url=base_url,
                                        params=params), str)

