from core import *

def main():
    print('Welcome to Ping Pong Records')
    name = input('what is your name: ').title()
    opponent_name = input('Opponent what is your name:').title()
    recorder = recorder_scores
    names(recorder,name,opponent_name)
    your_score = input('What was your score:')
    opponent_score = input('What was your opponent\'s score: ')
    scores(your_score,opponent_score)
    # if (name in recorder) and (opponent_name in recorder):
    #     if your_score > opponent_score:
    #         recorder[name]['Wins'] += 1
    #         recorder[opponent_name]['Losses'] += 1
    #     elif your_score < opponent_score:
    #         recorder[opponent_name]['Wins'] += 1
    #         recorder[name]['Losses'] += 1
    # elif (name not in recorder) or (opponent_name not in recorder):
    #     if name:
    #         recorder[name] = {'Wins': 0, 'Losses': 0}
    #     if opponent_name:
    #         recorder[opponent_name] = {'Wins': 0, 'Losses': 0}

            


recorder_scores = {
        'Shedlia': {'Wins':0 , 'Losses':0 },
        'Jo':{'Wins': 0, 'Losses': 0}
        }

scores = {}
if __name__=='__main__':
    main()
