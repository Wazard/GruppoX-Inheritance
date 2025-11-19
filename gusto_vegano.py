from Taste import Taste

class GustoVegano(Taste):
    def __init__(self, name: str, base_price: float, allergens: list[str], base_vegetale: str):
        super().__init__(name, base_price, allergens)
        self._base_vegetale = base_vegetale

    def get_base_vegetale(self) -> str:
        return self._base_vegetale

    def set_base_vegetale(self, base_vegetale: str) -> None:
        self._base_vegetale = base_vegetale

    def descrizione_vegano(self) -> str:
        # Usiamo la description() della classe base e aggiungiamo info aggiuntive
        base_descr = super().description()
        return f"{base_descr}, Base vegetale: {self._base_vegetale}"





