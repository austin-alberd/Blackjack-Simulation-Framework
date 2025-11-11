
from dataclasses import dataclass
from typing import Any
from history import History

@dataclass
class Game_Log_Entry:
    GameHistory: list[History]

