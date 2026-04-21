def umsatz(data:dict):
    return data["menge"]* data["preis"]

def umsatz_produkt(data, produkt):
    produkt = produkt.lower()
    for index, item in enumerate(data):
        if item["produkt"] == produkt:
            return umsatz(data=data[index])
    raise ValueError("Not a valid Produktname")
    

sales_data = [
    {"produkt": "laptop", "preis": 1200.0, "menge": 3, "datum": "2023-01-15"},
    {"produkt": "smartphone", "preis": 800.0, "menge": 5, "datum": "2023-01-16"},
    {"produkt": "tablet", "preis": 500.0, "menge": 2, "datum": "2023-01-17"},
    {"produkt": "monitor", "preis": 300.0, "menge": 4, "datum": "2023-01-18"},
    {"produkt": "drucker", "preis": 200.0, "menge": 10, "datum": "2023-01-19"}
]

ums = umsatz_produkt(sales_data, "monitor")
print(ums)

gesamt_ums = list(map(lambda x: x["menge"]*x["preis"], sales_data))
gesamt_ums2 = list(map(umsatz, sales_data)) # Zeile 23 und 24 machen genau das gleiche
print(gesamt_ums)
print(gesamt_ums2)

filtered_ums = list(filter(lambda x: x>2000, gesamt_ums))
print(filtered_ums)

sorted_ums = sorted(filtered_ums, reverse=True)
print(sorted_ums)
print(sum(sorted_ums))