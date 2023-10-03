"""Handles all functions where the simulation runs"""

import sys
import time
import random
import re

from component_classes import Shop, User
from sim_startup import create_default_shop_and_inventory


USER_INTERACTIONS = {"sell items", "recommend dessert", "greet customer"}


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


def no_customer_interaction_bad_luck() -> None:
    """
    Terminal text displaying no customer interactions for the hour
    This occurs as a result of bad luck
    """

    message_in_terminal("Nobody has entered your shop :(")
    pause_terminal()
    message_in_terminal("One hour has now passed ...")
    pause_terminal()
    message_in_terminal("Moving onto next interaction.")
    pause_terminal()


def customer_entered_shop_message() -> None:
    """Text displayed as a result of a customer entering the shop"""

    message_in_terminal("A customer has just entered your shop!")
    pause_terminal()
    message_in_terminal("What would you like to do?")
    pause_terminal(0.3)


def display_user_interactions(possible_interactions: set) -> None:
    """Displays possible user interactions"""

    message_in_terminal("Please select from possible interactions below!")
    pause_terminal()

    for interaction in possible_interactions:
        print(interaction.title())
        time.sleep(0.25)


def get_user_interaction(allowed_user_interactions: set, failed_interactions: int = 0) -> str:
    """Returns user interaction"""

    if failed_interactions >= 3:
        display_user_interactions(allowed_user_interactions)

    user_interaction = input("Please select your interaction")
    user_interaction = re.sub(" +",  " ", user_interaction.lower())

    if user_interaction not in allowed_user_interactions:
        failed_interactions += 1
        get_user_interaction(allowed_user_interactions, failed_interactions)

    else:
        return user_interaction


def run_simulation(time: int, user_shop: Shop, user: User) -> None:
    """Runs simulation with user_shop and user account"""

    message_in_terminal(f"The time is {time} O\'clock ...")
    pause_terminal()

    if random.randint(0, 100) < user.bad_luck:
        no_customer_interaction_bad_luck()
        return

    else:
        customer_entered_shop_message()
        user_interaction = get_user_interaction(USER_INTERACTIONS)
        return


if __name__ == "__main__":

    example_user = User("example_user")
    # example_user_shop = create_default_shop_and_inventory()

    # run_simulation(example_user_shop, example_user)

    for num in range(9, 17):
        run_simulation(num, "shop", example_user)
        break
