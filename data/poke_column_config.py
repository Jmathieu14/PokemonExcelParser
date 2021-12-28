# Author: Jacques
# Date: 12/28/2021
# Time: 12:33 PM
from data.models.pokemon_column_model import PokeColumn


def get_poke_columns_config():
    return [PokeColumn('Card #', 2),
            PokeColumn('# Owned', 3),
            PokeColumn('Name', 1),
            PokeColumn('Rarity', 4),
            PokeColumn('Holo Count', 5),
            PokeColumn('Reverse-Holo Count', 6),
            PokeColumn('Type', 7)]
