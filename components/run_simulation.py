"""Handles all functions where the simulation runs"""


from component_classes import Shop, User
from sim_startup import create_default_shop_and_inventory


def run_simulation(user_shop: Shop, user: User) -> None:
    """Runs simulation with user_shop and user account"""


if __name__ == "__main__":

    example_user = User("example_user")
    example_user_shop = create_default_shop_and_inventory()

    run_simulation(example_user_shop, example_user)
