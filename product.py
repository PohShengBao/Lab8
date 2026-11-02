class Product:
    """Represents and manages a single product."""

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = 0
        self.update_stock(stock)  # reuse validation

    # Read-only access to the data main program needs
    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def stock(self):
        return self.__stock

    def update_stock(self, quantity):
        """Set the stock level. Product decides what is valid."""
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Stock must be a non-negative whole number.")
        self.__stock = quantity

    def display_information(self):
        print(f"{self.__product_id:<8}{self.__name:<20}${self.__price:>10.2f}{self.__stock:>8}")

    def matches(self, term):
        """True if the term matches this product's ID or name."""
        term = term.lower()
        return term == self.__product_id.lower() or term in self.__name.lower()

    # Conversion helpers so file code never touches private attributes
    def to_dict(self):
        return {"product_id": self.__product_id, "name": self.__name,
                "price": self.__price, "stock": self.__stock}

    @classmethod
    def from_dict(cls, data):
        return cls(data["product_id"], data["name"], data["price"], data["stock"])
