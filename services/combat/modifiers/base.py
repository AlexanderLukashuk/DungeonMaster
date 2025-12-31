from abc import ABC, abstractmethod


class DamageModifier(ABC):
    @abstractmethod
    def apply(self, context):
        pass