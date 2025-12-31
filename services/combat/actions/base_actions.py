from abc import ABC, abstractmethod


class Action(ABC):
    name: str

    @abstractmethod
    def calculate_damage(self, attacker) -> float:
        pass