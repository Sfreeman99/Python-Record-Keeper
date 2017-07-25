def give_roster():
    with open("Roster.txt","r") as files:
        files.readline()
        contestants = files.readlines()
    roster = {}
    for item in contestants:
        sublist = item.split(', ')
        roster[sublist[0]] = {'Wins': int(sublist[1]),'Losses': int(sublist[2])}
    return roster

# def add_to_roster(roster):
#     with open("Roster.txt", "a") as files:
#         files.write('\n{}, {}, {}'.format(roster[0], roster[1], roster[2]))
    
def dict_to_file(new_roster):
    message = 'Name, Wins, Losses\n'
    for key, value in new_roster.items():
        message += '{}, {}, {}\n'.format(key, value['Wins'], value['Losses'])
    with open("Roster.txt", "w") as files:
        files.write(message)
            

