from dataclasses import dataclass

@dataclass
class AppState:
    mousePos: tuple
    region: tuple
    tolerance: int
    color: tuple
    delay: int
    