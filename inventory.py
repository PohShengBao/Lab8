class Inventory:
    """Manages a collection of Product objects."""

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if self.get_product(product.product_id) is not None:
            return False  # duplicate ID
        self.__products.append(product)
        return True

    def get_product(self, product_id):
        """Exact ID lookup. Returns Product or None."""
        for p in self.__products:
            if p.product_id.lower() == product_id.lower():
                return p
        return None

    def search_product(self, term):
        """Return all products whose ID or name matches the term."""
        return [p for p in self.__products if p.matches(term)]

    def display_all(self):
        if not self.__products:
            print("Inventory is empty.")
            return
        print(f"{'ID':<8}{'Name':<20}{'Price':>11}{'Stock':>8}")
        print("-" * 47)
        for p in self.__products:
            p.display_information()

    def get_products(self):
        return list(self.__products)
