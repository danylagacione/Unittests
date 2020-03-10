
import unittest

from unittest.mock import Mock, patch, call, MagicMock

from run import consulta_api_viacep


class TestMock(unittest.TestCase):


    @patch('run.input')
    def test_input(self,  mock_input):
        #Arrange, comportamento que o mock deve ter
        mock_input.return_value ='89037530'
        #Actions
        consulta_api_viacep()
        #Acssertions
        mock_input.side_effects = ['89037530', '89037520']
        mock_input.assert_called_once_with('Informe o cep para consulta: ')


    @patch('run.print')
    def test_print(self,mock_print,):
        json = {'cep': '89037-530', 'logradouro': 'Rua Thomé Venera dos Santos', 'complemento': ''
            , 'bairro': 'Escola Agrícola', 'localidade': 'Blumenau', 'uf': 'SC'
            , 'unidade': '', 'ibge': '4202404', 'gia': ''}
        mock_print.return_value = json

        mock_print.assert_not_called()

























