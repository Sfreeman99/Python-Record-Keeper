from core import *

def main():
    print('Welcome to Ping Pong Records')

    player_1 = input('what is your name: ').title()
    
    player_2 = input('Opponent what is your name:').title()
    
    recorder = recorder_scores
    
    names(roster,p1_score,p2_score)
    
    p1_score = input('What was your score:')
    
    p2_score = input('What was your opponent\'s score: ')
    
    scores(your_score,opponent_score)

recorder_scores = {
        'Shedlia': {'Wins':0 , 'Losses':0 },
        'Jo':{'Wins': 0, 'Losses': 0}
        }
        roster[winner]['wins'] = roster[winner]['wins'] + 1

# def main():
#     roster, winner, loser = record_game(player_1, p1_score, player_2, p2_score, roster)

scores = {}
if __name__=='__main__':
    main()
