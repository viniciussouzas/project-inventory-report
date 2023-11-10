from inventory_report.product import Product


def test_product_report() -> None:
    product = Product(
        '1',
        'NoProduct',
        'NoName',
        '01/11/2023',
        '30/11/2024',
        '12345',
        'NoInstructions',
    )

    assert str(product) == (
        "The product 1 - NoProduct "
        "with serial number 12345 "
        "manufactured on 01/11/2023 "
        "by the company NoName "
        "valid until 30/11/2024 "
        "must be stored according to the following instructions: "
        "NoInstructions."
    )
