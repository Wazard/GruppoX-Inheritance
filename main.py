from Taste import Taste
from PremiumTaste import GustoPremium as Premium
from VeganTaste import GustoVegano as Vegan
from Menu import Menu


def main():
    # Create some Taste objects
    vanilla = Taste("Vanilla", 2.50, ["Milk"])
    vegan_vanilla = Vegan("Vanilla", 2.50, allergens=["Milk"], base_vegetale="Boh")
    premium_chocolate = Premium("Chocolate", 3.00, allergens=["Milk", "Soy"], sovrapprezzo=2, ingredienti_speciali=["Nicaragua's Cacao"])
    chocolate = Taste("Chocolate", 3.00, ["Milk", "Soy"])
    strawberry = Taste("Strawberry", 2.75, [])

    # Initialize Menu with a couple of tastes
    menu = Menu([vanilla, chocolate])

    print("Initial menu:")
    print(menu.list_tastes())

    # Add a new taste
    added = menu.add_taste(strawberry)
    print(f"\nAdding Strawberry: {'Success' if added else 'Already exists'}")
    print(menu.list_tastes())
    added = menu.add_taste(vegan_vanilla)
    added = menu.add_taste(premium_chocolate)
    print(menu.list_tastes())

    # Add already existing new taste
    added = menu.add_taste(strawberry)
    print(f"\nAdding Strawberry: {'Success' if added else 'Already exists'}")

    # Try removing Chocolate
    removed = menu.remove_taste(chocolate)
    print(f"\nRemoving Chocolate: {'Success' if removed else 'Not found'}")
    print(menu.list_tastes())

    # Show full descriptions of each taste
    print("\nDetailed descriptions:")
    for taste in menu._tastes:
        print(taste.description())

if __name__ == "__main__":
    main()