'A script for helping players figure out whether dodge is necessary in a current League of Legends game.'
import requests
import pandas as pd
import time
import matplotlib.pyplot as plt

class Winrate:
    def __init__(self,region,user_id,api_key):
        self.region=region
        self.user_id=user_id
        self.api=api_key

    def acc_id(self):
        '''Finding the encrypted account id of the player.
            
        Returns:
            acc_id(str): the encrypted account id of the player.
        '''
        endpoint= 'https://'+self.region+'.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+self.user_id+'?api_key='+self.api
        response =requests.get(endpoint)
        response.raise_for_status()
        summoner_data=response.json()
        acc_id=summoner_data['accountId']
        return acc_id
        
    
    def get_match_list(self,acc_id,queue_id,endindex):
        '''Finding the match list of the player.
        
        Args:
        acc_id(str): The encrypted account id of the player.
        queue_id(str): The queue type of the game, 420 for solo/duo, 440 for 
        rank flex.
        endindex(str): The range you want to search for. The maximum range is 
        30.    
        
        Returns:
            match_df(set): the match_df contains lists of matches of the player.
        '''
        endpoint= 'https://'+self.region+'.api.riotgames.com/lol/match/v4/matchlists/by-account/'+acc_id+'?queue='+queue_id+'&endIndex='+endindex+'&api_key='+self.api
        response =requests.get(endpoint)
        response.raise_for_status()
        match_list=response.json()
        matches=match_list['matches']
        final_match_list=[]
        for games in matches:
            champion_name=games['champion']
            match_id=games['gameId']
            games_tuple=champion_name,str(match_id)
            final_match_list.append(games_tuple)
            
        b=((n, s) for n, s in final_match_list)        
        match_df=pd.DataFrame(b)
        match_df.columns = ['Champion ID', 'Match ID']
        return match_df
        

    
    def win_or_loss(self,match_id,acc_id):
        '''Finding if the game was win or lose of a specific match id.
        
        Args:
        match_id(str): The match_id of a specific game.
        acc_id(str): The encrypted account id of the player.   
        
        Returns:
            wf_tuple(tuple): the first element for this tuple is the match id, 
            and the second element for this tuple is whether the game was win 
            or loss.
                             
        '''
        endpoint='https://'+self.region+'.api.riotgames.com/lol/match/v4/matches/'+match_id+'?api_key='+self.api
        response =requests.get(endpoint)
        response.raise_for_status()
        ingame_info=response.json()
        all_participant_info=ingame_info["participantIdentities"]
        participantid_counter=0
        for each_participant in all_participant_info:
            if each_participant['player']['accountId']==acc_id:
                participantid_counter = each_participant['participantId']
        team_info=ingame_info['teams']
        win_or_not=0
        if participantid_counter in range(1,6):
            win_or_not=team_info[0]['win']
        else:
            win_or_not=team_info[1]['win']
        wf_tuple = match_id,win_or_not
        
        return  wf_tuple

    
    
    def win_loss_graph(self,match_df,acc_id):
        '''Finding if games in a dataframe were win or lose.
        
        Args:
        match_df(str): match_df(set): the match_df contains lists of matches 
        of the player.
        acc_id(str): The encrypted account id of the player.   
        
        Returns:
            final_df(DataFrame): the dataframe that contains the champion id,
            match id and win/fail
                             
        '''
        total_list=[]
        for each_id in match_df['Match ID']:
            time.sleep(0.05)
            win_loss_tuple = self.win_or_loss(each_id,acc_id)
            total_list.append(win_loss_tuple)
        b=((n, s) for n, s in total_list)        
        win_loss_df=pd.DataFrame(b)
        win_loss_df.columns = ['Match ID', 'Win/Fail']
        final_df=pd.merge(match_df,win_loss_df,how='left',on='Match ID')
        return final_df

    def champ_name_id_list(self):
        '''Getting the information of champion names and their related champion 
        ids.
          
        Returns:
            champ_list(list): A list contains the champion names and related 
            champion ids.                    
        '''
        champ_list=[]
        a='http://ddragon.leagueoflegends.com/cdn/10.10.3208608/data/en_US/champion.json'
        response =requests.get(a)
        champion_data=response.json()
        for i in champion_data['data']:
            champ_name_id=i,champion_data['data'][i]['key']
            champ_list.append(champ_name_id)
        return champ_list

    def get_champ_name(self,champ_id):
        '''Getting the information of champion name based on champion id.
          
        Returns:
            champ_name(str): the champion name.                    
        '''
        champ_name=''
        champion_list=self.champ_name_id_list()
        for i in champion_list:
            a,b=i
            if b==champ_id:
                champ_name=a
        return champ_name
          
    def get_champ_id(self,champ_name):
        '''Getting the information of champion id based on champion name.
          
        Returns:
            champ_id(str): the champion id.                    
        '''
        champ_id=''
        champion_list=self.champ_name_id_list()
        for i in champion_list:
            a,b=i
            if a == champ_name:
                champ_id=b
        return champ_id



    def get_graph(self,df):
        '''Add Champ_Name coloumn to a dataframe.
        
        Args:
            df(DataFrame):the target dataframe for modified
        Returns:
            final_df(DataFrame): the dataframe contains the information of 
            champion names.                    
        '''
        champ_name_list=[]
        for champ_id in df['Champion ID']:
            champ_name=self.get_champ_name(str(champ_id))
            champ_name_list.append(champ_name)
        final_df=df.assign(Champ_Name=champ_name_list)
        final_df=final_df.reindex(columns=['Champion ID','Champ_Name',
                                           'Match ID','Win/Fail'])
        return final_df

    def champ_winrate(self,df):
        '''Calculate the winrate of a dataframe.
        
        Args:
            df(DataFrame):the dataframe for winrate calculating.
        Returns:
            game_df(DataFrame): the dataframe contains winrate information.                    
        '''
        game_dict=dict()
        df_champ_win=pd.Series(df['Win/Fail'])
        df_champ_win.index=df['Champ_Name']
    
        win_list=[]
        lose_list=[]
        for i,k in df_champ_win.iteritems():
            if k =='Win':
                win_list.append(i)
            elif k=='Fail':
                lose_list.append(i)
                
        for i,k in df_champ_win.iteritems():
            wins=win_list.count(i)
            loses=lose_list.count(i)
            winrate=round(wins/(wins+loses),2)
            game_dict[i]=winrate
        game_df = pd.DataFrame(list(game_dict.items()),
                               columns = ['Champion Name','Winrate'])
        return game_df

            
    def all_winrate(self,queue_id,endindex):
        '''The function goes through all the process for getting final df
    
        Args:
            
            queue_id(str): The queue type of the game, 420 for solo/duo, 440 
            for rank flex.
            endindex(str): The range you want to search for. The maximum range 
            is 30. 
        Returns:
            get_champ_winrate(DataFrame): the dataframe contains all the 
            information.                    
        '''
        get_encrypted_id=self.acc_id() 
        get_match_list_df=self.get_match_list(get_encrypted_id,queue_id,endindex)
        get_win_loss_df=self.win_loss_graph(get_match_list_df,get_encrypted_id)
        get_final_graph=self.get_graph(get_win_loss_df)
        get_champ_winrate=self.champ_winrate(get_final_graph)
        return get_champ_winrate

    def champ_mastery(self,champ_name):
        '''The function for getting the champion level and champion mastery 
        points.
    
        Args:
            
            champ_name(str):the champion name searching for. 
        Returns:
            mastery_pt(tuple): the tuple contains champion level and champion 
            points.                    
        '''
        endpoint1= 'https://'+self.region+'.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+self.user_id+'?api_key='+self.api
        response1 =requests.get(endpoint1)
        response1.raise_for_status()
        summoner_data=response1.json()
        sum_id=summoner_data['id'] 
        a=self.get_champ_id(champ_name)
        endpoint2='https://'+self.region+'.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/'+sum_id+'/by-champion/'+a+'?api_key='+self.api
        response2 =requests.get(endpoint2)
        response2.raise_for_status()
        champion_data=response2.json()
        
        champ_level=champion_data['championLevel']
        champ_points=champion_data['championPoints']
        mastery_pt=champ_level,champ_points
        return mastery_pt
    
