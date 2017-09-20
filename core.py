#need a function to see if both names in the recorder
def winners_and_losers(team_1, team_2):
    """ Item, Item -> Item, Item """
    if team_1['score'] > team_2['score']:
        team_1['win'] = 'WINNER'
        team_2['win'] = 'LOSER'

    elif team_1['score'] == team_2['score']:
        team_1['win'] = 'TIE'
        team_2['win'] = 'TIE'

    else:
        team_1['win'] = 'LOSER'
        team_2['win'] = 'WINNER'
    return team_1, team_2


def names(roster, team):
    ''' dict of names, Item -> dict of names
    
    Takes in both names and either sends you to the next function
    of adds the name of the player
    
    '''
    for player in team['players']:
        if not roster.get(player, False):
            roster[player] = {'Wins': 0, 'Losses': 0, 'Ties': 0}
    return roster


def record_game(team_1, team_2, roster):
    """ str, str, {'name': {'wins': int, 'losses': int}} -> {'name': {'wins': int, 'losses': int}}, str, str """
    if team_1['score'] > team_2['score']:
        for player in team_1['players']:
            roster[player]['Wins'] += 1
        for player in team_2['players']:
            roster[player]['Losses'] += 1
    elif team_1['score'] < team_2['score']:
        for player in team_1['players']:
            roster[player]['Losses'] += 1
        for player in team_2['players']:
            roster[player]['Wins'] += 1
    elif team_1['score'] == team_2['score']:
        for player in team_1['players']:
            roster[player]['Ties'] += 1
        for player in team_2['players']:
            roster[player]['Ties'] += 1
    return roster
