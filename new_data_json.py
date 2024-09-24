import json

file_path = 'products.json'

new_product = {
    'name': 'Wireless Charger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '2024-09-22'
}

with open(file_path, mode='r') as file:
    products = json.load(file)

products.append(new_product)

with open(file_path, mode='w') as file:
    json.dump(products, file, indent=4)
