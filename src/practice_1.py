from typing import List


class Player:
    def __init__(self, name, xp, team):
        self.name: str = name
        self.xp: int = xp
        self.team: str = team

    def introduce(self):
        print(f"Hello, I am {self.name} from team {self.team}.")


class Team:

    def __init__(self, team_name):
        self.team_name: str = team_name
        self.players: List[Player] = []

    # public
    def add_player(self, name, xp):
        new_player = Player(name, xp, self.team_name)
        self.players.append(new_player)

    def show_players(self):
        for player in self.players:
            player.introduce()

    def remove_player(self, name):
        player_index = self._find_player_index(name)
        if player_index is None:
            print(f"Player {name} not found.")
            return
        self.players.pop(player_index)

    def all_players_xp(self):
        total_xp = 0
        for player in self.players:
            total_xp += player.xp
        print(f"Total {self.team_name} XP: {total_xp}")

    # private
    def _find_player_index(self, name):
        for i, player in enumerate(self.players):
            if player.name == name:
                return i


team_x = Team("Team X")
team_blue = Team("Team Blue")

team_x.add_player("nico", 1200)
team_x.add_player("bryon", 1300)
team_x.add_player("thor", 1500)
team_blue.add_player("lynn", 1000)
team_blue.add_player("spet", 1000)
team_blue.add_player("kate", 1000)

team_x.show_players()
team_blue.show_players()

team_x.remove_player("bryon")
team_x.show_players()

team_x.all_players_xp()
team_blue.all_players_xp()
