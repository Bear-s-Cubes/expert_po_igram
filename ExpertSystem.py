from experta import *

class ExperSystem(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.trust_scores = {
            "Dota2": 0.0,
            "Minecraft": 0.0,
            "Factorio": 0.0,
            "Poppy": 0.0,
            "WoT": 0.0,
        }
        self.distrust_scores = {
            "Dota2": 0.0,
            "Minecraft": 0.0,
            "Factorio": 0.0,
            "Poppy": 0.0,
            "WoT": 0.0,
        }
    
    def addTrust(self, game: str, multiplier: float):
        """
        Обновляет Меры доверия
        """
        self.trust_scores[game] += multiplier * (1 - self.trust_scores[game])

    def addDistrust(self, game: str, multiplier: float):
        """
        Обновляет Меры недоверия
        """
        self.distrust_scores[game] += multiplier * (1 - self.distrust_scores[game])

    @Rule(Fact(answ="1-1") | 
          Fact(answ="3-1") | 
          Fact(answ="3-2") |
          Fact(answ="7-1") |
          Fact(answ="7-2") )
    def handle_casual_player(self):
        """
        Игрок - казуальщик
        """        
        self.addTrust("Minecraft", 0.2)
        self.addDistrust("Dota2", 0.2)
        self.addDistrust("WoT", 0.2)

    @Rule(Fact(answ="1-2") | 
          Fact(answ="3-3") | 
          Fact(answ="3-4") |
          Fact(answ="7-4") )    
    def handle_tryhard_player(self):
        """
        Игрок - трайхардер
        """
        self.addTrust("Dota2", 0.2)
        self.addTrust("Minecraft", 0.2)
        self.addTrust("WoT", 0.2)

    @Rule(Fact(answ="1-1") | 
          Fact(answ="2-1") )
    def handle_steampunk_enjoyer(self):
        """
        Игрок любит сеттинг steampunk
        """
        self.addTrust("Minecraft", 0.2)
        self.addTrust("Factorio", 0.2)
        
    @Rule(Fact(answ ="5-1") | 
          Fact(answ ="6-1") | 
          Fact(answ = "7-2") | 
          Fact(answ = "13-1"))
    def handle_Singler(self):
        self.addTrust("Poppy", 0.4)
        self.addTrust("Minecraft", 0.3)
        self.addTrust("Factorio", 0.4)
        self.addTrust("WoT", 0.1)
        self.addDistrust("Dota2", 0.4)
    
    @Rule(Fact(answ ="5-2") | 
          Fact(answ ="6-2") | 
          Fact(answ = "7-3") | 
          Fact(answ = "13-2"))
    def handle_Coop(self):
        self.addDistrust("Poppy", 0.2)
        self.addTrust("Minecraft", 0.4)
        self.addTrust("Factorio", 0.2)
        self.addTrust("WoT", 0.3)
        self.addTrust("Dota2", 0.4)
    
    @Rule(Fact(answ ="5-3") | 
          Fact(answ ="6-3") | 
          Fact(answ = "7-1") | 
          Fact(answ = "13-3"))
    def handle_Multi(self):
        self.addDistrust("Poppy", 0.4)
        self.addTrust("Minecraft", 0.2)
        self.addDistrust("Factorio", 0.2)
        self.addTrust("WoT", 0.5)
        self.addTrust("Dota2", 0.5)
        
    @Rule(Fact(answ ="1-2") | 
          Fact(answ = "8-2") |
          Fact(answ = "9-1") |
          Fact(answ = "11-2") | 
          Fact(answ ="12-3"))
    def handle_TrueTryhard(self):
        self.addTrust("Factorio", 0.4)
        self.addTrust("WoT", 0.3)
        self.addTrust("Dota2", 0.5)
        self.addDistrust("Minecraft", 0.1)
        self.addDistrust("Poppy", 0.4)
        
    @Rule(Fact(answ ="1-3") |
          Fact(answ = "7-1") | 
          Fact(answ ="8-3") | 
          Fact(answ = "10-2") | 
          Fact(answ = "12-2") |
          Fact(answ = "13-4") |
          Fact(answ ="14-1"))
    def handle_Mind(self):
        self.addTrust("Factorio", 0.5)
        self.addTrust("Minecraft", 0.2)
        self.addDistrust("Poppy", 0.3)
        self.addDistrust("WoT", 0.3)
        self.addDistrust("Dota2", 0.2)
        