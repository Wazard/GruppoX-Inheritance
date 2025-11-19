from Taste import Taste as Taste
from PremiumTaste import GustoPremium as Premium
from VeganTaste import GustoVegano as Vegan

class Menu:
    def __init__(self, tastes: list[Taste]):
        
            #Constructor for Taste class.
        # param tastes: list of tastes (ex., ['Vanilla', 'Chocolate'])

        self._tastes = tastes if tastes is not None else []

    # --- Methods ---
    def add_taste(self, taste:Taste):
        #adds given taste to list, gives feedback
        if not taste in self._tastes:
            self._tastes.append(taste)
            return True
        return False

    def remove_taste(self, taste:Taste):
        # removes given taste from list, gives feedback
        if taste in self._tastes:
            self._tastes.remove(taste)
        return False

    def list_tastes(self) -> str:
        return ("\n").join((str(t) if type(t) is Taste else (t.descrizione_premium() if type(t) is Premium else t.descrizione_vegano())) for t in self._tastes)
    

