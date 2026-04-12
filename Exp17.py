print("251034,30/03/26\n")
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity
        print(f"Stock updated. New stock of {self.name}: {self.stock}")


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class ShoppingCart:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, product, quantity):
        if product.stock >= quantity:
            self.items.append((product, quantity))
            product.update_stock(-quantity)
            print(f"Added {quantity} of {product.name} to cart.")
        else:
            print(f"Insufficient stock for {product.name}.")

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.items)

    def process_order(self):
        total_cost = self.calculate_total()
        print(f"Order processed for {self.customer.name}. Total cost: ${total_cost}")


if __name__ == "__main__":
    product1 = Product("Laptop", 1000, 10)
    product2 = Product("Smartphone", 500, 20)

    customer = Customer("Alice", "alice@eng.rizvi.edu.in")

    cart = ShoppingCart(customer)
    cart.add_item(product1, 1)
    cart.add_item(product2, 2)

    cart.process_order()
