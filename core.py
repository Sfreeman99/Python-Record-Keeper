#need a function to see if both names in the recorder
def winners_and_losers(team_1, team_2):
    """ Item, Item -> Item, Item """
    if team_1['score'] > team_2['score']:
        team_1['win'] = 'WINNER'
        team_2['win'] = 'LOSER'
    else:
        team_1 ['win'] = 'LOSER'
        team_2['win'] = 'WINNER'
    return team_1, team_2


def names(roster,team):
    ''' dict of names, Item -> dict of names
    
    Takes in both names and either sends you to the next function
    of adds the name of the player
    
    '''
    for player in team['players']:
        if not roster.get(player, False):
            roster[player] = {'Wins': 0, 'Losses': 0}
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
