"""Contains all the class components used in the simulation"""

import re
import sys
import time


def message_in_terminal(message: str, delay: float = 0.05) -> None:
    """Writes message to the terminal"""

    for letter in message:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)

    print("\n")


class Food():
    """Food class"""

    def __init__(self, name: str, price: int, amount: int, allergies: str = "None") -> None:
        """Initialise cake class with specified properties"""

        if not isinstance(price, int) or not isinstance(amount, int):
            raise TypeError("Price & Value should both be integer types!")
        if price < 0:
            raise ValueError("Price cannot be negative!")
        if amount < 0:
            raise ValueError("Cannot have negative amount of produce!")

        self._name = re.sub(" +", " ", name.strip().title())
        self._price = price
        self._amount = amount
        self._allergies = allergies

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def amount(self):
        return self._amount


class Cupcake(Food):
    """Cupcake class"""

    def __init__(self, name: str, price: int, amount: int, allergies: str = "None") -> None:
        super().__init__(name, price, amount, allergies)


class Cake(Food):
    """Cake class"""

    def __init__(self, name: str, price: int, amount: int, size: int, allergies: str = "None") -> None:
        super().__init__(name, price, amount, allergies)

        self._size = size

    @property
    def size(self):
        return self._size


class Shop():
    """Shop class"""

    def __init__(self, shop_name: str) -> None:
        """Initialise shop class with specified properties"""
        self._shop_name = re.sub(" +", " ", shop_name.title().strip())
        self._shop_stock = []

    @property
    def shop_name(self):
        return self._shop_name

    @property
    def stock(self):
        return self._shop_stock

    def add_food_item_to_stock(self, food_item: Food):
        """Adds food item to the shop stock"""

        self.stock.append(food_item)

        if food_item.amount == 1:
            message_in_terminal(f"{food_item.name} was added to your stock!")
        else:
            message_in_terminal(
                f"{food_item.amount} {food_item.name}s were added to your stock!")

    def display_stock(self):
        """Displays shop stock for user"""

        pass


if __name__ == "__main__":

    pass
