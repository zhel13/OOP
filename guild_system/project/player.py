from typing import Dict


class Player:

    def __init__(self, name: str, hp: int, mp: int) -> None:
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[str, int] = {}
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f'Skill {skill_name} added to the collection of the player {self.name}'
        return f'Skill already added'

    def player_info(self) -> str:
        result = (f'Name: {self.name}\n'
                f'Guild: {self.guild}\n'
                f'HP: {self.hp}\n'
                f'MP: {self.mp}\n')
        formated_items = [f'==={k} - {v}' for k, v in self.skills.items()]

        result += '\n'.join(formated_items) + '\n'
        return result
