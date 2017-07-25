from core import *
from record_disk import *

def main():
    print('Welcome to Ping Pong Records')

    player_1 = input('what is your name: ').title()
    
    player_2 = input('Opponent what is your name:').title()
    
    roster = give_roster()

    roster = give_name(roster,player_1,player_2)

    add_to_roster(roster)
    
    p1_score = int(input('What was your score:'))
    
    p2_score = int(input('What was your opponent\'s score: '))
    
    

# recorder_scores = {
#         'Shedlia': {'Wins':0 , 'Losses':0 },
#         'Jo':{'Wins': 0, 'Losses': 0}
#         }
#         roster[winner]['wins'] = roster[winner]['wins'] + 1
# def main():
#     roster = record_game(player_1, p1_score, player_2, p2_score, roster)
if __name__=='__main__':
    main()
