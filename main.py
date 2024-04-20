class Store:
    def __init__(self, name, address):
        self.items = {}
        self.name = name
        self.address = address

    def add_item(self, item, price):
        self.items[item] = price
        print(f"Товар {item} добавлен в ассортимент магазина {self.name}")

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
            print(f"Товар {item} удален из ассортимента магазина {self.name}")
        else:
            print(f"Товар {item} отсутствует в ассортименте.")
            return 'None'

    def get_price(self, item):
        if item in self.items:
            print(f"Цена товара {item} в магазине {self.name} -{self.items[item]}")
            return self.items[item]

        else:
            print(f"Товар {item} отсутствует в ассортименте.")
            return 'None'

    def new_price(self, item, price):
        if item in self.items:
            self.items[item] = price
            print(f"Цена товара {item} изменена, новая цена {price}")
        else:
            print(f"Товар {item} отсутствует в ассортименте.")
            return 'None'

    def get_all_items(self):
        print(self.items)


Shop1 = Store("X5", "Коммунистический тупик, 1")
Shop2 = Store("Горздрав", "проспект Согдаймулды Моокулдаева, 15")
Shop3 = Store("Saturn", "Adolfplatz,14")

Shop1.add_item("Огурец соленый", 10)
Shop1.add_item("Водка паленая", 20)
Shop1.add_item("Сырок плавленный", 15)
Shop1.add_item("Вобла", 12)
Shop1.get_all_items()

Shop2.add_item("Кружка Эсмарха", 17)
Shop2.add_item("Виагра", 30)
Shop2.add_item("Витамин С", 10)
Shop2.add_item("Аспирин", 5)
Shop2.get_all_items()

Shop3.add_item("iPhone45", 1000)
Shop3.add_item("Notebook Figovo 15", 25)
Shop3.add_item("Smartphone Gumanoid 19", 250)
Shop3.add_item("Vacuum Cleaner Sucks 38", 100)
Shop3.get_all_items()

Shop3.get_price("iPhone45")
Shop3.new_price("iPhone45", 800)
Shop3.get_price("iPhone45")
Shop3.remove_item("Notebook Figovo 15")
Shop3.get_all_items()
Shop3.add_item("Notebook PassionFruit 14", 500)
Shop3.get_all_items()
