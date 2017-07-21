#need a function to see if both names in the recorder
def names(recorder,name, opponent_name):
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
    if (name in recorder) and (opponent_name in recorder):
        return None
    elif (name not in recorder) or (opponent_name not in recorder):
        if name not in recorder:
            recorder[name] = {'Wins': 0, 'Losses': 0}
        if opponent_name not in recorder:
            recorder[opponent_name] = {'Wins': 0, 'Losses': 0}
        return recorder
        
def scores(your_score, opponent_score):
    ''' '''
               

#need another function to compare the scores
def compare_score(recorder, scores):
    '''(dict, dict) -> 
    
    takes in both scores and compares them to each other
    then returns who won and who loss
    
    >>> compare_score({'Shedlia':{'Wins': 0, 'Losses': 0}, 'Jo': {'Wins': 0, 'Losses': 0}}, {'a': 3, 'b': 7})'''
    if your_score > opponent_score:
        recorder[name]['Wins'] += 1
        recorder[opponent_name]['Losses'] += 1
        return recorder[name]['Wins'] and recorder[opponent_name]['Losses']
    elif your_score < opponent_score:
        recorder[opponent_name]['Wins'] += 1
        recorder[name]['Losses'] += 1
        return recorder[opponent_name]['Wins'] and recorder[name]['Losses']