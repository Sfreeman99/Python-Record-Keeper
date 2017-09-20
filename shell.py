from core import *
from record_disk import *

def get_players(team):
    ''' str -> {player: [str], score: int}
    get the players on a team
    '''
    players = input("Who was on {}?\n".format(team)).split()
    while True:
        score = input('What was the score?\n')
        if score.isnumeric():
            return {'name': team, 'players': players, 'score': int(score)}
        print('invalid')

def print_record(team_1, team_2):
    """ Item, Item -> None """
    t_1 = 'Player(s): {}\nScore: {}\n{}'.format(', '.join(team_1['players']), team_1['score'], team_1['win'])
    t_2 = 'Player(s): {}\nScore: {}\n{}'.format(', '.join(team_2['players']), team_2['score'], team_2['win'])
    print(t_1, t_2, sep="\n\n")

def main():
    print('Welcome To Record Keeper!!')
    
    while True:
        team_1 = get_players('Team 1')
        team_2 = get_players('Team 2')
        team_1, team_2 = winners_and_losers(team_1, team_2)
        roster = give_roster()
        roster = names(roster, team_1)
        roster = names(roster, team_2)
        print(roster)
        # add to records
        # update file
        print_record(team_1, team_2)
        if input('continue? (y/n) ') == 'y':
            continue
        else: 
            exit()
    

def one_vs_one_main():
    print('Welcome to Ping Pong Records')

    player_1 = input('what is your name: ').title()
    
    player_2 = input('Opponent what is your name:').title()
    
    

    new_roster = names(roster,player_1,player_2)

    dict_to_file(new_roster)

    p1_score = int(input('What was your score:'))
    
    p2_score = int(input('What was your opponent\'s score: '))
    
    new_record = record_game(player_1,p1_score,player_2,p2_score, roster)
    
    dict_to_file(new_record)

def two_vs_two_main():
    print('Works')


if __name__=='__main__':
    main()
