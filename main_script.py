'A script for helping players figure out whether dodge is necessary in a current League of Legends game.'
import requests

class Player:
    '''A class for stroing details for a player.
    
    Attributes:
        api(str):The generated api key.
        id(str):The summoner name of the player.
        region(str):The region where the player belongs to.
    ''' 
    
    def __init__(self,api_key,user_id,region='na1'):
        '''Initializing a player object.
        
        Args:
        api_key(str):The generated api key.
        user_id(str):The summoner name of the player.
        region(str):The region where the player belongs to,defaultd to na1.
        '''
        self.region=region
        self.id=user_id
        self.api=api_key
        
    def acc_id(self):
        '''Finding the encrypted account id of the player.
        
        Returns:
            acc_id(str): the encrypted account id of the player.
        '''
        endpoint= 'https://'+self.region+'.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+self.id+'?api_key='+self.api
        response =requests.get(endpoint)
        response.raise_for_status()
        summoner_data=response.json()
        acc_id=summoner_data['accountId']
        return acc_id
    
    #Unfinished
    def match_id(self,acc_id):
        '''Finding the match ID of the player.
        
        Args:
        acc_id(str):The encrypted account ID of the player.
        
        Returns:
            match_id(str): the match ID of the player.
        '''
        match_id=''
        return match_id
    
    #Unfinished function
    def match_history(self,match_id):
        '''Finding the match history of the player.
       
        Args:
        match_id(str):The match ID of the player.
        
        Returns:
            match_history(dict): the match history of the player.
        '''
        endpoint='https://'+self.region+'.api.riotgames.com/lol/match/v4/matches/'+match_id+'?api_key='+self.api
        response =requests.get(endpoint)
        response.raise_for_status()
        a=response.json()
        match_history={}
        return match_history

def player_winrate(user_id,game_range=10):
    '''Finding the player winrate within the newest matches.
       
    Args:
    user_id(str):The summoners name of the player.
    game_range(int): It indicates how many games to be checked on the player;s match history.
        
    Returns:
    player_winrate(float): The winrate of the player.
    '''
    return player_winrate

def champ_winrate(champ_name,user_id):
    '''Finding the winrate of the champion that the player is playing.
       
    Args:
    champ_name(str):The name of the champion that is being played.
    user_id(str): The summoners name of the player.
        
    Returns:
    champ_winrate(float): The winrate of the champion.
    '''
    return champ_winrate

def against_winrate(champ_name1,champ_name2,user_id1,user_id2):
    '''Finding the match wirnate of champions of two players.
       
    Args:
    champ_name1(str):The name of the champion that is being played by the first player.
    champ_name2(str):The name of the champion that is being played by the second player.
    user_id1(str): The summoners name of the first player.
    user_id2(str): The summoners name of the second player.
    
    Returns:
    against_winrate(float): The winrate of this champion match.
    '''
    return against_winrate

def find_dodge(champ_winrate,against_winrate,player_winrate):
    '''Determining whether the player need to dodge the game.
       
    Args:
    champ_winrate(float): The winrate of the champion.
    against_winrate(float): The winrate of this champion match.
    player_winrate(float): The winrate of the player.
    
    Returns:
    find_dodge(bool):Return true, if the player need to dodge the game, otherwise return false
    '''
    return find_dodge

def main():
    return None