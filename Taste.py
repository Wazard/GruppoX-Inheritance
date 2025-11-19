class Taste:
    def __init__(self, name: str, base_price: float, allergens: list[str]):

        #Constructor for Taste class.
        # param name: Name of the taste (e.g., 'Vanilla', 'Chocolate')
        # param base_price: Base price of the taste as a float
        # param allergens: List of allergens associated with this taste

        self._name = name
        self._base_price = base_price
        self._allergens = allergens

    # --- Getters ---
    def get_name(self) -> str:
        #Return the name of the taste.
        return self._name

    def get_base_price(self) -> float:
        # Return the base price of the taste.
        return self._base_price

    def get_allergens(self) -> list[str]:
        # Return the list of allergens for this taste.
        return self._allergens

    # --- Setters ---
    def set_name(self, name: str) -> None:
        # Set a new name for the taste.
        self._name = name

    def set_base_price(self, base_price: float) -> None:
        # Set a new base price for the taste.
        self._base_price = base_price

    def set_allergens(self, allergens: list[str]) -> None:
        # Set a new list of allergens for the taste.
        self._allergens = allergens

    # --- Description ---
    def description(self) -> str:

        #Return a string description of the taste, including name,
        #base price, and allergens.

        allergens_str = ", ".join(self._allergens) if self._allergens else "None"
        return f"Taste: {self._name}, Price: {self._base_price:.2f}, Allergens: {allergens_str}"