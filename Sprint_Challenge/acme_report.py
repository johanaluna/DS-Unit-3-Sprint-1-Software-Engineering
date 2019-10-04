from acme import Product
import random


NAME = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUN = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(n_product=30):

    list_products = []
    for _ in range(n_product):
        name = (random.choice(NAME) + " " + random.choice(NOUN))
        weight = random.randint(5, 101)
        price = random.randint(5, 101)
        flammability = random.uniform(0, 2.5)
        product = Product(name=name, weight=weight, price=price,
                          flammability=flammability)
        list_products.append(product)
    return list_products


def inventory_report(list_products):
    unique_values_names = []
    mean_price = 0
    mean_weight = 0
    mean_flamma = 0

    for x in range(0, len(list_products)):
        productx = list_products[x]
        if (productx.name not in unique_values_names):
            unique_values_names.append(productx.name)
        mean_price += productx.price
        mean_weight += productx.weight
        mean_flamma += productx.flammability

    mean_price /= len(list_products)
    mean_weight /= len(list_products)
    mean_flamma /= len(list_products)

    print(f'''
    ACME CORPORATION OFFICIAL INVENTORY REPORT
    Unique product names: {len(unique_values_names)}
    Average price\t: {mean_price}
    Average weight\t: {mean_weight}
    Average flammability: {mean_flamma}
    ''')

if __name__ == '__main__':
    inventory_report(generate_products())
