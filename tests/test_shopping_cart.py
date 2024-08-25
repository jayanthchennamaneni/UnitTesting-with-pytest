import pytest
from src.shopping_cart import ShoppingCart

@pytest.fixture
def cart() -> ShoppingCart:
    """
    Fixture to create a ShoppingCart instance with a max capacity of 4 items.
    
    :return: A ShoppingCart instance.
    """
    return ShoppingCart(max_items=4)  # Create a ShoppingCart with a capacity of 4 items

def test_can_add_item_to_cart(cart: ShoppingCart) -> None:
    """
    Test that an item can be added to the cart.
    
    :param cart: The ShoppingCart instance.
    """
    cart.add("mugs")  # Add an item to the cart
    assert cart.size() == 1  # Assert that the cart size is 1 after adding the item

def test_added_item_is_in_cart(cart: ShoppingCart) -> None:
    """
    Test that an added item is present in the cart.
    
    :param cart: The ShoppingCart instance.
    """
    cart.add("book")  # Add an item to the cart
    assert "book" in cart.get_items()  # Assert that the added item is in the cart

def test_max_size_of_cart(cart: ShoppingCart) -> None:
    """
    Test that the cart does not accept more items than its maximum capacity.
    
    :param cart: The ShoppingCart instance.
    """
    for _ in range(4):
        cart.add("book")  # Add items to fill the cart

    with pytest.raises(OverflowError):
        cart.add("book")  # Try to add an item beyond the cart's capacity, expecting an OverflowError

def test_total_price(cart: ShoppingCart) -> None:
    """
    Test that the total price calculation for items in the cart is correct.
    
    :param cart: The ShoppingCart instance.
    """
    cart.add("book")
    cart.add("e-book")

    price_map = {
        "book": 3.0,
        "e-book": 1.20
    }

    assert cart.get_total_price(price_map) == 4.20  # Assert that the total price is correctly calculated