def main():
    region=''
    while region not in ['br1','eun1','euw1','jp1','kr','la1','la2','na1','oc1',
                         'tr1','ru']:
        print('Regions:br1/eun1/euw1/jp1/kr/la1/la2/na1/oc1/tr1/ru')
        region=input('Which region are you playing(select one from above)?: ')   
    name1=input("The summoner name: ")
    
    api_key=input("Input the api key u got: ")
    
    queue_type=''
    while queue_type not in ['1','2']:
        queue_type=input("Input 1 for solo/duo, 2 for rank flex: " )

    if queue_type=='1':
        queue_id=str(420)
    elif queue_type=='2':
        queue_id=str(440) 
    
    games_num='100'
    while int(games_num) not in range(10,31):
        games_num=input('How many games you want to search for?(range is 10~30): ')
    
    champ=''
    lmao=Winrate('na1','1 gpa',api_key)
    alist=lmao.champ_name_id_list()
    blist=[]
    for i in alist:
        haha,baba=i
        blist.append(haha)        
    while champ not in blist:
        champ=input('What champ is relating to this summoner name?:')
    
    champ_playing=champ.capitalize()
    #data for first player:
    a=Winrate(region,name1,api_key)
    df1=a.all_winrate(queue_id,games_num)
    bbb=a.champ_mastery(champ_playing)
    bbb1,bbb2=bbb
    print('-------------------------------------------')
    print('-------------------------------------------')
    print('-------------------------------------------')
    print('Summoner name: '+name1)
    print('This summoner is playing: '+champ)
    print('The champion level is: '+str(bbb1))
    print('The champion mastery is: '+str(bbb2))
    print('Please wait for 30 second to let the code run.-----')
    print('The winrate of this summoner winthin '+games_num+'games,is: ')
    print(df1)
    plt.bar(df1['Champion Name'],df1['Winrate'])
    plt.show()
    
if __name__ == "__main__":    
    main()
