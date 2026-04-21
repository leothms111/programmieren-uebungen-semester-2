import sys 

class Produktverwaltung:
    def __init__(self):
        self.product_list = []

    def add_products(self, products:list):
        for product in products:
            self.product_list.append(product.capitalize())
        print("Produkt erfolgreich hinzugefügt.")
        print("Deine neue Liste:")
        self.display_products()

    def remove_product(self, products:str):
        for product in products:
            self.product_list = [item for item in self.product_list if item.lower() != product.lower()]

    def display_products(self):
        for i, product in enumerate(self.product_list):
            print(f"[{i+1}]  {product}")

    def choose_products(self):
        prodcuts = input("Bitte gib ein Produkt ein:").split(",")
        prodcuts = prodcuts
        return prodcuts
    
    def exit(self):
        print("Das Programm wird beendet...")
        sys.exit()

    def run(self):
            mapping = {
                "1": self.add_products,
                "2": self.remove_product,
                "3": self.display_products,
                "4": self.exit
            }

            while True:
                print("\nWas möchtest du tun?")
                print("1: Hinzufügen | 2: Löschen | 3: Anzeigen | 4: Beenden")
                wahl = input("Auswahl: ")

                if wahl in mapping:
                    if int(wahl) <=2:
                        produkte = self.choose_products()
                        mapping[wahl](produkte)
                    else: 
                        mapping[wahl]()
                else:
                    print("Ungültige Eingabe, bitte nochmal.")


app = Produktverwaltung()
app.run()
    
