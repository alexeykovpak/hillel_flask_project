from unittest import TestCase
from unittest.mock import patch#, MagicMock
from parse import parse, main


class ParseTestCase(TestCase):

    def test_parse_1(self):
        expected_value = {'name': 'ferret', 'color': 'purple'}
        value = parse('https://example.com/path/to/page?name=ferret&color=purple')
        self.assertEqual(expected_value, value, 'Error in test 1')

    def test_parse_1_0(self):
        expected_value = {'name': 'not_ferret', 'color': 'purple'}
        value = parse('https://example.com/path/to/page?name=ferret&color=purple')
        self.assertEqual(expected_value, value, 'Error in test 1_0')

    def test_parse_2(self):
        expected_value = {'name': 'ferret', 'color': 'purple'}
        value = parse('https://example.com/path/to/page?name=ferret&color=purple&')
        self.assertEqual(expected_value, value, 'Error in test 2')

    def test_parse_2_0(self):
        expected_value = {'name': 'ferret', 'color': 'green'}
        value = parse('https://example.com/path/to/page?name=ferret&color=purple&')
        self.assertEqual(expected_value, value, 'Error in test 2_0')

    def test_parse_3(self):
        expected_value = {}
        value = parse('http://example.com/')
        self.assertEqual(expected_value, value, 'Error in test 3')

    def test_parse_3_0(self):
        expected_value = {'key_': 'WTF'}
        value = parse('http://example.com/')
        self.assertEqual(expected_value, value, 'Error in test 3_0')

    def test_parse_4(self):
        expected_value = {}
        value = parse('http://example.com/?')
        self.assertEqual(expected_value, value, 'Error in test 4')

    def test_parse_4_0(self):
        expected_value = {"key_": 'yew'}
        value = parse('http://example.com/?')
        self.assertEqual(expected_value, value, 'Error in test 4_0')

    def test_parse_5(self):
        expected_value = {'name': 'Dima'}
        value = parse('http://example.com/?name=Dima')
        self.assertEqual(expected_value, value, 'Error in test 5')

    def test_parse_5_0(self):
        expected_value = {'name': 'Olya'}
        value = parse('http://example.com/?name=Dima')
        self.assertEqual(expected_value, value, 'Error in test 5_0')

    @patch('tests.main', return_value='Test main parse function')
    def test_main_(self, mock_main): 
        main()
        mock_main.assert_called_once_with()

