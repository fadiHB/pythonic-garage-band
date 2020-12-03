from abc import ABC,abstractmethod


class Band(ABC):

    list_of_Bands = []

    def __init__(self, name, members):
      self.name = name
      self.members = members
      Band.list_of_Bands.append(self)

    @classmethod
    def to_list(cls):
        return cls.list_of_Bands


    def play_solos(self):
        list_of_play_solo = []
        for i in range(len(self.members)):
            list_of_play_solo.append(self.members[i].play_solo())

        return list_of_play_solo
        

    def __repr__(self):
        return (f"{self.name}")

    def __str__(self):
        return (f"{self.name}")


class Musician(Band):
    list_of_Musicians = []

    def __init__(self, name):
      self.name = name

      Musician.list_of_Musicians.append(self)

    @classmethod
    def to_list(cls):
        return cls.list_of_Musicians

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass

    def __str__(self):
        return (f"My name is {self.name} and I play {(self.get_instrument)}")

    def __repr__(self):
        return( f'{self.name} <Musician>' )

    

class Guitarist(Musician):

    def __init__(self,name):
        super().__init__(name)

    def get_instrument(self):
        print('Guitar')

    def play_solo(self):
        return('face melting guitar solo')
    

class Bassist(Musician):

    def __init__(self, name):
      super().__init__(name)

    def get_instrument(self):
        print('Bass')

    def play_solo(self):
        return('bom bom buh bom')
    

class Drummer(Musician):

    def __init__(self,name):
        super().__init__(name)

    def get_instrument(self):
        print('drums')

    def play_solo(self):
        return('rattle boom crash')
    


if __name__ == "__main__":
    player1 = Guitarist ('fadi')
    player2 = Bassist ('hadi')
    player3 = Drummer ('shadi')

    Band1 = Band ('Rockers' ,[player1,player2,player3])

    print(Band.to_list())
    print(Musician.to_list())
    print(Band1.play_solos())