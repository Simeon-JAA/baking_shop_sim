"""Contains all functions related to setting up the simulation"""


import sys
import time
import re

from component_classes import Cupcake, Shop


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

    user_shop_names_disallowed = {None, "", " "}

    user_shop_name = input("Chose a name for your shop: ")
    user_shop_name = re.sub(" +", " ", user_shop_name).title()

    if user_shop_name in user_shop_names_disallowed:
        message_in_terminal("Your shop name cannot be blank!")
        get_user_shop_name()

    return user_shop_name


def create_default_shop_and_inventory() -> Shop:
    """Adds default items to user shop stock"""

    user_shop_name = get_user_shop_name()

    user_shop = Shop(user_shop_name)

    default_chocolate_cupcakes = Cupcake("chocolate", 499, 5)
    default_vanilla_cupcakes = Cupcake("vanilla", 499, 5)
    default_strawberry_cupcakes = Cupcake("strawberry", 699, 2)

    message_in_terminal("Adding to stock...")
    message_in_terminal("....", 0.35)

    user_shop.add_food_item_to_stock(default_chocolate_cupcakes)
    user_shop.add_food_item_to_stock(default_vanilla_cupcakes)
    user_shop.add_food_item_to_stock(default_strawberry_cupcakes)

    message_in_terminal("Successfully added items to stock!")

    return user_shop


def run_simulation_start() -> Shop:
    """Runs whole simulation start up procedure and returns user shop to work with moving forward"""

    message_in_terminal(WELCOME_MESSAGE)
    pause_terminal()
    setup_instructions()

    inventory_setup = select_inventory_setup()

    if inventory_setup == "default":

        user_shop = create_default_shop_and_inventory()

    else:
        # TODO Add option for custom inventory build
        print("Custom inventory is still in progress. Exiting simulation")

    return user_shop


if __name__ == "__main__":

    user_shop = run_simulation_start()
