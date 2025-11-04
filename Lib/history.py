#The history data class. View this like a log

from dataclasses import dataclass
from typing import Any
@dataclass
class History:
    player: str
    action: str
    result:str
    hand: list[Any]
    soft_total: int
    hard_total: int
    game_ending_flag: bool
