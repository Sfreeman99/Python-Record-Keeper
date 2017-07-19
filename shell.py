def main():
    print('Welcome to Ping Pong Records')
    name = input('what is your name: ').title()
    opponent_name = input('Opponent what is your name:').title()
    your_score = input('What was your score:')
    opponent_score = input('What was your opponent\'s score: ')
    if (name in recorder) and (opponent_name in recorder):
        if your_score > opponent_score:
            recorder[name]['Wins'] += 1
            recorder[opponent_name]['Losses'] += 1
        elif opponent_score > your_score:
            recorder[opponent_name]['Wins'] += 1
            recorder[name]['Losses'] += 1



recorder = {
        'Shedlia': {'Wins':0 , 'Losses':0 },
        'Jo':{'Wins': 0, 'Losses': 0}
        }
if __name__=='__main__':
    main()
