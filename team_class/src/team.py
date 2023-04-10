class Team: 
    def __init__(self, name = str, players = list, coach = str):
        self.name = name
        self.players = players
        self.coach = coach
    
    # single_class_lab.md tasks tackled first so I created the add_player() 
    # and has_player() methods before creating the other functions

# Team is the class
# def __init__(self) is there so that every instance of the class has these properties
# must use dot notation to access the properties and store them in variables (e.g. self.name = name)
# then can access those properties when making any object out of the Team class
# in this example, I used dot notation to make reference to the name, players and coach properties present in the Team class
# I set the properties to the relevant data type in the def __init__ method

# 1
def team_has_name(self, name):
    return self.team.name

# 2
def team_has_players(self, players):
    return self.team.players

# 3
def team_has_coach(self, coach):
    return self.team.coach

# 4
def coach_can_be_changed(self, coach):
    return self.team.coach

# 5
def can_add_player_to_team(self, new_player):
    return len(self.team.add_player(new_player))

# B: Part 2:
    # Has player method (related to # 6 and # 7)
def has_player(self, name):
        if name in ["players"]:
            return True
        else: return False
# 6 and # 7
def check_player_in_team_found(self, name, players):
    has_player(self, name)
    if name in ["players"]:
        return True
    else: return None

# All of the tests have successfully passed :)

# Extension lab questions:

# 8
def team_has_points(self):
    return self.team.points

# 9 and # 10
def play_game_win(self, points):
    if points >= 3:
        return self.team.play_game(True)
    else: return False

# This was fun! :)





