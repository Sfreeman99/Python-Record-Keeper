from core import *
from record_disk import *


def get_players(team):
    ''' str -> {player: [str], score: int}
    get the players on a team
    '''
    players = input("Who was on {}?\n".format(team)).title().split()
    while True:
        score = input('What was the score?\n')
        if score.isnumeric():
            return {'name': team, 'players': players, 'score': int(score)}
        print('invalid')


def print_record(team_1, team_2):
    """ Item, Item -> None """
    t_1 = 'Player(s): {}\nScore: {}\n{}'.format(', '.join(team_1['players']),
                                                team_1['score'], team_1['win'])
    t_2 = 'Player(s): {}\nScore: {}\n{}'.format(', '.join(team_2['players']),
                                                team_2['score'], team_2['win'])
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
        record_game(team_1, team_2, roster)
        dict_to_file(roster)

        # add to records
        # update file
        print_record(team_1, team_2)
        if input('continue? (y/n) ') == 'y':
            continue
        else:
            exit()


if __name__ == '__main__':
    main()
