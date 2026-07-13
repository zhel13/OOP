from typing import List

from OOP.guild_system.project.player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player):
        if player.name not in self.players:
            self.players.append(player)
            player.guild = self.name
            return f'Welcome player {player.name} to the guild {self.name}'
        elif player.name in self.players and player.guild != self.name:
            return f'Player {player.name} is in another guild.'
        return f'Player {player.name} is already in the guild'

    def kick_player(self, player_name: str):
        try:
            player = [p for p in self.players if p.name == player_name][0]
            self.players.remove(player)
            player.guild = 'Unaffiliated'
            return f"Player {player_name} has been removed from the guild."
        except IndexError:
            return f'Player {player_name} is not in the guild'

    def guild_info(self):
        guild_info = f"Guild: {self.name}\n"
        guild_info += '\n'.join(p.player_info() for p in self.players)
        return guild_info


