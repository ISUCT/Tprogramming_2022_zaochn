from abc import ABC, abstractmethod, abstractproperty

class Player(ABC):

    @property
    @abstractmethod
    def health(self):
        pass

    @property
    @abstractmethod
    def power(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def class_name(self):
        pass

    @property
    @abstractmethod
    def ability_name(self):
        pass

    @property
    @abstractmethod
    def is_ability_activated(self):
        pass
    
    @property
    @abstractmethod
    def damage(self):
        pass

    @abstractmethod
    def special_ability(self):
        pass
