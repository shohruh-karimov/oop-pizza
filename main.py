class Pizza:
    def __init__(self, dough, sauce, toppings):
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings

    def prepare(self):
        print("Готовим пиццу...")
        # код для приготовления пиццы

    def bake(self):
        print("Выпекаем пиццу...")
        # код для выпекания пиццы

    def cut(self):
        print("Разрезаем пиццу...")
        # код для нарезки пиццы

    def package(self):
        print("Упаковываем пиццу...")
        # код для упаковки пиццы


class Order:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def calculate_total(self):
        total = 0
        for pizza in self.pizzas:
            total += pizza.price
        return total


class Terminal:
    def __init__(self):
        self.menu = {
            1: Pizza("Pepperoni Dough", "Pepperoni Sauce", ["pepperoni"]),
            2: Pizza("Barbecue Dough", "Barbecue Sauce", ["bacon", "onions", "pineapple"]),
            3: Pizza("Seafood Dough", "Seafood Sauce", ["shrimp", "calamari", "mussels"])
        }

    def display_menu(self):
        print("MENU:")
        for index, pizza in self.menu.items():
            print(f"{index}. {pizza.dough} {pizza.sauce} {pizza.toppings}")

    def create_order(self):
        order = Order()
        while True:
            self.display_menu()
            selected_pizza = int(input("Выберите пиццу из меню (введите число): "))
            order.add_pizza(self.menu[selected_pizza])

            more_pizzas = input("Хотите добавить еще пиццы в свой заказ? (да/нет): ")
            if more_pizzas.lower() != "да":
                break

        print("Заказ подтвержден!")
        total = order.calculate_total()
        print(f"Общая сумма: {total} USD")

        payment = float(input("Введите сумму платежа: "))
        if payment >= total:
            print("Оплата получена. Спасибо!")
            order.process()
        else:
            print("Недостаточная оплата. Заказ отменен.")


terminal = Terminal()
terminal.create_order()