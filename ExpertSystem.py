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
    
    def updTrust(self, game: str, multiplier: float):
        """
        Обновляет Меры доверия
        """
        self.trust_scores[game] += multiplier * (1 - self.trust_scores[game])

    def updDistrust(self, game: str, multiplier: float):
        """
        Обновляет Меры недоверия
        """
        self.distrust_scores[game] += multiplier * (1 - self.trust_scores[game])

#прежде чем правила писать надо схему завершить и игры туда напихать, чтобы их связи знать. На глаголы не рифмуй, за щеку получишь хуй
    @Rule(Fact(answ="1-1") | Fact(answ="2-1"))
    def handle_casual_player(self):
        self.updTrust("Minecraft", 0.2)
        

    def handle_tryhard_player(self):
        self.updTrust()