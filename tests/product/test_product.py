from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
        '1',
        'NoProduct',
        'NoName',
        '01/11/2023',
        '30/11/2024',
        '12345',
        'NoInstructions',
    )

    assert product.id == '1'
    assert product.company_name == 'NoName'
    assert product.product_name == 'NoProduct'
    assert product.manufacturing_date == '01/11/2023'
    assert product.expiration_date == '30/11/2024'
    assert product.serial_number == '12345'
    assert product.storage_instructions == 'NoInstructions'
