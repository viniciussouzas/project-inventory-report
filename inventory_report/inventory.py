from inventory_report.product import Product


class Inventory:
    def __init__(self, data: list[Product] | None = None) -> None:
        if data is None:
            self._data = []
        else:
            self._data = data

    @property
    def data(self) -> list[Product] | None:
        return self._data

    def add_data(self, data: list[Product]) -> None:
        for product in data:
            self._data.append(product)
