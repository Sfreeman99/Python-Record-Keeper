#need a function to see if both names in the recorder
def names(roster,player_1, player_2):
    ''' dict of names -> 
    
    Takes in both names and either sends you to the next function
    of adds the name of the player
    
    '''
    
    if not roster.get(player_1, False):
        roster[player_1] = {'Wins': 0, 'Losses': 0, 'Ties': 0}
    if not roster.get(player_2, False):
        roster[player_2] = {'Wins': 0, 'Losses': 0, 'Ties': 0}
    return roster

def record_game(player_1, p1_score, player_2, p2_score, roster):
    """ str, str, {'name': {'wins': int, 'losses': int}} -> {'name': {'wins': int, 'losses': int}}, str, str """
    if p1_score > p2_score:
        roster[player_1]['Wins'] += 1
        roster[player_2]['Losses'] += 1
    if p1_score < p2_score:
        roster[player_2]['Wins'] += 1
        roster[player_1]['Losses'] += 1

    if p1_score == p2_score:
        roster[player_1]['Ties'] += 1
        roster[player_2]['Ties'] += 1
    return roster
