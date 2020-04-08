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
        return match_id
    
    #Unfinished
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

def player_winrate(user_id,game_index=10):
    return player_winrate

def champ_winrate(champ_name,user_id):
    return champ_winrate

def against_winrate(champ_name1,champ_name2,user_id1,user_id2):
    return against_winrate

def find_dodge(champ_winrate,against_winrate):
    return find_dodge

def main():
    return None