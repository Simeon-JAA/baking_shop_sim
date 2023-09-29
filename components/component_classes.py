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
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> int:
        return self._price

    @property
    def amount(self) -> int:
        return self._amount


class Cupcake(Food):
    """Cupcake class"""

    def __init__(self, flavor: str, price: int, amount: int, allergies: str = "None") -> None:
        super().__init__(flavor, price, amount, allergies)

        self._name = re.sub(" +", " ", flavor.title().strip()) + " Cupcake"


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
    def shop_name(self) -> str:
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


class User():
    """User class containing user stats"""

    def __init__(self, username: str, email: str = None) -> None:
        """Initialise user class with name and stats"""

        if len(username) < 6:
            raise ValueError(
                "Invalid Username: Minimum characters requires is 6!")
        if len(username) > 20:
            raise ValueError(
                "Invalid Username: Maximum characters allowed is 20!")
        if not re.search("[a-zA-Z0-9!_-]{6,20}", username) or username.count(" ") > 0:
            raise ValueError(
                "Invalid Username: Username contains spaces or invalid characters!")

        if email:
            if email.count(" ") > 0:
                raise ValueError("Invalid email: Email cannot contain spaces!")
            if not re.search("[a-zA-Z0-9._-]+@[a-zA-Z]+.[a-z]{2,3}(.[a-z]{2})?", email):
                raise ValueError(
                    "Invalid email: Email does not fall within format constraint!")

            self._email = email

        else:
            self._email = email

        self._username = username
        self._xp = 0
        self._level = 1
        self._good_luck = 10
        self._bad_luck = 0

    @property
    def username(self) -> str:
        return self._username

    @property
    def email(self) -> str:
        return self._email

    @property
    def level(self) -> int:
        return self._level

    @property
    def xp(self) -> int:
        return self._xp

    @property
    def good_luck(self) -> int:
        return self._good_luck

    @property
    def bad_luck(self) -> int:
        return self._bad_luck


if __name__ == "__main__":

    pass
