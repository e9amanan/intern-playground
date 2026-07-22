"""
Module providing an e-commerce shopping cart and product representation.
"""

from dataclasses import dataclass


@dataclass
class Product:
    """Represents a product with a name and price."""

    name: str
    price: float

    def __post_init__(self) -> None:
        """Validate the product attributes after initialization."""
        if self.price < 0:
            raise ValueError("Price cannot be negative")


class ShoppingCart:
    """Manages a collection of products and their quantities."""

    def __init__(self) -> None:
        """Initialize an empty shopping cart."""
        self._items: dict[str, tuple[Product, int]] = {}

    def add_item(self, product: Product, quantity: int = 1) -> None:
        """Add a product to the cart or update its quantity."""
        if product.name in self._items:
            existing_product, existing_qty = self._items[product.name]
            self._items[product.name] = (existing_product, existing_qty + quantity)
        else:
            self._items[product.name] = (product, quantity)

    def remove_item(self, product_name: str) -> None:
        """Remove a product entirely from the cart."""
        if product_name in self._items:
            del self._items[product_name]

    def get_total(self) -> float:
        """Calculate the total price of all items in the cart."""
        return sum(item[0].price * item[1] for item in self._items.values())

    def __len__(self) -> int:
        """Return the total number of items (quantities included) in the cart."""
        return sum(item[1] for item in self._items.values())
