from datetime import date
from typing import List
from inventory_report.inventory import Inventory
from inventory_report.reports import Report


class SimpleReport(Report):
    def __init__(self) -> None:
        self.inventories: List[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories.append(inventory)

    def get_oldest_manufact_date(self) -> date:
        oldest_manufact_date = date.max

        for inventory in self.inventories:
            for product in inventory._data:
                manufacturing_date = date.fromisoformat(
                    product.manufacturing_date)

                if manufacturing_date < oldest_manufact_date:
                    oldest_manufact_date = manufacturing_date

        return oldest_manufact_date

    def get_closest_expiration_date(self) -> date:
        closest_expiration_date = date.max

        for inventory in self.inventories:
            for product in inventory._data:
                expiration_date = date.fromisoformat(product.expiration_date)

                if (expiration_date > date.today() and expiration_date < closest_expiration_date):
                    closest_expiration_date = expiration_date

        return closest_expiration_date

    def get_largest_inventory_company(self) -> str:
        largest_inventory_count = 0
        inventory_counts = {}
        largest_inventory = ""

        for inventory in self.inventories:
            for product in inventory._data:
                if product.company_name not in inventory_counts:
                    inventory_counts[product.company_name] = 0
                inventory_counts[product.company_name] += 1

                if inventory_counts[
                    product.company_name
                ] > largest_inventory_count:
                    largest_inventory_count = inventory_counts[
                        product.company_name]
                    largest_inventory = product.company_name

        return largest_inventory

    def generate(self) -> str:
        oldest_manufact_date = self.get_oldest_manufact_date()
        closest_expiration_date = self.get_closest_expiration_date()
        largest_inventory = self.get_largest_inventory_company()

        return (
            f"Oldest manufacturing date: {oldest_manufact_date}\n"
            f"Closest expiration date: {closest_expiration_date}\n"
            f"Company with the largest inventory: {largest_inventory}"
        )
