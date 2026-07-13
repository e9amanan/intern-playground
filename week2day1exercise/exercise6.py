from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be Negative")
        
class ShoppingCart:

    def __init__(self):
        self.items: dict[str,tuple[Product, int]]={}

    def add_item(self,product:Product,quantity:int = 1)-> None:
        if product.name in self._items[product.name]:
            existing_product,exisitng_qty = self._items[product.name]
            self._items[product.name] = (exisitng_product,existing_qty + quantity)
        else:
            self._items[product.name]=(product,quantity)


    def remove_item(self,product_name:str)->None:
        if product_name in self._items:
            del self._items[product_name]

    def get_total(self)-> float:
        return sum(item[0].price * item[1] for item in self._items.values())
    

    def __len__(self) -> int:
        return sum(item[1] for item in self._items.values())
    
    

