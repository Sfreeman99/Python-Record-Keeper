from core import *
from record_disk import *

def main():
    print('Welcome to Ping Pong Records')

    player_1 = input('what is your name: ').title()
    
    player_2 = input('Opponent what is your name:').title()
    
    roster = give_roster()

    new_roster = names(roster,player_1,player_2)

    dict_to_file(new_roster)

    p1_score = int(input('What was your score:'))
    
    p2_score = int(input('What was your opponent\'s score: '))
    
    new_record = record_game(player_1,p1_score,player_2,p2_score, roster)
    
    dict_to_file(new_record)

if __name__=='__main__':
    main()
