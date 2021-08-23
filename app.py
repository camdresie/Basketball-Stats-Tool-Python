import math
import constants

PLAYERS = constants.PLAYERS
TEAMS = constants.TEAMS
cleaned_players = []


def clean_data(players):
    for player in players:
        player['height'] = int(player['height'][0:2])
        player['experience'] = True if player['experience'] == 'YES' else False
        cleaned_players.append(player)


def balance_teams(players, teams):
    players_per_team = math.floor(len(players) / len(teams))
    slice_index_start = 0
    slice_index_end = players_per_team
    balanced_teams = {}
    for team in teams:
        players_list = cleaned_players[slice_index_start:slice_index_end]
        slice_index_start += players_per_team
        slice_index_end += players_per_team
        balanced_teams[team] = players_list
    return balanced_teams


def print_stats(teams, team):
    print(f'{team}\n')
    print(f'Number of Players: {len(teams[team])}\n')
    players_list = []
    for player in teams[team]:
        players_list.append(player['name'])
    print(f'{players_list}\n')


def app_header():
    print('BASKETBALL TEAM STATS TOOL\n')
    print('---MENU---\n')


def get_user_input_continue():
    invalid = True
    while invalid:
        user_choice = input("""Here are your choices:\nA). Display Team Stats\nB). Quit\nPlease enter A or B: \n""").lower()
        if user_choice == 'a' or user_choice == 'b':
            return user_choice


def list_teams(teams):
    for index, team in enumerate(teams, 1):
        print(f'{index}. {team}')


def get_user_team_input(teams):
    invalid = True
    choice_list = [i for i in range(1, len(teams) + 1)]
    while invalid:
        user_choice = input(f"""Choose a number 1 - {len(teams)}\n""")
        try:
            user_choice = int(user_choice)
            if user_choice in choice_list:
                return user_choice
            else:
                raise ValueError
        except ValueError:
            print(f"You must choose a number 1 - {len(teams)}\n")


def list_team_stats(teams, user_input):
    team_map = {}
    target_team = ''
    index = 1
    for team in teams:
        team_map[index] = team
        index += 1
    target_team = team_map[user_input]
    team_players = [player['name'] for player in teams[target_team]]
    team_players = ', '.join(team_players)
    experience_total = 0
    inexperienced_total = 0
    height_total = 0
    for player in teams[target_team]:
        height_total += player['height']
        if player['experience']:
            experience_total += 1
        else:
            inexperienced_total += 1
    print(f'Team: {target_team}')
    print('--------------------')
    print(f"Total Players: {len(teams[target_team])}")
    print(f"Total Experienced: {experience_total}")
    print(f"Total Inexperienced: {inexperienced_total}")
    print(f"Average Player Height: {round(height_total / len(teams[target_team]), 2)} inches\n")
    print(f"Players on the Team: \n{team_players}\n")


if __name__ == '__main__':
    app_header()
    clean_data(PLAYERS)
    teams = balance_teams(PLAYERS, TEAMS)
    user_choice = ''
    while user_choice != 'b':
        user_choice = get_user_input_continue()
        if user_choice == 'a':
            list_teams(teams)
            user_num = get_user_team_input(teams)
            list_team_stats(teams, user_num)
    print("Thanks for using the stats tool!")

