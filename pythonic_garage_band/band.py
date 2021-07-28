from abc import ABC, abstractmethod



class Musician:
    
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass
    
    @abstractmethod
    def get_instrument(self):
        pass
    
    @abstractmethod
    def play_solo(self):
        pass

names = []

class Band:
    
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def to_list(self):
        names.append(self.name)
        return names

    def play_solos(self):
        solos = []
        solos.append(Guitarist.play_solo(self))
        solos.append(Bassist.play_solo(self))
        solos.append(Drummer.play_solo(self))
        return solos

    def __str__(self):
        pass

    def __repr__(self):
        pass


class Guitarist(Musician):

    def __init__(self,name):
        self.name = name

    def __str__(self):
       return "My name is " + str(self.name) +  " and I play guitar"

    def __repr__(self):
        return "Guitarist instance. Name = " + str(self.name) 

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"

class Drummer(Musician):

    def __init__(self,name):
        self.name = name

    def __str__(self):
       return "My name is " + str(self.name) +  " and I play drums"

    def __repr__(self):
        return "Drummer instance. Name = " + str(self.name) 

    def get_instrument(self):
        return "drums"
    
    def play_solo(self):
        return "rattle boom crash"

class Bassist(Musician):

    def __init__(self,name):
        self.name = name

    def __str__(self):
       return "My name is " + str(self.name) +  " and I play bass"

    def __repr__(self):
        return "Bassist instance. Name = " + str(self.name) 

    def get_instrument(self):
        return "bass"
    
    def play_solo(self):
        return "bom bom buh bom"

