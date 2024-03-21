from experta import *

class ExperSystem(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        # Меры доверия
        self.MDDota2 = 0
        self.MDMinecraft = 0
        self.MDFactorio = 0
        # Меры недоверия
        self.MNDDota2 = 0
        self.MNDMinecraft = 0
        self.MNDFactorio = 0

    @Rule(
        Fact(answ="1-1") | Fact(answ="2-1"))
    def __(self):
        self.MDDota2 += 0.2 * (1 - self.MDDota2)