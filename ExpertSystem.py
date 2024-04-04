from experta import KnowledgeEngine, Rule, Fact

class ExpertSystem(KnowledgeEngine):
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
        
        Args:
            game(str): Название игры
            multiplier(float): Вес доверия
        
        Returns: none
        """
        self.trust_scores[game] += multiplier * (1 - self.trust_scores[game])

    def addDistrust(self, game: str, multiplier: float):
        """
        Обновляет Меры недоверия
        
        Args:
            game(str): Название игры
            multiplier(float): Вес недоверия
        
        Returns: none
        """
        self.distrust_scores[game] += multiplier * (1 - self.distrust_scores[game])

    @Rule(Fact(answ = "1-1") | 
          Fact(answ = "3-1") | 
          Fact(answ = "3-2") |
          Fact(answ = "7-1") |
          Fact(answ = "7-2") )
    def handle_casual_player(self):
        """
        Игрок - казуальщик
        """        
        self.addTrust("Minecraft", 0.2)
        self.addDistrust("Dota2", 0.2)
        self.addDistrust("WoT", 0.2)

    @Rule(Fact(answ = "1-2") | 
          Fact(answ = "3-3") | 
          Fact(answ = "3-4") |
          Fact(answ = "7-4") )    
    def handle_tryhard_player(self):
        """
        Игрок - трайхардер
        """
        self.addTrust("Dota2", 0.2)
        self.addTrust("Minecraft", 0.2)
        self.addTrust("WoT", 0.2)

    @Rule(Fact(answ = "1-3") | 
          Fact(answ = "2-3") )
    def handle_fantsy_enjoyer(self):
        """
        Игрок любит сеттинг fntsy
        """
        self.addTrust("Minecraft", 0.4)
        
    @Rule(Fact(answ = "5-1") | 
          Fact(answ = "6-1") | 
          Fact(answ = "7-2") | 
          Fact(answ = "13-1"))
    def handle_Singler(self):
        self.addTrust("Poppy", 0.4)
        self.addTrust("Minecraft", 0.3)
        self.addTrust("Factorio", 0.4)
        self.addTrust("WoT", 0.1)
        self.addDistrust("Dota2", 0.4)
    
    @Rule(Fact(answ = "5-2") | 
          Fact(answ = "6-2") | 
          Fact(answ = "7-3") | 
          Fact(answ = "13-2"))
    def handle_Coop(self):
        self.addDistrust("Poppy", 0.2)
        self.addTrust("Minecraft", 0.4)
        self.addTrust("Factorio", 0.2)
        self.addTrust("WoT", 0.3)
        self.addTrust("Dota2", 0.4)
    
    @Rule(Fact(answ = "5-3") | 
          Fact(answ = "6-3") | 
          Fact(answ = "7-1") | 
          Fact(answ = "13-3"))
    def handle_Multi(self):
        self.addDistrust("Poppy", 0.4)
        self.addTrust("Minecraft", 0.2)
        self.addDistrust("Factorio", 0.2)
        self.addTrust("WoT", 0.5)
        self.addTrust("Dota2", 0.5)
        
    @Rule(Fact(answ = "1-2") | 
          Fact(answ = "8-2") |
          Fact(answ = "9-1") |
          Fact(answ = "11-2") | 
          Fact(answ = "12-3"))
    def handle_TrueTryhard(self):
        self.addTrust("Factorio", 0.4)
        self.addTrust("WoT", 0.3)
        self.addTrust("Dota2", 0.5)
        self.addDistrust("Minecraft", 0.1)
        self.addDistrust("Poppy", 0.4)
        
    @Rule(Fact(answ = "1-3") |
          Fact(answ = "7-1") | 
          Fact(answ = "8-3") | 
          Fact(answ = "10-2") | 
          Fact(answ = "12-2") |
          Fact(answ = "13-4") |
          Fact(answ = "14-1"))
    def handle_Mind(self):
        self.addTrust("Factorio", 0.5)
        self.addTrust("Minecraft", 0.2)
        self.addDistrust("Poppy", 0.3)
        self.addDistrust("WoT", 0.3)
        self.addDistrust("Dota2", 0.2)
    
    @Rule(Fact(answ = "3-2") |
          Fact(answ = "7-4") |
          Fact(answ = "8-1") |
          Fact(answ = "9-3") |
          Fact(answ = "12-1") |
          Fact(answ = "14-2"))
    def handle_Fool(self):
        self.addTrust("Dota2", 0.2)
        self.addTrust("Minecraft", 0.4)
        self.addDistrust("WoT", 0.3)
        self.addDistrust("Poppy", 0.2)
        self.addDistrust("Factorio", 0.2)        
    
    @Rule(Fact(answ = "1-4") |
          Fact(answ = "2-2") |
          Fact(answ = "3-1") |
          Fact(answ = "3-2") |
          Fact(answ = "9-2") |
          Fact(answ = "10-3") |
          Fact(answ = "11-1") |
          Fact(answ = "14-3"))
    def handle_Scuf(self):
        self.addTrust("WoT", 0.5)
        self.addTrust("Dota2", 0.3)
        self.addTrust("Factorio", 0.3)
        self.addDistrust("Poppy", 0.3)
        self.addDistrust("Minecraft", 0.1)
        
    @Rule(Fact(answ = "3-4") |
          Fact(answ = "10-1") |
          Fact(answ = "11-3"))
    def handle_Horror(self):
        self.addTrust("Poppy", 0.5)
        self.addTrust("Minecrft", 0.1)
        self.addDistrust("WoT", 0.4)
        self.addDistrust("Dota2", 0.4)
        self.addDistrust("Factorio", 0.4)
        
    @Rule(Fact(answ = "4-1"))
    def handle_Free(self):
        self.addTrust("Dota2", 0.4)
        self.addTrust("WoT", 0.4)
    
    @Rule(Fact(answ = "4-2"))
    def handle_Money(self):
        self.addTrust("Minecraft", 0.3)
        self.addTrust("Poppy", 0.5)
        self.addTrust("Factorio", 0.5)
        
    def getCC(self):
        """
        Returns confidence coefficient
        """
        ku = self.trust_scores.copy()
        for key in self.trust_scores.keys():
            ku[key] -= self.distrust_scores[key]
        return ku
    
    def get_game(self):
        ku = self.getCC()
        print(ku)
        max = -1
        key = ""
        for res in ku:
            if ku[res] > max:
                max = ku[res]
                key = res

        return key, max
        