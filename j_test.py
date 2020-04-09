""" Unit tests for the main_script """

import main_script as ms1
from pathlib import Path
import unittest

#Input the following variable for testing
#Api_key should be generated on Riot API website.
api_1='RGAPI-31e0b65a-b962-4843-b680-5d594d51e228'
match_id1=''
match_id2=''
match_id3=''
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
        self.assertEqual(self.pl1.acc_id(), 'PH2JxfvfIN7X_-S0sJGC7WLu6vmtkITUvrO6ZpCmvZZ8jG4','Error geting acc_id for summoners')
        self.assertEqual(self.pl2.acc_id(), 'gpAiwZ_elswytdFhTzaXieVq4O6Y2iUhbgB86ie6O7ua4k8','Error for getting acc_id for summoners name contains space')
        self.assertEqual(self.pl3.acc_id(), None,'Error for handling invalid summoners name(acc_id)')
        
    def test_match_id(self):
        """ Test whether match_id() works as expected. """
        self.assertEqual(self.pl1.match_id(), match_id1,'Error geting match_id')
        self.assertEqual(self.pl2.match_id(), match_id2,'Error for getting match_id for summoners name contains space')
        self.assertEqual(self.pl3.match_id(), None,'Error for handling invalid summoners name(match_id)')    
    
    def test_match_history(self):
        """ Test whether match_history() works as expected. """
        self.assertEqual(self.pl1.match_history(match_id1), 200,'Error geting match_history')
        self.assertEqual(self.pl2.match_history(match_id2), 200,'Error for getting match_history for summoners name contains space')
        self.assertEqual(self.pl3.match_history(match_id3), None,'Error for handling invalid summoners name(match_history)')
    
def test_player_winrate(self):
    """ Test whether player_winrate() works as expected. """
    self.assertEqual(self.player_winrate('lok666'), .4 , 'Error for handling invalid datatype')
    self.assertEqual(self.player_winrate('1 gpa'), .6, 'Error for handling invalid datatype')
    self.assertEqual(self.plplayer_winrate('EnjoyUrNoobness'), .3, 'Error for handling invalid datatype')              
    
def test_champ_winrate(self):
    """ Test whether champ_winrate() works as expected. """
    self.assertEqual(self.champ_winrate("Shaco", 'lok666'), .53, 'Error for handling invalid champion')
    self.assertEqual(self.champ_winrate("Zed", '1 gpa'), .75, 'Error for handling invalid champion')  
    self.assertEqual(self.champ_winrate("Yasuo", 'EnjoyUrNoobness'), .45, 'Error for handling invalid champion') 
    
def test_against_winrate(self):
    """ Test whether against_winrate() works as expected. """
    self.assertEqual(self.against_winrate('Shaco', 'Olaf'), .54, 'Error invalid champion')
    self.assertEqual(self.against_winrate('Zed', 'Ziggs'), .45, 'Error champion doesnt exist')
    self.assertEqual(self.against_winrate('Yasuo', 'Zilean'), .48, 'Error invalid champion') 
    
def test_find_dodge(self):
    """ Test whether find_dodge() works as expected. """
    self.assertEqual(self.find_dodge(.53, .54, .65), 'Error for handling invalid datatype')
    self.assertEqual(self.find_dodge(.75, .45, .57), 'Error for handling invalid datatype')
    self.assertEqual(self.find_dodge(.45, .48, .42), 'Error for handling invalid datatype')
