'A script for helping players figure out whether dodge is necessary in a current League of Legends game.'
import requests

class Player:
    '''A class for storing details for a player.
    
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
    
    def queue_name_to_id(self,queue_name):
        if queue_name == 'Solo/Duo':
            return int(420)
        elif queue_name == 'Rank Flex':
            return int(440)
        
    def match_list(self,queue_name,endIndex=100):
        '''Finding the match list of the player.
        
        Returns:
            match_list(set): the match list of the player.
        '''
        queue_id=self.queue_name_to_id(queue_name)
        acc_id=self.acc_id()
        endpoint= 'https://'+self.region+'.api.riotgames.com/lol/summoner/v4/matchlists/by-account/'+acc_id+'?api_key='+self.api+'?queue='+queue_id+'&season=13&endIndex='+endIndex
        # example: "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/VJk3vNblBShOVwciKL-Ua5e43Eo_2j3GEraQ-H4P_ZjY5sc?season=13&endIndex=100"
        response =requests.get(endpoint)
        response.raise_for_status()
        match_list_set=response.json()
        match_list=match_list_set[0]
        return match_list
        

    def get_match(self,match_list):
        '''Get the matchId of a specific game.
        
        Returns:
            match_data(str): the matchId of the specific game.
        '''
        match_data_list=[]
        for i in match_list:
            name=get_champ_name(i['champion'])
            match_id=i['gameId']
            endpoint = 'https://'+self.region+'.api.riotgames.com/lol/match/v4/matches/'+game_id
            response =requests.get(endpoint)
            response.raise_for_status()
            match_data=response.json()
            match_data_list.append(match_data.copy())
        return match_data_list

    def get_champ_name(self,champion_id):
        if id ==266:
            return "Aatrox"
        elif id == 412: 
            return "Thresh"
        elif id == 23: 
            return "Tryndamere"
        elif id == 79: 
            return "Gragas"
        elif id == 69: 
            return "Cassiopeia"
        elif id == 136: 
            return "Aurelion Sol"
        elif id == 13: 
            return "Ryze"
        elif id == 78: 
            return "Poppy"
        elif id == 14: 
            return "Sion"
        elif id == 1: 
            return "Annie"
        elif id == 202: 
            return "Jhin"
        elif id == 43: 
            return "Karma"
        elif id == 111: 
            return "Nautilus"
        elif id == 240: 
            return "Kled"
        elif id == 99: 
            return "Lux"
        elif id == 103: 
            return "Ahri"
        elif id == 2: 
            return "Olaf"
        elif id == 112: 
            return "Viktor"
        elif id == 34: 
            return "Anivia"
        elif id == 27: 
            return "Singed"
        elif id == 86: 
            return "Garen"
        elif id == 127: 
            return "Lissandra"
        elif id == 57: 
            return "Maokai"
        elif id == 25: 
            return "Morgana"
        elif id == 28: 
            return "Evelynn"
        elif id == 105: 
            return "Fizz"
        elif id == 74: 
            return "Heimerdinger"
        elif id == 238: 
            return "Zed"
        elif id == 68: 
            return "Rumble"
        elif id == 82: 
            return "Mordekaiser"
        elif id == 37: 
            return "Sona"
        elif id == 96: 
            return "Kog'Maw"
        elif id == 55: 
            return "Katarina"
        elif id == 117: 
            return "Lulu"
        elif id == 22: 
            return "Ashe"
        elif id == 30: 
            return "Karthus"
        elif id == 12:
            return "Alistar"
        elif id == 122: 
            return "Darius"
        elif id == 67: 
            return "Vayne"
        elif id == 110: 
            return "Varus"
        elif id == 77: 
            return "Udyr"
        elif id == 89: 
            return "Leona"
        elif id == 126: 
            return "Jayce"
        elif id == 134: 
            return "Syndra"
        elif id == 80:
            return "Pantheon"
        elif id == 92: 
            return "Riven"
        elif id == 121: 
            return "Kha'Zix"
        elif id == 42: 
            return "Corki"
        elif id == 268: 
            return "Azir"
        elif id == 51: 
            return "Caitlyn"
        elif id == 76: 
            return "Nidalee"
        elif id == 85:
            return "Kennen"
        elif id == 3:
            return "Galio"
        elif id == 45: 
            return "Veigar"
        elif id == 432: 
            return "Bard"
        elif id == 150: 
            return "Gnar"
        elif id == 90: 
            return "Malzahar"
        elif id == 104:
            return "Graves"
        elif id == 254:
            return "Vi"
        elif id == 10: 
            return "Kayle"
        elif id == 39: 
            return "Irelia"
        elif id == 64: 
            return "Lee Sin"
        elif id == 420: 
            return "Illaoi"
        elif id == 60: 
            return "Elise"
        elif id == 106: 
            return "Volibear"
        elif id == 20:
            return "Nunu"
        elif id == 4: 
            return "Twisted Fate"
        elif id == 24: 
            return "Jax"
        elif id == 102: 
            return "Shyvana"
        elif id == 429:
            return "Kalista"
        elif id == 36: 
            return "Dr. Mundo"
        elif id == 427: 
            return "Ivern"
        elif id == 131: 
            return "Diana"
        elif id == 223: 
            return "Tahm Kench"
        elif id == 63: 
            return "Brand"
        elif id == 113: 
            return "Sejuani"
        elif id == 8: 
            return "Vladimir"
        elif id == 154: 
            return "Zac"
        elif id == 421: 
            return "Rek'Sai"
        elif id == 133:
            return "Quinn"
        elif id == 84:
            return "Akali"
        elif id == 163: 
            return "Taliyah"
        elif id == 18: 
            return "Tristana"
        elif id == 120:
            return "Hecarim"
        elif id == 15:
            return "Sivir"
        elif id == 236: 
            return "Lucian"
        elif id == 107:
            return "Rengar"
        elif id == 19:
            return "Warwick"
        elif id == 72: 
            return "Skarner"
        elif id == 54: 
            return "Malphite"
        elif id == 157: 
            return "Yasuo"
        elif id == 101:
            return "Xerath"
        elif id == 17: 
            return "Teemo"
        elif id == 75: 
            return "Nasus"
        elif id == 58: 
            return "Renekton"
        elif id == 119:
            return "Draven"
        elif id == 35:
            return "Shaco"
        elif id == 50: 
            return "Swain"
        elif id == 91:
            return "Talon"
        elif id == 40: 
            return "Janna"
        elif id == 115: 
            return "Ziggs"
        elif id == 245: 
            return "Ekko"
        elif id == 61: 
            return "Orianna"
        elif id == 114: 
            return "Fiora"
        elif id == 9: 
            return "Fiddlesticks"
        elif id == 31: 
            return "Cho'Gath"
        elif id == 33: 
            return "Rammus"
        elif id == 7: 
            return "LeBlanc"
        elif id == 16: 
            return "Soraka"
        elif id == 26: 
            return "Zilean"
        elif id == 56: 
            return "Nocturne"
        elif id == 222: 
            return "Jinx"
        elif id == 83: 
            return "Yorick"
        elif id == 6: 
            return "Urgot"
        elif id == 203: 
            return "Kindred"
        elif id == 21: 
            return "Miss Fortune"
        elif id == 62: 
            return "Wukong"
        elif id == 53: 
            return "Blitzcrank"
        elif id == 98: 
            return "Shen"
        elif id == 201: 
            return "Braum"
        elif id == 5: 
            return "Xin Zhao"
        elif id == 29: 
            return "Twitch"
        elif id == 11: 
            return "Master Yi"
        elif id == 44: 
            return "Taric"
        elif id == 32: 
            return "Amumu"
        elif id == 41: 
            return "Gangplank"
        elif id == 48: 
            return "Trundle"
        elif id == 38: 
            return "Kassadin"
        elif id == 161:
            return "Vel'Koz"
        elif id == 143: 
            return "Zyra"
        elif id == 267: 
            return "Nami"
        elif id == 59: 
            return "Jarvan IV"
        elif id == 81: 
            return "Ezreal"

    def player_winrate(self,match_list):
    '''Finding the player winrate within the newest matches.
       
    Args:
    match_list(set):the match list of the player.
        
    Returns:
    player_winrate(float): The winrate of the player.
    '''
    wins_counter=0
    loss_counter=0
    player_winrate=[wins_counter,loss_counter]
        
        
    
    
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

def against_winrate(champ_name1,champ_name2):
    '''Finding the match wirnate of champions of two players.
       
    Args:
    champ_name1(str):The name of the champion that is being played by the player in your team.
    champ_name2(str):The name of the champion that is being played by the enemy player.
    
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