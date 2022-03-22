from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def serialize(self) -> str:
        pass
