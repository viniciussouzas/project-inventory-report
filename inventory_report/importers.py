import json
import csv
from typing import Dict, Type
from abc import ABC, abstractmethod
from inventory_report.product import Product


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        ...


class JsonImporter(Importer):
    def __init__(self, path: str) -> None:
        super().__init__(path)

    def import_data(self) -> list[Product]:
        list_product = []
        with open(self.path, 'r') as file:
            products = json.load(file)

        for product in products:
            list_product.append(Product(
                product["id"],
                product["product_name"],
                product["company_name"],
                product["manufacturing_date"],
                product["expiration_date"],
                product["serial_number"],
                product["storage_instructions"],
            ))
        return list_product


class CsvImporter(Importer):
    def __init__(self, path: str) -> None:
        super().__init__(path)

    def import_data(self) -> list[Product]:
        list_product = []

        with open(self.path, 'r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                (
                    id,
                    product_name,
                    company_name,
                    manufacturing_date,
                    expiration_date,
                    serial_number,
                    storage_instructions
                ) = row

                list_product.append(
                    Product(
                        id,
                        product_name,
                        company_name,
                        manufacturing_date,
                        expiration_date,
                        serial_number,
                        storage_instructions
                    ))

            return list_product


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
