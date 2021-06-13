from unittest import TestCase
from unittest.mock import patch#, MagicMock
from parse_cookie import parse_cookie, main


class Parse_cookieTestCase(TestCase):

    def test_parse_cookie_1(self):
        expected_value = {'name': 'Dima'}
        value = parse_cookie('name=Dima;')
        self.assertEqual(expected_value, value, 'Error in test 1')

    def test_parse_cookie_1_0(self):
        expected_value = {'name': 'Oxana'}
        value = parse_cookie('name=Dima;')
        self.assertEqual(expected_value, value, 'Error in test 1_0')

    def test_parse_cookie_2(self):
        expected_value = {}
        value = parse_cookie('')
        self.assertEqual(expected_value, value, 'Error in test 2')

    def test_parse_cookie_2_0(self):
        expected_value = {'yew': 'oak'}
        value = parse_cookie('')
        self.assertEqual(expected_value, value, 'Error in test 2_0')

    def test_parse_cookie_3(self):
        expected_value = {'name': 'Dima', 'age': '28'}
        value = parse_cookie('name=Dima;age=28;')
        self.assertEqual(expected_value, value, 'Error in test 3')

    def test_parse_cookie_3_0(self):
        expected_value = {'name': 'Dima', 'age': '99'}
        value = parse_cookie('name=Dima;age=28;')
        self.assertEqual(expected_value, value, 'Error in test 3_0')

    def test_parse_cookie_4(self):
        expected_value = {'name': 'Dima=User', 'age': '28'}
        value = parse_cookie('name=Dima=User;age=28;')
        self.assertEqual(expected_value, value, 'Error in test 4')

    def test_parse_cookie_4_0(self):
        expected_value = {'name': 'Dima=Admin', 'age': '28'}
        value = parse_cookie('name=Dima=User;age=28;')
        self.assertEqual(expected_value, value, 'Error in test 4_0')

    @patch('tests.main', return_value='Test main parse_сookie function')
    def test_main(self, mock_main):
        main()
        mock_main.assert_called_once_with()


