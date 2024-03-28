from experta import *

class ExperSystem(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.trust_scores = {
            "Dota2": 0,
            "Minecraft": 0,
            "Factorio": 0,
            "Poppy": 0,
            "WoT": 0,
        }
        self.distrust_scores = {
            "Dota2": 0,
            "Minecraft": 0,
            "Factorio": 0,
            "Poppy": 0,
            "WoT": 0,
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
        self.distrust_scores[game] += multiplier * (1 - self.trust_scores[game])

    @Rule(Fact(answ="1-1") | Fact(answ="2-1"))
    def handle_casual_player(self):
        """
        Игрок - казуальщик
        """        
        self.addTrust("Minecraft", 0.2)
        self.addDistrust("Dota2", 0.2)
        self.addDistrust("WoT", 0.2)

    @Rule(Fact(answ="1-1") | Fact(answ="2-1"))    
    def handle_tryhard_player(self):
        """
        Игрок - трайхардер
        """
        self.addTrust("Dota2", 0.2)
        self.addTrust("Minecraft", 0.2)
        self.addTrust("WoT", 0.2)

    @Rule(Fact(answ="1-1") | Fact(answ="2-1"))
    def handle_steampunk_enjoyer(self):
        """
        Игрок любит сеттинг steampunk
        """
        self.addTrust("Minecraft", 0.2)
        self.addTrust("Factorio", 0.2)
        
    @Rule(Fact(answ="5-1") | Fact(answ="6-1") | Fact(answ = "7 - 2") | Fact(answ = "13 - 1"))
    def handle_Singler(self):
        self.updTrust("Poppy", 0.4)
        self.updTrust("Minecraft", 0.3)
        self.updTrust("Factorio", 0.4)
        self.updTrust("WoT", 0.1)
        self.updDistrust("Dota2", 0.4)
    
    @Rule(Fact(answ="5-2") | Fact(answ="6-2") | Fact(answ = "7 - 3") | Fact(answ = "13 - 2"))
    def handle_Coop(self):
        self.updDistrust("Poppy", 0.2)
        self.updTrust("Minecraft", 0.4)
        self.updTrust("Factorio", 0.2)
        self.updTrust("WoT", 0.3)
        self.updTrust("Dota2", 0.4)
    
    @Rule(Fact(answ="5-3") | Fact(answ="6-3") | Fact(answ = "7 - 1") | Fact(answ = "13 - 3"))
    def handle_Multi(self):
        self.updDistrust("Poppy", 0.4)
        self.updTrust("Minecraft", 0.2)
        self.updDistrust("Factorio", 0.2)
        self.updTrust("WoT", 0.5)
        self.updTrust("Dota2", 0.5)
        
