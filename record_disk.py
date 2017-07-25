def give_roster():
    with open("Roster.txt","r") as files:
        files.readline()
        contestants = files.readlines()
    roster = {}
    for item in contestants:
        sublist = item.split(', ')
        roster[sublist[0]] = {'Wins': int(sublist[1]),'Losses': int(sublist[2])}
    return roster

def add_to_roster(roster):
    print(roster)


