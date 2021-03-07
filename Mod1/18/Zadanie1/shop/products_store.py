
products = {
    "chleb": {"quantity": 6,
              "price": 2
              },
    "jablka": {"quantity": 4,
               "price": 3.5
               },
    "maslo": {"quantity": 5,
               "price": 3.2
              }
}

def update_product_quantity(product_name, oredered_quantity):
    products[product_name]["quantity"] -= oredered_quantity
