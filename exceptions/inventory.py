class ArticleNotFoundError(Exception):
    pass

class InvalidQuantity(Exception):
    pass

class InsufficientStockError(Exception):
    pass

def print_inventory(inventory):
    print("Wir haben folgende Artikel im Angebot:")
    print(f"{'Artikel':<15} | {'Anzahl':>6}")
    print("-" * 25)
    for artikel, anzahl in inventory.items():
        print(f"{artikel.capitalize():<15} | {anzahl:>6}")

inventory = {
            "handy": 5,
            "laptop": 3,
            "uhr": 10,
            "staubsauger": 15
        }

print_inventory(inventory)
try:
    artikel = input("Welchen Artikel möchtest du kaufen? ").lower()
    artikel_cap  =artikel.capitalize()
    current_quantity = inventory[artikel]
    print(f"Es sind noch {current_quantity} vom Artikel {artikel_cap} vorhanden.")
    quantity = int(input("Wie viele davon möchtest du kaufen? "))
    new_quantity = current_quantity - quantity
    if new_quantity < 0:
        raise InsufficientStockError("Mehr Artikel gekauft als vorhanden. DHL mal wieder zu spät.")
    inventory[artikel] = new_quantity
except KeyError:
    raise ArticleNotFoundError("Dieses Produkt ist leider momentan nicht vorrätig") from None
except ValueError:
    raise InvalidQuantity("Bitte gib eine gültige Anzahl ein.") from None
else:
    print(f"Du hast folgenden Artikel erfolgereich erworben: {artikel_cap}, Anzahl: {quantity}")
finally:
    print_inventory(inventory)

