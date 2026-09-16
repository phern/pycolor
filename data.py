from dataclasses import dataclass


# attempt to manage program data with a data class
@dataclass
class AppState:
    points: list
    mousePos: tuple
    region: tuple
    tolerance: int
    color: tuple
    delay: float
    
    # calculate points of rectangle for scanning and matching
    def calculateRegion(self):
        x1 = min(self.points[0][0], self.points[1][0])
        y1 = min(self.points[0][1], self.points[1][1])
        x2 = max(self.points[0][0], self.points[1][0])
        y2 = max(self.points[0][1], self.points[1][1])
        width = x2 - x1
        height = y2 - y1
        self.region = (
            x1,
            y1,
            width,
            height
        )

