def give_roster():
    with open("Roster.txt","r") as files:
        files.readline()
        roster = files.readlines()
    return roster
        

    