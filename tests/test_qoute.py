
import unittest
from app.models import Quote

class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Quote class
    
    '''

    def setUp(self):

        '''
        Set up method that will run before every
        
        '''
        self.new_quote = Quote(4,'jane', 'amazing deeds are just but gifts')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))