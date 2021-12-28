import constants
import copy
import sys
import math



players_db = copy.deepcopy(constants.PLAYERS)
teams = copy.deepcopy(constants.TEAMS)

exp = []
noexp = []

panthers = []
bandits = []
warriors = []

def clean_data():
    for player in players_db:
        player['height'] = int(player['height'][:2])
        player['guardians'] = player['guardians'].split('and')
        player['guardians'] = list(player['guardians'])
        if player['experience'] == 'YES':
            player['experience'] = True
        else: 
            player['experience'] = False

clean_data()

for player in players_db:
    if player['experience'] == True:
        exp.append(player)
    else:
        noexp.append(player)
        
def assign_team(team):
    for player in exp:
        if len(team) != 3:
            team.append(player)
            exp.remove(player)
    for player in noexp:
        if len(team) != 6:
            team.append(player)
            noexp.remove(player)
            
assign_team(panthers)
assign_team(bandits)
assign_team(warriors)

def basketball_stats():

    while True:
        try:
            start_menu = int(input("====  MENU  ====\n"
                "Welcome to the Basketball Statistics Menu.\n" 
                "Please choose an option from the following menu by typing the corresponding number.\n"
                " 1.  Basketball Team Statistics\n"
                " 2.  Quit\n"
                "What would you like to do?  "
                ))
            if start_menu < 1 or start_menu > 2:
                raise ValueError("That's not a valid input.  Please enter the number corresponding with your choice to select.")
        except ValueError:
            print("That's not a valid input.  Please enter the number corresponding with your choice to select.")
        else:
            while start_menu == 1:
                try:    
                    choose_team = int(input("The following is the roster of active teams for the season.\n"
                        "\n"
                        "1.  PANTHERS\n"
                        "2.  BANDITS\n"
                        "3.  WARRIORS\n"
                        "\n"
                        "Please enter the number corresponding with the team and statistics would you like to access.   "))
                    if choose_team == 1:
                        print("\n===TEAM PANTHERS===\n")
                        print("\nNumber of Players: {}\n".format(len(panthers)))
                        panthers_list = []
                        panthers_string = ", "
                        for player in panthers:
                            panthers_list.append(player['name'])
                        print("\nNames of Players:\n",
                                panthers_string.join(panthers_list), "\n")
                        print("\nIndividual Player Information and Statistics:\n")
                        for index, player in enumerate(panthers, 1):
                            print(f'{index}.  {player}\n')
                    elif choose_team == 2:
                        print("\n===TEAM BANDITS===\n")
                        print("\nNumber of Players: {}\n".format(len(bandits)))
                        bandits_list = []
                        bandits_string = ", "
                        for player in bandits:
                            bandits_list.append(player['name'])
                        print("\nNames of Players:\n",
                                bandits_string.join(bandits_list), "\n")
                        print("\nIndividual Player Information and Statistics:\n")
                        for index, player in enumerate(bandits, 1):
                            print(f'{index}.  {player}\n')
                    elif choose_team == 3:
                        print("\n===TEAM WARRIORS===\n")
                        print("\nNumber of Players: {}\n".format(len(warriors)))
                        warriors_list = []
                        warriors_string = ", "
                        for player in warriors:
                            warriors_list.append(player['name'])
                        print("\nNames of Players:\n",
                                warriors_string.join(warriors_list), "\n")
                        print("\nIndividual Player Information and Statistics:\n")
                        for index, player in enumerate(warriors, 1):
                            print(f'{index}.  {player}\n')
                    elif choose_team < 1 or choose_team > 3:
                        raise ValueError("That's not a valid input.  Please enter the number corresponding with your choice to select.")
                except ValueError as err:
                        print("That's not a valid input.  Please enter the number corresponding with your choice to select.")
                else:
                    break
            else:
                break
        print("\n====Thank you for using the Basketball Statistics Tool!====\n")
            

if __name__ == '__main__':
    basketball_stats()
        