#  Создайте класс "Товар" с атрибутами "название", "цена" и "количество",
#  Напишите метод, который выводит информацию о товарс в формате
#  "Название: название, Цена: цена, Количество: кол-во".

class Building:
    def __init__(self, name,price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f'Название: {self.name}, Количество: {self.quantity},Цена: {self.price}')


first = Building('Абрикосы', '228 рублей', '15')
second = Building('Помидоры','500 рублей', '10')
first.display_info()
second.display_info()