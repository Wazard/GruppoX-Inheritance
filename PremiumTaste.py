from Taste import Taste

class GustoPremium(Taste):
    def __init__(self, name, base_price, ingredienti_speciali: list [str], sovrapprezzo: float, allergens: list[str] = None):
        super().__init__(name, base_price, allergens)
        self._ingredienti_speciali = ingredienti_speciali 
        self._sovrapprezzo = sovrapprezzo
        
    def descrizione_premium(self) -> str:
        base = super().description()
        return f"{base}, ingredienti_speciali: {",".join(self._ingredienti_speciali)}, sovrapprezzo: {self._sovrapprezzo}."
