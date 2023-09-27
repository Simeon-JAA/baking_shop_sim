"""Contains all functions related to setting up the simulation"""


import sys
import time
import re


WELCOME_MESSAGE = """Welcome to the shop simulator!
This programme will simulate what it is like to run your own baking shop...
Follow the instructions below to begin"""


def message_in_terminal(message: str, delay: float = 0.05) -> None:
    """Writes message to the terminal"""

    for letter in message:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)

    print("\n")


def pause_terminal(pause_time: float = 0.5) -> None:
    """Sleep terminal for 0.5 seconds"""

    time.sleep(pause_time)


def setup_instructions() -> None:
    """Prints the setup instructions in the terminal"""

    message_in_terminal(
        "You will begin with £10 worth of stock on your first day!")
    pause_terminal()
    message_in_terminal(
        "You can choose a default inventory setup or a custom one...")
    pause_terminal()


def select_inventory_setup() -> str:
    """Returns type of inventory setup based on user input"""

    allowed_inventory_setups = {"default", "custom"}
    inventory_setup = input("Choose default or custom inventory setup: ")

    if inventory_setup.lower().strip() not in allowed_inventory_setups:
        select_inventory_setup()

    return inventory_setup.lower().strip()


def get_user_shop_name() -> str:
    """Returns the user shop name"""

    user_shop_name = input("Chose a name for your shop: ")
    user_shop_name = re.sub(" +", " ", user_shop_name).title()

    if user_shop_name == None or user_shop_name == "" or user_shop_name == " ":
        message_in_terminal("Your shop name cannot be blank!")
        get_user_shop_name()

    return user_shop_name


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


def create_default_inventory() -> list[Food]:
    """Creates a default inventory for user to use"""

    inventory = []

    return inventory


def run_simulation_start() -> None:
    """Runs whole simulation start up procedure"""

    message_in_terminal(WELCOME_MESSAGE)
    pause_terminal()
    setup_instructions()

    inventory_setup = select_inventory_setup()

    if inventory_setup == "default":

        message_in_terminal("Creating default inventory...")
        message_in_terminal("....", 0.5)
        message_in_terminal("Successfully created default inventory")

        user_inventory = create_default_inventory()
        print(user_inventory)

    else:
        print("custom")


if __name__ == "__main__":

    run_simulation_start()

    shop_name = get_user_shop_name()
