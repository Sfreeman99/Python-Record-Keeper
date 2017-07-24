def give_roster():
    with open("Roster.txt","r") as files:
        files.readline()
        contestants = files.readlines()
    roster = {}
    for item in contestants:
        sublist = item.split(', ')
        roster[sublist[0]] = {'Wins': int(sublist[1]),'Losses': int(sublist[2])}
    return roster

def add_roster():
    with open("Roster.txt", "r") as log:
        key_1, key_2, key_3 = log.readline().strip().split(', ')
        check_in = log.readlines()
    d = {}
    for item in check_in:
        Name, Wins, Losses = item.strip().split(', ')
        d = {key_1: Name, key_2: Wins, key_3: Losses}
    return d

