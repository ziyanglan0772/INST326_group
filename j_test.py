""" Unit tests for the main_script """

import wrcal as wr1
from pathlib import Path
import unittest

#Input the following variable for testing
#Api_key should be generated on Riot API website.

api_1=input('Input your riot api key: ')
match_id1='1 gpa '
match_id2='Old Tea Drinker'
match_id3='theAZ'

class TestWinrate(unittest.TestCase):
    """ Test the Winrate class.
    
    Attributes:
        pl1,
        pl2,
        pl3 (wr1.Winrate): instances of Winrate designed to test various aspects of the class.
    """
    def setUp(self):
        """ Create instances of Player to test in other methods. """
        self.pl1 = wr1.Winrate('euw1','lok666',api_1)
        self.pl2 = wr1.Winrate('na1','1 gpa',api_1)
        self.pl3 = wr1.Winrate('na1','gging2',api_1)
        
    def test_init(self):
        """ Test whether __init__() works as expected. """
        self.assertEqual(self.pl1.api, api_1,'Invalid API')
        self.assertEqual(self.pl1.user_id, 'lok666','Invalid ID')
        self.assertEqual(self.pl2.user_id,'1 gpa','Invalid ID')
        self.assertEqual(self.pl1.region,'euw1','Invalid region')
        self.assertEqual(self.pl3.region,'na1','Invalid region')               
        
    def test_acc_id(self):
        """ Test whether acc_id() works as expected. """
        self.assertEqual(self.pl1.acc_id(), "PH2JxfvfIN7X_-S0sJGC7WLu6vmtkITUvrO6ZpCmvZZ8jG4",'Error geting acc_id for summoners in not na region')
        self.assertEqual(self.pl2.acc_id(), "gpAiwZ_elswytdFhTzaXieVq4O6Y2iUhbgB86ie6O7ua4k8",'Error for getting acc_id for summoners contains space')
        self.assertEqual(self.pl3.acc_id(), "e_lqt2YYixYYXWx5kIJ8aczufB8ZnCiArCcgXn5FvEo1I4k",'Error for getting acc_id for summoners in na region')
          
    
    def test_win_or_loss(self):
        """ Test whether win_or_loss() works as expected. """
        self.assertEqual(self.pl2.win_or_loss('3415821173',"PH2JxfvfIN7X_-S0sJGC7WLu6vmtkITUvrO6ZpCmvZZ8jG4"), ('3415821173', 'Fail'),'Wrong win/lose result')
        self.assertEqual(self.pl2.win_or_loss('3415648559',"PH2JxfvfIN7X_-S0sJGC7WLu6vmtkITUvrO6ZpCmvZZ8jG4"), ('3415648559', 'Fail'),'Wrong win/lose result')
        self.assertEqual(self.pl3.win_or_loss('3419837850',"e_lqt2YYixYYXWx5kIJ8aczufB8ZnCiArCcgXn5FvEo1I4k"), ('3419837850','Win'),'Wrong win/lose result')
        
    def test_champ_name_id_list(self):
        """ Test whether champ_name_id_list() works as expected. """
        self.assertEqual(self.pl1.champ_name_id_list()[0], ('Aatrox', '266'),'Invalid champion name and champion id result')
        self.assertEqual(self.pl2.champ_name_id_list()[1], ('Ahri', '103'),'Invalid champion name and champion id result')
        self.assertEqual(self.pl3.champ_name_id_list()[2], ('Akali', '84'),'Invalid champion name and champion id result')
    
    def test_get_champ_name(self):
        """ Test whether get_champ_name() works as expected. """
        self.assertEqual(self.pl1.get_champ_name('266'), 'Aatrox','Invalid champion name result for Aatrox')
        self.assertEqual(self.pl2.get_champ_name('103'), 'Ahri','Invalid champion name result for Ahri')
        self.assertEqual(self.pl3.get_champ_name('84'), 'Akali','Invalid champion name result for Akali')
    
    def test_get_champ_id(self):
        """ Test whether get_champ_id() works as expected. """
        self.assertEqual(self.pl1.get_champ_id('Aatrox'), '266','Invalid champion id result for Aatrox')
        self.assertEqual(self.pl2.get_champ_id('Ahri'), '103','Invalid champion id result for Ahri')
        self.assertEqual(self.pl3.get_champ_id('Akali'), '84','Invalid champion id result for Akali')    
        
    def test_champ_mastery(self):
        """ Test whether champ_mastery() works as expected. """
        self.assertEqual(self.pl1.champ_mastery('Aatrox'), (2,1881),'Invalid champion mastery result for Aatrox(p1)')
        self.assertEqual(self.pl2.champ_mastery('Ahri'), (1,164),'Invalid champion mastery result for Ahri(p2)')
        self.assertEqual(self.pl3.champ_mastery('Sivir'), (3,7023),'Invalid champion mastery result for Akali(p3)')
                
if __name__ == "__main__":    
    unittest.main()
