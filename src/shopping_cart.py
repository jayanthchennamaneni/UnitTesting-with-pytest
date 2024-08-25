from typing import List, Dict

class ShoppingCart:
    def __init__(self, max_items: int) -> None:
        """
        Initialize the shopping cart with a maximum number of items.
        
        :param max_items: Maximum number of items allowed in the cart.
        """
        self.items: List[str] = []  # List to store items in the cart
        self.max_items = max_items  # Maximum capacity of the cart

    def add(self, item: str) -> None:
        """
        Add an item to the shopping cart.
        
        :param item: The item to be added to the cart.
        :raises OverflowError: If the cart is already full.
        """
        if self.size() == self.max_items:
            raise OverflowError("Cannot add more items")  # Raise an error if the cart is full
        self.items.append(item)  # Add the item to the cart

    def size(self) -> int:
        """
        Get the current number of items in the cart.
        
        :return: The number of items in the cart.
        """
        return len(self.items)  # Return the number of items in the cart

    def get_items(self) -> List[str]:
        """
        Get a list of all items in the cart.
        
        :return: A list of items in the cart.
        """
        return self.items  # Return the list of items

    def get_total_price(self, price_map: Dict[str, float]) -> float:
        """
        Calculate the total price of the items in the cart.
        
        :param price_map: A dictionary mapping item names to their prices.
        :return: The total price of all items in the cart.
        """
        total_value = 0.0
        for item in self.get_items():
            total_value += price_map.get(item, 0.0)  # Add the price of each item to the total
        return total_value  # Return the total price
