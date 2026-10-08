ADMIN_PASSWORD = "admin123"

format_price = lambda price: f"{price:.2f}грн"
cart_total = lambda cart: sum(item["price"] for item in cart)


def create_products():
    return {
        "1": {"name": "Хліб", "price": 25.50, "stock": 10},
        "2": {"name": "Молоко", "price": 42.90, "stock": 5},
        "3": {"name": "Яблука (кг)", "price": 38.75, "stock": 8},
        "4": {"name": "Кава", "price": 120.00, "stock": 3},
    }


def read_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        return None


def show_catalog(products):
    print("\n--- КАТАЛОГ ---")
    for product_id, product in products.items():
        print(f"{product_id}. {product['name']} - "
              f"{format_price(product['price'])} (залишок: {product['stock']})")


def show_cart(cart):
    print("\n--- КОШИК ---")
    if not cart:
        print("Кошик порожній")
        return
    for index, item in enumerate(cart, 1):
        print(f"{index}. {item['name']} - {format_price(item['price'])}")
    print(f"Разом: {format_price(cart_total(cart))}")


def add_to_cart(products, cart):
    show_catalog(products)
    choice = input("Номер товару: ")
    product = products.get(choice)
    if product is None or product["stock"] <= 0:
        print("Товару немає або він закінчився")
        return
    cart.append({"id": choice, "name": product["name"], "price": product["price"]})
    product["stock"] -= 1
    print(f"{product['name']} додано в кошик")


def remove_from_cart(products, cart):
    show_cart(cart)
    if not cart:
        return
    number = read_int("Номер товару для видалення: ")
    if number is None or not 1 <= number <= len(cart):
        print("Неправильний номер")
        return
    removed = cart.pop(number - 1)
    products[removed["id"]]["stock"] += 1
    print(f"{removed['name']} видалено з кошика")


def buy(cart):
    show_cart(cart)
    if not cart:
        return
    print(f"До сплати: {format_price(cart_total(cart))}")
    if input("Підтвердити покупку? (т/н): ").lower() == "т":
        cart.clear()
        print("Дякуємо за покупку!")


def admin_panel(products):
    if input("Пароль: ") != ADMIN_PASSWORD:
        print("Невірний пароль")
        return
    print("\n--- ЗАЛИШКИ НА СКЛАДІ ---")
    for product in products.values():
        print(f"{product['name']}: {product['stock']} шт.")


def menu():
    products = create_products()
    cart = []
    actions = {
        "1": lambda: show_catalog(products),
        "2": lambda: add_to_cart(products, cart),
        "3": lambda: remove_from_cart(products, cart),
        "4": lambda: show_cart(cart),
        "5": lambda: buy(cart),
        "6": lambda: admin_panel(products),
    }
    while True:
        print("\n=== МАГАЗИН ===")
        print("1. Каталог  2. В кошик  3. З кошика")
        print("4. Кошик    5. Купити   6. Адмін   0. Вихід")
        choice = input("> ")
        if choice == "0":
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Немає такого пункту")


if name == "main":
    menu()