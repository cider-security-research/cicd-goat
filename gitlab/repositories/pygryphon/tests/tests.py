import unittest
import requests
import pyaztro
import ssl
import urllib3
import datetime
import sys


class AztroResponseTest(unittest.TestCase):
    # List of valid signs :

    signs = [
        'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
        'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'
    ]

    # List of 'aries' sign in different case :
    any_case_sign = [
        'aries', 'Aries', 'ARIES', 'ArIes'
    ]

    # List of non valid signs :
    non_signs = [
        'phoenix', 'pegasus'
    ]

    # List of valid input for day parameter :
    days = ['yesterday', 'today', 'tomorrow']

    # List of non valid input for day parameter :
    wrong_date = ['day after tomorrow', '21st', 'tuesday']

    # Part of response to be returned on wrong input :
    wrong_param_response = "Seems to be some kind of problem in the parameters"

    # setUp method for setting up the test
    def setUp(self):
        try:
            self.check = pyaztro.Aztro(sign='aries', day='today')
        except Exception as networkerror:
            print("setUp method failed to execute :", networkerror)
            sys.exit(1)

            # Test for checking the types of attributes in response object

    def test_response_object_type(self):
        self.assertTrue(type(self.check.lucky_time) is str)
        self.assertTrue(type(self.check.description) is str)
        self.assertTrue(type(self.check.date_range) is list)
        self.assertTrue(type(self.check.color) is str)
        self.assertTrue(type(self.check.mood) is str)
        self.assertTrue(type(self.check.compatibility) is str)
        self.assertTrue(type(self.check.current_date) is datetime.date)
        self.assertTrue(type(self.check.lucky_number) is int)

    # Test when the sign passed is a valid sign:
    def test_correct_sign(self):
        for i in self.signs:
            print(i)
            data = pyaztro.Aztro(i)
            self.assertTrue(type(data) is pyaztro.aztro.Aztro)

    # Test for checking the response when wrong input for sign is passed : 
    # def test_wrong_sign(self):
    #     for i in self.non_signs:
    #         data = pyaztro.Aztro(sign=i)
    #         self.assertTrue(type(data) is str)
    #         self.assertTrue(self.wrong_param_response in data)

    # Test for checking the response when correct input is entered for day:
    def test_correct_date(self):
        for i in range(3):
            data = pyaztro.Aztro(sign='aries', day=self.days[i])
            self.assertTrue(type(data) is pyaztro.aztro.Aztro)
            self.assertEqual(type(data.current_date), type(datetime.date.today() - datetime.timedelta(days=(i - 1))))

    #  Test for checking the response object when wrong input is enteres for day:
    # def test_wrong_date(self):
    #     for i in self.wrong_date:
    #         data = pyaztro.Aztro(sign='aries', day=i)
    #         self.assertTrue(type(data) is str)
    #         self.assertTrue(self.wrong_param_response in data)

    # Test for checking the response object when sign is given in different case:
    def test_anycase_input(self):
        for i in self.any_case_sign:
            data = pyaztro.Aztro(sign=i)
            self.assertEqual(type(data), type(self.check))


# def suite(q):
#     suite = unittest.TestSuite()
#     suite.addTest(AztroResponseTest.test_correct_sign(q))
#     suite.addTest(AztroResponseTest.test_wrong_sign(q))
#     suite.addtest(AztroResponseTest.test_correct_date(q))
#     suite.addTest(AztroResponseTest.test_wrong_date(q))
#     suite.addTest(AztroResponseTest.test_parse_date(q))
#     suite.addTest(AztroResponseTest.test_parse_date_range(q))
#     suite.addTest(AztroResponseTest.test_parse_time(q))
#     return suite

if __name__ == '__main__':
    unittest.main()
    # runner = unittest.TextTestRunner()
    # query = AztroResponseTest()
    # runner.run(suite(query))
