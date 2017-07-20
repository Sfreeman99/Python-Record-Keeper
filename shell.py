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

recorder_scores = {
        'Shedlia': {'Wins':0 , 'Losses':0 },
        'Jo':{'Wins': 0, 'Losses': 0}
        }

scores = {}
if __name__=='__main__':
    main()
