
recorder = { 'Shedlia': {'Wins':0 , 'Lost':0 }}

print('Welcome to Ping Pong Records')
name = input('what is your name: ')
for item in recorder:
    if item == name:
        print(recorder[item])
    else:
        print('Name not found...')
        