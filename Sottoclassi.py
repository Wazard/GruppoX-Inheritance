from Taste import Taste

class GustoPremium(Taste):
    def __init__(self, name, base_price, allergens, ingredienti_speciali: list [str], sovrapprezzo: float):
        super().__init__(name, base_price, allergens)
        self._ingredienti_speciali = ingredienti_speciali 
        self._sovrapprezzo = sovrapprezzo
        
    def descrizione_premium(self):
        base = self.description()
        return f"{base}, ingredienti_speciali: {",".join(self._ingredienti_speciali)}, sovrapprezzo: {self._sovrapprezzo}."
    
        
    
g = GustoPremium("jhh", 3, ["5rerrt", "hgyhg"], ["pistacchio", "uhiuhgi"], 2)
print(g.description())