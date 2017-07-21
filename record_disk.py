def give_roster():
    with open("Roster.txt","r") as files:
        files.readline()
        roster = files.readlines()
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

def print_to_roster(roster,player_1, player_2):
    print(roster.keys())
    with open("Roster.txt", "a") as files:
        files.write("{}".format(roster))
        
        

    