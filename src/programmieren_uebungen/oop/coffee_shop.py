
class Product:
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return self.name


class Menu:
    def __init__(self):
        self.products = [
            Product(name="coffee", price=4.5, category="drink"),
            Product(name="tea", price=2.9, category="drink"),
            Product(name="cake", price=4, category="food"),
        ]

    def add_product(self, product):
        self.products.append(product)

    def display(self):
        menu = "\n--- UNSERE SPEISEKARTE ---\n"
        for i, product in enumerate(self.products, start=1):
            menu += f"[{i}] {product.name:15} | {product.price:>5.2f}€\n"
        return menu + "-" * 26

    def get_product_by_id(self, index):
        try:
            return self.products[index - 1]
        except IndexError:
            return None

    def get_product_by_name(self, name):
        for p in self.products:
            if p.name.lower() == name.lower():
                return p
        return None


class OrderItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def get_subtotal(self) -> float:
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product}, Quantity: {self.quantity}"


class Customer:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id


class Order:
    orders: list[OrderItem] = []

    def __init__(self, number: int, customer: Customer):
        self.orders: list[OrderItem] = []
        self.number = number
        self.customer = customer
        self.menu = Menu()

    def place_order(self, item: str, quantity: int):
        product = self.menu.get_product_by_name(item)
        orderitem = OrderItem(product=product, quantity=quantity)
        self.orders.append(orderitem)

    def get_bill(self):
        sum = 0
        bill: str = f"Bill number {self.number}\n{'-' * 15}\n"
        for i, order in enumerate(self.orders, start=1):
            sub_sum = order.get_subtotal()
            sum += sub_sum
            bill += f"[{i}] {order.product.name:15} | {order.quantity:>5} | {sub_sum:>5.2f}€\n"
        bill += f"Total Price: {sum:>22.2f}€"
        return bill


daniel = Customer(name="daniel", id=1)
order_1 = Order(number=1, customer=daniel)

order_1.place_order("tea", 2)
order_1.place_order("coffee", 1)
print(order_1.get_bill())

print(Menu().display())
