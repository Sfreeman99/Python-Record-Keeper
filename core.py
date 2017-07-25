#need a function to see if both names in the recorder
def names(roster,player_1, player_2):
    ''' dict of names -> 
    
    Takes in both names and either sends you to the next function
    of adds the name of the player
    
    >>> names({'Shedlia':{'Wins': 0, 'Losses': 0 }, 'Jo': {'Wins': 0, 'Losses': 0 }, 'Penny': {'Wins': 0, 'Losses': 0 }}, 'Shedlia', 'Jo')
    >>> names({'Shedlia':{'Wins': 0, 'Losses': 0 }, 'Jo': {'Wins': 0, 'Losses': 0 }, 'Penny': {'Wins': 0, 'Losses': 0 }}, 'Shedlia', 'Billy')
    {'Shedlia':{'Wins': 0, 'Losses': 0 }, 'Jo':{'Wins': 0, 'Losses': 0 }, 'Billy':{'Wins': 0, 'Losses': 0 }, 'Penny':{'Wins': 0, 'Losses': 0 }}
    >>> names({'Shedlia':{'Wins': 0, 'Losses': 0 }, 'Jo': {'Wins': 0, 'Losses': 0 }, 'Penny': {'Wins': 0, 'Losses': 0 }}, 'Dil', 'Jo')
    {'Shedlia':{'Wins': 0, 'Losses': 0 }, 'Jo':{'Wins': 0, 'Losses': 0 }, 'Dil':{'Wins': 0, 'Losses': 0}, 'Penny':{'Wins': 0, 'Losses': 0 }}    
    >>> names({'Shedlia':{'Wins': 0, 'Losses': 0 }, 'Jo': {'Wins': 0, 'Losses': 0 }, 'Penny': {'Wins': 0, 'Losses': 0 }}, 'Duke', 'Dil')
    {'Shedlia':{'Wins': 0, 'Losses': 0 }, 'Jo':{'Wins': 0, 'Losses': 0 }, 'Dil':{'Wins': 0, 'Losses': 0}, 'Penny':{'Wins': 0, 'Losses': 0 }, 'Duke': {'Wins': 0, 'Losses': 0}}
    >>> names({'Shedlia':{'Wins': 0, 'Losses': 0 }, 'Jo': {'Wins': 0, 'Losses': 0 }, 'Penny': {'Wins': 0, 'Losses': 0 }}, 'Penny', 'Jo')
    '''
    
    if not roster.get(player_1, False):
        roster[player_1] = {'Wins': 0, 'Losses': 0}
    if not roster.get(player_2, False):
        roster[player_2] = {'Wins': 0, 'Losses': 0}
    return roster

def record_game(player_1, p1_score, player_2, p2_score, roster):
    """ str, str, {'name': {'wins': int, 'losses': int}} -> {'name': {'wins': int, 'losses': int}}, str, str """
    print(roster)
    if p1_score > p2_score:
        roster[player_1]['Wins'] += 1
        roster[player_2]['Losses'] += 1
    else:
        roster[player_2]['Wins'] += 1
        roster[player_1]['Losses'] += 1
    return roster

def give_name(roster, player_1, player_2):
    for item in roster:
        print(item)
        if item != player_1:
            return player_1
        if item != player_2:
            return player_2