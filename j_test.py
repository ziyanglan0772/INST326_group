""" Unit tests for the main_script """

import main_script as ms1
from pathlib import Path
import unittest

api_1='RGAPI-31e0b65a-b962-4843-b680-5d594d51e228'
class TestPlayer(unittest.TestCase):
    """ Test the Player class.
    
    Attributes:
        pl1,
        pl2,
        pl3 (ms1.Player): instances of Players designed to test various aspects of the class.
    """
    def setUp(self):
        """ Create instances of Player to test in other methods. """
        self.pl1 = ms1.Player(api_1,'lok666','euw1')
        self.pl2 = ms1.Player(api_1,"1 gpa",'na1')
        self.pl3 = ms1.Player(api_1,'EnjoyUrNoobness','na1')
        
    def test_init(self):
        """ Test whether __init__() works as expected. """
        self.assertEqual(self.pl1.api, 'RGAPI-31e0b65a-b962-4843-b680-5d594d51e228','Invalid API')
        self.assertEqual(self.pl1.id, 'lok666','Invalid ID')
        self.assertEqual(self.pl2.id,'1%20gpa','Invalid ID')
        self.assertEqual(self.pl1.region,'na1','Invalid region')
        self.assertEqual(self.pl3.region,'na1','Invalid region')               
        
    def test_acc_id(self):
        """ Test whether test_acc_id() works as expected. """
        self.assertEqual(self.pl1.acc_id(), 'lok666','PH2JxfvfIN7X_-S0sJGC7WLu6vmtkITUvrO6ZpCmvZZ8jG4')
        self.assertEqual(self.pl2.acc_id(), 'lok666','gpAiwZ_elswytdFhTzaXieVq4O6Y2iUhbgB86ie6O7ua4k8')
        self.assertEqual(self.pl3.acc_id(), None,'Error for handling invalid summoners name')
        
    def test_match_id(self,):
        """ Test whether match_id() works as expected. """
        self.assertEqual(self.pl1.match_id(), 'lok666','PH2JxfvfIN7X_-S0sJGC7WLu6vmtkITUvrO6ZpCmvZZ8jG4')
        self.assertEqual(self.pl2.match_id(), 'lok666','gpAiwZ_elswytdFhTzaXieVq4O6Y2iUhbgB86ie6O7ua4k8')
        self.assertEqual(self.pl3.match_id(), None,'Error for handling invalid summoners name')    