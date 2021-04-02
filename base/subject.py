from dataclasses import dataclass
from abc import abstractmethod, ABCMeta


@dataclass
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def register_observer(self, obs):
        pass

    @abstractmethod
    def remove_observer(self, obs):
        pass

    @abstractmethod
    def notify_observer(self):
        pass
