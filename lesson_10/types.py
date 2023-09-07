from typing import Protocol


class CanCalculateArea(Protocol):
    def calculate_area(self) -> float:
        ...